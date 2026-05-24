# プロジェクト規約

## PRの作成・マージ方針

ユーザーの恒久的な承認に基づき、本リポジトリでは以下を**事前確認なしで自律実行してよい**:

- 作業ブランチへの commit & push
- そのブランチからの Pull Request の作成
- 作成した PR のマージ（base ブランチは `main`）

マージ方式は通常の merge commit でよい。マージ後はリモートの作業ブランチを削除する。

ただし以下は引き続き事前確認が必要:

- `main` への直接 push
- `git push --force`、`git reset --hard`、ブランチ削除（リモートのフィーチャーブランチ削除を除く）等の破壊的操作
- CI が赤い PR のマージ（落ちている理由を診断してから判断する）
- 機微な変更（認証、課金、デプロイ設定、秘密情報の取り扱いなど）

## 触らないファイル

`prompts/daily-research.md` のリサーチエージェント本体が触らない約束のファイル群（`index.html` / `app.js` / `style.css` / `config.json` / `prompts/` / `README.md` / `data/articles.sample.json` / `data/favorites.json`）は、エージェント実行時の制約。**通常の開発作業ではこれらの編集は許可されている**ので混同しないこと。
