# Milestone 1: A text file

## Goal

Write `atanor.py`, a small program that asks for a ceramic piece, saves it in a text file and lists every piece saved so far, numbered.

## Requires

Modules 0 to 4: terminal, variables, strings and f-strings, lists, `for`, functions with `return`, and reading and writing files.

## What you will build

When you run it, it looks like this:

```console
PS C:\Users\you\Projects\atanor> python atanor.py
Piece name: Blue bowl
Clay: stoneware
Saved!

Your pieces:
1. Blue bowl (stoneware)
2. Small vase (porcelain)
```

Each piece is one line in `pieces.txt`, with the name and the clay separated by a semicolon:

```text
Blue bowl;stoneware
Small vase;porcelain
```

Why a semicolon? Because it is a character that almost never appears in a piece name, so we can use it to split the line back into two parts.

## Steps

### Step 1: Create the folder and the file

Inside your `Projects` folder, create a folder called `atanor`, open it in Cursor and create an empty file called `atanor.py`.

<details>
<summary>Show answer</summary>

```powershell
cd ~\Projects
mkdir atanor
cd atanor
cursor .
```

In Cursor, create the file `atanor.py` in the sidebar.

</details>

### Step 2: Turn a piece into a line

Write a function `make_line(name, clay)` that **returns** the text that goes into the file. It does not print anything and does not touch the file. It only builds the text.

```python
print(make_line("Blue bowl", "stoneware"))
```

Should print:

```text
Blue bowl;stoneware
```

<details>
<summary>Hint</summary>

Use an f-string with a `;` between the two values.

</details>

<details>
<summary>Show answer</summary>

```python
def make_line(name, clay):
    return f"{name};{clay}"


print(make_line("Blue bowl", "stoneware"))
```

Output:

```text
Blue bowl;stoneware
```

The function only **returns** the text. Who calls it decides what to do with it: print it, save it, or both.

</details>

### Step 3: Turn a line back into a piece

Now the opposite. Write `describe(line)` that receives a line like `"Blue bowl;stoneware"` and returns `"Blue bowl (stoneware)"`.

<details>
<summary>Hint</summary>

`line.split(";")` cuts the text at each `;` and gives you a list. The first item is the name, the second is the clay.

</details>

<details>
<summary>Show answer</summary>

```python
def describe(line):
    parts = line.split(";")
    name = parts[0]
    clay = parts[1]
    return f"{name} ({clay})"


print(describe("Blue bowl;stoneware"))
print(describe("Small vase;porcelain"))
```

Output:

```text
Blue bowl (stoneware)
Small vase (porcelain)
```

</details>

### Step 4: Save a piece in the file

Write `save_piece(name, clay)` that opens `pieces.txt` in **append** mode (`"a"`) and writes the line followed by `\n`. Use the `make_line` function you already have.

Run it once by hand to test, then open `pieces.txt` in Cursor to check.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
def save_piece(name, clay):
    with open("pieces.txt", "a", encoding="utf-8") as file:
        file.write(make_line(name, clay) + "\n")


save_piece("Blue bowl", "stoneware")
```

- `"a"` adds to the end of the file. If you used `"w"`, every save would erase the previous pieces.
- `\n` puts each piece on its own line.
- `encoding="utf-8"` makes accented letters (like "cerâmica") work on Windows.

</details>

### Step 5: Read all the pieces

Write `load_pieces()` that reads `pieces.txt` and **returns a list of lines**, without the `\n` at the end.

<details>
<summary>Hint</summary>

`file.read()` gives you the whole text. `.splitlines()` turns it into a list, one item per line, already without `\n`.

</details>

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
def load_pieces():
    with open("pieces.txt", "r", encoding="utf-8") as file:
        return file.read().splitlines()


print(load_pieces())
```

```console
PS C:\Users\you\Projects\atanor> python atanor.py
['Blue bowl;stoneware']
```

</details>

### Step 6: List the pieces, numbered

Write `show_pieces(lines)` that receives the list of lines and prints each piece numbered from 1. Test it with a list you write by hand, without the file.

```python
show_pieces(["Blue bowl;stoneware", "Small vase;porcelain"])
```

Should print:

```text
Your pieces:
1. Blue bowl (stoneware)
2. Small vase (porcelain)
```

<details>
<summary>Hint</summary>

`enumerate(lines, start=1)` gives you the number and the line together. Use `describe` for the text.

</details>

<details>
<summary>Show answer</summary>

```python
def describe(line):
    parts = line.split(";")
    return f"{parts[0]} ({parts[1]})"


def show_pieces(lines):
    print("Your pieces:")
    for number, line in enumerate(lines, start=1):
        print(f"{number}. {describe(line)}")


show_pieces(["Blue bowl;stoneware", "Small vase;porcelain"])
```

Output:

```text
Your pieces:
1. Blue bowl (stoneware)
2. Small vase (porcelain)
```

</details>

### Step 7: One function to control everything

Your program now has small functions that each do one thing. Write a `main()` function that **controls the whole flow**:

1. Ask for the name and the clay with `input`.
2. Save the piece.
3. Print `Saved!` and an empty line.
4. Load all pieces and show them.

At the end of the file, call `main()`. This is the only line outside a function that actually does something.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
def make_line(name, clay):
    return f"{name};{clay}"


def describe(line):
    parts = line.split(";")
    return f"{parts[0]} ({parts[1]})"


def save_piece(name, clay):
    with open("pieces.txt", "a", encoding="utf-8") as file:
        file.write(make_line(name, clay) + "\n")


def load_pieces():
    with open("pieces.txt", "r", encoding="utf-8") as file:
        return file.read().splitlines()


def show_pieces(lines):
    print("Your pieces:")
    for number, line in enumerate(lines, start=1):
        print(f"{number}. {describe(line)}")


def main():
    name = input("Piece name: ")
    clay = input("Clay: ")
    save_piece(name, clay)
    print("Saved!")
    print()
    show_pieces(load_pieces())


main()
```

Reading `main()` is like reading the recipe of the program: you see every step in order, and the details live in the other functions.

</details>

## Checkpoint

Delete `pieces.txt` (if it exists) and run the program twice:

```console
PS C:\Users\you\Projects\atanor> python atanor.py
Piece name: Blue bowl
Clay: stoneware
Saved!

Your pieces:
1. Blue bowl (stoneware)
PS C:\Users\you\Projects\atanor> python atanor.py
Piece name: Small vase
Clay: porcelain
Saved!

Your pieces:
1. Blue bowl (stoneware)
2. Small vase (porcelain)
```

If the second run still shows the first piece, your file is working: the data survived after the program closed.

## Commit

No Git yet. That comes in the next milestone. For now, just keep the folder safe.

## Stretch goals

#### Stretch 1: Count the pieces

After the list, print `You have 2 pieces.` using the number of lines.

<details>
<summary>Show answer</summary>

```python
lines = ["Blue bowl;stoneware", "Small vase;porcelain"]
print(f"You have {len(lines)} pieces.")
```

Output:

```text
You have 2 pieces.
```

</details>

#### Stretch 2: Do not save empty names

If the user presses Enter without typing a name, print `The name cannot be empty.` and do not save anything.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
def main():
    name = input("Piece name: ").strip()
    if name == "":
        print("The name cannot be empty.")
        return
    clay = input("Clay: ")
    save_piece(name, clay)
    print("Saved!")
    print()
    show_pieces(load_pieces())
```

`.strip()` removes spaces at the start and end, so typing only spaces also counts as empty. A `return` with nothing after it simply ends the function early.

</details>

#### Stretch 3: Add the technique

Ask for a third field, the technique (for example `wheel` or `hand-built`), and show it too: `1. Blue bowl (stoneware, wheel)`.

<details>
<summary>Show answer</summary>

```python
def make_line(name, clay, technique):
    return f"{name};{clay};{technique}"


def describe(line):
    name, clay, technique = line.split(";")
    return f"{name} ({clay}, {technique})"


print(describe(make_line("Blue bowl", "stoneware", "wheel")))
```

Output:

```text
Blue bowl (stoneware, wheel)
```

`name, clay, technique = ...` puts each item of the list in its own variable at once. If your old `pieces.txt` has lines with only two parts, delete it first, or `describe` will fail on those lines.

</details>

**Next:** [Milestone 2: A repository](02-repository.md)
