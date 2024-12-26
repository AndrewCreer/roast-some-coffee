from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_coffee():
    return "<p>Hello Coffee!</p>"
