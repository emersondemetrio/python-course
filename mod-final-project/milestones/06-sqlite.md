# Milestone 6: SQLite

## Goal

Move the data from `pieces.json` into a real database, **SQLite**, so you can search and update one piece without rewriting the whole file every time.

## Requires

Module 9: SQL basics (`CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `WHERE`) and the `sqlite3` module.

## What you will build

- A database file `atanor.db` with a `pieces` table.
- `atanor/storage.py` rewritten with small functions, one per operation (this is often called a **repository**: the only place in the app that talks to the database).
- A one-time script that copies your existing `pieces.json` into the database.

Why change? With JSON, to advance **one** piece you load **all** pieces, change one, and write **all** of them back. With a database, you send one `UPDATE` for one row. It also lets the web server of milestone 7 handle several requests safely.

SQLite comes with Python: nothing to install. The whole database is a single file.

## Steps

### Step 1: The table

Write the `CREATE TABLE` for `pieces`. Each column is one attribute of `Piece`, plus an `id`. The `history` is a dictionary, so we store it as JSON text.

<details>
<summary>Show answer</summary>

```python
import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS pieces (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    clay        TEXT NOT NULL,
    technique   TEXT NOT NULL,
    glaze       TEXT NOT NULL DEFAULT '',
    temperature INTEGER NOT NULL DEFAULT 0,
    notes       TEXT NOT NULL DEFAULT '',
    created     TEXT NOT NULL,
    stage       TEXT NOT NULL,
    history     TEXT NOT NULL
)
"""

conn = sqlite3.connect(":memory:")
conn.execute(SCHEMA)
columns = [row[1] for row in conn.execute("PRAGMA table_info(pieces)")]
print(columns)
```

Output:

```text
['id', 'name', 'clay', 'technique', 'glaze', 'temperature', 'notes', 'created', 'stage', 'history']
```

- `":memory:"` creates a database that lives only in memory, perfect for experiments and tests. In the app you will use `"atanor.db"`.
- `INTEGER PRIMARY KEY AUTOINCREMENT` gives each piece a unique number, chosen by the database.
- `IF NOT EXISTS` lets you run this every time the app starts without errors.

</details>

### Step 2: Insert a piece

Write `insert_piece(conn, piece)` that inserts a `Piece` and returns the new `id`. Use `?` placeholders, never f-strings, to put values in SQL.

<details>
<summary>Show answer</summary>

```python
import json
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("""CREATE TABLE pieces (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, clay TEXT,
    technique TEXT, glaze TEXT, temperature INTEGER, notes TEXT, created TEXT, stage TEXT, history TEXT)""")


class Piece:
    def __init__(self, name, clay, technique, glaze="", temperature=0, notes="", created="2026-11-08"):
        self.id = None
        self.name, self.clay, self.technique = name, clay, technique
        self.glaze, self.temperature, self.notes = glaze, temperature, notes
        self.created = created
        self.stage = "modeled"
        self.history = {"modeled": created}


def insert_piece(conn, piece):
    cursor = conn.execute(
        """INSERT INTO pieces (name, clay, technique, glaze, temperature, notes, created, stage, history)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (piece.name, piece.clay, piece.technique, piece.glaze, piece.temperature,
         piece.notes, piece.created, piece.stage, json.dumps(piece.history)),
    )
    conn.commit()
    piece.id = cursor.lastrowid
    return piece.id


print(insert_piece(conn, Piece("Blue bowl", "stoneware", "wheel")))
print(insert_piece(conn, Piece("Small vase", "porcelain", "hand-built")))
```

Output:

```text
1
2
```

Why `?` and not an f-string? If a piece were called `Bob's mug`, the apostrophe would break the SQL. Worse, a malicious name could run any command on your database (this attack is called **SQL injection**). With `?`, `sqlite3` passes the values separately and safely.

`conn.commit()` makes the change permanent. Without it, the insert is lost when the program closes.

</details>

### Step 3: Read pieces back

Write `row_to_piece(row)` and `all_pieces(conn)`. Use `conn.row_factory = sqlite3.Row` so you can read columns by name, like a dictionary.

<details>
<summary>Show answer</summary>

```python
import json
import sqlite3


class Piece:
    def __init__(self, name, clay, technique, created="2026-11-08"):
        self.id = None
        self.name, self.clay, self.technique = name, clay, technique
        self.created = created
        self.stage = "modeled"
        self.history = {"modeled": created}

    def __str__(self):
        return f"{self.name} ({self.clay}, {self.technique}) - {self.stage}"


conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite3.Row
conn.execute("CREATE TABLE pieces (id INTEGER PRIMARY KEY, name TEXT, clay TEXT, technique TEXT, created TEXT, stage TEXT, history TEXT)")
conn.execute("INSERT INTO pieces (name, clay, technique, created, stage, history) VALUES ('Blue bowl', 'stoneware', 'wheel', '2026-11-01', 'drying', '{\"modeled\": \"2026-11-01\", \"drying\": \"2026-11-02\"}')")


def row_to_piece(row):
    piece = Piece(row["name"], row["clay"], row["technique"], row["created"])
    piece.id = row["id"]
    piece.stage = row["stage"]
    piece.history = json.loads(row["history"])
    return piece


def all_pieces(conn):
    rows = conn.execute("SELECT * FROM pieces ORDER BY id")
    return [row_to_piece(row) for row in rows]


for piece in all_pieces(conn):
    print(piece.id, piece, piece.history)
```

Output:

```text
1 Blue bowl (stoneware, wheel) - drying {'modeled': '2026-11-01', 'drying': '2026-11-02'}
```

`json.dumps` turns a dictionary into text (to save). `json.loads` turns the text back into a dictionary (to read). The `s` stands for "string".

</details>

### Step 4: Find one piece and update it

Write:

- `get_piece(conn, piece_id)`: returns one `Piece` or `None`.
- `find_by_name(conn, name)`: search ignoring uppercase and lowercase.
- `update_stage(conn, piece)`: saves the new `stage` and `history` of a piece.

<details>
<summary>Show answer</summary>

```python
import json
import sqlite3

conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite3.Row
conn.execute("CREATE TABLE pieces (id INTEGER PRIMARY KEY, name TEXT, stage TEXT, history TEXT)")
conn.execute("INSERT INTO pieces (name, stage, history) VALUES ('Blue bowl', 'modeled', '{\"modeled\": \"2026-11-01\"}')")


def get_piece(conn, piece_id):
    row = conn.execute("SELECT * FROM pieces WHERE id = ?", (piece_id,)).fetchone()
    return dict(row) if row else None


def find_by_name(conn, name):
    row = conn.execute("SELECT * FROM pieces WHERE lower(name) = lower(?)", (name,)).fetchone()
    return dict(row) if row else None


def update_stage(conn, piece_id, stage, history):
    conn.execute("UPDATE pieces SET stage = ?, history = ? WHERE id = ?",
                 (stage, json.dumps(history), piece_id))
    conn.commit()


piece = find_by_name(conn, "BLUE BOWL")
history = json.loads(piece["history"])
history["drying"] = "2026-11-02"
update_stage(conn, piece["id"], "drying", history)

print(get_piece(conn, 1)["stage"])
print(get_piece(conn, 99))
```

Output:

```text
drying
None
```

To keep this example short it uses dictionaries. In your `storage.py`, `get_piece` and `find_by_name` return `row_to_piece(row)`, and `update_stage(conn, piece)` reads `piece.stage`, `piece.history` and `piece.id`.

`(piece_id,)` with a comma is a tuple with one item. Without the comma, Python sees just a number in parentheses, and `sqlite3` complains.

</details>

### Step 5: The new `storage.py`

Put everything together in `atanor/storage.py`, with a `connect(path="atanor.db")` function that opens the database and creates the table if needed.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# atanor/storage.py
import json
import sqlite3

from atanor.piece import Piece

SCHEMA = """
CREATE TABLE IF NOT EXISTS pieces (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    clay        TEXT NOT NULL,
    technique   TEXT NOT NULL,
    glaze       TEXT NOT NULL DEFAULT '',
    temperature INTEGER NOT NULL DEFAULT 0,
    notes       TEXT NOT NULL DEFAULT '',
    created     TEXT NOT NULL,
    stage       TEXT NOT NULL,
    history     TEXT NOT NULL
)
"""


def connect(path="atanor.db"):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute(SCHEMA)
    return conn


def row_to_piece(row):
    piece = Piece(row["name"], row["clay"], row["technique"], row["glaze"],
                  row["temperature"], row["notes"], row["created"])
    piece.id = row["id"]
    piece.stage = row["stage"]
    piece.history = json.loads(row["history"])
    return piece


def insert_piece(conn, piece):
    cursor = conn.execute(
        """INSERT INTO pieces (name, clay, technique, glaze, temperature, notes, created, stage, history)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (piece.name, piece.clay, piece.technique, piece.glaze, piece.temperature,
         piece.notes, piece.created, piece.stage, json.dumps(piece.history)),
    )
    conn.commit()
    piece.id = cursor.lastrowid
    return piece.id


def all_pieces(conn):
    return [row_to_piece(row) for row in conn.execute("SELECT * FROM pieces ORDER BY id")]


def get_piece(conn, piece_id):
    row = conn.execute("SELECT * FROM pieces WHERE id = ?", (piece_id,)).fetchone()
    return row_to_piece(row) if row else None


def find_by_name(conn, name):
    row = conn.execute("SELECT * FROM pieces WHERE lower(name) = lower(?)", (name,)).fetchone()
    return row_to_piece(row) if row else None


def update_stage(conn, piece):
    conn.execute("UPDATE pieces SET stage = ?, history = ? WHERE id = ?",
                 (piece.stage, json.dumps(piece.history), piece.id))
    conn.commit()
```

Also add `self.id = None` to `Piece.__init__`, and include `"id"` in `to_dict`.

In `main.py`, open the connection once (`conn = connect()`) and call these functions instead of loading and saving the whole list.

</details>

### Step 6: Migrate the old data

Write `migrate.py`, a script you run **once**: it reads `pieces.json` with the old `load_pieces` logic and inserts every piece into the database.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# migrate.py
import json
from pathlib import Path

from atanor.piece import Piece
from atanor.storage import connect, insert_piece

source = Path("pieces.json")
if not source.exists():
    print("Nothing to migrate.")
else:
    conn = connect()
    with open(source, "r", encoding="utf-8") as f:
        data = json.load(f)
    for item in data:
        insert_piece(conn, Piece.from_dict(item))
    print(f"Migrated {len(data)} pieces into atanor.db.")
```

```console
PS C:\Users\you\Projects\atanor> uv run migrate.py
Migrated 3 pieces into atanor.db.
```

Run it only once, or every piece is inserted twice. Keep `pieces.json` as a backup until you are sure everything is in the database.

</details>

### Step 7: Tests with a database in memory

Update `tests/test_storage.py` to use `connect(":memory:")`. Every test gets a fresh, empty database.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# tests/test_storage.py
import pytest

from atanor.piece import Piece
from atanor.storage import connect, find_by_name, get_piece, insert_piece, update_stage


@pytest.fixture
def conn():
    return connect(":memory:")


def test_insert_and_get(conn):
    piece_id = insert_piece(conn, Piece("Bowl", "stoneware", "wheel", created="2026-11-01"))
    assert get_piece(conn, piece_id).name == "Bowl"


def test_update_stage_keeps_history(conn):
    piece = Piece("Bowl", "stoneware", "wheel", created="2026-11-01")
    insert_piece(conn, piece)
    piece.advance("2026-11-02")
    update_stage(conn, piece)
    saved = find_by_name(conn, "bowl")
    assert saved.stage == "drying"
    assert saved.history == {"modeled": "2026-11-01", "drying": "2026-11-02"}


def test_missing_piece_is_none(conn):
    assert get_piece(conn, 42) is None
```

A **fixture** is a function pytest runs before each test that asks for it by name. Here, every test that has a `conn` parameter receives a brand new database.

</details>

## Checkpoint

```console
PS C:\Users\you\Projects\atanor> uv run pytest
.......                                                     [100%]
7 passed in 0.05s
PS C:\Users\you\Projects\atanor> uv run main.py
...
> 2
1. Blue bowl (stoneware, wheel) - bisque_fired
2. Small vase (porcelain, hand-built) - drying
```

If you have the free app **DB Browser for SQLite**, open `atanor.db` with it and look at the table.

## Commit

```powershell
git add .
git commit -m "Store pieces in SQLite and migrate from JSON"
git push
```

`*.db` is already in `.gitignore`.

## Stretch goals

#### Stretch 1: Count by stage in SQL

Use `GROUP BY` to count pieces per stage in a single query.

<details>
<summary>Show answer</summary>

```python
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE pieces (name TEXT, stage TEXT)")
conn.executemany("INSERT INTO pieces VALUES (?, ?)",
                 [("Bowl", "drying"), ("Vase", "modeled"), ("Mug", "drying")])

for stage, total in conn.execute("SELECT stage, COUNT(*) FROM pieces GROUP BY stage ORDER BY stage"):
    print(stage, total)
```

Output:

```text
drying 2
modeled 1
```

</details>

#### Stretch 2: Search by part of the name

Return every piece whose name **contains** a word, for example all pieces with "bowl".

<details>
<summary>Show answer</summary>

```python
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE pieces (name TEXT)")
conn.executemany("INSERT INTO pieces VALUES (?)", [("Blue bowl",), ("Rice Bowl",), ("Vase",)])

word = "bowl"
rows = conn.execute("SELECT name FROM pieces WHERE lower(name) LIKE ?", (f"%{word.lower()}%",))
print([name for (name,) in rows])
```

Output:

```text
['Blue bowl', 'Rice Bowl']
```

In `LIKE`, `%` means "anything". Notice the f-string builds only the **value** (`%bowl%`), which is still passed with `?`. The SQL text itself never contains user input.

</details>

**Next:** [Milestone 7: A web API](07-web-api.md)
