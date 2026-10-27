from flask import Flask, render_template, request, redirect
app = Flask(__name__)
task=[]
@app.route("/")
def home():
    return render_template("index.html",tasks=task)
@app.route("/add",methods=["POST"])
def add_tasks():
    task=request.form.get("task")
    if task:
        task.append(task)
    return redirect("/")