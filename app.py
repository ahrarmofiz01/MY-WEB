from flask import Flask, render_template, request, jsonify
from log_processor import parse_log, analyze_logs
from database import init_db, save_upload, save_incidents,get_upload_history

app = Flask(__name__)
init_db()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/history")
def history():
    uploads = get_upload_history()

    return render_template(
        "history.html",
        uploads=uploads
    )

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["logfile"]

    log_data = file.read().decode("utf-8")
    lines = log_data.splitlines()

    parsed_logs = []

    for line in lines:
        parsed_log = parse_log(line)
        if parsed_log is not None:
            parsed_logs.append(parsed_log)

    # Loop complete hone ke baad analysis hoga
    error_counts = analyze_logs(parsed_logs)
    upload_id = save_upload(
    file.filename,
    len(parsed_logs))

    save_incidents(
    upload_id,
    error_counts)

    return render_template(
    "results.html",
    total_logs=len(parsed_logs),
    error_counts=error_counts,
    parsed_logs=parsed_logs
)


if __name__ == "__main__":
    app.run(debug=True)





    
