import sqlite3

conn = sqlite3.connect("incidentlens.db")
cursor = conn.cursor()

print("UPLOADS:")

cursor.execute("SELECT * FROM uploads")
uploads = cursor.fetchall()

for upload in uploads:
    print(upload)


print("\nINCIDENTS:")

cursor.execute("SELECT * FROM incidents")
incidents = cursor.fetchall()

for incident in incidents:
    print(incident)


conn.close()