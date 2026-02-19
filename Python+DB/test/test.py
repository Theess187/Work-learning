import sqlite3

with sqlite3.connect('logs.db') as con:
    cur = con.cursor()
    cur.execute('''SELECT * FROM logs''')
    # print("LOGS: \t", cur.fetchall())
    rows_logs = cur.fetchall()
    for id, time, level, message, service_id in rows_logs:
        print(f"{id:<5} | {time:<20} | {level:<10} | {message:<50} | {service_id}")
    cur.execute('''SELECT * FROM services''')   
    # print("SERVICES: \t", cur.fetchall())
    rows_services = cur.fetchall()
    for id, name in rows_services:
        print(f"Service {id}: {name}")
    cur.execute('''SELECT * FROM logs
                JOIN services ON logs.service_id = services.id
                WHERE logs.level = 'ERROR' ''')
    # print(cur.fetchone())
    rows_joined = cur.fetchall()
    for id, time, level, message, service_id, s_id, service_name in rows_joined:
        print(f"{id:<5} | {time:<20} | {level:<10} | {message:<30} | {service_name}")