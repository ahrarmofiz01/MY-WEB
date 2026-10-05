from flask import Flask, render_template, request, url_for, session, Response, redirect
app=Flask(__name__)
@app.route("/")
def login():
    return render_template("login.html")
@app.route("/submit",methods=["POST"])
def submit():
    username=request.form.get("username")
    password=request.form.get("password")
    if username == "admin" and password == "pass":
        return render_template("welcome.html", username=username)
    else:
        return "Invalid credentials"