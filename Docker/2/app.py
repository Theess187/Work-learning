import time 
import psycopg2
import os
# print(os.environ["DB_PASSWORD"])
time.sleep(10)
# try:
conn = psycopg2.connect(
    host="localhost",
    dbname="testdb",
    user="admin",
    password="admin"
)
print("Connected to PostgreSQL database!")
    
conn.close()
# except Exception as e:
#     print(f"ОШИБКА:")
    

# while True:
#     time.sleep(60)