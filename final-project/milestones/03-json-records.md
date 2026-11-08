# Milestone 3: JSON records

## Goal

Replace the text lines with **dictionaries**. Each piece gets all its fields and a `stage`, the whole list is saved in `pieces.json`, and the program gets a menu to list, search and move a piece to its next stage.

## Requires

Module 6: dictionaries, lists of dictionaries, JSON, and the `in` operator.

## What you will build

A piece now looks like this:

```python
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
```

The text line `Blue bowl;stoneware` could only hold what we decided to split by `;`. A dictionary has a **name for each value**, so we can add fields without breaking anything.

## Steps

### Step 1: The stages

At the top of `atanor.py`, create a list with the five stages, in order:

```python
STAGES = ["modeled", "drying", "bisque_fired", "glazed", "glaze_fired"]
```

The name is in UPPERCASE because it is a **constant**: a value the program reads but never changes. This is a convention, Python does not enforce it.

Then print the position of `"drying"` and the stage that comes after it.

<details>
<summary>Hint</summary>

`STAGES.index("drying")` tells you the position. The next stage is at position + 1.

</details>

<details>
<summary>Show answer</summary>

```python
STAGES = ["modeled", "drying", "bisque_fired", "glazed", "glaze_fired"]

position = STAGES.index("drying")
print(position)
print(STAGES[position + 1])
```

Output:

```text
1
bisque_fired
```

</details>

### Step 2: Create a piece

Write `make_piece(name, clay, technique, glaze, temperature, notes, created)` that returns a dictionary with all those fields and `"stage": "modeled"`. Every new piece starts as `modeled`.

<details>
<summary>Show answer</summary>

```python
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
```

Output:

```text
Blue bowl - modeled
```

To get today's date as text in the real program, use:

<!-- no-verify -->
```python
from datetime import date

created = date.today().isoformat()
```

</details>

### Step 3: Describe a piece

Write `describe(piece)` that returns one line like `Blue bowl (stoneware, wheel) - modeled`.

<details>
<summary>Show answer</summary>

```python
def describe(piece):
    return f"{piece['name']} ({piece['clay']}, {piece['technique']}) - {piece['stage']}"


bowl = {"name": "Blue bowl", "clay": "stoneware", "technique": "wheel", "stage": "modeled"}
print(describe(bowl))
```

Output:

```text
Blue bowl (stoneware, wheel) - modeled
```

Notice the quotes: the f-string uses double quotes, so inside the braces we use single quotes, `piece['name']`. Using the same kind of quote in both places confuses older versions of Python.

</details>

### Step 4: Save and load the list

Write `save_pieces(pieces)` and `load_pieces()` using `json`. If `pieces.json` does not exist yet, `load_pieces()` must return an empty list instead of crashing.

<details>
<summary>Hint</summary>

`json.dump(data, file)` writes, `json.load(file)` reads. To check if a file exists, use `from pathlib import Path` and `Path("pieces.json").exists()`.

</details>

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
import json
from pathlib import Path

FILE = Path("pieces.json")


def save_pieces(pieces):
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(pieces, file, ensure_ascii=False, indent=2)


def load_pieces():
    if not FILE.exists():
        return []
    with open(FILE, "r", encoding="utf-8") as file:
        return json.load(file)
```

- Here we use `"w"` on purpose: we always write the **whole list**, so the old content must be replaced.
- `ensure_ascii=False` keeps accents readable in the file.
- `indent=2` makes the file pretty, so you can open it in Cursor and read it.

</details>

### Step 5: Search by name

Write `find_piece(pieces, name)` that returns the first piece whose name matches, **ignoring uppercase and lowercase**. If none matches, return `None`.

<details>
<summary>Show answer</summary>

```python
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
```

Output:

```text
{'name': 'Small vase', 'stage': 'modeled'}
None
```

The `return` inside the `for` ends the function as soon as it finds the piece. The `return None` only runs if the loop finished without finding anything.

</details>

### Step 6: Move to the next stage

Write `advance(piece)` that changes the piece's `stage` to the next one in `STAGES`. If the piece is already `glaze_fired`, do not change it and return `False`. Otherwise return `True`.

<details>
<summary>Show answer</summary>

```python
STAGES = ["modeled", "drying", "bisque_fired", "glazed", "glaze_fired"]


def advance(piece):
    position = STAGES.index(piece["stage"])
    if position == len(STAGES) - 1:
        return False
    piece["stage"] = STAGES[position + 1]
    return True


bowl = {"name": "Blue bowl", "stage": "glazed"}
print(advance(bowl), bowl["stage"])
print(advance(bowl), bowl["stage"])
```

Output:

```text
True glaze_fired
False glaze_fired
```

`len(STAGES) - 1` is the position of the last stage. Because positions start at 0, a list with 5 items ends at position 4.

</details>

### Step 7: The menu

Write `main()` with a menu that repeats until the user types `0`:

```text
1. Add a piece
2. List pieces
3. Advance a piece
0. Exit
```

After adding or advancing, save the list.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
from datetime import date


def add_piece(pieces):
    name = input("Name: ")
    clay = input("Clay: ")
    technique = input("Technique: ")
    glaze = input("Glaze: ")
    temperature = int(input("Firing temperature (°C): "))
    notes = input("Notes: ")
    piece = make_piece(name, clay, technique, glaze, temperature, notes, date.today().isoformat())
    pieces.append(piece)
    save_pieces(pieces)
    print("Saved!")


def list_pieces(pieces):
    if not pieces:
        print("No pieces yet.")
    for number, piece in enumerate(pieces, start=1):
        print(f"{number}. {describe(piece)}")


def advance_piece(pieces):
    name = input("Which piece? ")
    piece = find_piece(pieces, name)
    if piece is None:
        print("Piece not found.")
    elif advance(piece):
        save_pieces(pieces)
        print(f"{piece['name']} is now {piece['stage']}.")
    else:
        print(f"{piece['name']} is already finished.")


def main():
    pieces = load_pieces()
    while True:
        print()
        print("1. Add a piece")
        print("2. List pieces")
        print("3. Advance a piece")
        print("0. Exit")
        choice = input("> ")
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


main()
```

`main()` loads the list **once**, and every function receives the same list. When `add_piece` does `pieces.append(...)`, the list in `main()` changes too, because it is the same list.

</details>

## Checkpoint

```console
PS C:\Users\you\Projects\atanor> python atanor.py

1. Add a piece
2. List pieces
3. Advance a piece
0. Exit
> 1
Name: Blue bowl
Clay: stoneware
Technique: wheel
Glaze: celadon
Firing temperature (°C): 1240
Notes: thin walls
Saved!

1. Add a piece
2. List pieces
3. Advance a piece
0. Exit
> 3
Which piece? blue bowl
Blue bowl is now drying.

1. Add a piece
2. List pieces
3. Advance a piece
0. Exit
> 0
```

Open `pieces.json` in Cursor: the piece is there, with `"stage": "drying"`. Close and run again: option 2 still shows it.

## Commit

```powershell
git add atanor.py
git commit -m "Store pieces as JSON records with a lifecycle stage"
git push
```

`pieces.json` is already in `.gitignore`, so it stays out of the repository.

## Stretch goals

#### Stretch 1: Filter by stage

Write `by_stage(pieces, stage)` that returns only the pieces in that stage. Use a list comprehension.

<details>
<summary>Show answer</summary>

```python
def by_stage(pieces, stage):
    return [piece for piece in pieces if piece["stage"] == stage]


pieces = [
    {"name": "Blue bowl", "stage": "drying"},
    {"name": "Small vase", "stage": "modeled"},
    {"name": "Mug", "stage": "drying"},
]
for piece in by_stage(pieces, "drying"):
    print(piece["name"])
```

Output:

```text
Blue bowl
Mug
```

</details>

#### Stretch 2: Count per stage

Print how many pieces are in each stage, in the order of `STAGES`.

<details>
<summary>Show answer</summary>

```python
STAGES = ["modeled", "drying", "bisque_fired", "glazed", "glaze_fired"]
pieces = [{"stage": "drying"}, {"stage": "modeled"}, {"stage": "drying"}]

counts = {stage: 0 for stage in STAGES}
for piece in pieces:
    counts[piece["stage"]] += 1

for stage, total in counts.items():
    print(f"{stage}: {total}")
```

Output:

```text
modeled: 1
drying: 2
bisque_fired: 0
glazed: 0
glaze_fired: 0
```

Starting every stage at 0 makes sure empty stages also appear.

</details>

#### Stretch 3: Import the old text file

Read your old `pieces.txt` and turn each line into a dictionary with `make_piece`, filling the missing fields with empty text.

<details>
<summary>Show answer</summary>

```python
def make_piece(name, clay, technique, glaze, temperature, notes, created):
    return {"name": name, "clay": clay, "technique": technique, "glaze": glaze,
            "temperature": temperature, "notes": notes, "created": created, "stage": "modeled"}


lines = ["Blue bowl;stoneware", "Small vase;porcelain"]
pieces = []
for line in lines:
    name, clay = line.split(";")
    pieces.append(make_piece(name, clay, "", "", 0, "", "2026-11-08"))

print(len(pieces), pieces[1]["name"], pieces[1]["clay"])
```

Output:

```text
2 Small vase porcelain
```

In the real program, `lines` comes from reading `pieces.txt` as in milestone 1, and at the end you call `save_pieces(pieces)`.

</details>

**Next:** [Milestone 4: Modules and tests](04-modules-and-tests.md)
