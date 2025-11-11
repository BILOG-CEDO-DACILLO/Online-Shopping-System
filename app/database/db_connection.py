import sqlite3
import os

class Database:
    def __init__(self):
        self.db_path = os.path.join("data", "database.db")
        os.makedirs("data", exist_ok=True)
        self.create_tables()

    def connect(self):
        return sqlite3.connect(self.db_path)

    def create_tables(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        """)

