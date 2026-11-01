
import markdown

from rag_retriever import retrieve_context
from flask import Flask, render_template, request
from log_processor import parse_log, analyze_logs

from database import (
    init_db,
    save_upload,
    save_incidents,
    get_upload_history,
    get_incidents_by_upload
)

from ai_analyzer import analyze_incidents


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


@app.route("/incidents/<int:upload_id>")
def incidents(upload_id):

    incident_data = get_incidents_by_upload(upload_id)

    return render_template(
        "incidents.html",
        incidents=incident_data,
        upload_id=upload_id
    )


@app.route("/analyze/<int:upload_id>", methods=["POST"])
def analyze(upload_id):

    # Step 1: Database se incidents retrieve karo
    incident_data = get_incidents_by_upload(upload_id)

    # Step 2: Agar incidents nahi hain to return karo
    if not incident_data:
        return "No incidents found for this upload."

    # Step 3: Incidents ko search query mein convert karo
    query = ""

    for fingerprint, frequency in incident_data:
        query += f"{fingerprint} "

    # Step 4: Relevant troubleshooting documentation retrieve karo
    retrieved_context = retrieve_context(query)

    # Step 5: Incidents + retrieved context AI ko bhejo
    ai_result = analyze_incidents(
        incident_data,
        retrieved_context
    )

    # Step 6: AI ke Markdown response ko HTML mein convert karo
    ai_html = markdown.markdown(
        ai_result,
        extensions=["tables", "fenced_code"]
    )

    # Step 7: AI analysis page render karo
    return render_template(
        "ai_analysis.html",
        ai_html=ai_html,
        upload_id=upload_id
    )


@app.route("/upload", methods=["POST"])
def upload():

    # Step 1: Uploaded file retrieve karo
    file = request.files["logfile"]

    # Step 2: File ko read karo
    log_data = file.read().decode("utf-8")

    # Step 3: Logs ko lines mein divide karo
    lines = log_data.splitlines()

    parsed_logs = []

    # Step 4: Har line ko parse karo
    for line in lines:

        parsed_log = parse_log(line)

        if parsed_log is not None:
            parsed_logs.append(parsed_log)

    # Step 5: Logs ka analysis karo
    error_counts = analyze_logs(parsed_logs)

    # Step 6: Upload information database mein save karo
    upload_id = save_upload(
        file.filename,
        len(parsed_logs)
    )

    # Step 7: Incidents database mein save karo
    save_incidents(
        upload_id,
        error_counts
    )

    # Step 8: Results page render karo
    return render_template(
        "results.html",
        total_logs=len(parsed_logs),
        error_counts=error_counts,
        parsed_logs=parsed_logs
    )


if __name__ == "__main__":
    app.run(debug=True)






    
