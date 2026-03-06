import sqlite3

DB = "POW_Kasse.db"

def create_db():
    purposes = ["Noten", "Essen", "Trinken", "Geschenke", "Spenden", "Auftritt", "Sonstiges"]

    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
        cur.execute("""CREATE TABLE IF NOT EXISTS transaction_purpose (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE) """)
        cur.execute("""CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    amount REAL,
                    purpose_id INTEGER,
                    FOREIGN KEY (purpose_id) REFERENCES transaction_purpose(id)
                    ) """)
        for purpose in purposes:
            cur.execute(f"INSERT OR IGNORE INTO transaction_purpose (name) VALUES '{purpose}'")

def new_transaction():
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        date = input("Datum (DD.MM.YYYY): ")
        amount = float(input("Betrag: "))

def view_transactions():
    pass

def view_balance():
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        res = cur.execute("SELECT SUM(amount) FROM transactions;")
        print(res.fetchone())

if __name__ == "__main__":
    create_db()
    new_transaction()
    view_transactions()