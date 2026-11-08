# SQL basics

> **In one sentence:** a database keeps data in tables, and SQL is the language you use to ask the database to create, find, change and remove that data.

## Why it matters

Almost every app you use (a bank, a store, a social network, a notes app on your phone) keeps its data in a database. JSON files are fine for a few dozen items, but a database can hold millions of rows, find exactly the ones you ask for in a fraction of a second, change one row without rewriting everything, and refuse data that breaks your rules. SQL (pronounced "S-Q-L" or "sequel", short for *Structured Query Language*) is around 50 years old and is still used everywhere, so what you learn here will be useful for a long time.

## Analogy

Picture a **spreadsheet** with a tab called `books`.

- The tab is a **table**.
- The header row (`id`, `title`, `author`, `year`) lists the **columns**. Each column holds one kind of information.
- Each line below the header is a **row**: one book.

| id | title | author | year |
|----|-------|--------|------|
| 1 | Dune | Frank Herbert | 1965 |
| 2 | Beloved | Toni Morrison | 1987 |

Now imagine that instead of clicking around the spreadsheet, you write short sentences to a very fast assistant: "give me the titles of all books from before 1970, newest first". That assistant is the database, and those sentences are SQL.

## The idea, step by step

### How to try SQL in this file

SQL is its own language, but we will run it from Python. Every example in this file starts with these lines:

<!-- no-verify -->
```python
import sqlite3
db = sqlite3.connect(":memory:")
```

`sqlite3` is SQLite, a database that comes with Python. `":memory:"` means "create a temporary database that lives only while this program runs", which is perfect for practicing. Then `db.execute("...")` sends one SQL command to the database. For now, treat these lines as your SQL playground; the next file explains them in detail. Focus on the text inside the quotes: that is the SQL.

SQL keywords are usually written in UPPERCASE (`SELECT`, `FROM`). SQL does not require it, but it makes the keywords stand out from table and column names.

### `CREATE TABLE`: making a table

Before storing anything, you describe the table: its name, its columns, and what kind of data each column holds.

```python
import sqlite3
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
```

Output:

```text
Table created
```

The triple quotes (`"""`) let you write a long text over several lines, which makes SQL easier to read.

The main **types** in SQLite are:

| SQLite type | Holds | Python equivalent |
|---|---|---|
| `INTEGER` | whole numbers | `int` |
| `REAL` | decimal numbers | `float` |
| `TEXT` | text | `str` |
| `BLOB` | raw bytes (images, files) | `bytes` |

`NOT NULL` is a rule: this column must always have a value. A book without a title will be refused.

### The primary key

`id INTEGER PRIMARY KEY` makes `id` the **primary key**: a number that identifies each row, and that no two rows can share. Think of it like a national ID number for each book. Two books can have the same title (there are many books called "Home"), but never the same `id`.

In SQLite, if you don't give an `id`, the database picks the next free number for you: 1, 2, 3...

### `INSERT`: adding rows

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT, year INTEGER)")

db.execute("INSERT INTO books (title, author, year) VALUES ('Dune', 'Frank Herbert', 1965)")
db.execute("INSERT INTO books (title, author, year) VALUES ('Beloved', 'Toni Morrison', 1987)")

for row in db.execute("SELECT * FROM books"):
    print(row)
```

Output:

```text
(1, 'Dune', 'Frank Herbert', 1965)
(2, 'Beloved', 'Toni Morrison', 1987)
```

`INSERT INTO books (title, author, year) VALUES (...)` reads as: "into the table books, in the columns title, author and year, put these values". The values follow the same order as the columns. Text values go in **single quotes** in SQL. We did not give an `id`, so the database numbered the rows.

Each row comes back to Python as a **tuple** (module 06), in the same order as the columns.

### `SELECT`: finding rows

`SELECT` is the command you will write most often. It reads data and never changes anything.

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT, year INTEGER);
    INSERT INTO books (title, author, year) VALUES ('Dune', 'Frank Herbert', 1965);
    INSERT INTO books (title, author, year) VALUES ('Beloved', 'Toni Morrison', 1987);
    INSERT INTO books (title, author, year) VALUES ('Emma', 'Jane Austen', 1815);
""")

for row in db.execute("SELECT title, year FROM books"):
    print(row)
```

Output:

```text
('Dune', 1965)
('Beloved', 1987)
('Emma', 1815)
```

- `db.executescript(...)` runs several SQL commands at once, separated by `;`. We use it here just to fill the table quickly.
- `SELECT *` means "all columns". `SELECT title, year` means "only these two columns".
- `FROM books` says which table to read.

### `WHERE`: filtering

`WHERE` keeps only the rows that match a condition, like an `if` for each row.

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT, year INTEGER);
    INSERT INTO books (title, author, year) VALUES ('Dune', 'Frank Herbert', 1965);
    INSERT INTO books (title, author, year) VALUES ('Beloved', 'Toni Morrison', 1987);
    INSERT INTO books (title, author, year) VALUES ('Emma', 'Jane Austen', 1815);
""")

for row in db.execute("SELECT title FROM books WHERE year < 1970"):
    print(row)

for row in db.execute("SELECT title FROM books WHERE author = 'Toni Morrison'"):
    print(row)
```

Output:

```text
('Dune',)
('Emma',)
('Beloved',)
```

SQL comparisons look like Python's, with one difference: **SQL uses a single `=` to compare**, not `==`. You can also use `<`, `>`, `<=`, `>=`, `!=` (or `<>`), and combine conditions with `AND` and `OR`, just like `and` and `or` in Python.

The comma in `('Dune',)` is how Python shows a tuple with only one item (module 06).

### `ORDER BY`: sorting

Without `ORDER BY`, the database returns rows in whatever order is convenient for it. If the order matters, always ask for it.

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT, year INTEGER);
    INSERT INTO books (title, author, year) VALUES ('Dune', 'Frank Herbert', 1965);
    INSERT INTO books (title, author, year) VALUES ('Beloved', 'Toni Morrison', 1987);
    INSERT INTO books (title, author, year) VALUES ('Emma', 'Jane Austen', 1815);
""")

for row in db.execute("SELECT title, year FROM books ORDER BY year DESC"):
    print(row)
```

Output:

```text
('Beloved', 1987)
('Dune', 1965)
('Emma', 1815)
```

`ORDER BY year` sorts from smallest to largest (`ASC`, ascending, is the default). `DESC` (descending) means largest first. You can sort by text too: `ORDER BY title` sorts alphabetically.

The parts of a `SELECT` always come in this order: `SELECT ... FROM ... WHERE ... ORDER BY ...`.

### `UPDATE`: changing rows

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT, year INTEGER);
    INSERT INTO books (title, author, year) VALUES ('Dune', 'Frank Herbert', 1966);
    INSERT INTO books (title, author, year) VALUES ('Beloved', 'Toni Morrison', 1987);
""")

db.execute("UPDATE books SET year = 1965 WHERE id = 1")

for row in db.execute("SELECT * FROM books"):
    print(row)
```

Output:

```text
(1, 'Dune', 'Frank Herbert', 1965)
(2, 'Beloved', 'Toni Morrison', 1987)
```

`UPDATE books SET year = 1965 WHERE id = 1` reads as "in books, set year to 1965, but only in the row whose id is 1". **Be very careful with the `WHERE`.** Without it, `UPDATE` changes **every row** in the table. That is why we usually update by `id`: it points to exactly one row.

### `DELETE`: removing rows

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT, year INTEGER);
    INSERT INTO books (title, author, year) VALUES ('Dune', 'Frank Herbert', 1965);
    INSERT INTO books (title, author, year) VALUES ('Beloved', 'Toni Morrison', 1987);
""")

db.execute("DELETE FROM books WHERE id = 2")

for row in db.execute("SELECT * FROM books"):
    print(row)
```

Output:

```text
(1, 'Dune', 'Frank Herbert', 1965)
```

Same warning as `UPDATE`, even stronger: `DELETE FROM books` without `WHERE` empties the whole table, and there is no "undo".

### `NULL`: the empty value

`NULL` means "no value", like an empty cell in a spreadsheet. It is the database version of Python's `None`. If you insert a row without giving a value for a column, that column is `NULL` (unless it is `NOT NULL`, in which case the database refuses).

To find empty values, you must use `IS NULL` (and `IS NOT NULL` for the opposite), never `= NULL`:

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT, year INTEGER);
    INSERT INTO books (title, author, year) VALUES ('Dune', 'Frank Herbert', 1965);
    INSERT INTO books (title) VALUES ('Untitled notes');
""")

for row in db.execute("SELECT * FROM books WHERE year IS NULL"):
    print(row)
```

Output:

```text
(2, 'Untitled notes', None, None)
```

Notice how `NULL` arrives in Python as `None`.

### Counting

One more useful piece: `COUNT(*)` counts rows.

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT, year INTEGER);
    INSERT INTO books (title, author, year) VALUES ('Dune', 'Frank Herbert', 1965);
    INSERT INTO books (title, author, year) VALUES ('Beloved', 'Toni Morrison', 1987);
    INSERT INTO books (title, author, year) VALUES ('Emma', 'Jane Austen', 1815);
""")

for row in db.execute("SELECT COUNT(*) FROM books WHERE year > 1900"):
    print(row)
```

Output:

```text
(2,)
```

### Why not just JSON?

| | JSON file | Database |
|---|---|---|
| Change one item | load everything, change, write everything back | `UPDATE ... WHERE id = 3` |
| Find items | write your own loop | `SELECT ... WHERE ... ORDER BY ...` |
| Rules (no empty title, unique id) | you must check yourself | the database enforces them |
| Large amounts of data | gets slow | stays fast |
| Readable in a text editor | yes | no, you need a tool |

JSON is still great for configuration files and for sending data between programs. For the main data of an app, use a database.

## Common mistakes

### A typo in the table name

<!-- error -->
```python
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT)")
db.execute("SELECT * FROM book")
```

```text
sqlite3.OperationalError: no such table: book
```

The table is `books`, with an "s". The database reads names exactly as written. When you see "no such table" or "no such column", check the spelling first.

### Forgetting the quotes around text

<!-- error -->
```python
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT)")
db.execute("SELECT * FROM books WHERE title = Dune")
```

```text
sqlite3.OperationalError: no such column: Dune
```

Without quotes, SQL thinks `Dune` is the name of a column. Text values need single quotes: `WHERE title = 'Dune'`. (In the next file you will learn an even better way: placeholders.)

### Using a column that does not exist

<!-- error -->
```python
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT)")
db.execute("INSERT INTO books (title, author) VALUES ('Dune', 'Frank Herbert')")
```

```text
sqlite3.OperationalError: table books has no column named author
```

The table was created with only `id` and `title`. A table does not grow new columns by itself: you decide the columns in `CREATE TABLE`.

### Breaking a NOT NULL rule

<!-- error -->
```python
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER)")
db.execute("INSERT INTO books (year) VALUES (1965)")
```

```text
sqlite3.IntegrityError: NOT NULL constraint failed: books.title
```

This "error" is the database doing its job: you said every book needs a title. A **constraint** is a rule on a column. Fix the data, not the rule: give the book a title.

### Comparing with `= NULL`

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, year INTEGER);
    INSERT INTO books (title) VALUES ('Untitled notes');
""")
rows = db.execute("SELECT * FROM books WHERE year = NULL").fetchall()
print(rows)
```

```text
[]
```

No error, but no results either, even though there is a book with no year. In SQL, `NULL` means "unknown", and "is this unknown thing equal to another unknown thing?" is also unknown, so the row is never matched. Always write `WHERE year IS NULL`. (`fetchall()` collects all results into a list; you will see it again in the next file.)

## Exercises

All exercises use this table. Copy the setup at the top of each answer you write.

<!-- no-verify -->
```python
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE movies (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER, rating REAL);
    INSERT INTO movies (title, year, rating) VALUES ('Amélie', 2001, 8.3);
    INSERT INTO movies (title, year, rating) VALUES ('Spirited Away', 2001, 8.6);
    INSERT INTO movies (title, year, rating) VALUES ('Central Station', 1998, 8.0);
    INSERT INTO movies (title, year, rating) VALUES ('Paddington 2', 2017, NULL);
""")
```

### Predict the output

#### Exercise 1: A simple filter

What does this print?

<!-- no-verify -->
```python
for row in db.execute("SELECT title FROM movies WHERE year = 2001 ORDER BY title"):
    print(row)
```

<details>
<summary>Show answer</summary>

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE movies (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER, rating REAL);
    INSERT INTO movies (title, year, rating) VALUES ('Amélie', 2001, 8.3);
    INSERT INTO movies (title, year, rating) VALUES ('Spirited Away', 2001, 8.6);
    INSERT INTO movies (title, year, rating) VALUES ('Central Station', 1998, 8.0);
    INSERT INTO movies (title, year, rating) VALUES ('Paddington 2', 2017, NULL);
""")
for row in db.execute("SELECT title FROM movies WHERE year = 2001 ORDER BY title"):
    print(row)
```

```text
('Amélie',)
('Spirited Away',)
```

Two movies are from 2001, sorted alphabetically.

</details>

#### Exercise 2: Which id?

After the setup, what `id` does `Paddington 2` have? And what does `SELECT COUNT(*) FROM movies WHERE rating IS NULL` return?

<details>
<summary>Show answer</summary>

`Paddington 2` has `id` 4, because it was the fourth row inserted and the database numbers rows automatically. The count returns `(1,)`: only Paddington 2 has no rating.

</details>

### Fix the bug

#### Exercise 3: The disappearing rating

Someone wanted to give Paddington 2 a rating of 7.8, and wrote this. Run it in your head: what went wrong, and how do you fix it?

<!-- no-verify -->
```python
db.execute("UPDATE movies SET rating = 7.8")
```

<details>
<summary>Show answer</summary>

There is no `WHERE`, so **every** movie now has a rating of 7.8. Always limit `UPDATE` with a `WHERE`, preferably by id:

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE movies (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER, rating REAL);
    INSERT INTO movies (title, year, rating) VALUES ('Amélie', 2001, 8.3);
    INSERT INTO movies (title, year, rating) VALUES ('Spirited Away', 2001, 8.6);
    INSERT INTO movies (title, year, rating) VALUES ('Central Station', 1998, 8.0);
    INSERT INTO movies (title, year, rating) VALUES ('Paddington 2', 2017, NULL);
""")
db.execute("UPDATE movies SET rating = 7.8 WHERE id = 4")
for row in db.execute("SELECT title, rating FROM movies ORDER BY id"):
    print(row)
```

```text
('Amélie', 8.3)
('Spirited Away', 8.6)
('Central Station', 8.0)
('Paddington 2', 7.8)
```

</details>

#### Exercise 4: No results

This should list the movie with no rating, but prints nothing. Fix it.

<!-- no-verify -->
```python
for row in db.execute("SELECT title FROM movies WHERE rating = NULL"):
    print(row)
```

<details>
<summary>Show answer</summary>

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE movies (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER, rating REAL);
    INSERT INTO movies (title, year, rating) VALUES ('Amélie', 2001, 8.3);
    INSERT INTO movies (title, year, rating) VALUES ('Paddington 2', 2017, NULL);
""")
for row in db.execute("SELECT title FROM movies WHERE rating IS NULL"):
    print(row)
```

```text
('Paddington 2',)
```

Use `IS NULL`, never `= NULL`.

</details>

### Write it

#### Exercise 5: Best rated first

Using the setup, print the title and rating of every movie that has a rating, from the highest rating to the lowest.

<details>
<summary>Hint</summary>

You need `WHERE rating IS NOT NULL` and `ORDER BY rating DESC`.

</details>

<details>
<summary>Show answer</summary>

```python
import sqlite3
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
```

```text
('Spirited Away', 8.6)
('Amélie', 8.3)
('Central Station', 8.0)
```

</details>

#### Exercise 6: Your own table

Create a table `plants` with columns `id` (primary key), `name` (text, required), `water_every_days` (integer) and `location` (text). Insert three plants, then print the names of the plants that need water every 7 days or less, sorted by name.

<details>
<summary>Show answer</summary>

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("""
    CREATE TABLE plants (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        water_every_days INTEGER,
        location TEXT
    )
""")
db.execute("INSERT INTO plants (name, water_every_days, location) VALUES ('Fern', 3, 'bathroom')")
db.execute("INSERT INTO plants (name, water_every_days, location) VALUES ('Cactus', 21, 'window')")
db.execute("INSERT INTO plants (name, water_every_days, location) VALUES ('Basil', 2, 'kitchen')")

for row in db.execute("SELECT name FROM plants WHERE water_every_days <= 7 ORDER BY name"):
    print(row)
```

```text
('Basil',)
('Fern',)
```

</details>

#### Exercise 7: Delete and count

Using the setup, delete all movies released before 2000, then count how many movies are left.

<details>
<summary>Show answer</summary>

```python
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
    CREATE TABLE movies (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER, rating REAL);
    INSERT INTO movies (title, year, rating) VALUES ('Amélie', 2001, 8.3);
    INSERT INTO movies (title, year, rating) VALUES ('Spirited Away', 2001, 8.6);
    INSERT INTO movies (title, year, rating) VALUES ('Central Station', 1998, 8.0);
    INSERT INTO movies (title, year, rating) VALUES ('Paddington 2', 2017, NULL);
""")
db.execute("DELETE FROM movies WHERE year < 2000")
for row in db.execute("SELECT COUNT(*) FROM movies"):
    print(row)
```

```text
(3,)
```

`Central Station` (1998) was deleted.

</details>

## Review

#### Review 1: Classes (module 08)

Write a class `Movie` with `title` and `year`, and a `__str__` that returns `Amélie (2001)`. Create one and print it.

<details>
<summary>Show answer</summary>

```python
class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year})"

print(Movie("Amélie", 2001))
```

```text
Amélie (2001)
```

</details>

#### Review 2: Tuples (module 06)

Each database row arrives as a tuple. What does this print?

```python
row = (3, "Central Station", 1998)
movie_id, title, year = row
print(title, "came out in", year)
```

<details>
<summary>Show answer</summary>

```text
Central Station came out in 1998
```

This is tuple unpacking: each name on the left gets the value in the same position on the right.

</details>

## Recap

- A **table** has **columns** (kinds of information) and **rows** (one item each), like a spreadsheet tab.
- `CREATE TABLE` describes columns and types; `id INTEGER PRIMARY KEY` gives every row a unique number.
- `INSERT` adds, `SELECT ... FROM ... WHERE ... ORDER BY ...` finds, `UPDATE ... SET ... WHERE` changes, `DELETE FROM ... WHERE` removes.
- Never run `UPDATE` or `DELETE` without a `WHERE` unless you really mean "every row".
- `NULL` is "no value" (Python's `None`); find it with `IS NULL`, never `= NULL`.

**Next:** [sqlite.md](sqlite.md)
