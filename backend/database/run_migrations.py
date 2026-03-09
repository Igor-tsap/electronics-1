import os
from pathlib import Path
from db import get_connection
import mysql.connector

MIGRATIONS_DIR = Path(__file__).parent / "migrations"
SEED_FILE = Path(__file__).parent / "seed.sql"

def applied_migrations(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS schema_migrations (
                version VARCHAR(50) PRIMARY KEY,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    except Exception as e:
        # Ignore if table already exists
        pass

    cursor.execute("SELECT version FROM schema_migrations")
    rows = cursor.fetchall()
    cursor.close()
    return {row[0] for row in rows}

def apply_migration(conn, filename):
    print(f"Applying {filename} ...")
    with open(MIGRATIONS_DIR / filename, "r", encoding="utf-8") as f:
        sql = f.read()

    cursor = conn.cursor()
    statements = [stmt.strip() for stmt in sql.split(";") if stmt.strip()]
    for stmt in statements:
        try:
            cursor.execute(stmt)
        except mysql.connector.errors.DatabaseError as e:
            if "already exists" in str(e):
                # Skip this table or index, just print a message
                print(f"Skipping existing table or object: {stmt.split()[2]}")
            else:
                # For any other error, stop
                cursor.close()
                conn.close()
                raise

    cursor.execute(
        "INSERT INTO schema_migrations (version) VALUES (%s)",
        (filename,)
    )
    conn.commit()
    cursor.close()
    print(f"{filename} applied successfully.\n")

def run_seed():
    conn = get_connection()
    cursor = conn.cursor()

    with open(SEED_FILE, "r", encoding="utf-8") as f:
        sql = f.read()

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

def main():
    conn = get_connection()
    applied = applied_migrations(conn)
    files = sorted(f for f in os.listdir(MIGRATIONS_DIR) if f.endswith(".sql"))
    for f in files:
        if f not in applied:
            apply_migration(conn, f)
    conn.close()
    print("All migrations applied.")

    # Run seed after migrations
    run_seed()

if __name__ == "__main__":
    main()