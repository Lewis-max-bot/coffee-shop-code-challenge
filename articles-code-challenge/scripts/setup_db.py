import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.db.connection import get_connection
from lib.db.schema import create_tables

def setup_db():
    conn = get_connection()
    with open("lib/db/schema.sql", "r") as file:
        conn.executescript(file.read())
    conn.close()
    print("Database tables created!")

if __name__ == "__main__":
    setup_db()
