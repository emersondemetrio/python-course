# SQLite from Python

> **In one sentence:** the `sqlite3` module lets your Python program open a database file, send it SQL, pass it values safely, and get the results back as Python data.

## Why it matters

In the previous file you wrote SQL. Now you will make it part of a real program: a program that remembers data between runs, that adds, finds, changes and removes items, and that does all of it safely. This is exactly what the final project needs to store ceramic pieces, and it is how most small apps (including many phone apps) store their data.

## Analogy

Think of a **library with a librarian**.

- The **database file** is the library building, with its shelves (tables).
- **Connecting** is walking into the library.
- **`execute`** is handing the librarian a request slip ("find all books by Toni Morrison").
- The results the librarian brings back are the **rows**.
- **`commit`** is the librarian stamping your changes into the official records. If you add a book to the shelf but nobody records it, it is gone the next day.
- **Placeholders** (`?`) are the blank spaces on a printed request form. You fill in the blanks; you never rewrite the form itself. That is what keeps the request safe.

## The idea, step by step

### Connecting

<!-- no-verify -->
```python
import sqlite3

db = sqlite3.connect("library.db")
```

`sqlite3.connect("library.db")` opens the database file `library.db` in the current folder. If the file does not exist, SQLite creates it. The result (`db`) is a **connection**: your open line to the database.

In this file, verified examples use `":memory:"` instead of a file name, which creates a temporary database that disappears when the program ends. Your real programs will use a file name.

### Running SQL and reading results

`db.execute(sql)` sends one command and returns a **cursor**: an object that holds the results and hands them over when you ask. There are three common ways to read them:

```python
import sqlite3
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

missing = db.execute("SELECT * FROM books WHERE id = 99").fetchone()
print(missing)

for row in db.execute("SELECT title FROM books"):
    print(row[0])
```

Output:

```text
[(1, 'Dune', 1965), (2, 'Beloved', 1987)]
(1, 'Dune', 1965)
None
Dune
Beloved
```

- `.fetchall()` gives you **a list of all rows**. Each row is a tuple.
- `.fetchone()` gives you **just the next row**, or `None` if there are no rows. Perfect when you look up one item by id.
- A `for` loop over the cursor gives you rows one at a time.
- `row[0]` is the first column of the row, like any tuple.

### Rows you can read by name: `sqlite3.Row`

`row[1]` is hard to read: was column 1 the title or the year? Set `row_factory` once, right after connecting, and you can use column names instead:

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.row_factory = sqlite3.Row
db.executescript("""
    CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER);
    INSERT INTO books (title, year) VALUES ('Dune', 1965);
""")

row = db.execute("SELECT * FROM books WHERE id = 1").fetchone()
print(row["title"], row["year"])
print(dict(row))
```

Output:

```text
Dune 1965
{'id': 1, 'title': 'Dune', 'year': 1965}
```

`dict(row)` turns the row into a normal dictionary, which is handy for printing, for JSON, and for building objects (module 08).

### Passing values: always use `?` placeholders

Your program usually gets values from somewhere else: the user typed them, they came from a file, from a form. To put them in SQL, write a `?` where each value goes, and pass the values as a **tuple** in the second argument of `execute`:

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER)")

title = "Beloved"
year = 1987
db.execute("INSERT INTO books (title, year) VALUES (?, ?)", (title, year))

row = db.execute("SELECT * FROM books WHERE title = ?", (title,)).fetchone()
print(row)
```

Output:

```text
(1, 'Beloved', 1987)
```

- Each `?` is filled by one value, in order.
- No quotes around `?`: SQLite takes care of quotes, numbers, `None` (becomes `NULL`), and special characters like apostrophes.
- With a single value, remember the comma: `(title,)`. Without the comma, `(title)` is just `title` in parentheses, not a tuple.

### Why never build SQL with f-strings

It is tempting to write `f"SELECT * FROM books WHERE title = '{title}'"`. Do not. Look at what happens when the value contains a quote:

```python
import sqlite3
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
```

Output:

```text
SELECT name, secret FROM users WHERE name = 'nobody' OR '1'='1'
[('ana', 'ana-password'), ('bruno', 'bruno-password')]
[]
```

The user typed some carefully chosen text. With the f-string, that text became **part of the SQL command**: `OR '1'='1'` is always true, so the database returned every user's secret. This attack is called **SQL injection**, and it is one of the most common ways real websites get hacked.

With `?`, the database knows the whole text is just a value, never a command. It looked for a user literally named `nobody' OR '1'='1`, found none, and returned an empty list. Placeholders also stop the simpler problem of names like `O'Brien`, whose apostrophe would break an f-string query.

**Rule:** values always go in `?`. f-strings are fine for messages you print, never for SQL with values.

### Saving changes: `commit`

When you change data (`INSERT`, `UPDATE`, `DELETE`), SQLite keeps the changes pending until you call `db.commit()`. If your program ends without committing, the changes are thrown away.

<!-- no-verify -->
```python
import sqlite3

db = sqlite3.connect("library.db")
db.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER)")
db.execute("INSERT INTO books (title, year) VALUES (?, ?)", ("Dune", 1965))
db.commit()
db.close()
```

- `CREATE TABLE IF NOT EXISTS` creates the table only the first time. Run the program again and it does not complain that the table already exists.
- `db.commit()` saves.
- `db.close()` closes the connection when you are done, like closing a file.

Run this program twice and then count the books: there will be two, because each run added one and saved it.

### Opening and closing safely

If something crashes between `connect` and `close`, the connection may stay open. A tidy way to always close it is `contextlib.closing` with `with`, the same idea as `with open(...)` from module 04:

<!-- no-verify -->
```python
import sqlite3
from contextlib import closing

with closing(sqlite3.connect("library.db")) as db:
    db.execute("INSERT INTO books (title, year) VALUES (?, ?)", ("Emma", 1815))
    db.commit()
# here the connection is already closed
```

You may also see `with sqlite3.connect(...) as db:` in other tutorials. Careful: that version commits automatically when the block ends without errors, but it does **not** close the connection. That is why we use `closing`.

### Organizing database code in functions

Instead of spreading SQL all over your program, put each operation in a small function. Then the rest of the program says `add_book(db, "Dune", 1965)` and never needs to know SQL. A group of functions like this is often called a **repository**.

```python
import sqlite3

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
```

Output:

```text
New id: 1
{'id': 1, 'title': 'Dune', 'year': 1965}
Dune 1965
None
```

- `cursor.lastrowid` is the `id` the database just gave the new row. Returning it lets the caller find the row later.
- Every function receives `db` as a parameter, so the same functions work with a file database or a `":memory:"` database (very useful for testing, module 07).
- `get_book` returns `None` when the id does not exist, which the caller can check with `if book is None:`.

### Moving data from JSON into a table

When you switch an app from JSON to a database, you need to copy the old data over once. This is called a **migration**. Here the JSON text is written directly in the code so the example can run anywhere; in real life you would read it from the file with `json.load` (module 06).

```python
import json
import sqlite3

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
```

Output:

```text
Migrated 3 books
[('Emma',)]
```

The `for` loop sends one `INSERT` per item, always with placeholders. One `commit()` at the end saves them all together.

A real migration script, reading the old file and writing a database file:

<!-- no-verify -->
```python
import json
import sqlite3
from contextlib import closing

with open("books.json", encoding="utf-8") as file:
    books = json.load(file)

with closing(sqlite3.connect("library.db")) as db:
    db.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER)")
    for book in books:
        db.execute("INSERT INTO books (title, year) VALUES (?, ?)", (book["title"], book["year"]))
    db.commit()
    print(f"Migrated {len(books)} books")
```

Run a migration only once, or you will copy the same books twice.

## Common mistakes

### Forgetting the comma in a one-value tuple

<!-- error -->
```python
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT)")
db.execute("INSERT INTO books (title) VALUES (?)", ("Dune"))
```

```text
sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 4 supplied.
```

`("Dune")` is just the text `"Dune"` in parentheses. SQLite then treats each letter as a separate value: D, u, n, e. That is 4 values for 1 placeholder. A **binding** is a value attached to a `?`. Fix: `("Dune",)`.

### Different number of `?` and values

<!-- error -->
```python
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, year INTEGER)")
db.execute("INSERT INTO books (title, year) VALUES (?, ?)", ("Dune",))
```

```text
sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 2, and there are 1 supplied.
```

Two `?` need two values. Count them: `("Dune", 1965)`.

### Putting quotes around `?`

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT)")
db.execute("INSERT INTO books (title) VALUES ('Dune')")
row = db.execute("SELECT * FROM books WHERE title = '?'", ()).fetchone()
print(row)
```

```text
None
```

With quotes, `'?'` is no longer a placeholder: it is the text "a question mark". The query looks for a book literally titled `?`. Write `?` without quotes and pass the value: `db.execute("SELECT * FROM books WHERE title = ?", ("Dune",))`.

### Forgetting to commit

<!-- no-verify -->
```python
import sqlite3

db = sqlite3.connect("library.db")
db.execute("INSERT INTO books (title, year) VALUES (?, ?)", ("Emma", 1815))
db.close()
```

No error appears, but the next time you open `library.db`, Emma is not there. The change was pending and `close()` threw it away. After `INSERT`, `UPDATE` or `DELETE`, call `db.commit()`. Putting `commit()` inside your repository functions (like `add_book` above) means you cannot forget it.

### Creating a table that already exists

<!-- error -->
```python
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT)")
db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT)")
```

```text
sqlite3.OperationalError: table books already exists
```

With a database file, this happens the second time you run your program. Fix: `CREATE TABLE IF NOT EXISTS books (...)`.

## Exercises

### Predict the output

#### Exercise 1: fetchone and fetchall

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE notes (id INTEGER PRIMARY KEY, text TEXT);
    INSERT INTO notes (text) VALUES ('buy milk');
    INSERT INTO notes (text) VALUES ('call mom');
""")
print(len(db.execute("SELECT * FROM notes").fetchall()))
print(db.execute("SELECT text FROM notes WHERE id = 2").fetchone())
print(db.execute("SELECT text FROM notes WHERE id = 3").fetchone())
```

<details>
<summary>Show answer</summary>

```text
2
('call mom',)
None
```

`fetchall` returns a list of 2 rows. `fetchone` returns one tuple, or `None` when nothing matches.

</details>

#### Exercise 2: The tricky name

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE people (id INTEGER PRIMARY KEY, name TEXT)")
name = "O'Brien"
db.execute("INSERT INTO people (name) VALUES (?)", (name,))
print(db.execute("SELECT name FROM people").fetchone()[0])
```

<details>
<summary>Show answer</summary>

```text
O'Brien
```

With a placeholder, the apostrophe is just part of the value. With an f-string, the apostrophe would have closed the SQL text early and caused an error.

</details>

### Fix the bug

#### Exercise 3: The crash on search

This search should print `('Emma', 1815)`. It crashes. Fix it.

<!-- error -->
```python
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, year INTEGER)")
db.execute("INSERT INTO books (title, year) VALUES (?, ?)", ("Emma", 1815))
print(db.execute("SELECT title, year FROM books WHERE title = ?", ("Emma")).fetchone())
```

```text
sqlite3.ProgrammingError: Incorrect number of bindings supplied. The current statement uses 1, and there are 4 supplied.
```

<details>
<summary>Show answer</summary>

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, year INTEGER)")
db.execute("INSERT INTO books (title, year) VALUES (?, ?)", ("Emma", 1815))
print(db.execute("SELECT title, year FROM books WHERE title = ?", ("Emma",)).fetchone())
```

```text
('Emma', 1815)
```

`("Emma")` is not a tuple. The comma in `("Emma",)` makes it one.

</details>

#### Exercise 4: The unsafe search

This code works, but it has a security problem. What is it, and how do you fix it?

<!-- no-verify -->
```python
def find_by_author(db, author):
    return db.execute(f"SELECT title FROM books WHERE author = '{author}'").fetchall()
```

<details>
<summary>Show answer</summary>

It builds SQL with an f-string, so it is open to **SQL injection**: someone could pass text like `x' OR '1'='1` and get every row. It also breaks with names that have apostrophes. Use a placeholder:

<!-- no-verify -->
```python
def find_by_author(db, author):
    return db.execute("SELECT title FROM books WHERE author = ?", (author,)).fetchall()
```

</details>

### Write it

#### Exercise 5: A to-do repository

Write these functions for a table `tasks` (`id`, `title` text required, `done` integer, 0 for not done and 1 for done):

- `create_table(db)`
- `add_task(db, title)`: inserts with `done = 0`, returns the new id
- `complete_task(db, task_id)`: sets `done = 1`
- `pending_tasks(db)`: returns the titles of tasks not done, sorted by title

Test with `":memory:"`: add "Water plants", "Buy coffee" and "Pay rent", complete "Buy coffee", and print the pending titles.

<details>
<summary>Hint</summary>

SQLite has no True/False type, so 0 and 1 are the usual way to store yes/no. Remember `db.commit()` in the functions that change data.

</details>

<details>
<summary>Show answer</summary>

```python
import sqlite3

def create_table(db):
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
create_table(db)
add_task(db, "Water plants")
coffee = add_task(db, "Buy coffee")
add_task(db, "Pay rent")
complete_task(db, coffee)
print(pending_tasks(db))
```

```text
['Pay rent', 'Water plants']
```

</details>

#### Exercise 6: Migrate a shopping list

You have this JSON text from an old version of your app. Create a table `items` (`id`, `name`, `quantity`), copy every item into it with placeholders, then print each item as `3 x apples`, sorted by name. Use `sqlite3.Row` so you can read columns by name.

<!-- no-verify -->
```python
old = '[{"name": "apples", "quantity": 3}, {"name": "bread", "quantity": 1}, {"name": "milk", "quantity": 2}]'
```

<details>
<summary>Show answer</summary>

```python
import json
import sqlite3

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
```

```text
3 x apples
1 x bread
2 x milk
```

</details>

#### Exercise 7: Rows into objects

Combine this file with module 08. Write a class `Book` with `id`, `title` and `year`, and a `@classmethod` `from_row(cls, row)` that builds a `Book` from a `sqlite3.Row`. Load all books from a table and print each one with a `__str__` like `#1 Dune (1965)`.

<details>
<summary>Show answer</summary>

```python
import sqlite3

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
```

```text
#1 Dune (1965)
#2 Beloved (1987)
```

This pattern (database rows in, objects out) is what the final project uses for ceramic pieces.

</details>

## Review

#### Review 1: SQL (previous file)

Write the SQL (just the text) to show the `name` of every row in a table `plants` whose `location` is `'kitchen'`, sorted by name.

<details>
<summary>Show answer</summary>

```sql
SELECT name FROM plants WHERE location = 'kitchen' ORDER BY name
```

From Python, with a placeholder: `db.execute("SELECT name FROM plants WHERE location = ? ORDER BY name", ("kitchen",))`.

</details>

#### Review 2: with and files (module 04)

What does `with` do for you in `with open("notes.txt") as file:`, and which tool from this file gives you the same benefit for a database?

<details>
<summary>Show answer</summary>

`with` closes the file automatically when the block ends, even if an error happens inside it. For a database connection, `with closing(sqlite3.connect("app.db")) as db:` (from `contextlib`) does the same: it closes the connection at the end of the block.

</details>

#### Review 3: Classes with rules (module 08)

What does this print?

```python
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
```

<details>
<summary>Show answer</summary>

```text
not enough stock 3
```

The first `remove(2)` works (5 - 2 = 3). The second raises before changing anything, so the amount stays 3.

</details>

## Recap

- `sqlite3.connect("file.db")` opens (or creates) a database; `db.execute(sql)` runs SQL; `fetchall()` returns all rows, `fetchone()` returns one row or `None`.
- `db.row_factory = sqlite3.Row` lets you read columns by name: `row["title"]`.
- Always pass values with `?` placeholders and a tuple (`(value,)` for one value). Never put values in SQL with f-strings: that opens the door to SQL injection.
- After `INSERT`, `UPDATE` or `DELETE`, call `db.commit()`, and close the connection when you are done.
- Keep SQL inside small functions (a repository), so the rest of your program never needs to know SQL.

**Next:** [Module 10: HTTP and the web](../mod-10-http-and-web/README.md)
