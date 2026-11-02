# IncidentLens

AI-powered log analysis and debugging platform built with Flask.

## Features

- Upload application log files
- Parse and analyze logs
- Group recurring errors into incidents
- Store upload history using SQLite
- Generate AI-powered incident analysis
- Retrieve relevant troubleshooting documentation using RAG

## Tech Stack

- Python
- Flask
- SQLite
- Groq API
- Scikit-learn
- TF-IDF
- Bootstrap

## Project Structure

```text
IncidentLens/
├── app.py
├── log_processor.py
├── database.py
├── ai_analyzer.py
├── rag_retriever.py
├── docs/
├── templates/
├── .env
├── .gitignore
└── README.md
```

## Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies.
4. Configure the Groq API key.
5. Run the Flask application.

## Run Locally

```bash
flask run
```

Open `http://127.0.0.1:5000` in your browser.

## Disclaimer

AI-generated incident analysis provides probable causes and debugging suggestions. It does not confirm the actual root cause of an incident.