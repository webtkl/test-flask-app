from flask import Flask, request
from random import randint


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Ricsi!"

@app.route("/email")
def email():
    return "<h1>Hello email!</h1>"

@app.route("/random")
def rand():
    number=int(request.args.get('number', 10))

    s=[]
    for i in range(number):
        s.append(str(randint(1,9)))
    return " ".join(s)


if __name__ == "__main__":
    app.run()