import psycopg

conn = psycopg.connect(
    host="127.0.0.1", port=5432, dbname="appdb",
    user="appuser", password="pass"
)

with conn:
    with conn.cursor() as cur:
        cur.execute("""
            SELECT * FROM logs l2 
            WHERE l2.timestamp < NOW() - INTERVAL '1 day' AND l2.id = id;
        """)
        rows = cur.fetchall()
for a,b,c,d,e  in rows:
    print(f"{a} | {b} | {c:<6} | {d:<25} | {e:<1}")
print(rows)


conn.close()