# Teacher's guide: Module 09, Databases
# Every example and exercise answer from this module's lessons, in order.
# Run it from this folder:  python guide.py
# ruff: noqa: E501

import json
import os
import sqlite3
from contextlib import closing

print("=" * 50)
print("LESSON: sql-basics.md")
# Every example uses ":memory:": a database that lives only while the program runs.

# --------------------------------------------------
print("\n--- Example: CREATE TABLE")
# Compare with a spreadsheet: the table is a sheet, columns are the headers.
db = sqlite3.connect(":memory:")
db.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT,
        year INTEGER
    )
""")
print("Table created")

print("\n--- Example: INSERT")
# Point out: we never gave an id, the database numbered the rows (primary key).
db = sqlite3.connect(":memory:")
db.execute(
    "CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT, year INTEGER)"
)

db.execute("INSERT INTO books (title, author, year) VALUES ('Dune', 'Frank Herbert', 1965)")
db.execute("INSERT INTO books (title, author, year) VALUES ('Beloved', 'Toni Morrison', 1987)")

for row in db.execute("SELECT * FROM books"):
    print(row)

print("\n--- Example: SELECT some columns")
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT, year INTEGER);
    INSERT INTO books (title, author, year) VALUES ('Dune', 'Frank Herbert', 1965);
    INSERT INTO books (title, author, year) VALUES ('Beloved', 'Toni Morrison', 1987);
    INSERT INTO books (title, author, year) VALUES ('Emma', 'Jane Austen', 1815);
""")

for row in db.execute("SELECT title, year FROM books"):
    print(row)

print("\n--- Example: WHERE, filtering")
# Ask her to predict which titles come out of each query.
for row in db.execute("SELECT title FROM books WHERE year < 1970"):
    print(row)

for row in db.execute("SELECT title FROM books WHERE author = 'Toni Morrison'"):
    print(row)

print("\n--- Example: ORDER BY, sorting")
for row in db.execute("SELECT title, year FROM books ORDER BY year DESC"):
    print(row)

print("\n--- Example: UPDATE")
# Always with WHERE. Without it, every row changes (see Exercise 3).
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT, year INTEGER);
    INSERT INTO books (title, author, year) VALUES ('Dune', 'Frank Herbert', 1966);
    INSERT INTO books (title, author, year) VALUES ('Beloved', 'Toni Morrison', 1987);
""")

db.execute("UPDATE books SET year = 1965 WHERE id = 1")

for row in db.execute("SELECT * FROM books"):
    print(row)

print("\n--- Example: DELETE")
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT, year INTEGER);
    INSERT INTO books (title, author, year) VALUES ('Dune', 'Frank Herbert', 1965);
    INSERT INTO books (title, author, year) VALUES ('Beloved', 'Toni Morrison', 1987);
""")

db.execute("DELETE FROM books WHERE id = 2")

for row in db.execute("SELECT * FROM books"):
    print(row)

print("\n--- Example: NULL, the empty value")
# In Python it comes back as None.
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT, year INTEGER);
    INSERT INTO books (title, author, year) VALUES ('Dune', 'Frank Herbert', 1965);
    INSERT INTO books (title) VALUES ('Untitled notes');
""")

for row in db.execute("SELECT * FROM books WHERE year IS NULL"):
    print(row)

print("\n--- Example: counting")
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT, year INTEGER);
    INSERT INTO books (title, author, year) VALUES ('Dune', 'Frank Herbert', 1965);
    INSERT INTO books (title, author, year) VALUES ('Beloved', 'Toni Morrison', 1987);
    INSERT INTO books (title, author, year) VALUES ('Emma', 'Jane Austen', 1815);
""")

for row in db.execute("SELECT COUNT(*) FROM books WHERE year > 1900"):
    print(row)

# --------------------------------------------------
print("\n--- Mistake: a typo in the table name")
# db.execute("SELECT * FROM book")
# sqlite3.OperationalError: no such table: book

print("\n--- Mistake: forgetting the quotes around text")
# db.execute("SELECT * FROM books WHERE title = Dune")
# sqlite3.OperationalError: no such column: Dune
# Without quotes, SQL thinks Dune is a column name. Fixed: title = 'Dune'

print("\n--- Mistake: using a column that does not exist")
# db.execute("INSERT INTO books (title, author) VALUES ('Dune', 'Frank Herbert')")
# sqlite3.OperationalError: table books has no column named author

print("\n--- Mistake: breaking a NOT NULL rule")
# db.execute("INSERT INTO books (year) VALUES (1965)")
# sqlite3.IntegrityError: NOT NULL constraint failed: books.title

print("\n--- Mistake: comparing with = NULL")
# No error, just no results. Ask her why before running.
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, year INTEGER);
    INSERT INTO books (title) VALUES ('Untitled notes');
""")
rows = db.execute("SELECT * FROM books WHERE year = NULL").fetchall()
print(rows)
rows = db.execute("SELECT * FROM books WHERE year IS NULL").fetchall()
print(rows)

# --------------------------------------------------
# The exercises all use this movies table.
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE movies (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER, rating REAL);
    INSERT INTO movies (title, year, rating) VALUES ('Amélie', 2001, 8.3);
    INSERT INTO movies (title, year, rating) VALUES ('Spirited Away', 2001, 8.6);
    INSERT INTO movies (title, year, rating) VALUES ('Central Station', 1998, 8.0);
    INSERT INTO movies (title, year, rating) VALUES ('Paddington 2', 2017, NULL);
""")

print("\n--- Exercise 1: a simple filter")
# Ask her to predict before running.
for row in db.execute("SELECT title FROM movies WHERE year = 2001 ORDER BY title"):
    print(row)

print("\n--- Exercise 2: which id?")
# Answer: Paddington 2 has id 4 (fourth row inserted). The count is (1,).
print(db.execute("SELECT id FROM movies WHERE title = 'Paddington 2'").fetchone())
print(db.execute("SELECT COUNT(*) FROM movies WHERE rating IS NULL").fetchone())

print("\n--- Exercise 3: the disappearing rating")
# Broken: db.execute("UPDATE movies SET rating = 7.8")  -> no WHERE, EVERY movie gets 7.8.
# Fixed:
db.execute("UPDATE movies SET rating = 7.8 WHERE id = 4")
for row in db.execute("SELECT title, rating FROM movies ORDER BY id"):
    print(row)

print("\n--- Exercise 4: no results")
# Broken: WHERE rating = NULL finds nothing. Fixed with IS NULL:
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE movies (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER, rating REAL);
    INSERT INTO movies (title, year, rating) VALUES ('Amélie', 2001, 8.3);
    INSERT INTO movies (title, year, rating) VALUES ('Paddington 2', 2017, NULL);
""")
for row in db.execute("SELECT title FROM movies WHERE rating IS NULL"):
    print(row)

print("\n--- Exercise 5: best rated first")
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE movies (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER, rating REAL);
    INSERT INTO movies (title, year, rating) VALUES ('Amélie', 2001, 8.3);
    INSERT INTO movies (title, year, rating) VALUES ('Spirited Away', 2001, 8.6);
    INSERT INTO movies (title, year, rating) VALUES ('Central Station', 1998, 8.0);
    INSERT INTO movies (title, year, rating) VALUES ('Paddington 2', 2017, NULL);
""")
sql = "SELECT title, rating FROM movies WHERE rating IS NOT NULL ORDER BY rating DESC"
for row in db.execute(sql):
    print(row)

print("\n--- Exercise 6: your own table")
plants_db = sqlite3.connect(":memory:")
plants_db.execute("""
    CREATE TABLE plants (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        water_every_days INTEGER,
        location TEXT
    )
""")
plants_db.execute(
    "INSERT INTO plants (name, water_every_days, location) VALUES ('Fern', 3, 'bathroom')"
)
plants_db.execute(
    "INSERT INTO plants (name, water_every_days, location) VALUES ('Cactus', 21, 'window')"
)
plants_db.execute(
    "INSERT INTO plants (name, water_every_days, location) VALUES ('Basil', 2, 'kitchen')"
)

for row in plants_db.execute("SELECT name FROM plants WHERE water_every_days <= 7 ORDER BY name"):
    print(row)

print("\n--- Exercise 7: delete and count")
# Uses the full movies table from Exercise 5.
db.execute("DELETE FROM movies WHERE year < 2000")
for row in db.execute("SELECT COUNT(*) FROM movies"):
    print(row)

# --------------------------------------------------
print("\n--- Review 1: classes (module 08)")


class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year})"


print(Movie("Amélie", 2001))

print("\n--- Review 2: tuples (module 06)")
# A row from the database is a tuple: unpack it into variables.
row = (3, "Central Station", 1998)
movie_id, title, year = row
print(title, "came out in", year)


print("\n" + "=" * 50)
print("LESSON: sqlite.md")

# --------------------------------------------------
print("\n--- Example: fetchall, fetchone and looping")
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER);
    INSERT INTO books (title, year) VALUES ('Dune', 1965);
    INSERT INTO books (title, year) VALUES ('Beloved', 1987);
""")

rows = db.execute("SELECT * FROM books").fetchall()
print(rows)

first = db.execute("SELECT * FROM books WHERE id = 1").fetchone()
print(first)

# fetchone gives None when nothing matches.
missing = db.execute("SELECT * FROM books WHERE id = 99").fetchone()
print(missing)

for row in db.execute("SELECT title FROM books"):
    print(row[0])

print("\n--- Example: rows you can read by name, sqlite3.Row")
db = sqlite3.connect(":memory:")
db.row_factory = sqlite3.Row
db.executescript("""
    CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER);
    INSERT INTO books (title, year) VALUES ('Dune', 1965);
""")

row = db.execute("SELECT * FROM books WHERE id = 1").fetchone()
print(row["title"], row["year"])
print(dict(row))

print("\n--- Example: always use ? placeholders")
# Note the comma in (title,): a tuple with one value.
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER)")

title = "Beloved"
year = 1987
db.execute("INSERT INTO books (title, year) VALUES (?, ?)", (title, year))

row = db.execute("SELECT * FROM books WHERE title = ?", (title,)).fetchone()
print(row)

print("\n--- Example: why never build SQL with f-strings")
# The typed text changes the SQL itself and leaks every secret. With ? it is just text.
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, secret TEXT);
    INSERT INTO users (name, secret) VALUES ('ana', 'ana-password');
    INSERT INTO users (name, secret) VALUES ('bruno', 'bruno-password');
""")

typed = "nobody' OR '1'='1"

unsafe = f"SELECT name, secret FROM users WHERE name = '{typed}'"
print(unsafe)
print(db.execute(unsafe).fetchall())

safe = db.execute("SELECT name, secret FROM users WHERE name = ?", (typed,)).fetchall()
print(safe)

print("\n--- Example: saving changes with commit (a real file)")
# This creates library.db in this folder. It is removed at the end of the lesson.
db = sqlite3.connect("library.db")
db.execute(
    "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER)"
)
db.execute("INSERT INTO books (title, year) VALUES (?, ?)", ("Dune", 1965))
db.commit()
db.close()

db = sqlite3.connect("library.db")
print(db.execute("SELECT * FROM books").fetchall())
db.close()

print("\n--- Example: opening and closing safely")
with closing(sqlite3.connect("library.db")) as db:
    db.execute("INSERT INTO books (title, year) VALUES (?, ?)", ("Emma", 1815))
    db.commit()
# here the connection is already closed

with closing(sqlite3.connect("library.db")) as db:
    print(db.execute("SELECT title FROM books").fetchall())

print("\n--- Example: organizing database code in functions")


def create_table(db):
    db.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            year INTEGER
        )
    """)


def add_book(db, title, year):
    cursor = db.execute("INSERT INTO books (title, year) VALUES (?, ?)", (title, year))
    db.commit()
    return cursor.lastrowid


def list_books(db):
    return db.execute("SELECT * FROM books ORDER BY title").fetchall()


def get_book(db, book_id):
    return db.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()


def update_year(db, book_id, year):
    db.execute("UPDATE books SET year = ? WHERE id = ?", (year, book_id))
    db.commit()


def delete_book(db, book_id):
    db.execute("DELETE FROM books WHERE id = ?", (book_id,))
    db.commit()


db = sqlite3.connect(":memory:")
db.row_factory = sqlite3.Row
create_table(db)

dune = add_book(db, "Dune", 1966)
add_book(db, "Beloved", 1987)
print("New id:", dune)

update_year(db, dune, 1965)
print(dict(get_book(db, dune)))

delete_book(db, 2)
for book in list_books(db):
    print(book["title"], book["year"])

print(get_book(db, 2))

print("\n--- Example: moving data from JSON into a table")
old_data = """
[
    {"title": "Dune", "year": 1965},
    {"title": "Beloved", "year": 1987},
    {"title": "Emma", "year": 1815}
]
"""
books = json.loads(old_data)

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER)")

for book in books:
    db.execute("INSERT INTO books (title, year) VALUES (?, ?)", (book["title"], book["year"]))
db.commit()

count = db.execute("SELECT COUNT(*) FROM books").fetchone()[0]
print(f"Migrated {count} books")
print(db.execute("SELECT title FROM books WHERE year < 1900").fetchall())

print("\n--- Example: the same migration from a real JSON file")
with open("books.json", "w", encoding="utf-8") as file:
    file.write(old_data)

with open("books.json", encoding="utf-8") as file:
    books = json.load(file)

with closing(sqlite3.connect("library.db")) as db:
    db.execute(
        "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER)"
    )
    for book in books:
        db.execute("INSERT INTO books (title, year) VALUES (?, ?)", (book["title"], book["year"]))
    db.commit()
    print(f"Migrated {len(books)} books")

# --------------------------------------------------
print("\n--- Mistake: forgetting the comma in a one-value tuple")
# db.execute("INSERT INTO books (title) VALUES (?)", ("Dune"))
# sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 4 supplied.
# ("Dune") is just a string, so each of its 4 letters counts as a value. Fixed: ("Dune",)

print("\n--- Mistake: different number of ? and values")
# db.execute("INSERT INTO books (title, year) VALUES (?, ?)", ("Dune",))
# sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 2, and there are 1 supplied.

print("\n--- Mistake: putting quotes around ?")
# No error, but '?' becomes the text "?" and nothing is found.
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT)")
db.execute("INSERT INTO books (title) VALUES ('Dune')")
row = db.execute("SELECT * FROM books WHERE title = '?'", ()).fetchone()
print(row)
row = db.execute("SELECT * FROM books WHERE title = ?", ("Dune",)).fetchone()
print(row)

print("\n--- Mistake: forgetting to commit")
# The insert is lost when the connection closes without commit().
db = sqlite3.connect("library.db")
before = db.execute("SELECT COUNT(*) FROM books").fetchone()[0]
db.execute("INSERT INTO books (title, year) VALUES (?, ?)", ("Emma", 1815))
db.close()

db = sqlite3.connect("library.db")
after = db.execute("SELECT COUNT(*) FROM books").fetchone()[0]
db.close()
print("Books before:", before, "after:", after)

print("\n--- Mistake: creating a table that already exists")
# db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT)")  (twice)
# sqlite3.OperationalError: table books already exists
# Fixed: CREATE TABLE IF NOT EXISTS books (...)

# The real files are no longer needed.
os.remove("library.db")
os.remove("books.json")

# --------------------------------------------------
print("\n--- Exercise 1: fetchone and fetchall")
# Ask her to predict before running.
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE notes (id INTEGER PRIMARY KEY, text TEXT);
    INSERT INTO notes (text) VALUES ('buy milk');
    INSERT INTO notes (text) VALUES ('call mom');
""")
print(len(db.execute("SELECT * FROM notes").fetchall()))
print(db.execute("SELECT text FROM notes WHERE id = 2").fetchone())
print(db.execute("SELECT text FROM notes WHERE id = 3").fetchone())

print("\n--- Exercise 2: the tricky name")
# Ask her to predict before running. The ' in O'Brien is no problem with ?.
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE people (id INTEGER PRIMARY KEY, name TEXT)")
name = "O'Brien"
db.execute("INSERT INTO people (name) VALUES (?)", (name,))
print(db.execute("SELECT name FROM people").fetchone()[0])

print("\n--- Exercise 3: the crash on search")
# Broken: ("Emma") instead of ("Emma",)
# sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 4 supplied.
# Fixed:
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, year INTEGER)")
db.execute("INSERT INTO books (title, year) VALUES (?, ?)", ("Emma", 1815))
print(db.execute("SELECT title, year FROM books WHERE title = ?", ("Emma",)).fetchone())

print("\n--- Exercise 4: the unsafe search")
# Broken: f"SELECT title FROM books WHERE author = '{author}'"
# Fixed: use ? and pass the value separately.


def find_by_author(db, author):
    return db.execute("SELECT title FROM books WHERE author = ?", (author,)).fetchall()


db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)")
db.execute("INSERT INTO books (title, author) VALUES (?, ?)", ("Beloved", "Toni Morrison"))
print(find_by_author(db, "Toni Morrison"))
print(find_by_author(db, "nobody' OR '1'='1"))

print("\n--- Exercise 5: a to-do repository")


def create_tasks_table(db):
    db.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            done INTEGER
        )
    """)


def add_task(db, title):
    cursor = db.execute("INSERT INTO tasks (title, done) VALUES (?, 0)", (title,))
    db.commit()
    return cursor.lastrowid


def complete_task(db, task_id):
    db.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    db.commit()


def pending_tasks(db):
    rows = db.execute("SELECT title FROM tasks WHERE done = 0 ORDER BY title").fetchall()
    return [row[0] for row in rows]


db = sqlite3.connect(":memory:")
create_tasks_table(db)
add_task(db, "Water plants")
coffee = add_task(db, "Buy coffee")
add_task(db, "Pay rent")
complete_task(db, coffee)
print(pending_tasks(db))

print("\n--- Exercise 6: migrate a shopping list")
old = '[{"name": "apples", "quantity": 3}, {"name": "bread", "quantity": 1}, {"name": "milk", "quantity": 2}]'
items = json.loads(old)

db = sqlite3.connect(":memory:")
db.row_factory = sqlite3.Row
db.execute("CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT NOT NULL, quantity INTEGER)")
for item in items:
    db.execute("INSERT INTO items (name, quantity) VALUES (?, ?)", (item["name"], item["quantity"]))
db.commit()

for row in db.execute("SELECT * FROM items ORDER BY name"):
    print(f"{row['quantity']} x {row['name']}")

print("\n--- Exercise 7: rows into objects")


class Book:
    def __init__(self, id, title, year):
        self.id = id
        self.title = title
        self.year = year

    @classmethod
    def from_row(cls, row):
        return cls(row["id"], row["title"], row["year"])

    def __str__(self):
        return f"#{self.id} {self.title} ({self.year})"


db = sqlite3.connect(":memory:")
db.row_factory = sqlite3.Row
db.executescript("""
    CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER);
    INSERT INTO books (title, year) VALUES ('Dune', 1965);
    INSERT INTO books (title, year) VALUES ('Beloved', 1987);
""")

books = [Book.from_row(row) for row in db.execute("SELECT * FROM books")]
for book in books:
    print(book)

# --------------------------------------------------
print("\n--- Review 1: SQL (previous file)")
# Answer: SELECT name FROM plants WHERE location = 'kitchen' ORDER BY name
for row in plants_db.execute("SELECT name FROM plants WHERE location = 'kitchen' ORDER BY name"):
    print(row)

print("\n--- Review 2: with and files (module 04)")
# Answer: `with` closes the file at the end of the block, even after an error.
# For a database: with closing(sqlite3.connect("app.db")) as db:
print('with closing(sqlite3.connect("app.db")) as db:')

print("\n--- Review 3: classes with rules (module 08)")
# Ask her to predict. The failed remove does not change the amount.


class Stock:
    def __init__(self, amount):
        self.amount = amount

    def remove(self, quantity):
        if quantity > self.amount:
            raise ValueError("not enough stock")
        self.amount = self.amount - quantity


stock = Stock(5)
stock.remove(2)
try:
    stock.remove(10)
except ValueError as error:
    print(error, stock.amount)
