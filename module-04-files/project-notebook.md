# Project: Quick Notes

> **In one sentence:** you will build `notes.py`, a small program that asks for a note, saves it in `notes.txt`, and shows all your notes numbered, even the ones from yesterday.

## Why it matters

This is your first program that **remembers**. It uses almost everything you have learned so far: variables, f-strings, `input`, lists, `for`, functions, `return` and files. Building it step by step, one small function at a time, is exactly how programmers build bigger programs too.

## Analogy

Think of a kitchen with three cooks and one head chef. One cook only **writes** orders on the board. One only **reads** the board aloud. One only **takes** orders from customers. None of them decides what happens next. The head chef, `main()`, says: "take the order, write it on the board, now read the board". Each cook does one simple job well, and only one person controls the flow.

## The idea, step by step

Create a folder for this project inside your `Projects` folder, open it in your editor, and create a file called `notes.py`.

```powershell
cd ~\Projects
mkdir notes
cd notes
cursor .
```

On macOS or Linux:

```bash
cd ~/Projects
mkdir notes
cd notes
cursor .
```

### Step 1: a constant for the file name

At the top of `notes.py`, write:

<!-- no-verify -->
```python
NOTES_FILE = "notes.txt"
```

This is just a string with the file's name. It does not open or create anything yet. We write the variable name in CAPITALS because it is a **constant**: a value that is set once and never changes. Python does not force this; it is a convention that tells other people "do not change me".

Why a variable at all? If one day you want to rename the file, you change it in **one** place instead of hunting through the whole program.

### Step 2: a function that saves one note

<!-- no-verify -->
```python
def save_note(file_name, note):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(note + "\n")
```

- `file_name` and `note` are **parameters**: names that only exist inside the function. They receive whatever values you pass when you call it.
- We use `"a"` because we want the list of notes to **grow**. With `"w"`, each new note would erase all the old ones.
- `+ "\n"` puts each note on its own line.

Test it right away. Add these lines below the function, save with `Ctrl+S`, and run `python notes.py`:

```python
def save_note(file_name, note):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(note + "\n")


save_note("notes.txt", "buy coffee")
save_note("notes.txt", "call the dentist")

with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

Output:

```text
buy coffee
call the dentist
```

You can also check the file in the terminal: `cat notes.txt` (it works in PowerShell too). If you run the program again, the two notes are added again: that is `"a"` doing its job. Delete `notes.txt` whenever you want to start fresh.

When it works, **remove the test lines**. Keep only the function.

### Step 3: a function that reads all notes

<!-- no-verify -->
```python
def read_notes(file_name):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write("")
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read().splitlines()
```

Two things to notice:

- The first `with` opens the file in `"a"` mode and writes nothing. Why? The very first time you run the program, `notes.txt` does not exist, and mode `"r"` would crash with `FileNotFoundError`. Mode `"a"` creates the file if it is missing, and never erases anything.
- This function **returns** the list of notes. It does not print anything. Reading and showing are two different jobs.

Test it:

```python
def save_note(file_name, note):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(note + "\n")


def read_notes(file_name):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write("")
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read().splitlines()


print(read_notes("notes.txt"))
save_note("notes.txt", "buy coffee")
print(read_notes("notes.txt"))
```

Output:

```text
[]
['buy coffee']
```

The first call returns an empty list `[]` because the file was just created, empty. After saving a note, the list has one item.

### Step 4: a function that shows the notes

<!-- no-verify -->
```python
def show_notes(notes):
    print("Your notes:")
    for number, note in enumerate(notes, start=1):
        print(f"{number}. {note}")
```

This one receives a **list** (not a file name) and only prints. It does not know or care where the list came from. Test it with a list you write by hand:

```python
def show_notes(notes):
    print("Your notes:")
    for number, note in enumerate(notes, start=1):
        print(f"{number}. {note}")


show_notes(["buy coffee", "call the dentist", "water the plants"])
```

Output:

```text
Your notes:
1. buy coffee
2. call the dentist
3. water the plants
```

### Step 5: a function that asks for a note

<!-- no-verify -->
```python
def ask_note():
    return input("Write a note: ")
```

`input` shows the message, waits for you to type and press Enter, and gives back what you typed as a string. The function returns that string to whoever called it.

### Step 6: `main()`, the head chef

Now the function that controls the whole flow:

<!-- no-verify -->
```python
def main():
    note = ask_note()
    save_note(NOTES_FILE, note)
    notes = read_notes(NOTES_FILE)
    show_notes(notes)


main()
```

Read `main()` aloud: "ask for a note, save it in the notes file, read all notes, show them". It reads like a recipe. Every detail lives inside the other functions.

The last line, `main()`, is the **call**. Without it, Python would only *define* the functions and the program would do nothing.

### The complete program

<!-- no-verify -->
```python
NOTES_FILE = "notes.txt"


def save_note(file_name, note):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(note + "\n")


def read_notes(file_name):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write("")
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read().splitlines()


def show_notes(notes):
    print("Your notes:")
    for number, note in enumerate(notes, start=1):
        print(f"{number}. {note}")


def ask_note():
    return input("Write a note: ")


def main():
    note = ask_note()
    save_note(NOTES_FILE, note)
    notes = read_notes(NOTES_FILE)
    show_notes(notes)


main()
```

Run it a few times. The notes from earlier runs are still there:

```console
PS C:\Users\you\Projects\notes> python notes.py
Write a note: buy coffee
Your notes:
1. buy coffee
PS C:\Users\you\Projects\notes> python notes.py
Write a note: call the dentist
Your notes:
1. buy coffee
2. call the dentist
```

### Parameter or global? Why `file_name` and `NOTES_FILE` are different names

`NOTES_FILE` is created at the top of the file, outside every function. `file_name` is a parameter that exists only inside `save_note` and `read_notes`. When `main()` calls `save_note(NOTES_FILE, note)`, the **value** of `NOTES_FILE` (the text `"notes.txt"`) is passed in, and inside the function it is called `file_name`.

The value you pass in a call is called an **argument**. So: in `def save_note(file_name, note)`, `file_name` is a **parameter**. In `save_note(NOTES_FILE, note)`, `NOTES_FILE` is an **argument**. Different names, same value, at that moment.

## Common mistakes

### Defining but never calling `main()`

<!-- no-verify -->
```python
def main():
    note = ask_note()
    save_note(NOTES_FILE, note)
```

You run the program and nothing happens. No error, no question. Defining a function does not run it. **Fix:** add `main()` at the end of the file, without indentation.

### Calling a function before it is defined

<!-- error -->
```python
main()


def main():
    print("Hello")
```

```text
NameError: name 'main' is not defined. Did you mean: 'min'?
```

(The "Did you mean" part is just Python guessing a similar built-in name, `min`. Here the guess is wrong; ignore it.) Python reads the file from top to bottom. On the first line, `main` does not exist yet. **Fix:** put all the `def`s first and the call `main()` at the very end.

### Forgetting to save the file before running

You change the code, run it, and the old behavior appears. The editor shows a dot (or a white circle) on the tab when there are unsaved changes. **Fix:** `Ctrl+S`, then run.

### Printing instead of returning

<!-- no-verify -->
```python
def read_notes(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        print(file.read().splitlines())
```

Now `notes = read_notes(NOTES_FILE)` stores `None`, and `show_notes(notes)` crashes:

<!-- error -->
```python
def show_notes(notes):
    for number, note in enumerate(notes, start=1):
        print(f"{number}. {note}")


show_notes(None)
```

```text
TypeError: 'NoneType' object is not iterable
```

A function without `return` gives back `None`. **Fix:** `return` the list, and let `show_notes` do the printing.

## Exercises

Each exercise changes the complete program above. Copy it into `notes.py` first and make sure it runs.

### Predict the output

#### Exercise 1: What gets saved?

Imagine `notes.txt` does not exist. What does this print?

```python
def save_note(file_name, note):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(note + "\n")


def read_notes(file_name):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write("")
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read().splitlines()


save_note("notes.txt", "pay rent")
save_note("notes.txt", "buy bread")
notes = read_notes("notes.txt")
print(len(notes))
print(notes[0])
```

<details>
<summary>Show answer</summary>

Output:

```text
2
pay rent
```

Two notes were saved. `notes[0]` is the first one, because lists start counting at 0.

</details>

### Fix the bug

#### Exercise 2: The notebook with amnesia

Someone changed one character in `save_note`, and now only the last note survives. What was it, and how do you fix it?

<!-- no-verify -->
```python
def save_note(file_name, note):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(note + "\n")
```

<details>
<summary>Show answer</summary>

The mode changed from `"a"` to `"w"`. Mode `"w"` erases the file every time it opens it. Change it back to `"a"`.

</details>

### Write it

#### Exercise 3: Show the count

After the list, show how many notes there are, like this:

```console
Your notes:
1. buy coffee
2. call the dentist
You have 2 notes.
```

<details>
<summary>Hint</summary>

`len(notes)` gives the number of items in the list. Add one line to `show_notes`, after the loop (not inside it).

</details>

<details>
<summary>Show answer</summary>

```python
def show_notes(notes):
    print("Your notes:")
    for number, note in enumerate(notes, start=1):
        print(f"{number}. {note}")
    print(f"You have {len(notes)} notes.")


show_notes(["buy coffee", "call the dentist"])
```

Output:

```text
Your notes:
1. buy coffee
2. call the dentist
You have 2 notes.
```

If the `print` were indented one level more, it would run once per note.

</details>

#### Exercise 4: Ignore empty notes

If you just press Enter without typing, an empty line is saved. Change `main()` so that an empty note (or one with only spaces) is **not** saved, and a message is shown instead.

```console
PS C:\Users\you\Projects\notes> python notes.py
Write a note:
Empty note, nothing saved.
Your notes:
1. buy coffee
```

<details>
<summary>Hint</summary>

`note.strip()` removes spaces from both ends. An empty string `""` counts as false in an `if`, so `if note.strip() == "":` (or `if not note.strip():`) detects an empty note.

</details>

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
def main():
    note = ask_note()
    if note.strip() == "":
        print("Empty note, nothing saved.")
    else:
        save_note(NOTES_FILE, note)
    notes = read_notes(NOTES_FILE)
    show_notes(notes)
```

The decision lives in `main()`, the function that controls the flow. `save_note` stays simple: it saves whatever it gets.

</details>

#### Exercise 5: A menu that keeps going (challenge)

Right now the program asks for one note and ends. Make it show a menu and keep running until the user chooses to leave:

```console
PS C:\Users\you\Projects\notes> python notes.py
1) Add a note
2) Show notes
0) Exit
Choose: 1
Write a note: buy coffee
1) Add a note
2) Show notes
0) Exit
Choose: 2
Your notes:
1. buy coffee
1) Add a note
2) Show notes
0) Exit
Choose: 0
Bye!
```

<details>
<summary>Hint</summary>

A `while True:` loop repeats its block forever. Inside it, `break` stops the loop immediately. So the shape is:

```python
while True:
    # show the menu
    # ask for a choice
    # if the choice is "0": print "Bye!" and break
    # elif "1": ask and save
    # elif "2": read and show
```

Remember that `input` always returns a string, so compare with `"1"`, not `1`.

</details>

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
def show_menu():
    print("1) Add a note")
    print("2) Show notes")
    print("0) Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose: ")
        if choice == "0":
            print("Bye!")
            break
        elif choice == "1":
            note = ask_note()
            save_note(NOTES_FILE, note)
        elif choice == "2":
            show_notes(read_notes(NOTES_FILE))
        else:
            print("Unknown option, try again.")


main()
```

`show_notes(read_notes(NOTES_FILE))` calls `read_notes` first, then passes its result straight into `show_notes`. It is the same as two lines with a variable in between.

</details>

## Review

#### Review 1: parameter or argument? (module 03)

In this code, which names are **parameters** and which values are **arguments**?

<!-- no-verify -->
```python
def greet(name, time_of_day):
    print(f"Good {time_of_day}, {name}!")


greet("Ana", "evening")
```

<details>
<summary>Show answer</summary>

`name` and `time_of_day` are parameters (in the `def`). `"Ana"` and `"evening"` are arguments (in the call). It prints `Good evening, Ana!`.

</details>

#### Review 2: concatenation vs interpolation (module 01)

What does each line print, and which one crashes?

<!-- no-verify -->
```python
count = 3
print(f"You have {count} notes")
print("You have " + str(count) + " notes")
print("You have " + count + " notes")
```

<details>
<summary>Show answer</summary>

The first two print `You have 3 notes`. The third crashes with `TypeError: can only concatenate str (not "int") to str`, because `+` cannot join a string and a number. The f-string converts the number for you; with `+` you need `str(count)`.

</details>

## Recap

- A real program is a set of small functions, each with one job, plus a `main()` that controls the flow.
- Save with mode `"a"` so the list grows; read with `read().splitlines()` to get a list.
- Opening the file in `"a"` mode before reading creates it on the first run and avoids `FileNotFoundError`.
- Functions that **read** should `return` the data; functions that **show** should print it.
- Define everything first, then call `main()` on the last line.

**Next:** [Module 05: Git and GitHub](../module-05-git-and-github/README.md)
