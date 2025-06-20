import sqlite3

def create_tables():
    con = sqlite3.connect("library_db.db")
    cur = con.cursor()

    # Table for storing book details
    cur.execute("""
        CREATE TABLE IF NOT EXISTS all_books (
            book_num INTEGER PRIMARY KEY,
            book_title TEXT,
            book_auth TEXT,
            book_pub TEXT
        )
    """)

    # Table for storing student details
    cur.execute("""
        CREATE TABLE IF NOT EXISTS all_studs (
            enroll INTEGER PRIMARY KEY,
            sname TEXT,
            semail TEXT,
            smob INTEGER
        )
    """)

    # Table for issued book records
    cur.execute("""
        CREATE TABLE IF NOT EXISTS all_issued (
            senroll INTEGER,
            bknum INTEGER,
            idate TEXT,
            rdate TEXT,
            rstatus TEXT
        )
    """)

    con.commit()
    con.close()
    print("✅ Database and tables created successfully.")

if __name__ == "__main__":
    create_tables()
