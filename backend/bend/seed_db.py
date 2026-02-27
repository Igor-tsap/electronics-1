from db import get_connection
from pathlib import Path

# шлях до seed.sql
sql_path = Path(__file__).parent.parent / "database" / "seed.sql"

conn = get_connection()
cursor = conn.cursor()

# відкриваємо файл і читаємо весь текст
with open(sql_path, "r", encoding="utf-8") as f:
    sql = f.read()

# розбиваємо на окремі запити за допомогою ;
statements = [stmt.strip() for stmt in sql.split(";") if stmt.strip()]

for stmt in statements:
    try:
        cursor.execute(stmt)
    except Exception as e:
        print(f"Error executing statement:\n{stmt}\n{e}")

conn.commit()
cursor.close()
conn.close()

print("Seed data inserted successfully!")