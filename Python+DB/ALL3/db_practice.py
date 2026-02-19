import sqlite3
from datetime import datetime, timedelta

DB_FILE = "logs.db"


def init_db():
    """Создание таблиц и тестовых данных."""
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()

        # Таблицы
        cur.execute("""
        CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            level TEXT NOT NULL,
            message TEXT NOT NULL,
            service_id INTEGER,
            FOREIGN KEY(service_id) REFERENCES services(id)
        );
        """)

        # Очистка
        cur.execute("DELETE FROM logs;")
        cur.execute("DELETE FROM services;")

        # Сервисы
        services = ["auth", "api", "payments", "frontend"]
        cur.executemany("INSERT INTO services(name) VALUES(?);", [(s,) for s in services])

        # service_id map
        cur.execute("SELECT id, name FROM services;")
        service_map = {name: sid for sid, name in cur.fetchall()}

        now = datetime.now()

        # Логи: часть свежих, часть старых
        logs_data = [
            (now - timedelta(hours=1),  "INFO",  "auth login ok",        "auth"),
            (now - timedelta(hours=2),  "ERROR", "token validation failed", "auth"),
            (now - timedelta(hours=3),  "ERROR", "timeout in upstream",  "api"),
            (now - timedelta(hours=4),  "INFO",  "api health ok",        "api"),
            (now - timedelta(days=2),   "ERROR", "payment gateway failed", "payments"),
            (now - timedelta(days=2),   "INFO",  "payments retry ok",    "payments"),
            (now - timedelta(days=5),   "INFO",  "frontend started",     "frontend"),
        ]

        rows = []
        for ts, level, msg, svc in logs_data:
            rows.append((ts.strftime("%Y-%m-%d %H:%M:%S"), level, msg, service_map[svc]))

        cur.executemany("""
            INSERT INTO logs(timestamp, level, message, service_id)
            VALUES(?, ?, ?, ?);
        """, rows)

        conn.commit()


# ---------------------------
# PRACTICE 1
# ---------------------------
def practice_1_select_last_errors(limit=5):
    """
    Задание 1:
    Вывести последние N ошибок (ERROR) с названием сервиса.
    """
    print("\n=== PRACTICE 1: last ERROR logs ===")

    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT l.timestamp, s.name, l.level, l.message
            FROM logs l
            JOIN services s ON l.service_id = s.id
            WHERE l.level = 'ERROR'
            ORDER BY l.timestamp DESC
            LIMIT ?;
        """, (limit,))

        rows = cur.fetchall()

    if not rows:
        print("No ERROR logs found.")
        return

    for ts, svc, level, msg in rows:
        print(f"{ts} | {svc:<10} | {level:<5} | {msg}")


# ---------------------------
# PRACTICE 2
# ---------------------------
def practice_2_count_errors_by_service():
    """
    Задание 2:
    Посчитать количество ошибок по каждому сервису.
    """
    print("\n=== PRACTICE 2: errors count by service ===")

    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT s.name, COUNT(*) AS errors
            FROM logs l
            JOIN services s ON l.service_id = s.id
            WHERE l.level = 'ERROR'
            GROUP BY s.name
            ORDER BY errors DESC;
        """)
        rows = cur.fetchall()

    for svc, errors in rows:
        print(f"{svc:<10} -> {errors}")


# ---------------------------
# PRACTICE 3
# ---------------------------
def practice_3_find_silent_services(hours=24):
    """
    Задание 3:
    Найти сервисы, у которых нет логов за последние N часов.
    Это классическая задача L2: "кто молчит?"
    """
    print(f"\n=== PRACTICE 3: services with no logs in last {hours}h ===")

    border = datetime.now() - timedelta(hours=hours)
    border_str = border.strftime("%Y-%m-%d %H:%M:%S")

    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()

        # Вариант через LEFT JOIN (то, что мы обсуждали)
        cur.execute("""
            SELECT s.id, s.name
            FROM services s
            LEFT JOIN logs l
              ON l.service_id = s.id
             AND l.timestamp >= ?
            WHERE l.id IS NULL
            ORDER BY s.name;
        """, (border_str,))

        rows = cur.fetchall()

    if not rows:
        print("No silent services.")
        return

    for sid, name in rows:
        print(f"{sid}: {name}")


def main():
    init_db()
    practice_1_select_last_errors(limit=5)
    practice_2_count_errors_by_service()
    practice_3_find_silent_services(hours=24)


if __name__ == "__main__":
    main()
    