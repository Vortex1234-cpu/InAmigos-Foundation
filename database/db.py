import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'inamigos.db')


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS contacts (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT    NOT NULL,
            email       TEXT    NOT NULL,
            phone       TEXT,
            subject     TEXT    NOT NULL,
            message     TEXT    NOT NULL,
            created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS volunteers (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT    NOT NULL,
            email       TEXT    NOT NULL,
            phone       TEXT,
            city        TEXT,
            interest    TEXT,
            created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS newsletter (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            email       TEXT    UNIQUE NOT NULL,
            subscribed_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    conn.close()
    print("Database initialised at", DB_PATH)


# ── CRUD helpers ──────────────────────────────────────────────────────────────

def save_contact(name, email, phone, subject, message):
    conn = get_connection()
    conn.execute(
        "INSERT INTO contacts (name, email, phone, subject, message) VALUES (?, ?, ?, ?, ?)",
        (name, email, phone, subject, message)
    )
    conn.commit()
    conn.close()


def save_volunteer(name, email, phone, city, interest):
    conn = get_connection()
    conn.execute(
        "INSERT INTO volunteers (name, email, phone, city, interest) VALUES (?, ?, ?, ?, ?)",
        (name, email, phone, city, interest)
    )
    conn.commit()
    conn.close()


def save_newsletter(email):
    conn = get_connection()
    try:
        conn.execute("INSERT INTO newsletter (email) VALUES (?)", (email,))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # already subscribed
    finally:
        conn.close()


def get_all_contacts():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM contacts ORDER BY created_at DESC").fetchall()
    conn.close()
    return rows


def get_all_volunteers():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM volunteers ORDER BY created_at DESC").fetchall()
    conn.close()
    return rows
