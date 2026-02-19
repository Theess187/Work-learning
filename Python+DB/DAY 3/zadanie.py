import sqlite3
import pandas as pd
from tabulate import tabulate  # pip install tabulate

# Создаем тестовую базу данных
conn = sqlite3.connect(':memory:')  # Временная БД в памяти
cur = conn.cursor()

# Создаем тестовую таблицу
cur.execute("""
CREATE TABLE sales (
    id INTEGER PRIMARY KEY,
    product_type TEXT,
    quantity INTEGER,
    price REAL,
    sale_date DATE
)
""")

# Добавляем тестовые данные
test_data = [
    ('Электроника', 5, 29999.99, '2024-01-15'),
    ('Одежда', 10, 4999.50, '2024-01-15'),
    ('Электроника', 3, 15999.99, '2024-01-16'),
    ('Книги', 20, 999.99, '2024-01-16'),
    ('Одежда', 8, 7999.99, '2024-01-17'),
    ('Электроника', 2, 45999.99, '2024-01-17'),
    ('Книги', 15, 1499.99, '2024-01-18'),
]

cur.executemany("""
INSERT INTO sales (product_type, quantity, price, sale_date)
VALUES (?, ?, ?, ?)
""", test_data)
conn.commit()


print("\n=== Отчёт с таблицей ===")
cur.execute("""
    SELECT 
        product_type,
        COUNT(*) as transactions,
        SUM(quantity) as total_quantity,
        SUM(price * quantity) as total_revenue,
        AVG(price) as avg_price
    FROM sales
    GROUP BY product_type
    ORDER BY total_revenue DESC
""")

data = cur.fetchall()

# Заголовки таблицы
headers = ["Тип товара", "Продаж", "Кол-во", "Выручка", "Ср. цена"]

print(tabulate(data, headers=headers, floatfmt=".2f", tablefmt="grid"))