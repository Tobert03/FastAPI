from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add_item/<item_name>", methods=["GET"])
def api_call(item_name):

    response = requests.put(f"http://127.0.0.1:8000/new_item/{item_name}")
    response_massage = response.json()
    return f"text from API: {response_massage}"


if __name__ == "__main__":
    app.run(debug=True, port=5000)