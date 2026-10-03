from flask import Flask, request
app=Flask(__name__)
@app.route("/")
def home():
    return "this is my home page"
@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method=="POST":
        return "you send data"
    else:
        return "you read data"
