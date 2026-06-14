import json

new_articles = [
  {
    "id": "17c1da8c6bba",
    "title": "Anthropic、「Mythos 5」「Fable 5」の提供を一時停止　米政府指示を受け",
    "url": "https://www.itmedia.co.jp/aiplus/article/2606/13/2000000087/",
    "url_normalized": "itmedia.co.jp/aiplus/article/2606/13/2000000087",
    "summary": "Anthropicは2026年6月12日（米国時間）、米政府から輸出管理指令を受け、AIモデル「Claude Fable 5」と「Claude Mythos 5」への全アクセスを即日停止した。指令は米国東部時間の午後5時21分に届き、「米国内外を問わずすべての外国人」へのアクセス遮断を求めるもので、外国籍のAnthropicの従業員も対象に含まれる。政府側の主張はFable 5の安全装置を回避するジェイルブレイク手法が確認されたというものだが、AnthropicはCNBCへの声明で「同様の脆弱性は他の主要モデルにも存在し、この基準を業界全体に適用すれば新規モデルのデプロイは実質的に停止する」と反論しながら法的指示には従った。生成AIを国家安全保障の文脈で輸出管理の対象とし、政府が直接の停止命令を発した点は異例であり、フロンティアAIの規制枠組みが具体的な「提供停止命令」という形で現実化した最初の事例と位置づけられる。AIモデルの輸出規制が本格化すれば、業務にフロンティアAIを組み込む企業は代替モデルの確保と法的対応を事前に計画に織り込む必要性が高まると考えられる。",
    "source": "ITmedia AI+",
    "lang": "ja",
    "tags": ["Anthropic", "輸出規制", "Claude", "国家安全保障", "ジェイルブレイク"],
    "matched_keyword": "生成AI",
    "published_at": "2026-06-13",
    "fetched_at": "2026-06-14T06:07:27+09:00"
  },
  {
    "id": "f57f80cd4a13",
    "title": "データセンター建設に足りないのは「発電」ではなく「送電」　AI需要で電力消費26％増、Gartner予想",
    "url": "https://www.itmedia.co.jp/aiplus/article/2606/12/2000000083/",
    "url_normalized": "itmedia.co.jp/aiplus/article/2606/12/2000000083",
    "summary": "Gartnerは2026年6月、世界のデータセンター電力消費量が2025年の447テラワット時（TWh）から2026年には26%増の565TWhに達するとの予測を発表し、ITmedia AI+が6月12日に報じた。AI最適化サーバが2026年のデータセンター全体の31%を占め、2030年には1200TWh超に達する見通しという。注目すべきは、国内における問題の核心が「発電不足」ではなく「送電網の整備不足」にある点で、北海道〜本州間の送電整備だけで約1.5〜1.8兆円を要するとされ、資金調達と費用回収が最大のボトルネックとされている。生成AIの基盤拡張ペースが電力インフラの更新速度を上回ることで、データセンターの立地選定や電力調達コストが企業のAI戦略の制約条件として表面化しつつある。AIサービスを業務で本格活用しようとする企業にとっては、クラウドベンダーの稼働保証や送電インフラへの依存リスクを考慮した調達先選定が中長期の業務設計の前提条件になっていくと考えられる。",
    "source": "ITmedia AI+",
    "lang": "ja",
    "tags": ["データセンター", "電力インフラ", "Gartner", "AI需要", "送電"],
    "matched_keyword": "生成AI",
    "published_at": "2026-06-12",
    "fetched_at": "2026-06-14T06:07:27+09:00"
  },
  {
    "id": "278e7c2dee27",
    "title": "「人型ロボ世界シェア1位」中国Unitreeに聞く“普及戦略”　日本市場をどう開拓？",
    "url": "https://www.itmedia.co.jp/aiplus/article/2606/12/2000000080/",
    "url_normalized": "itmedia.co.jp/aiplus/article/2606/12/2000000080",
    "summary": "中国Unitree Roboticsは2025年に二足歩行人型ロボット市場で世界シェア約40%を獲得し、売上高392億円・前年比435%増という急成長を遂げた企業だ。ITmedia AI+のインタビューに応じた同社幹部は、少子高齢化に伴う労働力不足が深刻な日本市場を「規模感としてトップクラスに重要」と位置づけ、飲食・介護などの労働集約型産業への参入に向けて代理店連携・ローカライズ・リースサービスを通じた展開を計画していると明かした。中国AI（ソフトウェア）と比較的安価な人型ロボット（ハードウェア）が組み合わさることで、従来は人間の手作業に依存していた定型作業の自動化が経済的な現実解に近づきつつある。日本の現場にはロボット導入に対する文化的・法的な障壁も残るが、人型ロボットが繰り返し作業を担うことで人が判断・接客・創造的問題解決といった高付加価値の業務に集中できる職場設計が現実的な選択肢として浮上してきた可能性があると考えられる。",
    "source": "ITmedia AI+",
    "lang": "ja",
    "tags": ["Unitree", "人型ロボット", "労働力不足", "日本市場", "製造自動化"],
    "matched_keyword": "業務改革",
    "published_at": "2026-06-12",
    "fetched_at": "2026-06-14T06:07:27+09:00"
  },
  {
    "id": "9239e28ce1e8",
    "title": "Genetic Study Offers Clues to Survival in the Peruvian Andes",
    "url": "https://archaeology.org/news/2026/06/12/genetic-study-offers-clues-to-survival-in-the-peruvian-andes/",
    "url_normalized": "archaeology.org/news/2026/06/12/genetic-study-offers-clues-to-survival-in-the-peruvian-andes",
    "summary": "バッファロー大学のオマー・ゴックメン氏らの研究チームは2026年6月12日、世界85集団・3700人以上のゲノムデータを解析した結果、ペルーのアンデス先住民がサリバリー・アミラーゼ遺伝子（唾液中のアミラーゼ酵素をコードし、デンプンを糖に分解する）のコピー数が世界で最も多いことを学術誌『Nature Communications』に発表した。約1万年前にアンデスでジャガイモが栽培化されて以降、炭水化物の消化効率が高い個体が生存・繁殖において有利だったことで自然選択が働いた結果とゴックメン氏は解釈しており、「まさに生死に関わる選択圧だった」と述べている。アリゾナ南西部のアキメル・オオダム族でも類似の高コピー数が確認され、地理的に離れた集団でも農耕化が同様の遺伝的変化をもたらした可能性が示唆される。特定の作物の栽培が数千年にわたって集団の遺伝的構成を変えていったことは、食文化と生物進化の深い相互作用を示す直接的な証拠となる。ゲノム解析技術の精緻化により「食と進化の関係」が分子レベルで解読できる時代に入っており、農業の起源や人類の適応戦略に関する研究が今後さらに進展すると考えられる。",
    "source": "Archaeology Magazine",
    "lang": "en",
    "tags": ["考古学", "アンデス", "遺伝学", "ジャガイモ", "食文化"],
    "matched_keyword": "歴史・教養",
    "published_at": "2026-06-12",
    "fetched_at": "2026-06-14T06:07:27+09:00"
  },
  {
    "id": "37dd81718145",
    "title": "Neolithic Figurines Uncovered in Northeastern Anatolia",
    "url": "https://archaeology.org/news/2026/06/12/neolithic-figurines-uncovered-in-northeastern-anatolia/",
    "url_normalized": "archaeology.org/news/2026/06/12/neolithic-figurines-uncovered-in-northeastern-anatolia",
    "summary": "アナドール大学のアリ・ウムト・テュルクチャン氏らの調査チームは2026年6月12日、トルコ・エスキシェヒル州のカンリタシュ・ホユック（新石器時代の丘状遺跡）から女性を象った頭部のない4体の素焼きテラコッタ像を発見したとArchaeology Magazineが報じた。最大のものは約12センチ、他の3体は約5センチで、長方形建物の下部埋め戻し層から出土した。頭部が意図的に切り離されたとみられる痕跡があり、建物閉鎖の際の儀礼として頭部が取り外された可能性を研究チームは示唆している。「腰部が強調されたプロポーション」という造形的特徴はポルスク文化の伝統に属しており、後の時代のバルカン半島の遺跡でも類似した様式が確認されることから、新石器時代における西方への文化伝播の証拠となる可能性がある。一方的な文化伝播ではなく、異なる集団が独自のモチーフを保ちながら相互に影響し合っていくプロセスを数千年前のテラコッタ像が示していることは、人類の情報伝達と文化交流の起源を理解するうえで重要な手がかりを与えると考えられる。",
    "source": "Archaeology Magazine",
    "lang": "en",
    "tags": ["考古学", "新石器時代", "トルコ", "アナトリア", "儀礼"],
    "matched_keyword": "歴史・教養",
    "published_at": "2026-06-12",
    "fetched_at": "2026-06-14T06:07:27+09:00"
  }
]

with open('data/articles.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

existing_urls = {a['url_normalized'] for a in existing}
new_unique = [a for a in new_articles if a['url_normalized'] not in existing_urls]
print(f"New unique articles: {len(new_unique)}")

combined = new_unique + existing
combined.sort(key=lambda a: a['fetched_at'], reverse=True)

json_str = json.dumps(combined, ensure_ascii=False, indent=2)
parsed = json.loads(json_str)
print(f"Total articles after update: {len(parsed)}")
print("JSON validation: OK")

with open('data/articles.json', 'w', encoding='utf-8') as f:
    f.write(json_str)
    f.write('\n')

print("articles.json written successfully")
