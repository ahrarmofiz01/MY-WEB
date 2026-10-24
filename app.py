from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/",methods=["POST","GET"])
def greet():
    name = None
    if request.method=="POST":
        name=request.form.get("name")
        
    return render_template("index.html",username=name)
    