import sqlite3

DB = "POW_Kasse.db"

def create_db():
    purposes = [("Noten",), ("Essen",), ("Trinken",), ("Geschenke",), ("Spenden",), ("Auftritt",), ("Sonstiges",)]

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
                    comment TEXT,
                    FOREIGN KEY (purpose_id) REFERENCES transaction_purpose(id)
                    ) """)
        cur.executemany("INSERT OR IGNORE INTO transaction_purpose (name) VALUES (?);", purposes)

def new_transaction():
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        date = input("Datum (DD.MM.YYYY): ")
        amount = float(input("Betrag: ").replace(",", "."))
        pur = int(input("Zweck: "))
        comment = input("Kommentar: ")
        cur.execute(f"INSERT INTO transactions (date, amount, purpose_id, comment) VALUES ('{date}', {amount}, {pur}, '{comment}');")

def view_transactions():
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        res = cur.execute("""SELECT t.id, t.date as Datum, t.amount as Betrag, p.name as Zweck, t.comment as Kommentar FROM transactions t
                          LEFT JOIN transaction_purpose p on p.id=t.purpose_id;""")
        return res.fetchall()

def view_balance():
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        res = cur.execute("SELECT SUM(amount) FROM transactions;")
        return res.fetchone()[0]

""" create_db()
new_transaction()
view_transactions()
view_balance() """