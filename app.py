from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def student_profile():
    return render_template(
        "profile.html",
        name="ahrar",
        is_topper=True,
        subjects=["math","science","history"]
    )