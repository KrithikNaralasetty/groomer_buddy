import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# ChatGPT API endpoint
API_URL = "https://api.openai.com/v1/chat/completions"

# Your ChatGPT API key
API_KEY = open()

@app.route("/chat", methods=["POST"])
def chat():
    # Get user message from the request
    user_message = request.json["message"]

    # Send user message to ChatGPT API
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": user_message}]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    response_json = response.json()

    # Extract and return the ChatGPT API response
    chat_gpt_response = response_json["choices"][0]["message"]["content"]
    return jsonify({"response": chat_gpt_response})

if __name__ == "__main__":
    app.run()