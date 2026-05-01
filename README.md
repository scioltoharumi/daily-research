# Daily Research

任意のキーワード（複数可）について、毎日自動でWeb調査を行い、結果を静的サイト（GitHub Pages）に蓄積していく仕組み。

- **初期キーワード**: 顔認証（`config.json` で複数指定・差し替え可能）
- **更新頻度**: 毎朝 06:00 JST
- **更新主体**: Claude Code Web 版の Scheduled Agent
- **公開URL**: `https://<your-github-user>.github.io/daily-research/`

サーバ・DB・ビルドツールは一切使わず、素のHTML/CSS/JavaScript と単一JSONファイルで完結している。
複数キーワードを設定した場合は、サイト上部にキーワード絞り込みチップが自動表示される。

---

## 仕組み

```text
[毎日 06:00 JST]
  Claude Code Web の Scheduled Agent がリポジトリを開く
    ↓
  config.json から keywords[]・関連語・件数 を読込
    ↓
  各キーワードについて WebSearch を複数クエリで実行（日本語＋英語）
    ↓
  WebFetch で記事本文取得 → タイトル/要約/タグ/matched_keyword を生成
    ↓
  data/articles.json を読み込み URL正規化キーで重複排除＆マージ
    ↓
  data/articles.json + data/last_updated.txt を更新
    ↓
  git commit & push
    ↓
  GitHub Pages が自動再デプロイ
    ↓
  ブラウザで https://<user>.github.io/daily-research/ を閲覧
```

サイトはトップに検索窓があり、タイトル・要約・タグに対して [Fuse.js](https://www.fusejs.io/) でリアルタイム絞り込みが効く。
検索窓の下に**期間フィルタ**（1日 / 1週間 / 1ヶ月 / 3ヶ月 / すべて、デフォルト1週間）があり、`published_at` を基準に記事を絞り込める（`published_at` が無ければ `fetched_at` にフォールバック）。
複数キーワードを設定した場合、その下にキーワードチップが自動表示されてキーワード単位の絞り込みもできる。検索・期間・キーワードはAND条件で重ねがけ可能。

各記事の `summary` には事実に加えて、**背景・文脈の考察**（なぜ今このタイミングで起こっているのか）と、**「ワクワクする仕事（無駄をなくし、効率的・生産的・楽しい仕事）」への示唆**が、章立てなしの1つの段落として350〜500字程度でまとめられる。

---

## ファイル構成

```text
.
├── README.md                  この説明
├── index.html                 サイト本体（末尾にフォールバックサンプル6件をインライン埋め込み）
├── app.js                     fetch + Fuse.js + 描画 + チップ + サンプルフォールバック
├── style.css                  CSS（ライト/ダーク自動切り替え）
├── config.json                キーワード・関連語・件数の設定（ここだけ変えれば挙動が変わる）
├── data/
│   ├── articles.json          全記事配列（増分追記、初期は空配列）
│   ├── last_updated.txt       最終実行時刻（ISO8601, JST）
│   └── favorites.json         お気に入りのエクスポート（任意・初回コミット時に出現）
└── prompts/
    └── daily-research.md      Scheduled Agent が読む実行手順
```

### サンプル表示の挙動

`articles.json` が空配列もしくは fetch 失敗時、`index.html` 末尾にインライン埋め込みされたサンプル記事6件が**自動で表示される**（上部に「サンプルデータを表示中」のバナーが出る）。
Scheduled Agent が記事を1件でも追加すると、自動的に実データに切り替わる。サンプルは fetch を使わないため、`file://` 直接開きでも動作確認できる。

---

## 初回セットアップ（マスター実施分）

### 1. リポジトリの作成と接続

GitHub で公開リポジトリ `daily-research` を新規作成（README あり、ライセンス MIT を推奨）。
ローカルにクローンし、本リポジトリの `repo/` 配下のファイル一式を配置・push する。

```bash
git clone https://github.com/<your-github-user>/daily-research.git
cd daily-research
# repo/ 配下のファイルをここに配置
git add .
git commit -m "feat: initial site and prompts"
git push
```

### 2. ローカルで表示確認（任意）

`index.html` をブラウザで直接開くだけでサンプルデータが表示される（サンプルは index.html にインライン埋め込み済みで、fetch を経由しないため `file://` でも動作する）。

`config.json` や `last_updated.txt` の内容まで含めて本番に近い挙動を確認したい場合は、`fetch` が同一オリジン経由になるよう簡易サーバを使う:

```bash
python -m http.server 8000
# → http://localhost:8000/
```

### 3. GitHub Pages の有効化

リポジトリの **Settings → Pages** で:

- **Source**: `Deploy from a branch`
- **Branch**: `main` / `/ (root)`

を選択して保存。数分後に `https://<your-github-user>.github.io/daily-research/` でサイトが表示される（初日はサンプルデータが見える）。

### 4. Scheduled Agent の登録

[claude.ai/code](https://claude.ai/code) でこのリポジトリを開き、`/schedule` コマンドで日次の routine を登録する。

- **cron**: `0 21 * * *` （UTC = JST 06:00）
- **prompt**:

  ```text
  prompts/daily-research.md の指示に厳密に従って、本日の調査を実行し、
  data/articles.json と data/last_updated.txt を更新してコミット&プッシュせよ。
  ```

登録後に `/schedule` から **手動1回実行** して、`data/articles.json` に新規記事が追加されサイトに反映されることを確認する。

---

## キーワードを変更・追加したいとき

`config.json` の `keywords` 配列を書き換えて push するだけ。

### 単一キーワード

```json
{
  "keywords": [
    {
      "name": "顔認証",
      "related_terms": ["生体認証", "face recognition", "facial recognition", "biometric authentication"]
    }
  ],
  "languages": ["ja", "en"],
  "max_per_run_per_keyword": 15,
  "lookback_hours": 48
}
```

### 複数キーワード

```json
{
  "keywords": [
    {
      "name": "顔認証",
      "related_terms": ["生体認証", "face recognition", "facial recognition"]
    },
    {
      "name": "音声認証",
      "related_terms": ["voice recognition", "speaker recognition", "声紋認証"]
    },
    {
      "name": "虹彩認証",
      "related_terms": ["iris recognition", "iris scan"]
    }
  ],
  "languages": ["ja", "en"],
  "max_per_run_per_keyword": 15,
  "lookback_hours": 48
}
```

複数キーワードのときは、サイト上部に「すべて / 顔認証 / 音声認証 / 虹彩認証」のチップが自動表示され、ワンクリックで絞り込める。
過去のデータ（`data/articles.json`）は履歴として保持される。完全に切り替えたい場合は `data/articles.json` を `[]` にリセットする。

### 件数制御の考え方

キーワードを増やすほど1日の収集件数も増えうる。設計では二段で制御している:

1. **`config.json` の `max_per_run_per_keyword`**: キーワード1つあたりの**上限**（デフォルト10）
2. **`prompts/daily-research.md` の規律**: 「上限であって目標ではない」「質の高い候補が少なければそのまま少なく終える」「ノイズで件数を埋めるくらいなら見送る」

| キーワード数 | 理論上限/日 | 想定実運用/日 | 月間想定 |
|-------------|-----------|-------------|---------|
| 1 | 10 | 3〜8 | 〜240件 |
| 3 | 30 | 10〜20 | 〜600件 |
| 4（現状） | 40 | 12〜25 | 〜750件 |
| 6 | 60 | 18〜35 | 〜1,000件 |

`max_per_run_per_keyword` を全体で揃えるのではなく**キーワードごとに個別**に持たせたい場合は、各 `keyword` エントリに `max_per_run` フィールドを追加し、エージェント側のプロンプトでオーバーライド処理を書けばよい（現状未実装、必要になれば対応）。

---

## お気に入り機能

各記事カードのメタ行右端に星ボタン（☆ / ★）があり、クリックでお気に入りを切り替えられる。状態はブラウザの `localStorage`（キー: `dr_favorites_v1`）に保存され、リロードしても残る。

### サイト上での絞り込み

ヘッダー下部の「★ お気に入りのみ」チップで、お気に入り登録した記事だけに絞り込める。検索 / 期間 / キーワードフィルタとは AND 条件で重ねがけ可能。

### Scheduled Agent への嗜好フィードバック

「エクスポート」ボタンで `favorites.json` をダウンロードし、`data/favorites.json` としてリポジトリに commit & push すると、翌朝以降の Scheduled Agent がそれを読み、嗜好プロファイル（頻出 source / matched_keyword / tags / 要約頻出語）を抽出する。

このプロファイルは **ハードフィルタではなく、品質審査時の加点要素**として使われる:

- 同程度の品質で甲乙つけ難い候補のあいだの優先順位付けにのみ使う
- 嗜好に合わないというだけで良質な記事は捨てない（多様性は意図的に残す）
- お気に入り件数が5件未満の場合は嗜好抽出をスキップする（ノイズ過多のため）

エクスポート＆コミットは数日に1回でOK。頻繁に行う必要はない。

### 制約

- サンプルデータ表示中は星ボタンが出ない（実データに切り替わってから使える）
- 過去の `articles.json` から消えた記事のお気に入りは、起動時に自動で `localStorage` から除去される
- バックエンドを持たない設計のため、ブラウザ間（端末間）でのお気に入り共有は手動エクスポート＆コミットに依存する

---

## 想定挙動

- **新着0件の日**: `last_updated.txt` だけが更新され、サイトには「最終更新」だけ進む
- **同じニュースの複数記事**: URL正規化＋title先頭40字一致で重複排除されるため、原則1本に絞られる
- **複数キーワードに該当しそうな記事**: 本文の主題に最も近いキーワード1つだけに紐付く（プロンプトで `keywords` 配列の上から評価し最初にマッチしたもの採用）
- **APIキー等は持たない設計**: `config.json` にも入れない。GitHub に上げてはいけない値はそもそも生まれない

---

## 技術的詳細

- **依存**: Fuse.js v7（CDN経由、`https://cdn.jsdelivr.net/npm/fuse.js@7.0.0/dist/fuse.min.js`）のみ
- **検索キー**: `title`（重み 0.45） / `summary`（0.35） / `tags`（0.2）
- **検索しきい値**: `threshold: 0.35`、`ignoreLocation: true`、`minMatchCharLength: 2`
- **ソート**: `fetched_at` 降順
- **期間フィルタ**: `published_at` 基準（無い場合は `fetched_at` にフォールバック）。1日 / 1週間 / 1ヶ月 / 3ヶ月 / すべて、デフォルトは1週間
- **キーワードフィルタ**: 記事の `matched_keyword` フィールドで判定。チップは記事中に出現する unique な keyword 集合から自動生成（1種類しかない場合はチップ非表示）
- **要約**: エージェントが生成。事実 + 背景・文脈 + 「ワクワクする仕事」への示唆を1段落で350〜500字
- **キャッシュ**: `fetch` に `cache: 'no-store'` を付け、Pagesのキャッシュを回避
- **ダーク対応**: `prefers-color-scheme` でCSS変数を切り替え
- **XSS対策**: 記事のレンダリングは全て `createElement` + `textContent`。`innerHTML` で外部データを埋めない
- **お気に入り**: `localStorage` のキー `dr_favorites_v1` に `{ version, ids[], meta }` で保存。エクスポート時は `{ version, exported_at, favorites[{id, favorited_at}] }` 形式で `favorites.json` にダウンロード。サンプル記事（id が `sample` で始まる）は対象外

---

## ライセンス

MIT
