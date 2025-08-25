from flask import Flask, render_template, request, jsonify
from faq_chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_input = data.get("message", "")
    answer = get_response(user_input)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
