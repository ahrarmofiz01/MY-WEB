from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def greet():
    if request.method=="POST":
        name=request.form.get("name")
        return f"Hello,{name}! welcome to flask."
    return render_template("index.html")