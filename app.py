from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/login",methods=["POST"])
def login():
    name=request.form.get("name")
    password=request.form.get("password")
    return render_template("base.html",name=name)





    
