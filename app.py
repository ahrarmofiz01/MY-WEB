from flask import Flask, render_template, request,jsonify
from log_processor import parse_log

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["logfile"]

    log_data= file.read().decode("utf-8")
    lines = log_data.splitlines()

    parsed_logs = []

    for line in lines:
        parsed_log = parse_log(line)
        parsed_logs.append(parsed_log)
    return jsonify(parsed_logs)


if __name__ == "__main__":
    app.run(debug=True)






    
