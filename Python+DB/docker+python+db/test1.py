import psycopg
from datetime import datetime, timedelta

conn = psycopg.connect(
    host="127.0.0.1",
    port=5432,
    dbname="appdb",
    user="appuser",
    password="pass"
)

with conn:
    # with conn.cursor() as cur:
    #     cur.execute("""
    #         	SELECT column_name, data_type 
	#             FROM information_schema.columns 
	#             WHERE table_name = 'logs';
    #     """)    
    #     print(cur.fetchall())

    with conn.cursor() as cur2:
        cur2.execute("""
            SELECT l.id,l.timestamp,l.level,l.message,s.name
            FROM logs l JOIN services s ON l.service_id = s.id
            WHERE l.level = 'ERROR';
        """)    
        # print(cur2.fetchall())
        rows = cur2.fetchall()
        for row in rows:
            print(f"ID:{row[0]:<2} | {row[1]} | {row[2]:<5} | {row[3]:<25} | {row[4]:<10}")