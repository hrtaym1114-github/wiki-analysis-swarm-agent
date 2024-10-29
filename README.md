# Wikipedia Analysis Swarm Agent

## 概要
このプロジェクトは、OpenAIのSwarmフレームワークを使用して、Wikipediaの記事を分析し、ユーザーの質問に対して包括的なレポートを生成するシステムです。

## 機能
- 質問に関連するWikipedia記事の自動検索
- 複数の記事からの情報収集
- AIによる分析レポートの生成
- 日本語Wikipediaに特化した検索と分析

## 必要条件
- Python 3.11以上
- Poetry

## インストール方法
1. リポジトリのクローン:
```
git clone [リポジトリURL]
cd wikipedia-analysis-swarm
```

2. 依存関係のインストール:
```
poetry install
```

3. 環境変数の設定:
`.env`ファイルを作成し、以下の内容を設定:
```
OPENAI_API_KEY=your_api_key_here
```

## 使用方法
1. プログラムの実行:
```
poetry run python wiki_analysis_swarm_agent.py
```

2. プロンプトが表示されたら、調査したい質問を入力してください。

## ライセンス
MIT

## 作者
Ayumu Harata