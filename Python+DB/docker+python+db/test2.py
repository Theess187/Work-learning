import psycopg
with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="appdb",
    user="appuser",
    password="pass") as conn:
    with conn.cursor() as cur:
        cur.execute("""
            SELECT COUNT(*) AS errors, s.name 
            FROM logs l JOIN services s 
            ON l.service_id = s.id GROUP BY s.name;
        """)    
        # print(cur.fetchall())
        rows = cur.fetchall()
        for error, name in rows:
            print(f"{name:<10} | {error:>5}")