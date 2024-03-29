import sqlite3

conn = sqlite3.connect('app.db', check_same_thread=False)

def create_tables():
    """
    create_db.py
    This script defines functions to
    create necessary database tables for the application.

    Functions:
    create_tables(): Creates the 'users' and 'nodes' tables in the 'app.db'
"""
    cursor = conn.cursor()
    
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone_number TEXT UNIQUE NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            slug TEXT NOT NULL
        )
        '''
    )

    conn.commit()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nodes (
            node_id TEXT PRIMARY KEY,
            text TEXT NOT NULL,
            title TEXT NOT NULL,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()

if __name__ == "__main__":
    create_tables()
