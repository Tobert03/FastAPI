from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api")
def api_call():
    response = requests.get("http://127.0.0.1:8000/text")
    data = response.json()
    return f"text from API: {data}"


if __name__ == "__main__":
    app.run(debug=True, port=5000)