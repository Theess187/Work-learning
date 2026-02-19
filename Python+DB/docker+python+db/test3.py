import psycopg
with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="appdb",
    user="appuser",
    password="pass") as conn:
    with conn.cursor() as cur:
        cur.execute("""
            SELECT l.id,l.timestamp,l.level,l.message,s.id, s.name 
            FROM logs l 
            LEFT JOIN services s 
            ON l.service_id = s.id
            WHERE NOT EXISTS (
                SELECT 1 FROM logs l2 
                WHERE l2.timestamp >= NOW() - INTERVAL '1 day' AND l2.id = l.id
            );
        """)    
        # print(cur.fetchall())
        rows = cur.fetchall()
        for a,b,c,d,e,f  in rows:
            print(f"{a} | {b} | {c:<6} | {d:<25} | {e:<1} | {f}")