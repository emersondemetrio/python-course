# Milestone 4: Modules and tests

## Goal

Split `atanor.py` into a **package** with one file per responsibility, replace the `True`/`False` of `advance` with a real error (an exception), and write automated tests that check the rules for you.

## Requires

Module 7: modules and packages, exceptions, uv and ruff, `pytest`.

## What you will build

```text
atanor/
├── main.py              # only the menu: asks, shows, calls
├── pyproject.toml       # created by uv: project info and libraries
├── uv.lock              # created by uv: exact library versions
├── atanor/
│   ├── __init__.py      # empty: it marks the folder as a package
│   ├── pieces.py        # the rules: STAGES, make_piece, find_piece, advance...
│   └── storage.py       # saving and loading pieces.json
└── tests/
    └── test_pieces.py
```

Yes, there is a folder `atanor` inside the folder `atanor`. The outer one is the **project**, the inner one is the **package** (the code you import).

Why split? `pieces.py` has rules that never touch the keyboard or the disk. That makes them easy to test. `main.py` talks to the person. `storage.py` talks to the disk. Each file has one job.

## Steps

### Step 1: Turn the folder into a uv project

Your `atanor` folder already has code and a Git history. Turn it into a uv project **without** creating extra files, then add `pytest` and `ruff` as developer tools.

<details>
<summary>Hint</summary>

`uv init --bare` creates only `pyproject.toml`, so it does not touch your existing files. Developer tools are added with `--dev`.

</details>

<details>
<summary>Show answer</summary>

```powershell
cd ~\Projects\atanor
uv init --bare
uv add --dev pytest ruff
```

Now the folder has `pyproject.toml` (the project and its libraries) and `uv.lock` (the exact versions). Both go into Git. `.venv/` is already in your `.gitignore`; someone who clones the project rebuilds it with `uv sync`.

Check that everything is tidy:

```powershell
uv run ruff check
uv run ruff format
```

</details>

### Step 2: An exception of our own

In `atanor/pieces.py`, create an exception called `StageError`. Then change `advance(piece)` so it **raises** `StageError` when the piece is already finished, instead of returning `False`.

Why? `False` is easy to ignore by accident. An exception cannot be ignored: if nobody handles it, the program stops and tells you exactly what happened.

<details>
<summary>Show answer</summary>

```python
STAGES = ["modeled", "drying", "bisque_fired", "glazed", "glaze_fired"]


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
```

Output:

```text
glaze_fired
Error: Blue bowl is already finished.
```

`class StageError(Exception): pass` creates a new kind of error that behaves exactly like any Python error, but has our own name. You will understand classes properly in module 8. For now, this line is a recipe.

</details>

### Step 3: Move the rules into `pieces.py`

Move `STAGES`, `StageError`, `make_piece`, `describe`, `find_piece` and `advance` into `atanor/pieces.py`. None of them use `input`, `print` or files.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# atanor/pieces.py
STAGES = ["modeled", "drying", "bisque_fired", "glazed", "glaze_fired"]


class StageError(Exception):
    pass


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


def describe(piece):
    return f"{piece['name']} ({piece['clay']}, {piece['technique']}) - {piece['stage']}"


def find_piece(pieces, name):
    for piece in pieces:
        if piece["name"].lower() == name.lower():
            return piece
    return None


def advance(piece):
    position = STAGES.index(piece["stage"])
    if position == len(STAGES) - 1:
        raise StageError(f"{piece['name']} is already finished.")
    piece["stage"] = STAGES[position + 1]
```

Also create an **empty** file `atanor/__init__.py`.

</details>

### Step 4: Move saving and loading into `storage.py`

Move `save_pieces` and `load_pieces` into `atanor/storage.py`. Make `load_pieces` also survive a broken JSON file: if the file exists but cannot be read, raise a clear error.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# atanor/storage.py
import json
from pathlib import Path

FILE = Path("pieces.json")


def save_pieces(pieces, file=FILE):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(pieces, f, ensure_ascii=False, indent=2)


def load_pieces(file=FILE):
    if not Path(file).exists():
        return []
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError(f"{file} is damaged. Fix it or delete it to start over.")
```

The `file=FILE` parameter has a **default value**: the program calls `load_pieces()` as before, but the tests can pass another file.

</details>

### Step 5: The menu in `main.py`

Move the menu into `main.py` at the project root. It imports what it needs from the package. `advance_piece` now uses `try`/`except`.

Use `if __name__ == "__main__":` before calling `main()`.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# main.py
from datetime import date

from atanor.pieces import StageError, advance, describe, find_piece, make_piece
from atanor.storage import load_pieces, save_pieces


def add_piece(pieces):
    name = input("Name: ")
    clay = input("Clay: ")
    technique = input("Technique: ")
    glaze = input("Glaze: ")
    try:
        temperature = int(input("Firing temperature (°C): "))
    except ValueError:
        print("Temperature must be a number. Piece not saved.")
        return
    notes = input("Notes: ")
    pieces.append(make_piece(name, clay, technique, glaze, temperature, notes, date.today().isoformat()))
    save_pieces(pieces)
    print("Saved!")


def list_pieces(pieces):
    if not pieces:
        print("No pieces yet.")
    for number, piece in enumerate(pieces, start=1):
        print(f"{number}. {describe(piece)}")


def advance_piece(pieces):
    piece = find_piece(pieces, input("Which piece? "))
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
        choice = input("> ")
        if choice == "0":
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid option.")
        else:
            action(pieces)


if __name__ == "__main__":
    main()
```

The `actions` dictionary maps each option to a **function** (without parentheses: we store the function, we do not call it). This replaces the long `if`/`elif` chain.

Run it with `python main.py` from the project folder. Delete the old `atanor.py` when everything works.

</details>

### Step 6: The first tests

Create `tests/test_pieces.py` with tests for:

1. A new piece starts as `modeled`.
2. `advance` moves `drying` to `bisque_fired`.
3. `advance` on a finished piece raises `StageError`.
4. `find_piece` ignores uppercase and lowercase.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# tests/test_pieces.py
import pytest

from atanor.pieces import StageError, advance, find_piece, make_piece


def test_new_piece_starts_modeled():
    piece = make_piece("Bowl", "stoneware", "wheel", "", 1240, "", "2026-11-08")
    assert piece["stage"] == "modeled"


def test_advance_moves_to_next_stage():
    piece = {"name": "Bowl", "stage": "drying"}
    advance(piece)
    assert piece["stage"] == "bisque_fired"


def test_cannot_advance_finished_piece():
    piece = {"name": "Bowl", "stage": "glaze_fired"}
    with pytest.raises(StageError):
        advance(piece)


def test_find_piece_ignores_case():
    pieces = [{"name": "Blue Bowl"}]
    assert find_piece(pieces, "blue bowl") is pieces[0]
```

Run from the project folder:

```powershell
uv run pytest
```

```console
tests/test_pieces.py ....                                   [100%]
4 passed in 0.02s
```

Each dot is a test that passed. `uv run pytest` (instead of just `pytest`) makes sure Python finds the `atanor` package from the project folder.

</details>

### Step 7: Test the storage with a temporary file

Write a test that saves a list and loads it back, using `tmp_path`, a temporary folder that pytest creates and deletes for you. Your real `pieces.json` is never touched.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# tests/test_storage.py
from atanor.storage import load_pieces, save_pieces


def test_save_and_load(tmp_path):
    file = tmp_path / "pieces.json"
    pieces = [{"name": "Cerâmica azul", "stage": "drying"}]
    save_pieces(pieces, file)
    assert load_pieces(file) == pieces


def test_missing_file_gives_empty_list(tmp_path):
    assert load_pieces(tmp_path / "nothing.json") == []
```

</details>

## Checkpoint

```console
PS C:\Users\you\Projects\atanor> uv run pytest
tests/test_pieces.py ....                                   [100%]
tests/test_storage.py ..                                    [100%]
6 passed in 0.03s
PS C:\Users\you\Projects\atanor> uv run main.py

1. Add a piece
2. List pieces
3. Advance a piece
0. Exit
> 2
1. Blue bowl (stoneware, wheel) - drying
```

Break something on purpose (for example, change `position + 1` to `position + 2` in `advance`) and run the tests again. One of them fails. Undo the change. That is the whole point of tests: they warn you before the person using the app does.

## Commit

```powershell
git add .
git status
git commit -m "Split into a package, add StageError and tests"
git push
```

Read the `git status` output before committing: `.venv/` and `pieces.json` must **not** be in the list.

## Stretch goals

#### Stretch 1: Advancing an unknown stage

What happens if a piece has `"stage": "broken"` and you call `advance`? Write a test that shows it, then make `advance` raise `StageError` with a clear message in that case.

<details>
<summary>Show answer</summary>

```python
STAGES = ["modeled", "drying", "bisque_fired", "glazed", "glaze_fired"]


class StageError(Exception):
    pass


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
```

Output:

```text
Unknown stage: broken
```

Without the check, `STAGES.index("broken")` raises a `ValueError` with a message that only a programmer would understand.

</details>

#### Stretch 2: One test, many cases

Use `@pytest.mark.parametrize` to test every pair of stage and next stage in a single test function.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
import pytest

from atanor.pieces import advance


@pytest.mark.parametrize("current, expected", [
    ("modeled", "drying"),
    ("drying", "bisque_fired"),
    ("bisque_fired", "glazed"),
    ("glazed", "glaze_fired"),
])
def test_every_step(current, expected):
    piece = {"name": "Bowl", "stage": current}
    advance(piece)
    assert piece["stage"] == expected
```

pytest runs this function four times, once per pair, and reports each one separately.

</details>

**Next:** [Milestone 5: The Piece class](05-piece-class.md)
