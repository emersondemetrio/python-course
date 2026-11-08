# Milestone 5: The Piece class

## Goal

Turn the piece dictionary into a `Piece` **class**. A piece now remembers **when** it entered each stage, and it protects its own rules: nobody can skip a stage by accident.

## Requires

Module 8: classes, `__init__`, `self`, methods, `__str__`.

## What you will build

<!-- no-verify -->
```python
bowl = Piece("Blue bowl", "stoneware", "wheel", created="2026-11-01")
bowl.advance("2026-11-02")
print(bowl)
print(bowl.history)
```

```text
Blue bowl (stoneware, wheel) - drying
{'modeled': '2026-11-01', 'drying': '2026-11-02'}
```

With a dictionary, any part of the code could write `piece["stage"] = "glaze_fired"` and jump over three stages. With a class, the way to change the stage is the `advance` method, and the rules live inside it.

The `history` is what makes the suggestions of milestone 8 possible: to say "drying for 8 days", we need to know the day drying started.

## Steps

### Step 1: The class and its attributes

In `atanor/piece.py`, create the class `Piece`. Its `__init__` receives `name`, `clay`, `technique`, and optionally `glaze=""`, `temperature=0`, `notes=""` and `created` (a date as text). It sets `stage` to `"modeled"` and starts `history` as `{"modeled": created}`.

<details>
<summary>Show answer</summary>

```python
class Piece:
    def __init__(self, name, clay, technique, glaze="", temperature=0, notes="", created="2026-11-08"):
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
```

Output:

```text
Blue bowl modeled {'modeled': '2026-11-01'}
```

`self` is the piece being created. `self.name = name` means "this piece's name is the name I received".

In the real program you will want today's date as the default. A default value is computed only once, when Python reads the `def`, so we use `None` and fill it inside:

<!-- no-verify -->
```python
from datetime import date


class Piece:
    def __init__(self, name, clay, technique, glaze="", temperature=0, notes="", created=None):
        if created is None:
            created = date.today().isoformat()
        ...
```

</details>

### Step 2: How a piece looks when printed

Add `__str__` so that `print(bowl)` shows `Blue bowl (stoneware, wheel) - modeled`.

<details>
<summary>Show answer</summary>

```python
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
```

Output:

```text
Blue bowl (stoneware, wheel) - modeled
```

This replaces the old `describe(piece)` function: now the piece knows how to describe itself.

</details>

### Step 3: Advancing, with the date

Add the method `advance(self, on_date)`. It moves to the next stage, writes `on_date` in `history` for the new stage, and raises `StageError` if the piece is already finished.

Why receive the date instead of using today's date inside? Because then you can test it with any date you want, and you can also register a stage you forgot to record yesterday.

<details>
<summary>Show answer</summary>

```python
STAGES = ["modeled", "drying", "bisque_fired", "glazed", "glaze_fired"]


class StageError(Exception):
    pass


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
```

Output:

```text
Blue bowl (stoneware, wheel) - bisque_fired
{'modeled': '2026-11-01', 'drying': '2026-11-02', 'bisque_fired': '2026-11-10'}
```

</details>

### Step 4: Is it finished?

Add a method `is_finished(self)` that returns `True` when the stage is `glaze_fired`.

<details>
<summary>Show answer</summary>

```python
STAGES = ["modeled", "drying", "bisque_fired", "glazed", "glaze_fired"]


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
```

Output:

```text
False
True
```

`STAGES[-1]` is the last item of the list. If one day you add a stage after `glaze_fired`, this method keeps working without changes.

</details>

### Step 5: From object to dictionary and back

JSON does not know what a `Piece` is. It only knows dictionaries, lists, text and numbers. Add:

- `to_dict(self)`: returns a dictionary with all the attributes.
- `from_dict(data)`: a **class method** that builds a `Piece` from such a dictionary.

<details>
<summary>Hint</summary>

A class method is written with `@classmethod` above it and receives `cls` (the class itself) instead of `self`. Inside it, `cls(...)` creates a new piece, exactly like `Piece(...)`.

</details>

<details>
<summary>Show answer</summary>

```python
class Piece:
    def __init__(self, name, clay, technique, glaze="", temperature=0, notes="", created="2026-11-08"):
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
        piece = cls(data["name"], data["clay"], data["technique"], data["glaze"],
                    data["temperature"], data["notes"], data["created"])
        piece.stage = data["stage"]
        piece.history = data.get("history", {data["stage"]: data["created"]})
        return piece


bowl = Piece("Blue bowl", "stoneware", "wheel", "celadon", 1240, "thin walls", "2026-11-01")
data = bowl.to_dict()
copy = Piece.from_dict(data)
print(copy.name, copy.temperature, copy.history)
print(copy.to_dict() == data)
```

Output:

```text
Blue bowl 1240 {'modeled': '2026-11-01'}
True
```

`data.get("history", ...)` handles the pieces you saved in milestones 3 and 4, which had no history yet: for them we create a history with only the current stage.

</details>

### Step 6: Plug the class into the app

Update `storage.py` so `load_pieces()` returns a list of `Piece` objects and `save_pieces()` saves `[piece.to_dict() for piece in pieces]`. Update `main.py` to use `piece.advance(date.today().isoformat())`, `print(piece)` and `piece.name`. Update the tests.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# atanor/storage.py
import json
from pathlib import Path

from atanor.piece import Piece

FILE = Path("pieces.json")


def save_pieces(pieces, file=FILE):
    with open(file, "w", encoding="utf-8") as f:
        json.dump([piece.to_dict() for piece in pieces], f, ensure_ascii=False, indent=2)


def load_pieces(file=FILE):
    if not Path(file).exists():
        return []
    with open(file, "r", encoding="utf-8") as f:
        return [Piece.from_dict(data) for data in json.load(f)]
```

<!-- no-verify -->
```python
# tests/test_piece.py
import pytest

from atanor.piece import Piece, StageError


def test_advance_records_the_date():
    piece = Piece("Bowl", "stoneware", "wheel", created="2026-11-01")
    piece.advance("2026-11-02")
    assert piece.stage == "drying"
    assert piece.history["drying"] == "2026-11-02"


def test_cannot_advance_finished_piece():
    piece = Piece("Bowl", "stoneware", "wheel")
    piece.stage = "glaze_fired"
    with pytest.raises(StageError):
        piece.advance("2026-11-02")


def test_round_trip():
    piece = Piece("Bowl", "stoneware", "wheel", "celadon", 1240, "", "2026-11-01")
    assert Piece.from_dict(piece.to_dict()).to_dict() == piece.to_dict()
```

Move `STAGES` and `StageError` into `atanor/piece.py` too, and delete `atanor/pieces.py` when nothing imports it anymore.

</details>

## Checkpoint

```console
PS C:\Users\you\Projects\atanor> uv run pytest
tests/test_piece.py ...                                     [ 60%]
tests/test_storage.py ..                                    [100%]
5 passed in 0.03s
PS C:\Users\you\Projects\atanor> uv run main.py
...
> 3
Which piece? blue bowl
Blue bowl is now bisque_fired.
```

Open `pieces.json`: each piece now has a `"history"` with the date of every stage it went through.

## Commit

```powershell
git add .
git commit -m "Model pieces with a Piece class that keeps stage history"
git push
```

## Stretch goals

#### Stretch 1: How many days in the current stage

Add `days_in_stage(self, today)` that returns how many days the piece has been in its current stage. `today` is a date as text, like `"2026-11-10"`.

<details>
<summary>Hint</summary>

`date.fromisoformat("2026-11-10")` turns text into a date. Subtracting two dates gives a `timedelta`, and `.days` gives the number.

</details>

<details>
<summary>Show answer</summary>

```python
from datetime import date


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
```

Output:

```text
8
```

You will use exactly this method in milestone 8.

</details>

#### Stretch 2: `__repr__`

In the terminal, a list of pieces prints as `[<__main__.Piece object at 0x...>]`. Add `__repr__` so it prints `[Piece('Blue bowl', 'drying')]`.

<details>
<summary>Show answer</summary>

```python
class Piece:
    def __init__(self, name, stage):
        self.name = name
        self.stage = stage

    def __repr__(self):
        return f"Piece({self.name!r}, {self.stage!r})"


print([Piece("Blue bowl", "drying"), Piece("Mug", "glazed")])
```

Output:

```text
[Piece('Blue bowl', 'drying'), Piece('Mug', 'glazed')]
```

`__str__` is for people using the app. `__repr__` is for you, the programmer, while debugging. The `!r` adds the quotes around text.

</details>

**Next:** [Milestone 6: SQLite](06-sqlite.md)
