
import sqlite3

DB_FILE = "logs.db"

with sqlite3.connect(DB_FILE) as conn:
    cur = conn.cursor()

    cur.execute("""
        SELECT *
        FROM logs l;
    """)

    rows = cur.fetchall()

print(rows)
for id, time, level, message, service_id in rows:
    print(f"{id:<5} | {time:<20} | {level:<10} | {message:<50} | {service_id}")