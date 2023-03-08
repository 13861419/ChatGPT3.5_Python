from flask import Flask, request

from chatGPT import chatGPT, chat, chatGPT35

app = Flask(__name__)

@app.route("/")
def get_result():
    return "Hello World!"

@app.route("/add", methods=["POST"])
def add():
    content = request.json['content']
    result = chatGPT(content)
    return result

@app.route("/speark", methods=["POST"])
def speark():
    content = request.json['content']
    result = chat(content)
    return result

@app.route("/ask", methods=["POST"])
def speark():
    content = request.json['q']
    result = chatGPT35(content)
    return result


if __name__ == "__main__":
    app.run(port=8186)