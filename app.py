from flask import Flask, render_template,request,redirect,url_for,flash
from forms import registrationForm
app= Flask(__name__)
app.secret_key="my-secret-Key"
@app.route("/", methods=["GET","POST"])
def register():
    form=registrationForm()
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        flash(f"welcome,{name} ! your Resistered succesfully","success")
        return  redirect(url_for("success"))
    return render_template("resister.html",form=form)
@app.route("/success")
def success():
     return render_template("success.html")



