from flask import Flask, request, render_template
from random import randint


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Ricsi!"

@app.route("/email")
def email():
    return render_template("mail.html", name="Ricsi")


@app.route("/random")
def rand():
    number=int(request.args.get('number', 10))

    s=[]
    for i in range(number):
        s.append(randint(1,9))
    return render_template("randoms.html", numbers=s)


if __name__ == "__main__":
    app.run()