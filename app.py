from flask import Flask, render_template, request, redirect
app = Flask(__name__)
tasks=[]
@app.route("/")
def home():
    return render_template("index.html",tasks=tasks)
@app.route("/add",methods=["POST"])
def add_tasks():
    new_task=request.form.get("task")
    if new_task:
        tasks.append(new_task)
    return redirect("/")