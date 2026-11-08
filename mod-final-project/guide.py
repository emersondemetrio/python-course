# ruff: noqa: UP015, E402, F811
# Teacher's guide: Final project, Atanor
# Every step and stretch-goal answer from the milestones, in order.
# Run it from this folder:  python guide.py
#
# Where the real program uses input(), this guide uses a list of answers
# (the ones from the milestone's checkpoint) and takes them one by one with
# answers.pop(0). Files are created here and removed at the end of each
# milestone. Flask, pytest, git, uv and the AI calls are only shown as comments.

import json
import os
import sqlite3
from datetime import date

print("=" * 50)
print("MILESTONE 1: a text file")

print("\n--- Step 1: create the folder and the file (terminal)")
# cd ~\Projects
# mkdir atanor
# cd atanor
# cursor .

print("\n--- Step 2: turn a piece into a line")


def make_line(name, clay):
    return f"{name};{clay}"


print(make_line("Blue bowl", "stoneware"))

print("\n--- Step 3: turn a line back into a piece")


def describe(line):
    parts = line.split(";")
    name = parts[0]
    clay = parts[1]
    return f"{name} ({clay})"


print(describe("Blue bowl;stoneware"))
print(describe("Small vase;porcelain"))

print("\n--- Step 4: save a piece in the file")


def save_piece(name, clay):
    with open("pieces.txt", "a", encoding="utf-8") as file:
        file.write(make_line(name, clay) + "\n")


save_piece("Blue bowl", "stoneware")
print("Saved one line in pieces.txt")

print("\n--- Step 5: read all the pieces")


def load_pieces():
    with open("pieces.txt", "r", encoding="utf-8") as file:
        return file.read().splitlines()


print(load_pieces())

print("\n--- Step 6: list the pieces, numbered")


def show_pieces(lines):
    print("Your pieces:")
    for number, line in enumerate(lines, start=1):
        print(f"{number}. {describe(line)}")


show_pieces(["Blue bowl;stoneware", "Small vase;porcelain"])

print("\n--- Step 7: one function to control everything")
# In the real program, name and clay come from input("Piece name: ") and input("Clay: ").
answers = ["Small vase", "porcelain"]


def main():
    name = answers.pop(0)  # input("Piece name: ")
    clay = answers.pop(0)  # input("Clay: ")
    save_piece(name, clay)
    print("Saved!")
    print()
    show_pieces(load_pieces())


main()

print("\n--- Stretch 1: count the pieces")
lines = ["Blue bowl;stoneware", "Small vase;porcelain"]
print(f"You have {len(lines)} pieces.")

print("\n--- Stretch 2: do not save empty names")
# def main():
#     name = input("Piece name: ").strip()
#     if name == "":
#         print("The name cannot be empty.")
#         return
#     clay = input("Clay: ")
#     save_piece(name, clay)
#     print("Saved!")
#     print()
#     show_pieces(load_pieces())
name = "   ".strip()  # what happens if she only types spaces
if name == "":
    print("The name cannot be empty.")

print("\n--- Stretch 3: add the technique")


def make_line_3(name, clay, technique):
    return f"{name};{clay};{technique}"


def describe_3(line):
    name, clay, technique = line.split(";")
    return f"{name} ({clay}, {technique})"


print(describe_3(make_line_3("Blue bowl", "stoneware", "wheel")))
# (In her file both functions keep the names make_line and describe.)

os.remove("pieces.txt")


print("\n" + "=" * 50)
print("MILESTONE 2: a repository (all terminal)")

print("\n--- Step 1: start the repository")
# cd ~\Projects\atanor
# git init
# git status

print("\n--- Step 2: keep your data out of Git (.gitignore)")
# # My personal data
# pieces.txt
# pieces.json
# *.db
#
# # Python creates these automatically
# __pycache__/
# .venv/

print("\n--- Step 3: write the README.md")
# # Atanor
#
# A small program to catalog my ceramic pieces.
#
# ## How to run
#
#     python atanor.py
#
# ## Status
#
# Milestone 2 of 8: pieces are saved in a text file.

print("\n--- Step 4: the first commit")
# git add atanor.py .gitignore README.md
# git status
# git commit -m "Save and list ceramic pieces in a text file"
# git log --oneline

print("\n--- Step 5: create the repository on GitHub")
# Create an EMPTY repo called atanor on github.com, then:
# git remote add origin https://github.com/YOUR-USER/atanor.git
# git push -u origin main

print("\n--- Step 6: the everyday cycle")
# git status
# git diff
# git add atanor.py
# git commit -m "Make the save message clearer"
# git push

print("\n--- Stretch 1: a good commit message")
# 1. changes   2. fixed stuff in atanor   3. Ask for the technique when saving a piece
print("Best: 'Ask for the technique when saving a piece': says what it does, starts with a verb.")

print("\n--- Stretch 2: look at the past")
# git log --oneline
# git show a1b2c3d     (use the hash of her first commit; q to leave)


print("\n" + "=" * 50)
print("MILESTONE 3: JSON records")

print("\n--- What one piece looks like")
piece = {
    "name": "Blue bowl",
    "clay": "stoneware",
    "technique": "wheel",
    "glaze": "celadon",
    "temperature": 1240,
    "notes": "thin walls",
    "created": "2026-11-08",
    "stage": "modeled",
}
print(piece)

print("\n--- Step 1: the stages")
STAGES = ["modeled", "drying", "bisque_fired", "glazed", "glaze_fired"]

position = STAGES.index("drying")
print(position)
print(STAGES[position + 1])

print("\n--- Step 2: create a piece")


def make_piece(name, clay, technique, glaze, temperature, notes, created):
    return {
        "name": name,
        "clay": clay,
        "technique": technique,
        "glaze": glaze,
        "temperature": temperature,
        "notes": notes,
        "created": created,
        "stage": "modeled",
    }


bowl = make_piece("Blue bowl", "stoneware", "wheel", "celadon", 1240, "thin walls", "2026-11-08")
print(bowl["name"], "-", bowl["stage"])
# Today's date, in the real program:
created = date.today().isoformat()

print("\n--- Step 3: describe a piece")


def describe_piece(piece):
    return f"{piece['name']} ({piece['clay']}, {piece['technique']}) - {piece['stage']}"


bowl = {"name": "Blue bowl", "clay": "stoneware", "technique": "wheel", "stage": "modeled"}
print(describe_piece(bowl))
# (In her file this function is called describe.)

print("\n--- Step 4: save and load the list")
FILE = "pieces.json"


def save_pieces(pieces):
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(pieces, file, ensure_ascii=False, indent=2)


def load_json_pieces():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as file:
        return json.load(file)


# The lesson uses pathlib: FILE = Path("pieces.json") and FILE.exists(). Same idea.
# (In her file the loader is called load_pieces.)
print(load_json_pieces())  # no file yet: empty list
save_pieces([bowl])
print(load_json_pieces())

print("\n--- Step 5: search by name")


def find_piece(pieces, name):
    for piece in pieces:
        if piece["name"].lower() == name.lower():
            return piece
    return None


pieces = [
    {"name": "Blue bowl", "stage": "drying"},
    {"name": "Small vase", "stage": "modeled"},
]
print(find_piece(pieces, "small VASE"))
print(find_piece(pieces, "Teapot"))

print("\n--- Step 6: move to the next stage")


def advance(piece):
    position = STAGES.index(piece["stage"])
    if position == len(STAGES) - 1:
        return False
    piece["stage"] = STAGES[position + 1]
    return True


bowl = {"name": "Blue bowl", "stage": "glazed"}
print(advance(bowl), bowl["stage"])
print(advance(bowl), bowl["stage"])

print("\n--- Step 7: the menu (with the checkpoint's answers)")
# Every answers.pop(0) is an input(...) in the real program.
answers = [
    "1",
    "Blue bowl",
    "stoneware",
    "wheel",
    "celadon",
    "1240",
    "thin walls",
    "3",
    "blue bowl",
    "0",
]


def ask(prompt):
    value = answers.pop(0)
    print(prompt + value)
    return value


def add_piece(pieces):
    name = ask("Name: ")
    clay = ask("Clay: ")
    technique = ask("Technique: ")
    glaze = ask("Glaze: ")
    temperature = int(ask("Firing temperature (°C): "))
    notes = ask("Notes: ")
    piece = make_piece(name, clay, technique, glaze, temperature, notes, date.today().isoformat())
    pieces.append(piece)
    save_pieces(pieces)
    print("Saved!")


def list_pieces(pieces):
    if not pieces:
        print("No pieces yet.")
    for number, piece in enumerate(pieces, start=1):
        print(f"{number}. {describe_piece(piece)}")


def advance_piece(pieces):
    name = ask("Which piece? ")
    piece = find_piece(pieces, name)
    if piece is None:
        print("Piece not found.")
    elif advance(piece):
        save_pieces(pieces)
        print(f"{piece['name']} is now {piece['stage']}.")
    else:
        print(f"{piece['name']} is already finished.")


def menu():
    pieces = []  # the real program starts with load_pieces()
    while True:
        print()
        print("1. Add a piece")
        print("2. List pieces")
        print("3. Advance a piece")
        print("0. Exit")
        choice = ask("> ")
        if choice == "1":
            add_piece(pieces)
        elif choice == "2":
            list_pieces(pieces)
        elif choice == "3":
            advance_piece(pieces)
        elif choice == "0":
            break
        else:
            print("Invalid option.")


menu()
# Commit:
# git add atanor.py
# git commit -m "Store pieces as JSON records with a lifecycle stage"
# git push

print("\n--- Stretch 1: filter by stage")


def by_stage(pieces, stage):
    return [piece for piece in pieces if piece["stage"] == stage]


pieces = [
    {"name": "Blue bowl", "stage": "drying"},
    {"name": "Small vase", "stage": "modeled"},
    {"name": "Mug", "stage": "drying"},
]
for piece in by_stage(pieces, "drying"):
    print(piece["name"])

print("\n--- Stretch 2: count per stage")
pieces = [{"stage": "drying"}, {"stage": "modeled"}, {"stage": "drying"}]

counts = {stage: 0 for stage in STAGES}
for piece in pieces:
    counts[piece["stage"]] += 1

for stage, total in counts.items():
    print(f"{stage}: {total}")

print("\n--- Stretch 3: import the old text file")
lines = ["Blue bowl;stoneware", "Small vase;porcelain"]
pieces = []
for line in lines:
    name, clay = line.split(";")
    pieces.append(make_piece(name, clay, "", "", 0, "", "2026-11-08"))

print(len(pieces), pieces[1]["name"], pieces[1]["clay"])

os.remove("pieces.json")

print("\n" + "=" * 50)
print("MILESTONE 4: modules and tests")

print("\n--- The folder she will end up with")
# atanor/
# ├── main.py              # only the menu: asks, shows, calls
# ├── pyproject.toml       # created by uv
# ├── uv.lock              # created by uv
# ├── atanor/
# │   ├── __init__.py      # empty: marks the folder as a package
# │   ├── pieces.py        # STAGES, make_piece, find_piece, advance...
# │   └── storage.py       # saving and loading pieces.json
# └── tests/
#     └── test_pieces.py

print("\n--- Step 1: turn the folder into a uv project (terminal)")
# cd ~\Projects\atanor
# uv init --bare
# uv add --dev pytest ruff
# uv run ruff check
# uv run ruff format

print("\n--- Step 2: an exception of our own")


class StageError(Exception):
    pass


def advance(piece):
    position = STAGES.index(piece["stage"])
    if position == len(STAGES) - 1:
        raise StageError(f"{piece['name']} is already finished.")
    piece["stage"] = STAGES[position + 1]


bowl = {"name": "Blue bowl", "stage": "glazed"}
advance(bowl)
print(bowl["stage"])
try:
    advance(bowl)
except StageError as error:
    print("Error:", error)

print("\n--- Step 3: move the rules into atanor/pieces.py")
# The file atanor/pieces.py contains exactly these, moved from atanor.py:
#   STAGES, StageError, make_piece, describe, find_piece, advance (the new one, with raise)
# Nothing changes in the code, only where it lives.

print("\n--- Step 4: move saving and loading into atanor/storage.py")
# Same as milestone 3, plus a file parameter (so tests can use another file)
# and a clear error when the JSON is damaged:


def save_pieces(pieces, file="pieces.json"):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(pieces, f, ensure_ascii=False, indent=2)


def load_pieces(file="pieces.json"):
    if not os.path.exists(file):
        return []
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError(f"{file} is damaged. Fix it or delete it to start over.") from None


# The lesson uses pathlib: FILE = Path("pieces.json") and Path(file).exists().
with open("broken.json", "w", encoding="utf-8") as f:
    f.write("{ this is not json")
try:
    load_pieces("broken.json")
except ValueError as error:
    print(error)
os.remove("broken.json")

print("\n--- Step 5: the menu in main.py (with the checkpoint's answers)")
# main.py starts with:
#   from datetime import date
#   from atanor.pieces import StageError, advance, describe, find_piece, make_piece
#   from atanor.storage import load_pieces, save_pieces
# New ideas here: try/except around int(), and a dictionary of actions instead of if/elif.
# The second piece types "hot" as the temperature, to show the new try/except.
answers = ["1", "Blue bowl", "stoneware", "wheel", "celadon", "1240", "thin walls"]
answers += ["1", "Mug", "porcelain", "wheel", "white", "hot", "2", "0"]


def add_piece(pieces):
    name = ask("Name: ")
    clay = ask("Clay: ")
    technique = ask("Technique: ")
    glaze = ask("Glaze: ")
    try:
        temperature = int(ask("Firing temperature (°C): "))
    except ValueError:
        print("Temperature must be a number. Piece not saved.")
        return
    notes = ask("Notes: ")
    pieces.append(
        make_piece(name, clay, technique, glaze, temperature, notes, date.today().isoformat())
    )
    save_pieces(pieces)
    print("Saved!")


def advance_piece(pieces):
    piece = find_piece(pieces, ask("Which piece? "))
    if piece is None:
        print("Piece not found.")
        return
    try:
        advance(piece)
    except StageError as error:
        print(error)
        return
    save_pieces(pieces)
    print(f"{piece['name']} is now {piece['stage']}.")


def main():
    pieces = load_pieces()
    actions = {"1": add_piece, "2": list_pieces, "3": advance_piece}
    while True:
        print()
        print("1. Add a piece")
        print("2. List pieces")
        print("3. Advance a piece")
        print("0. Exit")
        choice = ask("> ")
        if choice == "0":
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid option.")
        else:
            action(pieces)


main()
# In main.py the call is protected:
# if __name__ == "__main__":
#     main()

print("\n--- Step 6: the first tests (tests/test_pieces.py, run with: uv run pytest)")
# import pytest
#
# from atanor.pieces import StageError, advance, find_piece, make_piece
#
#
# def test_new_piece_starts_modeled():
#     piece = make_piece("Bowl", "stoneware", "wheel", "", 1240, "", "2026-11-08")
#     assert piece["stage"] == "modeled"
#
#
# def test_advance_moves_to_next_stage():
#     piece = {"name": "Bowl", "stage": "drying"}
#     advance(piece)
#     assert piece["stage"] == "bisque_fired"
#
#
# def test_cannot_advance_finished_piece():
#     piece = {"name": "Bowl", "stage": "glaze_fired"}
#     with pytest.raises(StageError):
#         advance(piece)
#
#
# def test_find_piece_ignores_case():
#     pieces = [{"name": "Blue Bowl"}]
#     assert find_piece(pieces, "blue bowl") is pieces[0]
#
# Expected:  4 passed

print("\n--- Step 7: test the storage with a temporary file (tests/test_storage.py)")
# from atanor.storage import load_pieces, save_pieces
#
#
# def test_save_and_load(tmp_path):
#     file = tmp_path / "pieces.json"
#     pieces = [{"name": "Cerâmica azul", "stage": "drying"}]
#     save_pieces(pieces, file)
#     assert load_pieces(file) == pieces
#
#
# def test_missing_file_gives_empty_list(tmp_path):
#     assert load_pieces(tmp_path / "nothing.json") == []
#
# Expected:  6 passed (both test files)
# Commit:
# git add .
# git commit -m "Split into a package, add StageError and tests"
# git push

print("\n--- Stretch 1: advancing an unknown stage")


def advance(piece):
    if piece["stage"] not in STAGES:
        raise StageError(f"Unknown stage: {piece['stage']}")
    position = STAGES.index(piece["stage"])
    if position == len(STAGES) - 1:
        raise StageError(f"{piece['name']} is already finished.")
    piece["stage"] = STAGES[position + 1]


try:
    advance({"name": "Mug", "stage": "broken"})
except StageError as error:
    print(error)

print("\n--- Stretch 2: one test, many cases (pytest)")
# import pytest
#
# from atanor.pieces import advance
#
#
# @pytest.mark.parametrize("current, expected", [
#     ("modeled", "drying"),
#     ("drying", "bisque_fired"),
#     ("bisque_fired", "glazed"),
#     ("glazed", "glaze_fired"),
# ])
# def test_every_step(current, expected):
#     piece = {"name": "Bowl", "stage": current}
#     advance(piece)
#     assert piece["stage"] == expected

os.remove("pieces.json")


print("\n" + "=" * 50)
print("MILESTONE 5: the Piece class")

print("\n--- Step 1: the class and its attributes")


class Piece:
    def __init__(
        self, name, clay, technique, glaze="", temperature=0, notes="", created="2026-11-08"
    ):
        self.name = name
        self.clay = clay
        self.technique = technique
        self.glaze = glaze
        self.temperature = temperature
        self.notes = notes
        self.created = created
        self.stage = "modeled"
        self.history = {"modeled": created}


bowl = Piece("Blue bowl", "stoneware", "wheel", created="2026-11-01")
print(bowl.name, bowl.stage, bowl.history)
# In the real app, created defaults to today:
#     def __init__(self, ..., created=None):
#         if created is None:
#             created = date.today().isoformat()

print("\n--- Step 2: how a piece looks when printed")


class Piece:
    def __init__(self, name, clay, technique, created="2026-11-08"):
        self.name = name
        self.clay = clay
        self.technique = technique
        self.created = created
        self.stage = "modeled"
        self.history = {"modeled": created}

    def __str__(self):
        return f"{self.name} ({self.clay}, {self.technique}) - {self.stage}"


print(Piece("Blue bowl", "stoneware", "wheel"))

print("\n--- Step 3: advancing, with the date")


class Piece:
    def __init__(self, name, clay, technique, created="2026-11-08"):
        self.name = name
        self.clay = clay
        self.technique = technique
        self.created = created
        self.stage = "modeled"
        self.history = {"modeled": created}

    def __str__(self):
        return f"{self.name} ({self.clay}, {self.technique}) - {self.stage}"

    def advance(self, on_date):
        position = STAGES.index(self.stage)
        if position == len(STAGES) - 1:
            raise StageError(f"{self.name} is already finished.")
        self.stage = STAGES[position + 1]
        self.history[self.stage] = on_date


bowl = Piece("Blue bowl", "stoneware", "wheel", created="2026-11-01")
bowl.advance("2026-11-02")
bowl.advance("2026-11-10")
print(bowl)
print(bowl.history)

print("\n--- Step 4: is it finished?")


class Piece:
    def __init__(self, name):
        self.name = name
        self.stage = "modeled"

    def is_finished(self):
        return self.stage == STAGES[-1]


mug = Piece("Mug")
print(mug.is_finished())
mug.stage = "glaze_fired"
print(mug.is_finished())

print("\n--- Step 5: from object to dictionary and back")


class Piece:
    def __init__(
        self, name, clay, technique, glaze="", temperature=0, notes="", created="2026-11-08"
    ):
        self.name = name
        self.clay = clay
        self.technique = technique
        self.glaze = glaze
        self.temperature = temperature
        self.notes = notes
        self.created = created
        self.stage = "modeled"
        self.history = {"modeled": created}

    def to_dict(self):
        return {
            "name": self.name,
            "clay": self.clay,
            "technique": self.technique,
            "glaze": self.glaze,
            "temperature": self.temperature,
            "notes": self.notes,
            "created": self.created,
            "stage": self.stage,
            "history": self.history,
        }

    @classmethod
    def from_dict(cls, data):
        piece = cls(
            data["name"],
            data["clay"],
            data["technique"],
            data["glaze"],
            data["temperature"],
            data["notes"],
            data["created"],
        )
        piece.stage = data["stage"]
        piece.history = data.get("history", {data["stage"]: data["created"]})
        return piece


bowl = Piece("Blue bowl", "stoneware", "wheel", "celadon", 1240, "thin walls", "2026-11-01")
data = bowl.to_dict()
copy = Piece.from_dict(data)
print(copy.name, copy.temperature, copy.history)
print(copy.to_dict() == data)

print("\n--- Step 6: plug the class into the app")
# atanor/storage.py now saves and loads Piece objects:
#
# from atanor.piece import Piece
#
# def save_pieces(pieces, file=FILE):
#     with open(file, "w", encoding="utf-8") as f:
#         json.dump([piece.to_dict() for piece in pieces], f, ensure_ascii=False, indent=2)
#
# def load_pieces(file=FILE):
#     if not Path(file).exists():
#         return []
#     with open(file, "r", encoding="utf-8") as f:
#         return [Piece.from_dict(data) for data in json.load(f)]
#
# tests/test_piece.py (uv run pytest):
#
# def test_advance_records_the_date():
#     piece = Piece("Bowl", "stoneware", "wheel", created="2026-11-01")
#     piece.advance("2026-11-02")
#     assert piece.stage == "drying"
#     assert piece.history["drying"] == "2026-11-02"
#
# def test_cannot_advance_finished_piece():
#     piece = Piece("Bowl", "stoneware", "wheel")
#     piece.stage = "glaze_fired"
#     with pytest.raises(StageError):
#         piece.advance("2026-11-02")
#
# def test_round_trip():
#     piece = Piece("Bowl", "stoneware", "wheel", "celadon", 1240, "", "2026-11-01")
#     assert Piece.from_dict(piece.to_dict()).to_dict() == piece.to_dict()
#
# Commit:
# git add .
# git commit -m "Model pieces with a Piece class that keeps stage history"
# git push

print("\n--- Stretch 1: how many days in the current stage")


class Piece:
    def __init__(self, name):
        self.name = name
        self.stage = "drying"
        self.history = {"modeled": "2026-11-01", "drying": "2026-11-02"}

    def days_in_stage(self, today):
        started = date.fromisoformat(self.history[self.stage])
        return (date.fromisoformat(today) - started).days


bowl = Piece("Blue bowl")
print(bowl.days_in_stage("2026-11-10"))

print("\n--- Stretch 2: __repr__")


class Piece:
    def __init__(self, name, stage):
        self.name = name
        self.stage = stage

    def __repr__(self):
        return f"Piece({self.name!r}, {self.stage!r})"


print([Piece("Blue bowl", "drying"), Piece("Mug", "glazed")])

print("\n" + "=" * 50)
print("MILESTONE 6: SQLite")

print("\n--- Step 1: the table")
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
conn.close()

print("\n--- The Piece class from milestone 5, all together")
# Steps 2 to 7 use the complete class: history, advance, __str__, to_dict, from_dict.


class Piece:
    def __init__(
        self, name, clay, technique, glaze="", temperature=0, notes="", created="2026-11-08"
    ):
        self.id = None
        self.name = name
        self.clay = clay
        self.technique = technique
        self.glaze = glaze
        self.temperature = temperature
        self.notes = notes
        self.created = created
        self.stage = "modeled"
        self.history = {"modeled": created}

    def __str__(self):
        return f"{self.name} ({self.clay}, {self.technique}) - {self.stage}"

    def advance(self, on_date):
        position = STAGES.index(self.stage)
        if position == len(STAGES) - 1:
            raise StageError(f"{self.name} is already finished.")
        self.stage = STAGES[position + 1]
        self.history[self.stage] = on_date

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "clay": self.clay,
            "technique": self.technique,
            "glaze": self.glaze,
            "temperature": self.temperature,
            "notes": self.notes,
            "created": self.created,
            "stage": self.stage,
            "history": self.history,
        }

    @classmethod
    def from_dict(cls, data):
        piece = cls(
            data["name"],
            data["clay"],
            data["technique"],
            data["glaze"],
            data["temperature"],
            data["notes"],
            data["created"],
        )
        piece.stage = data["stage"]
        piece.history = data.get("history", {data["stage"]: data["created"]})
        return piece


print("\n--- Step 2: insert a piece")
# history is a dictionary, so it is saved as JSON text.


def connect(path):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute(SCHEMA)
    return conn


def insert_piece(conn, piece):
    cursor = conn.execute(
        """INSERT INTO pieces
           (name, clay, technique, glaze, temperature, notes, created, stage, history)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            piece.name,
            piece.clay,
            piece.technique,
            piece.glaze,
            piece.temperature,
            piece.notes,
            piece.created,
            piece.stage,
            json.dumps(piece.history),
        ),
    )
    conn.commit()
    piece.id = cursor.lastrowid
    return piece.id


conn = connect(":memory:")  # the real app uses connect("atanor.db")
print(insert_piece(conn, Piece("Blue bowl", "stoneware", "wheel", created="2026-11-01")))
print(insert_piece(conn, Piece("Small vase", "porcelain", "hand-built")))

print("\n--- Step 3: read pieces back")


def row_to_piece(row):
    piece = Piece(
        row["name"],
        row["clay"],
        row["technique"],
        row["glaze"],
        row["temperature"],
        row["notes"],
        row["created"],
    )
    piece.id = row["id"]
    piece.stage = row["stage"]
    piece.history = json.loads(row["history"])
    return piece


def all_pieces(conn):
    return [row_to_piece(row) for row in conn.execute("SELECT * FROM pieces ORDER BY id")]


for piece in all_pieces(conn):
    print(piece.id, piece, piece.history)

print("\n--- Step 4: find one piece and update it")


def get_piece(conn, piece_id):
    row = conn.execute("SELECT * FROM pieces WHERE id = ?", (piece_id,)).fetchone()
    return row_to_piece(row) if row else None


def find_by_name(conn, name):
    row = conn.execute("SELECT * FROM pieces WHERE lower(name) = lower(?)", (name,)).fetchone()
    return row_to_piece(row) if row else None


def update_stage(conn, piece):
    conn.execute(
        "UPDATE pieces SET stage = ?, history = ? WHERE id = ?",
        (piece.stage, json.dumps(piece.history), piece.id),
    )
    conn.commit()


piece = find_by_name(conn, "BLUE BOWL")
piece.advance("2026-11-02")
update_stage(conn, piece)

print(get_piece(conn, 1).stage, get_piece(conn, 1).history)
print(get_piece(conn, 99))

print("\n--- Step 5: the new storage.py")
# All the functions above (SCHEMA, connect, row_to_piece, insert_piece, all_pieces,
# get_piece, find_by_name, update_stage) go into atanor/storage.py, with:
#     def connect(path="atanor.db"):
# and at the top:
#     from atanor.piece import Piece

print("\n--- Step 6: migrate the old data (migrate.py)")
# Create a small pieces.json like the one from milestone 5, then move it into the database.
old = [
    Piece("Blue bowl", "stoneware", "wheel", "celadon", 1240, "", "2026-11-01").to_dict(),
    Piece("Small vase", "porcelain", "hand-built", "", 0, "", "2026-11-03").to_dict(),
    Piece("Mug", "stoneware", "wheel", "", 0, "", "2026-11-05").to_dict(),
]
with open("pieces.json", "w", encoding="utf-8") as f:
    json.dump(old, f, ensure_ascii=False, indent=2)

if not os.path.exists("pieces.json"):
    print("Nothing to migrate.")
else:
    new_conn = connect(":memory:")  # the real script uses connect() -> atanor.db
    with open("pieces.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    for item in data:
        insert_piece(new_conn, Piece.from_dict(item))
    print(f"Migrated {len(data)} pieces into atanor.db.")
    new_conn.close()

os.remove("pieces.json")

print("\n--- Step 7: tests with a database in memory (tests/test_storage.py, pytest)")
# import pytest
#
# from atanor.piece import Piece
# from atanor.storage import connect, find_by_name, get_piece, insert_piece, update_stage
#
#
# @pytest.fixture
# def conn():
#     return connect(":memory:")
#
#
# def test_insert_and_get(conn):
#     piece_id = insert_piece(conn, Piece("Bowl", "stoneware", "wheel", created="2026-11-01"))
#     assert get_piece(conn, piece_id).name == "Bowl"
#
#
# def test_update_stage_keeps_history(conn):
#     piece = Piece("Bowl", "stoneware", "wheel", created="2026-11-01")
#     insert_piece(conn, piece)
#     piece.advance("2026-11-02")
#     update_stage(conn, piece)
#     saved = find_by_name(conn, "bowl")
#     assert saved.stage == "drying"
#     assert saved.history == {"modeled": "2026-11-01", "drying": "2026-11-02"}
#
#
# def test_missing_piece_is_none(conn):
#     assert get_piece(conn, 42) is None
#
# Commit:
# git add .
# git commit -m "Store pieces in SQLite and migrate from JSON"
# git push

print("\n--- Stretch 1: count by stage in SQL")
counting = sqlite3.connect(":memory:")
counting.execute("CREATE TABLE pieces (name TEXT, stage TEXT)")
counting.executemany(
    "INSERT INTO pieces VALUES (?, ?)",
    [("Bowl", "drying"), ("Vase", "modeled"), ("Mug", "drying")],
)

for stage, total in counting.execute(
    "SELECT stage, COUNT(*) FROM pieces GROUP BY stage ORDER BY stage"
):
    print(stage, total)
counting.close()

print("\n--- Stretch 2: search by part of the name")
search = sqlite3.connect(":memory:")
search.execute("CREATE TABLE pieces (name TEXT)")
search.executemany("INSERT INTO pieces VALUES (?)", [("Blue bowl",), ("Rice Bowl",), ("Vase",)])

word = "bowl"
rows = search.execute("SELECT name FROM pieces WHERE lower(name) LIKE ?", (f"%{word.lower()}%",))
print([name for (name,) in rows])
search.close()


print("\n" + "=" * 50)
print("MILESTONE 7: a web API")

print("\n--- How it all connects")
# You click "Add" -> JavaScript (fetch) -> HTTP POST /pieces -> Flask -> storage.py -> atanor.db
# The page updates <- JavaScript reads the JSON <- HTTP response <- Flask <-

print("\n--- Step 1: install Flask (terminal)")
# uv add flask

print("\n--- Step 2: validate what arrives (atanor/validation.py)")


def validate_new_piece(data):
    errors = []
    for field in ["name", "clay", "technique"]:
        if not str(data.get(field, "")).strip():
            errors.append(f"{field} is required")
    temperature = data.get("temperature", 0)
    if not isinstance(temperature, int) or not 0 <= temperature <= 1400:
        errors.append("temperature must be a whole number between 0 and 1400")
    return errors


print(
    validate_new_piece(
        {"name": "Bowl", "clay": "stoneware", "technique": "wheel", "temperature": 1240}
    )
)
print(validate_new_piece({"name": " ", "clay": "stoneware", "temperature": 5000}))

print("\n--- Step 3: the first route (app.py, needs Flask)")
# from flask import Flask, jsonify
#
# from atanor.storage import all_pieces, connect
#
# app = Flask(__name__)
#
#
# @app.get("/pieces")
# def list_pieces():
#     conn = connect()
#     return jsonify([piece.to_dict() for piece in all_pieces(conn)])
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
#
# Run:  uv run app.py   then open http://127.0.0.1:5000/pieces

print("\n--- Step 4: the other routes (app.py, needs Flask)")
# from datetime import date
#
# from flask import Flask, jsonify, request
#
# from atanor.piece import Piece, StageError
# from atanor.storage import all_pieces, connect, get_piece, insert_piece, update_stage
# from atanor.validation import validate_new_piece
#
# app = Flask(__name__, static_folder="static", static_url_path="")
#
#
# @app.get("/")
# def home():
#     return app.send_static_file("index.html")
#
#
# @app.get("/pieces")
# def list_pieces():
#     return jsonify([piece.to_dict() for piece in all_pieces(connect())])
#
#
# @app.post("/pieces")
# def create_piece():
#     data = request.get_json(silent=True) or {}
#     errors = validate_new_piece(data)
#     if errors:
#         return jsonify(errors=errors), 400
#     piece = Piece(
#         data["name"].strip(), data["clay"].strip(), data["technique"].strip(),
#         data.get("glaze", ""), data.get("temperature", 0), data.get("notes", ""),
#         date.today().isoformat(),
#     )
#     insert_piece(connect(), piece)
#     return jsonify(piece.to_dict()), 201
#
#
# @app.get("/pieces/<int:piece_id>")
# def show_piece(piece_id):
#     piece = get_piece(connect(), piece_id)
#     if piece is None:
#         return jsonify(error="piece not found"), 404
#     return jsonify(piece.to_dict())
#
#
# @app.post("/pieces/<int:piece_id>/advance")
# def advance_piece(piece_id):
#     conn = connect()
#     piece = get_piece(conn, piece_id)
#     if piece is None:
#         return jsonify(error="piece not found"), 404
#     try:
#         piece.advance(date.today().isoformat())
#     except StageError as error:
#         return jsonify(error=str(error)), 400
#     update_stage(conn, piece)
#     return jsonify(piece.to_dict())
#
#
# if __name__ == "__main__":
#     app.run(debug=True)

print("\n--- Step 4, the same logic without Flask")
# What POST /pieces/1/advance does, step by step, with the database from milestone 6:
piece = get_piece(conn, 1)
if piece is None:
    print(404, {"error": "piece not found"})
else:
    try:
        piece.advance("2026-11-10")
        update_stage(conn, piece)
        print(200, piece.to_dict())
    except StageError as error:
        print(400, {"error": str(error)})

print("\n--- Step 5: try the API from the terminal (try_api.py, server must be running)")
# import json
# from urllib.request import Request, urlopen
#
# BASE = "http://127.0.0.1:5000"
#
# body = json.dumps({"name": "Rice bowl", "clay": "stoneware", "technique": "wheel"}).encode()
# request = Request(f"{BASE}/pieces", data=body,
#                   headers={"Content-Type": "application/json"}, method="POST")
# with urlopen(request) as response:
#     print(response.status, json.load(response))
#
# with urlopen(f"{BASE}/pieces") as response:
#     for piece in json.load(response):
#         print(piece["id"], piece["name"], piece["stage"])
#
# Run:  uv run try_api.py

print("\n--- Step 6: the page (static/index.html, style.css, app.js)")
# Show the three files from the milestone on screen. The key JavaScript parts:
#   const response = await fetch("/pieces");
#   const pieces = await response.json();
# and to create a piece:
#   await fetch("/pieces", {
#     method: "POST",
#     headers: { "Content-Type": "application/json" },
#     body: JSON.stringify(data),
#   });
# and to advance:
#   await fetch(`/pieces/${id}/advance`, { method: "POST" });

print("\n--- Step 7: test the API without a browser (tests/test_api.py, pytest)")
# import pytest
#
# import app as atanor_app
#
#
# @pytest.fixture
# def client(tmp_path, monkeypatch):
#     db = tmp_path / "test.db"
#     real_connect = atanor_app.connect
#     monkeypatch.setattr(atanor_app, "connect", lambda: real_connect(db))
#     return atanor_app.app.test_client()
#
#
# def test_create_and_list(client):
#     response = client.post(
#         "/pieces", json={"name": "Bowl", "clay": "stoneware", "technique": "wheel"}
#     )
#     assert response.status_code == 201
#     names = [piece["name"] for piece in client.get("/pieces").get_json()]
#     assert names == ["Bowl"]
#
#
# def test_invalid_piece(client):
#     response = client.post("/pieces", json={"name": ""})
#     assert response.status_code == 400
#
#
# def test_missing_piece(client):
#     assert client.get("/pieces/999").status_code == 404
#
# Commit:
# git add .
# git commit -m "Add Flask API and web page"
# git push

print("\n--- Stretch 1: show the pieces grouped by stage")
pieces = [
    {"name": "Bowl", "stage": "drying"},
    {"name": "Vase", "stage": "modeled"},
    {"name": "Mug", "stage": "drying"},
]

groups = {stage: [] for stage in STAGES}
for piece in pieces:
    groups[piece["stage"]].append(piece["name"])

for stage, names in groups.items():
    if names:
        print(f"{stage}: {', '.join(names)}")

print("\n--- Stretch 2: escape the names (JavaScript)")
# Use textContent instead of innerHTML, so a name like <b>Bowl</b> shows as text:
# const name = document.createElement("span");
# name.textContent = `${piece.name} `;
# const stage = document.createElement("span");
# stage.className = "stage";
# stage.textContent = `(${piece.stage})`;
# name.appendChild(stage);
# item.appendChild(name);

conn.close()


print("\n" + "=" * 50)
print("MILESTONE 8: suggestions")

print("\n--- Step 1: the waiting times")
READY_AFTER_DAYS = {
    "modeled": 1,  # leather-hard, ready to trim and start drying
    "drying": 7,  # bone dry, ready for the bisque firing
    "bisque_fired": 2,  # cooled down, ready to glaze
    "glazed": 1,  # glaze dry, ready for the final firing
}
print(READY_AFTER_DAYS)

print("\n--- Step 2: one suggestion for one piece")
NEXT_ACTION = {
    "modeled": "trim it and start drying",
    "drying": "the bisque firing",
    "bisque_fired": "glazing",
    "glazed": "the glaze firing",
}


def days_in_stage(piece, today):
    started = date.fromisoformat(piece["history"][piece["stage"]])
    return (date.fromisoformat(today) - started).days


def suggest(piece, today):
    stage = piece["stage"]
    if stage not in READY_AFTER_DAYS:
        return None
    days = days_in_stage(piece, today)
    if days < READY_AFTER_DAYS[stage]:
        return None
    return (
        f"{piece['name']} has been {stage} for {days} days. It is ready for {NEXT_ACTION[stage]}."
    )


bowl = {
    "name": "Blue bowl",
    "stage": "drying",
    "history": {"modeled": "2026-11-01", "drying": "2026-11-02"},
}
print(suggest(bowl, "2026-11-10"))
print(suggest(bowl, "2026-11-05"))

print("\n--- Step 3: suggestions for all pieces")


def suggest_all(pieces, today):
    waiting = sorted(pieces, key=lambda piece: days_in_stage(piece, today), reverse=True)
    suggestions = [suggest(piece, today) for piece in waiting]
    return [text for text in suggestions if text is not None]


pieces = [
    {"name": "Blue bowl", "stage": "drying", "history": {"drying": "2026-11-02"}},
    {"name": "Mug", "stage": "glazed", "history": {"glazed": "2026-10-30"}},
    {"name": "Vase", "stage": "drying", "history": {"drying": "2026-11-08"}},
    {"name": "Plate", "stage": "glaze_fired", "history": {"glaze_fired": "2026-10-01"}},
]
for text in suggest_all(pieces, "2026-11-10"):
    print("-", text)

print("\n--- Step 4: test the rules (tests/test_suggestions.py, pytest)")
# from atanor.suggestions import suggest, suggest_all
#
#
# def piece(stage, since):
#     return {"name": "Bowl", "stage": stage, "history": {stage: since}}
#
#
# def test_drying_long_enough():
#     assert "bisque firing" in suggest(piece("drying", "2026-11-01"), "2026-11-08")
#
#
# def test_drying_too_soon():
#     assert suggest(piece("drying", "2026-11-05"), "2026-11-08") is None
#
#
# def test_finished_piece_has_no_suggestion():
#     assert suggest(piece("glaze_fired", "2026-01-01"), "2026-11-08") is None
#
#
# def test_suggest_all_skips_pieces_not_ready():
#     pieces = [piece("drying", "2026-11-07"), piece("glazed", "2026-11-01")]
#     assert len(suggest_all(pieces, "2026-11-08")) == 1

print("\n--- Step 5: get an API key and keep it secret (terminal)")
# uv add anthropic
# $env:ANTHROPIC_API_KEY = "sk-ant-..."      (or a .env file, never in the code)

print("\n--- Step 6: summarize your studio for the AI")


def studio_summary(pieces):
    lines = []
    for piece in pieces:
        glaze = piece["glaze"] or "no glaze yet"
        lines.append(
            f"- {piece['name']}: {piece['clay']}, {piece['technique']}, {glaze}, "
            f"stage {piece['stage']}"
        )
    return "\n".join(lines)


studio = [
    {
        "name": "Blue bowl",
        "clay": "stoneware",
        "technique": "wheel",
        "glaze": "celadon",
        "stage": "glaze_fired",
    },
    {
        "name": "Small vase",
        "clay": "porcelain",
        "technique": "hand-built",
        "glaze": "",
        "stage": "drying",
    },
]
print(studio_summary(studio))

print("\n--- Step 7: ask the model (atanor/suggestions.py, needs anthropic and a key)")
# import anthropic
#
# SYSTEM_PROMPT = (
#     "You are an experienced ceramics teacher helping a hobby potter. "
#     "Based on their pieces, suggest 3 short, concrete ideas for what to try next: "
#     "new glaze and clay combinations, techniques they have not used, or improvements. "
#     "Each idea in one sentence. Do not repeat information they already know."
# )
#
#
# def ai_suggestions(pieces):
#     client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment
#     message = client.messages.create(
#         model="claude-haiku-5-5",
#         max_tokens=400,
#         system=SYSTEM_PROMPT,
#         messages=[{"role": "user", "content": f"My pieces:\n{studio_summary(pieces)}"}],
#     )
#     return message.content[0].text
print("This is the text the model receives:")
print(f"My pieces:\n{studio_summary(studio)}")

print("\n--- Step 8: handle failures")
# def safe_ai_suggestions(pieces):
#     if not pieces:
#         return "Add some pieces first, then I can suggest ideas."
#     try:
#         return ai_suggestions(pieces)
#     except anthropic.APIError as error:
#         return f"AI suggestions are unavailable right now ({error.__class__.__name__})."

print("\n--- Step 9: the route and the page (needs Flask)")
# @app.get("/suggestions")
# def suggestions():
#     pieces = [piece.to_dict() for piece in all_pieces(connect())]
#     result = {"rules": suggest_all(pieces, date.today().isoformat())}
#     if request.args.get("ai") == "1":
#         result["ai"] = safe_ai_suggestions(pieces)
#     return jsonify(result)
#
# On the page: a <ul id="rules">, a button "Ask for creative ideas" and a <p id="ai">,
# filled with fetch("/suggestions") or fetch("/suggestions?ai=1").
print("What GET /suggestions returns (rules only, on 2026-11-10):")
print({"rules": suggest_all(pieces, "2026-11-10")})
# Commit:
# git add .
# git commit -m "Suggest next steps with rules and with Claude"
# git push

print("\n--- Stretch 1: friendly stage names")
FRIENDLY = {
    "modeled": "freshly modeled",
    "drying": "drying",
    "bisque_fired": "out of the bisque firing",
    "glazed": "glazed",
}

print(f"Small vase has been {FRIENDLY['bisque_fired']} for 3 days.")

print("\n--- Stretch 2: let the AI know the rules")
today = "2026-11-10"
studio = [
    {
        "name": "Blue bowl",
        "clay": "stoneware",
        "technique": "wheel",
        "glaze": "",
        "stage": "drying",
        "history": {"drying": "2026-11-02"},
    },
]
content = (
    f"My pieces:\n{studio_summary(studio)}\n\n"
    "Already planned:\n"
    + "\n".join(f"- {text}" for text in suggest_all(studio, today))
    + "\n\nSuggest ideas beyond what is already planned."
)
print(content)

print("\n--- Stretch 3: a desktop window (desktop.py, needs pywebview)")
# uv add pywebview
#
# import threading
#
# import webview
#
# from app import app
#
#
# def run_server():
#     app.run(port=5000)
#
#
# threading.Thread(target=run_server, daemon=True).start()
# webview.create_window("Atanor", "http://127.0.0.1:5000", width=900, height=700)
# webview.start()
#
# Run:  uv run desktop.py
