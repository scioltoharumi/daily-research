#!/usr/bin/env python3
import json, hashlib

FETCHED_AT = "2026-06-05T14:30:00+09:00"

new_articles = [
  {
    "id": "f09ec984629c",
    "title": "AIがAIを作る時代の到来か――Anthropicが示す「再帰的自己改善」の実態とリスク",
    "url": "https://www.itmedia.co.jp/aiplus/article/2606/05/2000000061/",
    "url_normalized": "itmedia.co.jp/aiplus/article/2606/05/2000000061",
    "summary": "Anthropicは2026年6月4日、自社のAIが独立して後継モデルを開発する「再帰的自己改善（Recursive Self-Improvement）」の現状とリスクを論じたブログ記事を公開し、ITmedia AI+が6月5日に報じた。同社のコードベースに組み込まれるコードの80%以上をClaudeが執筆しており、エンジニア1人当たりのコード生産量は2024年比で約8倍に達したと明かされた。AIが単独タスクを継続できる時間は2024年3月の4分から2026年2月の720分へ拡大し、タスク成功率は76〜89%に達している。Anthropicは「完全な再帰ループが実現した場合、モデルが後継を複利的な速度で生成し、ミスアラインメントが人類の制御を超えて増幅する可能性がある」と警告しつつも、開発の停止ではなく複数のAI開発組織間での検証可能な国際協調による管理強化を提案している。AIが自身の開発を主導するペースが人間のレビュー速度を超えつつある現実は、コードレビュー自体のAI支援強化が急務であることを示しており、安全性を担保しながら開発生産性を上げるという新たな業務設計の課題として現場に降りてきていると考えられる。",
    "source": "ITmedia AI+",
    "lang": "ja",
    "tags": ["Anthropic", "Claude", "再帰的自己改善", "AIリスク", "安全性"],
    "matched_keyword": "生成AI",
    "published_at": "2026-06-05",
    "fetched_at": FETCHED_AT
  },
  {
    "id": "e24e657afdf2",
    "title": "「仕事がなくなる？」“AIの影響”可視化へ　東大松尾研、Anthropic、PKSHAが協業",
    "url": "https://www.itmedia.co.jp/aiplus/article/2606/04/2000000058/",
    "url_normalized": "itmedia.co.jp/aiplus/article/2606/04/2000000058",
    "summary": "東京大学の松尾・岩澤研究室は2026年6月4日、米AnthropicおよびPKSHA Technologyと協力し、日本におけるAI影響を実測する基盤「Japan AI Index」の構築を発表した。同プロジェクトはLLM利用統計データと経済・雇用・教育に関する日本の公的データを組み合わせ、職種ごとのAI活用実態・年齢や地域別の利用率・生産性変化などを継続的に測定する。松尾研が中立的な分析設計を主導し、AnthropicはClaudeの利用統計データを、PKSHAは企業へのAI実装から得た知見を提供する役割分担で、2026年10〜11月に初回レポートとダッシュボードの公開を予定している。PKSHA代表は「漠然とした不安はあるのに、ファクトベースで議論できる土台がない」と指摘しており、同インデックスの公表が日本社会での建設的なAI議論の出発点になることを目指す。生成AIが業務に浸透する速度と実態を定量的に可視化することで、企業がAI投資の優先順位や人材再配置の判断に使えるエビデンスが初めて整う可能性があり、日本のAI政策・経営判断を証拠ベースに引き上げる試みとして注目される。",
    "source": "ITmedia AI+",
    "lang": "ja",
    "tags": ["Japan AI Index", "東京大学", "Anthropic", "PKSHA", "雇用"],
    "matched_keyword": "生成AI",
    "published_at": "2026-06-04",
    "fetched_at": FETCHED_AT
  },
  {
    "id": "e3567c4784c7",
    "title": "Microsoft、初の自社推論モデル「MAI-Thinking-1」発表　蒸留なしでゼロから学習",
    "url": "https://www.itmedia.co.jp/aiplus/article/2606/03/2000000050/",
    "url_normalized": "itmedia.co.jp/aiplus/article/2606/03/2000000050",
    "summary": "MicrosoftはBuild 2026開発者会議（2026年6月2日・米国時間）で、同社初の自社開発推論モデル「MAI-Thinking-1」を発表し、ITmediaが6月3日に報じた。アクティブパラメータ数350億のMoEアーキテクチャで、他モデルからの蒸留を一切行わず商用ライセンス済みのクリーンデータのみで学習した点が特徴で、エンタープライズグレードの信頼性を訴求する。独自AIアクセラレーター「Maia 200」で動作し、NVIDIA GB200比で1ワット当たり1.4倍の電力効率を実現。性能面ではClaude Sonnet 4.6よりブラインドテストで高評価を獲得し、SWE-bench Proで53%を達成した。MicrosoftはOpenAIへの依存を段階的に低減しながら自社AIモデルファミリー「MAI」を構築しており、Azure Agent Mesh・Office 365エージェントモード・Windows Agent Frameworkなど職場全体をAIで刷新するプラットフォーム戦略の中核として位置づけている。推論コスト効率の高い自社モデルが整うことで、Azure上での大規模エージェント展開のコスト障壁が下がり、業務自動化プロジェクトの投資対効果が改善すると考えられる。",
    "source": "ITmedia AI+",
    "lang": "ja",
    "tags": ["Microsoft", "MAI-Thinking-1", "推論モデル", "Build 2026", "自社開発"],
    "matched_keyword": "生成AI",
    "published_at": "2026-06-03",
    "fetched_at": FETCHED_AT
  },
  {
    "id": "42d6ebc25f01",
    "title": "三菱重工×Preferred Networks、国産AI共同開発で業務提携｜社会インフラ・防衛の自律化へ",
    "url": "https://innovatopia.jp/ai/ai-news/107091/",
    "url_normalized": "innovatopia.jp/ai/ai-news/107091",
    "summary": "三菱重工業とPreferred Networks（PFN）は2026年6月2日、社会インフラ・防衛分野の自律化を目指す業務提携契約を締結したと発表し、innovatopiaが6月4日に報じた。三菱重工のハードウェア・制御技術とPFNのAI基盤モデル・AI半導体を組み合わせ、「運用の知能化・自律化、高度な予測保全、危機管理の迅速化」を実現することを目的とし、2026年度内に資本業務提携契約の締結を目指す。背景には国産AIへの需要増大と、海外製AIに依存した場合の経済安全保障上のリスクがある。PFNは日本最大規模の計算機「MN-3」を保有し独自のAI半導体「MN-Core」も開発してきた実績を持つが、防衛・インフラ用途への大規模展開には三菱重工の産業システム統合ノウハウが不可欠であった。重工業×AI研究機関という異業種の資本提携は、日本製造業でのAIエージェント・自律システム実装を加速させる可能性があり、過酷な現場環境での設備保守や異常検知といった「人が立ち入りにくい業務」をAIが代替する実用段階への移行が近づいていると考えられる。",
    "source": "innovatopia",
    "lang": "ja",
    "tags": ["三菱重工", "Preferred Networks", "国産AI", "社会インフラ", "業務提携"],
    "matched_keyword": "生成AI",
    "published_at": "2026-06-04",
    "fetched_at": FETCHED_AT
  },
  {
    "id": "6fcabd1d1ffc",
    "title": "AIエージェントが国内1,127社のDXを全件解析。「DX INSIGHTS AWARD 2026」にて先進的な取り組みを推進する企業を選定",
    "url": "https://prtimes.jp/main/html/rd/p/000000309.000038674.html",
    "url_normalized": "prtimes.jp/main/html/rd/p/000000309.000038674.html",
    "summary": "株式会社SIGNATEは2026年6月3日、独自開発のAIエージェントを活用して国内上場企業1,127社の統合報告書を全件解析し、優れたDX推進企業を選出する「DX INSIGHTS AWARD 2026」を発表した。情報収集・分析・5項目のスコアリング・レポートの誌面デザインに至る全工程をAIエージェントが自律的に完結させた点が特徴で、人の主観を排除し企業が公表した事実のみを均一なアルゴリズムで評価した。1,000社超・累計5万ページ超の統合報告書を横断解析することは人力では不可能な規模であり、総合グランプリには旭化成（スコア70.5）が選ばれ、ソフトバンク（68.9）・武田薬品工業（67.8）・西日本旅客鉄道（67.8）が続いた。知名度や企業規模に依存しない定量的なDX評価の公開は、投資家・取引先・求職者が企業の実態を把握しやすくする情報インフラになる可能性を示す。AIが自律的に大量文書を読解・評価するワークフローが実用段階にあることを示した事例でもあり、企業内の大量文書（規程・報告書・議事録）を継続的にAI分析するBPRへの応用可能性が高まっていると考えられる。",
    "source": "PR TIMES（SIGNATE）",
    "lang": "ja",
    "tags": ["SIGNATE", "AIエージェント", "DX", "企業評価", "統合報告書"],
    "matched_keyword": "業務改革",
    "published_at": "2026-06-03",
    "fetched_at": FETCHED_AT
  },
  {
    "id": "25f07e82e8cc",
    "title": "Wired found code for an unreleased facial recognition feature in Meta's AI app",
    "url": "https://www.engadget.com/2187824/wired-found-code-for-an-unreleased-facial-recognition-feature-in-meta-s-ai-app/",
    "url_normalized": "engadget.com/2187824/wired-found-code-for-an-unreleased-facial-recognition-feature-in-meta-s-ai-app",
    "summary": "テック系メディアWiredは2026年6月4日、MetaのAIアプリに「NameTag」と呼ばれる未公開の顔認証機能のコードが埋め込まれていることを発見し、Engadgetが同日報じた。Ray-BanとOakleyのスマートグラス向けAIアプリ内で3つの機械学習モデルが顔を検出・照合するこの機能は、2026年1月頃から数千万台のスマートフォンにすでに配布されており、セキュリティ研究者は「ほぼ機能完成状態」と評価している。現時点では無効化されサーバーへの生体データ送信もないとMetaは説明するが、サーバー側の更新のみで容易に有効化できる可能性があり、ACLUを含む75の市民団体が即座の廃止を要求した。Metaは2021年に同様の技術を廃止した経緯があり、今回も「探索中の段階」だと主張するが、数千万台のデバイスに同意なく他者の顔をリアルタイム識別できる技術が先行展開されていた現実は大きな問題を提起している。日本の個人情報保護法改正（2028年施行見込みの生体情報強化規定）が整う前に消費者向けウェアラブルでの大規模展開が先行するリスクを示す事例であり、「デバイスに搭載済みでいつでも有効化できる技術」への規制的視点の重要性が高まっていると考えられる。",
    "source": "Engadget",
    "lang": "en",
    "tags": ["Meta", "スマートグラス", "顔認証", "NameTag", "プライバシー"],
    "matched_keyword": "顔認証",
    "published_at": "2026-06-04",
    "fetched_at": FETCHED_AT
  },
  {
    "id": "9d8ebb94b602",
    "title": "Possible Early Saw Technology Uncovered in Japan",
    "url": "https://archaeology.org/news/2026/06/05/possible-early-saw-technology-uncovered-in-japan/",
    "url_normalized": "archaeology.org/news/2026/06/05/possible-early-saw-technology-uncovered-in-japan",
    "summary": "福井県立埋蔵文化財調査研究センターの魚津友勝氏らは2026年6月5日、福井県の林・富島遺跡から紀元2世紀後期の鉄製小型工具を発見したとArchaeology Magazineが報じた。全長約5センチ未満のくちばし型の鉄器で、先端は尖り縁に沿って小さな三角形の歯が規則的に並んでいる。研究チームはこれを「ノコギリ」の可能性がある工具と解釈しており、中国で出土している2〜3世紀の同様の鋸歯状鉄器と構造的に類似することを確認した。「この工芸品は日本海沿岸の弥生時代における鉄製品文化の進歩を支持する重要な証拠となりうる」と魚津氏は評価する。2世紀の日本においてノコギリ状工具が存在したとすれば、大陸から渡来した鉄器技術が東日本にまで及んでいた可能性を示し、弥生時代の技術交流ネットワークの範囲を再評価する手がかりになると考えられる。埋蔵文化財のデジタル記録・3D計測技術の普及が細部の比較研究を可能にしており、地方機関が保管する未解析標本からも今後類似の再発見が続くと予想される。",
    "source": "Archaeology Magazine",
    "lang": "en",
    "tags": ["考古学", "弥生時代", "福井県", "鉄器", "鋸歯"],
    "matched_keyword": "歴史・教養",
    "published_at": "2026-06-05",
    "fetched_at": FETCHED_AT
  },
  {
    "id": "c9009e9db5ec",
    "title": "18th-Century Shipwreck Discovered in Deep Water Near Norway",
    "url": "https://archaeology.org/news/2026/06/04/18th-century-shipwreck-discovered-in-deep-water-near-norway/",
    "url_normalized": "archaeology.org/news/2026/06/04/18th-century-shipwreck-discovered-in-deep-water-near-norway",
    "summary": "ノルウェー海洋博物館のスヴェン・アーレンス氏らは2026年6月4日、スカゲラック海峡の水深約600メートルの海底で18世紀の商船が高い保存状態で発見されたとArchaeology Magazineが報じた。船内には中国製磁器・ガラス製品・シャンデリア・封印された木箱などの積み荷が海底に整然と残っており、「完全な皿が積み重なって海底に置かれていた」と研究者は述べた。無人潜水機（ROV）で約40点の遺物を回収し、沈没場所の3Dモデルも作成した。積み荷の構成からゴーテンブルク・コペンハーゲン・アムステルダムのいずれかの港で中国産品を積み込み北ヨーロッパ海域を航行中に沈んだと推定され、海洋考古学者のイヴァル・アーレスタッド氏は「経済史の理解を深める重要な役割を担う」と評価する。深海という環境が腐敗を防いだことで積み荷が当時のままの状態で残っており、18世紀ヨーロッパの東洋貿易ルートや商品流通の実態を一次資料から再構成できる稀有な機会となっている。ROVや3Dフォトグラメトリーなどのデジタル調査技術がこれまで到達不可能だった深海遺跡を非破壊的に記録・解析できる段階に入ったことを示す好例と考えられる。",
    "source": "Archaeology Magazine",
    "lang": "en",
    "tags": ["考古学", "沈没船", "ノルウェー", "18世紀", "海洋考古学"],
    "matched_keyword": "歴史・教養",
    "published_at": "2026-06-04",
    "fetched_at": FETCHED_AT
  },
  {
    "id": "86ba9373b319",
    "title": "Ancient Egyptian Capital City Investigated",
    "url": "https://archaeology.org/news/2026/06/05/ancient-egyptian-capital-city-investigated/",
    "url_normalized": "archaeology.org/news/2026/06/05/ancient-egyptian-capital-city-investigated",
    "summary": "エジプト最高考古評議会は2026年6月5日、エジプト中部のイフナスィヤ・アル・マディーナ（古代名ヘラクレオポリス・マグナ）の調査成果を発表した。この都市は紀元前22〜21世紀にエジプト第9・10王朝の首都として栄えた場所で、今回の発掘ではセンウセルト3世のカルトゥーシュが刻まれた再利用石材、ドーリア様式ギリシャ神殿の痕跡、ローマ時代のバシリカ遺跡、愛の女神アフロディーテの大理石頭部彫刻、ローマ時代のコイン製造用陶製型などが出土した。多様な時代の遺構が一箇所に重層的に残ることは、この都市が古代エジプト・ヘレニズム・ローマという三文明期にわたり主要拠点であり続けた証拠である。建造物を後継文明が再利用・改築してきたパターンが可視化されたことで、中東における文明の連続性と接触が改めて裏付けられた。デジタルGISや3D地中探査技術の進歩により広大な複合遺跡の全体像を系統的に記録・共有できる環境が整い、国際共同研究の加速によって過去の発掘断片が統合される新しい段階に入りつつあると考えられる。",
    "source": "Archaeology Magazine",
    "lang": "en",
    "tags": ["考古学", "古代エジプト", "ヘラクレオポリス", "ローマ時代", "発掘"],
    "matched_keyword": "歴史・教養",
    "published_at": "2026-06-05",
    "fetched_at": FETCHED_AT
  }
]

# Load existing articles
with open('/home/user/daily-research/data/articles.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

# Check for duplicates
existing_ids = {a['id'] for a in existing}
existing_urls = {a['url_normalized'] for a in existing}
dupes = []
for a in new_articles:
    if a['id'] in existing_ids:
        dupes.append(f"DUPLICATE ID: {a['id']}")
    if a['url_normalized'] in existing_urls:
        dupes.append(f"DUPLICATE URL: {a['url_normalized']}")

if dupes:
    for d in dupes:
        print(d)
else:
    print("No duplicates found")

print(f'New articles: {len(new_articles)}')
print(f'Existing articles: {len(existing)}')

# Prepend new articles
combined = new_articles + existing

# Sort by fetched_at descending
combined.sort(key=lambda x: x.get('fetched_at', ''), reverse=True)

# Validate JSON
json_str = json.dumps(combined, ensure_ascii=False, indent=2)
json.loads(json_str)  # self-validation

print(f'Total articles after merge: {len(combined)}')
print('JSON validation: OK')

# Write
with open('/home/user/daily-research/data/articles.json', 'w', encoding='utf-8') as f:
    f.write(json_str + '\n')

print('Written successfully')
