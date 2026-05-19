import os
from litellm import completion
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/v1/chat/completions", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])
    model = data.get("model", "groq/llama-3.3-70b-versatile")

    try:
        response = completion(
            model=model,
            messages=messages,
            temperature=data.get("temperature", 0.7),
            max_tokens=data.get("max_tokens", 2048)
        )
        return jsonify(response.choices[0].message.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
