from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/signein",methods=["POST"])
def signin():
    name=request.form.get("name")
    password=request.form.get("password")
    return render_template("index.html",name=name)
