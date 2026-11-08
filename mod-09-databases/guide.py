"""Teacher's guide for module 09: Databases.

Every example and every exercise answer from this module's lessons, ready to
show in class. Each item prints its own code and then runs it.

Usage (from this folder):
    uv run guide.py                  list sections and items
    uv run guide.py sql_basics          run every item in a section
    uv run guide.py sqlite.ex05     run one item
    uv run guide.py all              run everything
"""

# Lesson code is copied as-is: long SQL lines and the unused variables in the
# "Common mistakes" items are intentional.
# ruff: noqa: E501, F841

import builtins
import contextlib
import inspect
import os
import sys
import tempfile
import textwrap

SECTIONS: dict[str, dict[str, tuple]] = {}


def item(section, name, note="", run=True):
    """Register a function as a guide item: `section.name`, with a teaching note.

    Use run=False for code that should only be shown (servers, network, API keys,
    third-party libraries): the guide prints it without executing it.
    """

    def register(fn):
        SECTIONS.setdefault(section, {})[name] = (fn, note, run)
        return fn

    return register


@contextlib.contextmanager
def typed(*answers):
    """Simulate a person typing `answers` into input(), echoing them like a terminal."""
    queue = list(answers)
    original = builtins.input

    def fake_input(prompt=""):
        value = queue.pop(0)
        print(f"{prompt}{value}")
        return value

    builtins.input = fake_input
    try:
        yield
    finally:
        builtins.input = original


@contextlib.contextmanager
def scratch_folder():
    """Run file examples inside a throwaway folder, so nothing is left behind."""
    previous = os.getcwd()
    with tempfile.TemporaryDirectory() as folder:
        os.chdir(folder)
        try:
            yield folder
        finally:
            os.chdir(previous)


def show(section, name):
    fn, note, run = SECTIONS[section][name]
    source = inspect.getsource(fn)
    body = source.split(":\n", 1)[1] if source.lstrip().startswith(("@", "def")) else source
    body = textwrap.dedent(body.split('"""', 2)[-1] if fn.__doc__ else body).strip("\n")
    title = fn.__doc__.strip() if fn.__doc__ else name
    print(f"\n=== {section}.{name}: {title}")
    if note:
        print(f"Teacher note: {note}")
    print("--- code")
    print(body)
    if not run:
        print("--- (shown only: run it in a project, see the lesson)")
        return
    print("--- output")
    try:
        fn()
    except Exception as error:  # noqa: BLE001 - broken-on-purpose examples show their error
        print(f"{type(error).__name__}: {error}")


def main(args):
    if not args:
        for section, items in SECTIONS.items():
            print(f"{section}: {', '.join(items)}")
        return
    target = args[0]
    if target == "all":
        for section, items in SECTIONS.items():
            for name in items:
                show(section, name)
        return
    section, _, name = target.partition(".")
    if section not in SECTIONS or (name and name not in SECTIONS[section]):
        print(f"Unknown item: {target}. Run without arguments to see the list.")
        sys.exit(1)
    for each in [name] if name else SECTIONS[section]:
        show(section, each)


# --- sql_basics ------------------------------------------------------------


@item("sql_basics", "playground", "These two lines open every example. Focus on the SQL text.")
def sql_basics_playground():
    """How to try SQL in this file"""
    import sqlite3

    db = sqlite3.connect(":memory:")


@item("sql_basics", "create_table", "Compare with a spreadsheet: columns and their types.")
def sql_basics_create_table():
    """CREATE TABLE: making a table"""
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


@item(
    "sql_basics", "insert", "No id given: the database numbers the rows. Rows come back as tuples."
)
def sql_basics_insert():
    """INSERT: adding rows"""
    import sqlite3

    db = sqlite3.connect(":memory:")
    db.execute(
        "CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT, year INTEGER)"
    )

    db.execute("INSERT INTO books (title, author, year) VALUES ('Dune', 'Frank Herbert', 1965)")
    db.execute("INSERT INTO books (title, author, year) VALUES ('Beloved', 'Toni Morrison', 1987)")

    for row in db.execute("SELECT * FROM books"):
        print(row)


@item("sql_basics", "select", "SELECT never changes anything. * means all columns.")
def sql_basics_select():
    """SELECT: finding rows"""
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


@item("sql_basics", "where", "SQL compares with a single =. Explain the comma in ('Dune',).")
def sql_basics_where():
    """WHERE: filtering"""
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


@item("sql_basics", "order_by", "Without ORDER BY, the order is not guaranteed.")
def sql_basics_order_by():
    """ORDER BY: sorting"""
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


@item("sql_basics", "update", "Ask: what happens without the WHERE?")
def sql_basics_update():
    """UPDATE: changing rows"""
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


@item("sql_basics", "delete", "No undo. DELETE without WHERE empties the table.")
def sql_basics_delete():
    """DELETE: removing rows"""
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


@item("sql_basics", "null", "NULL arrives in Python as None. Use IS NULL.")
def sql_basics_null():
    """NULL: the empty value"""
    import sqlite3

    db = sqlite3.connect(":memory:")
    db.executescript("""
        CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, author TEXT, year INTEGER);
        INSERT INTO books (title, author, year) VALUES ('Dune', 'Frank Herbert', 1965);
        INSERT INTO books (title) VALUES ('Untitled notes');
    """)

    for row in db.execute("SELECT * FROM books WHERE year IS NULL"):
        print(row)


@item("sql_basics", "counting", "COUNT(*) comes back as a one-item tuple.")
def sql_basics_counting():
    """Counting"""
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


@item("sql_basics", "mistake_table_typo", "Check the spelling first: books, with an s.")
def sql_basics_mistake_table_typo():
    """A typo in the table name"""
    import sqlite3

    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT)")
    db.execute("SELECT * FROM book")


@item("sql_basics", "mistake_missing_quotes", "Without quotes, SQL thinks Dune is a column.")
def sql_basics_mistake_missing_quotes():
    """Forgetting the quotes around text"""
    import sqlite3

    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT)")
    db.execute("SELECT * FROM books WHERE title = Dune")


@item("sql_basics", "mistake_unknown_column", "Columns are decided in CREATE TABLE.")
def sql_basics_mistake_unknown_column():
    """Using a column that does not exist"""
    import sqlite3

    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT)")
    db.execute("INSERT INTO books (title, author) VALUES ('Dune', 'Frank Herbert')")


@item("sql_basics", "mistake_not_null", "The database doing its job: a rule was broken.")
def sql_basics_mistake_not_null():
    """Breaking a NOT NULL rule"""
    import sqlite3

    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER)")
    db.execute("INSERT INTO books (year) VALUES (1965)")


@item("sql_basics", "mistake_equals_null", "No error and no rows. The fix is IS NULL.")
def sql_basics_mistake_equals_null():
    """Comparing with = NULL"""
    import sqlite3

    db = sqlite3.connect(":memory:")
    db.executescript("""
        CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, year INTEGER);
        INSERT INTO books (title) VALUES ('Untitled notes');
    """)
    rows = db.execute("SELECT * FROM books WHERE year = NULL").fetchall()
    print(rows)


@item("sql_basics", "ex01", "Ask her to predict the output before running.")
def sql_basics_ex01():
    """Exercise 1: A simple filter"""
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


@item("sql_basics", "ex02", "Ask her to answer before running.")
def sql_basics_ex02():
    """Exercise 2: Which id?"""
    import sqlite3

    db = sqlite3.connect(":memory:")
    db.executescript("""
        CREATE TABLE movies (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER, rating REAL);
        INSERT INTO movies (title, year, rating) VALUES ('Amélie', 2001, 8.3);
        INSERT INTO movies (title, year, rating) VALUES ('Spirited Away', 2001, 8.6);
        INSERT INTO movies (title, year, rating) VALUES ('Central Station', 1998, 8.0);
        INSERT INTO movies (title, year, rating) VALUES ('Paddington 2', 2017, NULL);
    """)
    print(db.execute("SELECT id FROM movies WHERE title = 'Paddington 2'").fetchone())
    print(db.execute("SELECT COUNT(*) FROM movies WHERE rating IS NULL").fetchone())


@item("sql_basics", "ex03", "Answer: the fixed code. Show the broken version first.")
def sql_basics_ex03():
    """Exercise 3: The disappearing rating"""
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


@item("sql_basics", "ex04", "Answer: the fixed code. Show the broken version first.")
def sql_basics_ex04():
    """Exercise 4: No results"""
    import sqlite3

    db = sqlite3.connect(":memory:")
    db.executescript("""
        CREATE TABLE movies (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER, rating REAL);
        INSERT INTO movies (title, year, rating) VALUES ('Amélie', 2001, 8.3);
        INSERT INTO movies (title, year, rating) VALUES ('Paddington 2', 2017, NULL);
    """)
    for row in db.execute("SELECT title FROM movies WHERE rating IS NULL"):
        print(row)


@item("sql_basics", "ex05", "Answer to Exercise 5.")
def sql_basics_ex05():
    """Exercise 5: Best rated first"""
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


@item("sql_basics", "ex06", "Answer to Exercise 6.")
def sql_basics_ex06():
    """Exercise 6: Your own table"""
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
    db.execute(
        "INSERT INTO plants (name, water_every_days, location) VALUES ('Fern', 3, 'bathroom')"
    )
    db.execute(
        "INSERT INTO plants (name, water_every_days, location) VALUES ('Cactus', 21, 'window')"
    )
    db.execute(
        "INSERT INTO plants (name, water_every_days, location) VALUES ('Basil', 2, 'kitchen')"
    )

    for row in db.execute("SELECT name FROM plants WHERE water_every_days <= 7 ORDER BY name"):
        print(row)


@item("sql_basics", "ex07", "Answer to Exercise 7.")
def sql_basics_ex07():
    """Exercise 7: Delete and count"""
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


@item("sql_basics", "review01", "Ask her to predict the output before running.")
def sql_basics_review01():
    """Review 1: Classes (module 08)"""

    class Movie:
        def __init__(self, title, year):
            self.title = title
            self.year = year

        def __str__(self):
            return f"{self.title} ({self.year})"

    print(Movie("Amélie", 2001))


@item("sql_basics", "review02", "Ask her to predict the output before running.")
def sql_basics_review02():
    """Review 2: Tuples (module 06)"""
    row = (3, "Central Station", 1998)
    movie_id, title, year = row
    print(title, "came out in", year)


# --- sqlite ----------------------------------------------------------------


@item("sqlite", "connecting", "connect creates the file the first time. Runs in a temp folder.")
def sqlite_connecting():
    """Connecting"""
    import sqlite3

    with scratch_folder():
        db = sqlite3.connect("library.db")
        db.close()
        print(os.path.exists("library.db"))


@item("sqlite", "fetch_results", "fetchall gives a list; fetchone gives one row or None.")
def sqlite_fetch_results():
    """Running SQL and reading results"""
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


@item("sqlite", "row_factory", "Rows that read by name, like a dictionary.")
def sqlite_row_factory():
    """Rows you can read by name: sqlite3.Row"""
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


@item("sqlite", "placeholders", "Values always go in ?. Note the comma in (title,).")
def sqlite_placeholders():
    """Passing values: always use ? placeholders"""
    import sqlite3

    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER)")

    title = "Beloved"
    year = 1987
    db.execute("INSERT INTO books (title, year) VALUES (?, ?)", (title, year))

    row = db.execute("SELECT * FROM books WHERE title = ?", (title,)).fetchone()
    print(row)


@item("sqlite", "sql_injection", "Ask what the typed text does to the unsafe query.")
def sqlite_sql_injection():
    """Why never build SQL with f-strings"""
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


@item("sqlite", "commit", "The program runs twice, so there are two books. Temp folder.")
def sqlite_commit():
    """Saving changes: commit"""
    import sqlite3

    def program():
        db = sqlite3.connect("library.db")
        db.execute(
            "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER)"
        )
        db.execute("INSERT INTO books (title, year) VALUES (?, ?)", ("Dune", 1965))
        db.commit()
        db.close()

    with scratch_folder():
        program()
        program()
        db = sqlite3.connect("library.db")
        print(db.execute("SELECT COUNT(*) FROM books").fetchone())
        db.close()


@item("sqlite", "closing", "Same idea as with open(...) in module 04. Temp folder.")
def sqlite_closing():
    """Opening and closing safely"""
    import sqlite3
    from contextlib import closing

    with scratch_folder():
        with closing(sqlite3.connect("library.db")) as db:
            db.execute(
                "CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER)"
            )
            db.execute("INSERT INTO books (title, year) VALUES (?, ?)", ("Emma", 1815))
            db.commit()
        # here the connection is already closed
        try:
            db.execute("SELECT * FROM books")
        except sqlite3.ProgrammingError as error:
            print(error)


@item("sqlite", "repository_functions", "One small function per action; each one commits.")
def sqlite_repository_functions():
    """Organizing database code in functions"""
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


@item("sqlite", "json_to_table", "One INSERT per item, one commit at the end.")
def sqlite_json_to_table():
    """Moving data from JSON into a table"""
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


@item("sqlite", "json_file_migration", "A real migration: run it only once. Temp folder.")
def sqlite_json_file_migration():
    """A real migration from books.json into library.db"""
    import json
    import sqlite3
    from contextlib import closing

    with scratch_folder():
        with open("books.json", "w", encoding="utf-8") as file:  # the old data file
            json.dump([{"title": "Dune", "year": 1965}, {"title": "Emma", "year": 1815}], file)

        with open("books.json", encoding="utf-8") as file:
            books = json.load(file)

        with closing(sqlite3.connect("library.db")) as db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT NOT NULL, year INTEGER)"
            )
            for book in books:
                db.execute(
                    "INSERT INTO books (title, year) VALUES (?, ?)", (book["title"], book["year"])
                )
            db.commit()
            print(f"Migrated {len(books)} books")


@item(
    "sqlite",
    "mistake_one_value_tuple",
    "Without the comma, ('Dune') is just text: 4 letters, 4 values.",
)
def sqlite_mistake_one_value_tuple():
    """Forgetting the comma in a one-value tuple"""
    import sqlite3

    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT)")
    db.execute("INSERT INTO books (title) VALUES (?)", ("Dune"))


@item("sqlite", "mistake_wrong_count", "Count the ? and the values: they must match.")
def sqlite_mistake_wrong_count():
    """Different number of ? and values"""
    import sqlite3

    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, year INTEGER)")
    db.execute("INSERT INTO books (title, year) VALUES (?, ?)", ("Dune",))


@item(
    "sqlite",
    "mistake_quoted_placeholder",
    "'?' is the text ?, not a placeholder: no error, no row.",
)
def sqlite_mistake_quoted_placeholder():
    """Putting quotes around ?"""
    import sqlite3

    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT)")
    db.execute("INSERT INTO books (title) VALUES ('Dune')")
    row = db.execute("SELECT * FROM books WHERE title = '?'", ()).fetchone()
    print(row)


@item("sqlite", "mistake_no_commit", "No error, but Emma is gone when the file is opened again.")
def sqlite_mistake_no_commit():
    """Forgetting to commit"""
    import sqlite3

    with scratch_folder():
        db = sqlite3.connect("library.db")
        db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, year INTEGER)")
        db.commit()
        db.close()

        db = sqlite3.connect("library.db")
        db.execute("INSERT INTO books (title, year) VALUES (?, ?)", ("Emma", 1815))
        db.close()  # no commit: the insert is thrown away

        db = sqlite3.connect("library.db")
        print(db.execute("SELECT COUNT(*) FROM books").fetchone())
        db.close()


@item("sqlite", "mistake_table_exists", "The fix is CREATE TABLE IF NOT EXISTS.")
def sqlite_mistake_table_exists():
    """Creating a table that already exists"""
    import sqlite3

    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT)")
    db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT)")


@item("sqlite", "ex01", "Ask her to predict the output before running.")
def sqlite_ex01():
    """Exercise 1: fetchone and fetchall"""
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


@item("sqlite", "ex02", "Ask her to predict the output before running.")
def sqlite_ex02():
    """Exercise 2: The tricky name"""
    import sqlite3

    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE people (id INTEGER PRIMARY KEY, name TEXT)")
    name = "O'Brien"
    db.execute("INSERT INTO people (name) VALUES (?)", (name,))
    print(db.execute("SELECT name FROM people").fetchone()[0])


@item("sqlite", "ex03", "Answer: the fixed code. Show the broken version first.")
def sqlite_ex03():
    """Exercise 3: The crash on search"""
    import sqlite3

    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, year INTEGER)")
    db.execute("INSERT INTO books (title, year) VALUES (?, ?)", ("Emma", 1815))
    print(db.execute("SELECT title, year FROM books WHERE title = ?", ("Emma",)).fetchone())


@item("sqlite", "ex04", "Unsafe vs fixed: the f-string version returns every row.")
def sqlite_ex04():
    """Exercise 4: The unsafe search"""
    import sqlite3

    def find_by_author_unsafe(db, author):
        return db.execute(f"SELECT title FROM books WHERE author = '{author}'").fetchall()

    def find_by_author(db, author):
        return db.execute("SELECT title FROM books WHERE author = ?", (author,)).fetchall()

    db = sqlite3.connect(":memory:")
    db.executescript("""
        CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT);
        INSERT INTO books (title, author) VALUES ('Dune', 'Frank Herbert');
        INSERT INTO books (title, author) VALUES ('Beloved', 'Toni Morrison');
    """)
    attack = "x' OR '1'='1"
    print(find_by_author_unsafe(db, attack))
    print(find_by_author(db, attack))
    print(find_by_author(db, "Toni Morrison"))


@item("sqlite", "ex05", "Answer to Exercise 5.")
def sqlite_ex05():
    """Exercise 5: A to-do repository"""
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


@item("sqlite", "ex06", "Answer to Exercise 6.")
def sqlite_ex06():
    """Exercise 6: Migrate a shopping list"""
    import json
    import sqlite3

    old = '[{"name": "apples", "quantity": 3}, {"name": "bread", "quantity": 1}, {"name": "milk", "quantity": 2}]'
    items = json.loads(old)

    db = sqlite3.connect(":memory:")
    db.row_factory = sqlite3.Row
    db.execute("CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT NOT NULL, quantity INTEGER)")
    for item in items:
        db.execute(
            "INSERT INTO items (name, quantity) VALUES (?, ?)", (item["name"], item["quantity"])
        )
    db.commit()

    for row in db.execute("SELECT * FROM items ORDER BY name"):
        print(f"{row['quantity']} x {row['name']}")


@item("sqlite", "ex07", "Answer to Exercise 7.")
def sqlite_ex07():
    """Exercise 7: Rows into objects"""
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


@item("sqlite", "review01", "The SQL answer, run against a small plants table.")
def sqlite_review01():
    """Review 1: SQL (previous file)"""
    import sqlite3

    db = sqlite3.connect(":memory:")
    db.executescript("""
        CREATE TABLE plants (id INTEGER PRIMARY KEY, name TEXT, location TEXT);
        INSERT INTO plants (name, location) VALUES ('Basil', 'kitchen');
        INSERT INTO plants (name, location) VALUES ('Fern', 'bathroom');
        INSERT INTO plants (name, location) VALUES ('Aloe', 'kitchen');
    """)
    sql = "SELECT name FROM plants WHERE location = ? ORDER BY name"
    print(db.execute(sql, ("kitchen",)).fetchall())


@item("sqlite", "review02", "with closes at the end of the block, like closing(...) does.")
def sqlite_review02():
    """Review 2: with and files (module 04)"""
    with scratch_folder():
        with open("notes.txt", "w", encoding="utf-8") as file:
            file.write("buy milk")
        print(file.closed)


@item("sqlite", "review03", "Ask her to predict the output before running.")
def sqlite_review03():
    """Review 3: Classes with rules (module 08)"""

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


if __name__ == "__main__":
    main(sys.argv[1:])
