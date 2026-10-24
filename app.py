
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Database aur table create karna
def init_db():
    conn = sqlite3.connect("visitors.db")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS visitors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def greet():
    name = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()

        if name:
            conn = sqlite3.connect("visitors.db")

            conn.execute(
                "INSERT INTO visitors (name) VALUES (?)",
                (name,)
            )

            conn.commit()
            conn.close()

    return render_template("index.html", username=name)


# Saare saved visitors dekhna
@app.route("/visitors")
def visitors():
    conn = sqlite3.connect("visitors.db")
    conn.row_factory = sqlite3.Row

    all_visitors = conn.execute(
        "SELECT id, name FROM visitors ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template(
        "visitors.html",
        visitors=all_visitors
    )


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
