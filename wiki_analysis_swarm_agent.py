from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
from swarm import Swarm, Agent
import urllib.parse
import time

# 環境変数の読み込み
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

class WikipediaAnalyzer:
    def __init__(self):
        self.base_url = "https://ja.wikipedia.org/wiki/"
        
    def collect_article_data(self, topic):
        """Wikipediaの記事データを収集"""
        print(f"\n🔍 Wikipedia記事「{topic}」の取得を開始...")
        
        try:
            # URLエンコードして日本語タイトルを処理可能な形式に変換
            encoded_topic = urllib.parse.quote(topic)
            url = f"{self.base_url}{encoded_topic}"
            print(f"📡 アクセスするURL: {url}")
            
            # 記事の取得
            response = requests.get(url)
            print(f"📥 ステータスコード: {response.status_code}")
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # 記事タイトルの取得
                title = soup.find(id="firstHeading").text
                print(f"📑 記事タイトル: {title}")
                
                # 目次の取得
                toc = soup.find(id="toc")
                sections = [link.text for link in toc.find_all('a')] if toc else []
                print(f"📚 目次セクション数: {len(sections)}")
                
                # 本文パラグラフの取得
                content = soup.find(id="mw-content-text")
                paragraphs = [p.text for p in content.find_all('p') if p.text.strip()]
                print(f"📝 取得したパラグラフ数: {len(paragraphs)}")
                
                return {
                    'title': title,
                    'sections': sections,
                    'paragraphs': paragraphs
                }
            else:
                error_msg = f"ページの取得に失敗: {response.status_code}"
                print(f"❌ {error_msg}")
                return {"error": error_msg}
                
        except Exception as e:
            error_msg = f"例外が発生: {str(e)}"
            print(f"❌ {error_msg}")
            return {"error": error_msg}

def create_research_agent():
    """調査用エージェントの作成"""
    print("\n🤖 調査エージェントを初期化中...")
    return Agent(
        name="WikiResearcher",
        instructions="""
        あなたは質問に基づいてWikipedia記事を探すエージェントです。
        
        以下のルールを必ず守ってください：
        1. 必ず日本語版Wikipediaに存在する基本的な名詞の記事タイトルのみを選択
        2. 以下のような記事タイトルは絶対に避ける：
           - 動詞や助詞を含むフレーズ（例：「〜における〜」「〜の歴史」）
           - 造語や複合フレーズ（例：「AIの進化」「未来技術」）
           - カタカナ用語は基本形を使用（例：「コンピュータ」ではなく「計算機」）
        
        3. 記事タイトルは以下のような基本的な名詞を選ぶ：
           - 技術用語の例：人工知能、機械学習、ニューラルネットワーク
           - 概念の例：知能、認知、学習
           - 分野の例：情報工学、計算機科学
        
        以下の形式で出力してください：
        ---
        KEY1: [基本名詞1]
        KEY2: [基本名詞2]
        KEY3: [基本名詞3]
        ---
        """
    )

def create_report_agent():
    """レポート作成用エージェントの作成"""
    print("\n📝 レポート作成エージェントを初期化中...")
    return Agent(
        name="ReportWriter",
        instructions="""
        あなたは収集された情報を整理してレポートを作成するエージェントです。
        
        以下の形式で必ずレポートを作成してください：
        
        # 分析レポート
        
        ## 📋 概要
        [質問の要点と主要な発見事項をまとめる]
        
        ## 🔍 詳細分析
        [重要なポイントの詳細な説明]
        
        ## 💡 まとめ
        [質問に対する直接的な回答と追加の考察]
        
        ## 📚 参考情報
        [使用した記事や追加の参考情報]
        ---
        lang:ja
        """
    )

class WikipediaAnalyzer:
    def __init__(self):
        self.base_url = "https://ja.wikipedia.org/wiki/"
        
    def check_article_exists(self, topic):
        """Wikipediaの記事が存在するか確認"""
        encoded_topic = urllib.parse.quote(topic)
        url = f"{self.base_url}{encoded_topic}"
        response = requests.head(url)
        return response.status_code == 200

    def collect_article_data(self, topic):
        """Wikipediaの記事データを収集"""
        print(f"\n🔍 Wikipedia記事「{topic}」の取得を開始...")
        
        if not self.check_article_exists(topic):
            print(f"❌ 記事「{topic}」は存在しません。")
            return {"error": f"記事「{topic}」は存在しません。"}
        
        try:
            # URLエンコードして日本語タイトルを処理可能な形式に変換
            encoded_topic = urllib.parse.quote(topic)
            url = f"{self.base_url}{encoded_topic}"
            print(f"📡 アクセスするURL: {url}")
            
            # 記事の取得
            response = requests.get(url)
            print(f"📥 ステータスコード: {response.status_code}")
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # 記事タイトルの取得
                title = soup.find(id="firstHeading").text
                print(f"📑 記事タイトル: {title}")
                
                # 目次の取得
                toc = soup.find(id="toc")
                sections = [link.text for link in toc.find_all('a')] if toc else []
                print(f"📚 目次セクション数: {len(sections)}")
                
                # 本文パラグラフの取得
                content = soup.find(id="mw-content-text")
                paragraphs = [p.text for p in content.find_all('p') if p.text.strip()]
                print(f"📝 取得したパラグラフ数: {len(paragraphs)}")
                
                return {
                    'title': title,
                    'sections': sections,
                    'paragraphs': paragraphs
                }
            else:
                error_msg = f"ページの取得に失敗: {response.status_code}"
                print(f"❌ {error_msg}")
                return {"error": error_msg}
                
        except Exception as e:
            error_msg = f"例外が発生: {str(e)}"
            print(f"❌ {error_msg}")
            return {"error": error_msg}

def run_analysis(query):
    """分析の実行"""
    print(f"\n🎯 分析を開始: '{query}'")
    
    analyzer = WikipediaAnalyzer()
    client = Swarm()
    researcher = create_research_agent()
    report_writer = create_report_agent()
    
    # 研究エージェントによるキーワード抽出
    print("\n📚 研究エージェントによるキーワード抽出を開始...")
    research_messages = [
        {
            "role": "user",
            "content": f"以下の質問に関連するWikipediaの記事キーワードを抽出してください：\n{query}"
        }
    ]
    
    research_response = client.run(
        agent=researcher,
        messages=research_messages
    )
    
    # キーワードの抽出と検証
    keywords = []
    research_result = research_response.messages[-1]["content"]
    for line in research_result.split('\n'):
        if line.startswith('KEY'):
            keyword = line.split(':')[1].strip()
            # 記事の存在確認を行ってから追加
            if analyzer.check_article_exists(keyword):
                keywords.append(keyword)
            else:
                print(f"⚠️ 警告: 記事「{keyword}」は存在しないため、スキップします")
                # 記事が存在しない場合、研究エージェントに再度リクエスト
                if len(keywords) < 2:  # 最低2つのキーワードを確保
                    retry_messages = [
                        {
                            "role": "user",
                            "content": f"前回のキーワード「{keyword}」は存在しませんでした。別の基本的な記事名を1つ提案してください。"
                        }
                    ]
                    retry_response = client.run(
                        agent=researcher,
                        messages=retry_messages
                    )
                    new_keyword = retry_response.messages[-1]["content"].split(':')[-1].strip()
                    if analyzer.check_article_exists(new_keyword):
                        keywords.append(new_keyword)
    
    print(f"\n🔑 抽出されたキーワード: {keywords}")
    
    # 各キーワードについてWikipedia記事を取得
    all_data = []
    for keyword in keywords:
        print(f"\n📖 キーワード '{keyword}' の記事を取得中...")
        data = analyzer.collect_article_data(keyword)
        if "error" not in data:
            all_data.append(data)
    
    if not all_data:
        return "関連する記事が見つかりませんでした。"
    
    # レポート作成
    print("\n✍️ レポート作成を開始...")
    report_messages = [
        {
            "role": "user",
            "content": f"""
            以下の質問と収集データに基づいてレポートを作成してください：
            
            質問：{query}
            
            収集データ：
            {str(all_data)}
            """
        }
    ]
    
    report_response = client.run(
        agent=report_writer,
        messages=report_messages
    )
    
    return report_response.messages[-1]["content"]
if __name__ == "__main__":
    print("🤖 Wikipedia分析システムを起動しました")
    print("----------------------------------------")
    
    # ユーザーからの入力を受け付ける
    user_query = input("🔍 調べたいことを入力してください：")
    
    # 全体の処理時間を計測
    total_start_time = time.time()
    
    result = run_analysis(user_query)
    
    print("\n📊 最終レポート:")
    print("----------------------------------------")
    print(result)
    print("----------------------------------------")
    print(f"\n⏱️ 総処理時間: {time.time() - total_start_time:.2f}秒")