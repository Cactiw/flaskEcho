
from flask import Flask, request

app = Flask(__name__)


@app.route("/webhooks/rocketchat/webhook", methods=["GET", "POST"])
def echo():
    print("got request:")
    print(request.json)
    return "Ok"


@app.route("/", methods=["GET", "POST"])
def echo_():
    print("got request:")
    print(request.json)
    return "Ok"


if __name__ == "__main__":
    app.run("0.0.0.0", port=5055)
