import sqlite3

DATABASE = "incidentlens.db"


def init_db():
    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS uploads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            total_logs INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            upload_id INTEGER,
            fingerprint TEXT,
            frequency INTEGER,
            FOREIGN KEY (upload_id) REFERENCES uploads(id)
        )
    """)

    conn.commit()
    conn.close()
def save_upload(filename, total_logs):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO uploads (filename, total_logs)
        VALUES (?, ?)
    """, (filename, total_logs))

    upload_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return upload_id


def save_incidents(upload_id, error_counts):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    for fingerprint, frequency in error_counts.items():
        cursor.execute("""
            INSERT INTO incidents
            (upload_id, fingerprint, frequency)
            VALUES (?, ?, ?)
        """, (upload_id, fingerprint, frequency))

    conn.commit()
    conn.close()