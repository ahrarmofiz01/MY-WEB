from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/signin",methods=["POST"])
def signin():
    if request.method =="POST":
        name=request.form.get("name")
        password=request.form.get("password")
        return render_template("base.html",name=name)
    return render_template("index.html")
