import sqlite3

DB_NAME = "fitbuddy.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            goal TEXT,
            plan TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_user(name, age, goal, plan):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (name, age, goal, plan)
        VALUES (?, ?, ?, ?)
    """, (name, age, goal, plan))

    conn.commit()
    conn.close()


def get_users():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()
    return users
