import sqlite3

def create_db_table():
    con = sqlite3.connect("db1.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    con.commit()
    con.close()

def view_all():
    con = sqlite3.connect("db1.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    con.close()
    return rows

def search(title="", author="", year="", isbn=""):
    con = sqlite3.connect("db1.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM books where title=? OR author=? OR year=? OR isbn=?",(title, author, year,isbn))
    rows = cur.fetchall()
    con.close()
    return rows

def delete(id):
    con = sqlite3.connect("db1.db")
    cur = con.cursor()
    cur.execute("DELETE FROM books WHERE id = ?",(id,))
    con.commit()
    con.close()

def add_entry(title, author, year, isbn):
    con = sqlite3.connect("db1.db")
    cur = con.cursor()
    cur.execute("INSERT INTO books VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    con.commit()
    con.close()


def update(id, title, author, year, isbn):
    con = sqlite3.connect("db1.db")
    cur = con.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id = ?",(title, author, year, isbn, id))
    con.commit()
    con.close() 

# def del_table():
#     con = sqlite3.connect("db1.db")
#     cur = con.cursor()
#     cur.execute("DROP TABLE books")
#     con.commit()
#     con.close()   
