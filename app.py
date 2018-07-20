from flask import Flask, request

app = Flask(__name__)

@app.route("/index", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def index():
    return "Hello world"

@app.route("/publish", methods=["GET", "POST"])
def publish():
    posting = request.form["posting"]
    return posting

@app.route("/whatever", methods=["GET", "POST"])
def whatever():
    return "whatever"


if __name__ == '__main__':
    app.run()
