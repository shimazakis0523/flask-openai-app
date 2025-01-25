from flask import Flask, request, jsonify
from langchain.chat_models import ChatOpenAI  # Chatモデルをインポート
from dotenv import load_dotenv
import os
from flask_cors import CORS

# .envファイルを読み込む
load_dotenv()

app = Flask(__name__)

# CORS対策
CORS(app)

# OpenAI APIキーを環境変数から取得
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set. Please set it in your environment or .env file.")

# LangChainのChatOpenAIモデルを設定
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-4o", max_tokens=100)

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "message": "Server is running"}), 200

@app.route('/api/generate', methods=['POST'])
def generate_text():
    try:
        # リクエストからpromptを取得
        data = request.get_json()
        prompt = data.get('prompt')

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        # Chatモデルを使ってテキスト生成
        response = llm.predict(prompt)

        # 応答を返却
        return jsonify({"response": response.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # アプリを起動
    app.run(host='0.0.0.0', port=5000)



