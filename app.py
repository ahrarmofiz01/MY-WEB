from flask import Flask,request,url_for,session,Response,redirect
app = Flask(__name__)
app.secret_key="supersecreatkey"
#home page
@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        if username=="admin" and password=="123":
            session["user"]=username
            return redirect(url_for("welcome"))
        else:
            return Response("invalid Credentials try again",mimetype="text/plain")
    return"""
             <h2>login page</h2>
             <form method="post">
                 username:<input type="text" name="username"><br>
                 password:<input type="text" name="password"><br>
                 <input type="submit" value="Login">
             </form>
"""
#welcome page after login
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
                <h2>welcome,{session["user"]}!</h2>
                <a href={url_for("logout")}>logout</a>

'''
    return redirect(url_for("login"))
#logout page
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))