(() => {
  'use strict';

  const NO_CACHE = { cache: 'no-store' };
  const DEBOUNCE_MS = 100;
  const KEYWORD_ALL = '__ALL__';
  const DATE_DAYS = { '1d': 1, '7d': 7, '30d': 30, '90d': 90 };
  const DATE_LABELS = { '1d': '1日', '7d': '1週間', '30d': '1ヶ月', '90d': '3ヶ月' };
  const FAVORITES_KEY = 'dr_favorites_v1';
  const FAVORITES_VERSION = 1;

  const $list = document.getElementById('article-list');
  const $title = document.getElementById('site-title');
  const $lastUpdated = document.getElementById('last-updated');
  const $search = document.getElementById('search-input');
  const $count = document.getElementById('result-count');
  const $repoLink = document.getElementById('repo-link');
  const $chipsRow = document.getElementById('keyword-chips');
  const $dateFilterRow = document.getElementById('date-filter-row');
  const $sampleBanner = document.getElementById('sample-banner');
  const $favRow = document.getElementById('favorite-filter-row');
  const $favToggle = document.getElementById('fav-filter-toggle');
  const $favExport = document.getElementById('fav-export-btn');
  const $favCount = document.getElementById('fav-count');

  const state = {
    articles: [],
    fuse: null,
    selectedKeyword: KEYWORD_ALL,
    dateRange: '7d',
    isSample: false,
    favorites: new Set(),
    favoritesMeta: new Map(),
    favoritesOnly: false
  };

  loadFavorites();

  setRepoLinkFromLocation();

  Promise.all([
    fetchJson('./config.json').catch(() => null),
    fetchArticlesWithFallback(),
    fetchText('./data/last_updated.txt').catch(() => '')
  ]).then(([config, articlesResult, lastUpdated]) => {
    state.articles = articlesResult.articles.slice();
    state.articles.sort(byFetchedAtDesc);
    state.isSample = articlesResult.isSample;

    applyTitle(config, state.articles);

    state.fuse = new Fuse(state.articles, {
      keys: [
        { name: 'title', weight: 0.45 },
        { name: 'summary', weight: 0.35 },
        { name: 'tags', weight: 0.2 }
      ],
      threshold: 0.35,
      ignoreLocation: true,
      includeScore: false,
      minMatchCharLength: 1
    });

    if (!state.isSample) {
      pruneStaleFavorites(state.articles);
    }

    renderSampleBanner(state.isSample);
    renderLastUpdated(lastUpdated);
    renderKeywordChips(buildKeywordList(state.articles));
    setupDateChips();
    setupFavoriteFilter();
    setupFavoriteExport();
    renderFavoriteRow();
    updateFavCount();
    runSearch();

    $search.addEventListener('input', onSearchInput);
    $search.focus();
  }).catch((err) => {
    console.error(err);
    $list.innerHTML = '';
    const p = document.createElement('p');
    p.className = 'status status-empty';
    p.textContent = '記事データの読み込みに失敗しました。時間を置いて再読み込みしてください。';
    $list.appendChild(p);
  });

  let debounceTimer = 0;
  function onSearchInput() {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(runSearch, DEBOUNCE_MS);
  }

  function runSearch() {
    const q = $search.value.trim();
    let items = q ? state.fuse.search(q).map((r) => r.item) : state.articles;
    items = filterByDate(items, state.dateRange);
    if (state.selectedKeyword !== KEYWORD_ALL) {
      items = items.filter((a) => a.matched_keyword === state.selectedKeyword);
    }
    if (state.favoritesOnly) {
      items = items.filter((a) => state.favorites.has(a.id));
    }
    render(items, q);
  }

  function filterByDate(items, range) {
    const days = DATE_DAYS[range];
    if (!days) return items;
    const threshold = Date.now() - days * 24 * 60 * 60 * 1000;
    return items.filter((a) => {
      const dateStr = a.published_at || a.fetched_at;
      if (!dateStr) return false;
      const t = Date.parse(dateStr);
      return !isNaN(t) && t >= threshold;
    });
  }

  function render(items, query) {
    $list.innerHTML = '';

    if (!items.length) {
      const p = document.createElement('p');
      p.className = 'status status-empty';
      p.textContent = buildEmptyMessage(query);
      $list.appendChild(p);
      $count.textContent = '0 件';
      return;
    }

    const frag = document.createDocumentFragment();
    for (const article of items) {
      frag.appendChild(buildCard(article));
    }
    $list.appendChild(frag);
    $count.textContent = `${items.length} 件`;
  }

  function buildCard(article) {
    const card = document.createElement('article');
    card.className = 'article-card';

    const h2 = document.createElement('h2');
    h2.className = 'article-title';
    const a = document.createElement('a');
    a.href = article.url || '#';
    a.target = '_blank';
    a.rel = 'noopener noreferrer';
    a.textContent = article.title || '(無題)';
    h2.appendChild(a);
    card.appendChild(h2);

    if (article.summary) {
      const p = document.createElement('p');
      p.className = 'article-summary';
      p.textContent = article.summary;
      card.appendChild(p);
    }

    const meta = document.createElement('div');
    meta.className = 'article-meta';
    if (article.matched_keyword) {
      const k = document.createElement('span');
      k.className = 'matched-keyword';
      k.textContent = `# ${article.matched_keyword}`;
      meta.appendChild(k);
    }
    if (article.source) {
      const s = document.createElement('span');
      s.className = 'source';
      s.textContent = article.source;
      meta.appendChild(s);
    }
    if (article.published_at) {
      const p = document.createElement('span');
      p.textContent = `公開: ${formatDate(article.published_at)}`;
      meta.appendChild(p);
    }
    if (article.fetched_at) {
      const f = document.createElement('span');
      f.textContent = `取得: ${formatDate(article.fetched_at)}`;
      meta.appendChild(f);
    }
    if (article.lang) {
      const l = document.createElement('span');
      l.textContent = article.lang.toUpperCase();
      meta.appendChild(l);
    }
    card.appendChild(meta);

    if (isFavoriteable(article)) {
      meta.appendChild(buildFavoriteButton(article));
    }

    if (Array.isArray(article.tags) && article.tags.length) {
      const tags = document.createElement('div');
      tags.className = 'tags';
      for (const t of article.tags) {
        const chip = document.createElement('span');
        chip.className = 'tag';
        chip.textContent = t;
        tags.appendChild(chip);
      }
      card.appendChild(tags);
    }

    return card;
  }

  function buildEmptyMessage(query) {
    const reasons = [];
    if (query) reasons.push(`「${query}」`);
    if (state.selectedKeyword !== KEYWORD_ALL) reasons.push(`キーワード「${state.selectedKeyword}」`);
    if (state.favoritesOnly) reasons.push('お気に入り');
    const periodLabel = DATE_LABELS[state.dateRange];
    if (periodLabel) {
      if (reasons.length) {
        return `直近${periodLabel}で${reasons.join('かつ')}に一致する記事はありません。期間を広げてみてください。`;
      }
      return `直近${periodLabel}に新着記事はありません。期間を広げてみてください。`;
    }
    if (reasons.length) {
      return `${reasons.join('かつ')}に一致する記事はありません。`;
    }
    return 'まだ新着記事がありません。';
  }

  function setupDateChips() {
    if (!$dateFilterRow) return;
    $dateFilterRow.addEventListener('click', (e) => {
      const btn = e.target.closest('.chip');
      if (!btn) return;
      const range = btn.dataset.range;
      if (!range) return;
      state.dateRange = range;
      $dateFilterRow.querySelectorAll('.chip').forEach((b) => {
        const active = b.dataset.range === state.dateRange;
        b.classList.toggle('chip-active', active);
        b.setAttribute('aria-pressed', active ? 'true' : 'false');
      });
      runSearch();
    });
  }

  function buildKeywordList(articles) {
    const seen = new Set();
    const order = [];
    for (const a of articles) {
      const k = a && a.matched_keyword;
      if (k && !seen.has(k)) {
        seen.add(k);
        order.push(k);
      }
    }
    return order;
  }

  function renderKeywordChips(keywords) {
    $chipsRow.innerHTML = '';
    if (keywords.length < 2) {
      $chipsRow.hidden = true;
      return;
    }
    $chipsRow.hidden = false;

    const all = createChip('すべて', KEYWORD_ALL);
    $chipsRow.appendChild(all);
    for (const k of keywords) {
      $chipsRow.appendChild(createChip(k, k));
    }
    updateChipActive();
  }

  function createChip(label, value) {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'chip';
    btn.dataset.value = value;
    btn.textContent = label;
    btn.addEventListener('click', () => {
      state.selectedKeyword = value;
      updateChipActive();
      runSearch();
    });
    return btn;
  }

  function updateChipActive() {
    const chips = $chipsRow.querySelectorAll('.chip');
    chips.forEach((c) => {
      if (c.dataset.value === state.selectedKeyword) {
        c.classList.add('chip-active');
        c.setAttribute('aria-pressed', 'true');
      } else {
        c.classList.remove('chip-active');
        c.setAttribute('aria-pressed', 'false');
      }
    });
  }

  function applyTitle(config, articles) {
    let names = [];
    if (config && Array.isArray(config.keywords)) {
      names = config.keywords
        .map((k) => (typeof k === 'string' ? k : k && k.name))
        .filter(Boolean);
    } else if (config && typeof config.keyword === 'string' && config.keyword) {
      names = [config.keyword];
    }
    if (!names.length && Array.isArray(articles)) {
      const seen = new Set();
      for (const a of articles) {
        const k = a && a.matched_keyword;
        if (k && !seen.has(k)) {
          seen.add(k);
          names.push(k);
        }
      }
    }
    if (!names.length) return;
    const joined = names.join(' / ');
    $title.textContent = `Daily Research: ${joined}`;
    document.title = `Daily Research: ${joined}`;
  }

  function renderSampleBanner(isSample) {
    if (!$sampleBanner) return;
    $sampleBanner.hidden = !isSample;
  }

  function renderLastUpdated(text) {
    if (!text || !text.trim()) {
      $lastUpdated.textContent = '最終更新: ―';
      return;
    }
    const trimmed = text.trim();
    const d = new Date(trimmed);
    if (!isNaN(d.getTime())) {
      $lastUpdated.textContent = `最終更新: ${formatDateTime(d)}`;
    } else {
      $lastUpdated.textContent = `最終更新: ${trimmed}`;
    }
  }

  function fetchArticlesWithFallback() {
    return fetchJson('./data/articles.json')
      .catch(() => null)
      .then((arr) => {
        if (Array.isArray(arr) && arr.length > 0) {
          return { articles: arr, isSample: false };
        }
        const inline = readInlineSample();
        if (inline.length > 0) {
          return { articles: inline, isSample: true };
        }
        return { articles: Array.isArray(arr) ? arr : [], isSample: false };
      });
  }

  function readInlineSample() {
    try {
      const el = document.getElementById('fallback-sample');
      if (!el) return [];
      const txt = (el.textContent || '').trim();
      if (!txt) return [];
      const data = JSON.parse(txt);
      return Array.isArray(data) ? data : [];
    } catch (e) {
      console.warn('inline sample parse failed:', e);
      return [];
    }
  }

  function byFetchedAtDesc(a, b) {
    const ta = a.fetched_at ? Date.parse(a.fetched_at) : 0;
    const tb = b.fetched_at ? Date.parse(b.fetched_at) : 0;
    return tb - ta;
  }

  function formatDate(s) {
    if (!s) return '';
    const d = new Date(s);
    if (isNaN(d.getTime())) return s;
    return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
  }

  function formatDateTime(d) {
    return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())} ${pad(d.getHours())}:${pad(d.getMinutes())}`;
  }

  function pad(n) {
    return String(n).padStart(2, '0');
  }

  function fetchJson(url) {
    return fetch(url, NO_CACHE).then((r) => {
      if (!r.ok) throw new Error(`${r.status} ${url}`);
      return r.json();
    });
  }

  function fetchText(url) {
    return fetch(url, NO_CACHE).then((r) => {
      if (!r.ok) throw new Error(`${r.status} ${url}`);
      return r.text();
    });
  }

  function isFavoriteable(article) {
    return !!(article && article.id && !String(article.id).startsWith('sample'));
  }

  function loadFavorites() {
    try {
      const raw = localStorage.getItem(FAVORITES_KEY);
      if (!raw) return;
      const parsed = JSON.parse(raw);
      if (!parsed || !Array.isArray(parsed.ids)) return;
      state.favorites = new Set(parsed.ids);
      const meta = parsed.meta && typeof parsed.meta === 'object' ? parsed.meta : {};
      state.favoritesMeta = new Map(Object.entries(meta));
    } catch (e) {
      console.warn('failed to load favorites:', e);
      state.favorites = new Set();
      state.favoritesMeta = new Map();
    }
  }

  function saveFavorites() {
    try {
      const meta = {};
      for (const [id, v] of state.favoritesMeta.entries()) {
        if (state.favorites.has(id)) meta[id] = v;
      }
      const payload = {
        version: FAVORITES_VERSION,
        ids: Array.from(state.favorites),
        meta
      };
      localStorage.setItem(FAVORITES_KEY, JSON.stringify(payload));
    } catch (e) {
      console.warn('failed to save favorites:', e);
    }
  }

  function pruneStaleFavorites(articles) {
    if (!state.favorites.size) return;
    const valid = new Set(articles.map((a) => a.id).filter(Boolean));
    let changed = false;
    for (const id of Array.from(state.favorites)) {
      if (!valid.has(id)) {
        state.favorites.delete(id);
        state.favoritesMeta.delete(id);
        changed = true;
      }
    }
    if (changed) saveFavorites();
  }

  function toggleFavorite(articleId) {
    if (!articleId) return;
    if (state.favorites.has(articleId)) {
      state.favorites.delete(articleId);
      state.favoritesMeta.delete(articleId);
    } else {
      state.favorites.add(articleId);
      state.favoritesMeta.set(articleId, { favorited_at: new Date().toISOString() });
    }
    saveFavorites();
    updateFavCount();
    if (state.favoritesOnly) runSearch();
  }

  function buildFavoriteButton(article) {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'fav-btn';
    const isFav = state.favorites.has(article.id);
    btn.setAttribute('aria-pressed', isFav ? 'true' : 'false');
    btn.setAttribute('aria-label', isFav ? 'お気に入りから外す' : 'お気に入りに追加');
    btn.textContent = isFav ? '★' : '☆';
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      toggleFavorite(article.id);
      const nowFav = state.favorites.has(article.id);
      btn.setAttribute('aria-pressed', nowFav ? 'true' : 'false');
      btn.setAttribute('aria-label', nowFav ? 'お気に入りから外す' : 'お気に入りに追加');
      btn.textContent = nowFav ? '★' : '☆';
    });
    return btn;
  }

  function setupFavoriteFilter() {
    if (!$favToggle) return;
    $favToggle.addEventListener('click', () => {
      state.favoritesOnly = !state.favoritesOnly;
      $favToggle.classList.toggle('chip-active', state.favoritesOnly);
      $favToggle.setAttribute('aria-pressed', state.favoritesOnly ? 'true' : 'false');
      runSearch();
    });
  }

  function setupFavoriteExport() {
    if (!$favExport) return;
    $favExport.addEventListener('click', exportFavoritesJson);
  }

  function exportFavoritesJson() {
    const favorites = Array.from(state.favorites).map((id) => {
      const m = state.favoritesMeta.get(id) || {};
      return { id, favorited_at: m.favorited_at || null };
    });
    const payload = {
      version: FAVORITES_VERSION,
      exported_at: new Date().toISOString(),
      favorites
    };
    const blob = new Blob([JSON.stringify(payload, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'favorites.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(() => URL.revokeObjectURL(url), 0);
  }

  function renderFavoriteRow() {
    if (!$favRow) return;
    $favRow.hidden = state.isSample;
  }

  function updateFavCount() {
    if (!$favCount) return;
    $favCount.textContent = String(state.favorites.size);
  }

  function setRepoLinkFromLocation() {
    try {
      const host = location.hostname;
      const m = host.match(/^([^.]+)\.github\.io$/);
      if (!m) {
        $repoLink.textContent = 'GitHub';
        return;
      }
      const owner = m[1];
      const segments = location.pathname.split('/').filter(Boolean);
      const repo = segments[0] || 'daily-research';
      $repoLink.href = `https://github.com/${owner}/${repo}`;
    } catch (_) {
      $repoLink.textContent = 'GitHub';
    }
  }
})();
