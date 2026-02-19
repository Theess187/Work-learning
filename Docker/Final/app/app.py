import psycopg2
import time
# def connect_to_db():
# while True: 
try: 
    time.sleep(20)
    with psycopg2.connect(
        host="db", 
        database="base", 
        user="user", 
        password="pass"
    ) as conn:
        print("Database connection successful!")
        
except psycopg2.OperationalError as e:print(f"Database connection failed: {e}")
with conn.cursor() as cursor:
    cursor.execute('''CREATE TABLE IF NOT EXISTS services ( id SERIAL PRIMARY KEY, name TEXT, info TEXT);''')
    conn.commit()
    cursor.execute('''INSERT INTO services(name,info) VALUES ('api','АПИ СЕРВИСА'),('bd','БАЗА ДАННЫХ'),('nothing','НИЧЕГО');''')
    conn.commit()
    cursor.execute('''CREATE TABLE IF NOT EXISTS logs ( id SERIAL PRIMARY KEY, level TEXT, message TEXT, service_id INT);''')
    conn.commit()
    cursor.execute('''INSERT INTO logs (level, message,service_id) VALUES ('INFO', 'Service started',1), ('ERROR', 'Database timeout',2), ('ERROR', 'Connection timeout'
                    ,2), ('INFO', 'Health check OK',1), ('ERROR', 'Disk full',2);''')
    conn.commit()
    cursor.execute('''SELECT * FROM logs;''')
    rows = cursor.fetchall()
    for row in rows:
        print(f"logs: {row}")    
    print("____________________________________________________________")
    cursor.execute('''SELECT * FROM services;
                    ''')
    rows = cursor.fetchall()
    for row in rows:
        print(f"services: {row}")  
    #ОТЧЕТ
    cursor.execute('''
                    SELECT COUNT(*) FROM logs WHERE level = 'ERROR';
                    ''')
    err = cursor.fetchone()[0]
    print(f"Количество ошибок: {err}")
    
    cursor.execute(''' 
                    SELECT s.name, COUNT(l.id) FROM logs l RIGHT JOIN services s 
                    ON l.service_id = s.id AND l.level = 'ERROR'
                    
                    GROUP BY s.name ORDER BY COUNT(l.id) DESC;
                    ''')
    rows = cursor.fetchall()
    for row in rows:
        print(f"Сервисы с количеством ошибок: {row[0]} - {row[1]} ошибок")
        time.sleep(1)
    time.sleep(10)