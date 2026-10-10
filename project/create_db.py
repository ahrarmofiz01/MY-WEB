import sqlite3
from flask_sqlalchemy import SQLAlchemy
conn=sqlite3.connect('site.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
id  INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
email TEXTX UNIQUE NOT NULL
)



''')
conn.commit()
conn.close()