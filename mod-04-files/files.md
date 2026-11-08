# Files

> **In one sentence:** a file lets your program save text on the disk and read it back later, even after the program has finished.

## Why it matters

Variables live in the computer's memory, and memory is wiped when the program ends. If you want a shopping list, a diary, or a list of clients to still be there tomorrow, you have to put it in a file. Almost every real program you use (a notes app, a spreadsheet, a game with saved progress) reads and writes files.

## Analogy

Think of a notebook in a drawer. The drawer is the disk. The **name written on the cover** is the file name. Knowing the name of the notebook does not let you read it: you have to **take it out of the drawer and open it** first. Then you can read the pages, or write on a new page at the end. When you are done, you **close it and put it back** so nothing gets damaged.

Python works the same way: a file name, then open, then read or write, then close.

## The idea, step by step

### A file name is just a string

This line does **not** open, create or read anything:

<!-- no-verify -->
```python
file_name = "shopping.txt"
```

`file_name` is a variable holding the text `"shopping.txt"`. It is the name on the notebook cover, nothing more. The file on the disk is a separate thing. To use the file, you have to ask Python to open it.

### Creating a file with `open` and mode `"w"`

`open` is a built-in function. It takes the file name and a **mode**, which says what you want to do:

| Mode | Name | What it does |
|---|---|---|
| `"r"` | read | Opens an existing file to read it. Fails if the file does not exist. |
| `"w"` | write | Creates the file, or **erases everything** in it if it already exists, then lets you write. |
| `"a"` | append | Opens the file and adds to the **end**. Creates it if it does not exist. Never erases. |

The safe way to open a file is with `with`:

```python
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("milk\n")
    file.write("eggs\n")
    file.write("bread\n")

print("Saved!")
```

Output:

```text
Saved!
```

Let's read that line slowly:

- `open("shopping.txt", "w", encoding="utf-8")` opens the file for writing.
- `as file` gives the opened file a name, so you can use it inside the block.
- The `:` and the indentation create a block, just like in `if`, `for` and `def`.
- When the block ends, `with` **closes the file for you**. That is why we use it: you never forget to close.
- `encoding="utf-8"` tells Python how to store letters like `ç`, `ã` and `é`. On Windows, without it, accented letters can turn into strange symbols. Always include it.

### Reading the whole file with `read()`

```python
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("milk\n")
    file.write("eggs\n")

with open("shopping.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

Output:

```text
milk
eggs
```

`file.read()` returns the whole content as **one string**. Notice the parentheses: `read` is a method, and the `()` is what makes it run.

### Opening is not reading

If you print the opened file itself, you do not get the text. You get a description of the open file:

```python
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("milk\n")

with open("shopping.txt", "r", encoding="utf-8") as file:
    print(file)
```

Output:

```text
<_io.TextIOWrapper name='shopping.txt' mode='r' encoding='utf-8'>
```

That is Python saying: "this is an open file called `shopping.txt`, in read mode". The notebook is open on the table, but nobody has read it yet. To get the text, call `file.read()`.

The same thing happens if you forget the parentheses:

<!-- no-verify -->
```python
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("milk\n")

with open("shopping.txt", "r", encoding="utf-8") as file:
    print(file.read)
```

Output:

```text
<built-in method read of _io.TextIOWrapper object at 0x7f3a2c1b2e80>
```

The number at the end changes every run, but the message is always "built-in method read". `file.read` is the **method itself**; `file.read()` **runs** it.

### Why `"\n"` matters when writing

`write` writes exactly what you give it. It does **not** add a line break:

```python
with open("colors.txt", "w", encoding="utf-8") as file:
    file.write("red")
    file.write("green")
    file.write("blue")

with open("colors.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

Output:

```text
redgreenblue
```

The words got glued together. `"\n"` is the "new line" character. Add it at the end of each line:

```python
with open("colors.txt", "w", encoding="utf-8") as file:
    file.write("red\n")
    file.write("green\n")
    file.write("blue\n")

with open("colors.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

Output:

```text
red
green
blue
```

### Adding without erasing: mode `"a"`

Mode `"w"` starts from a blank page every time. Mode `"a"` (append) keeps what is there and adds to the end:

```python
with open("diary.txt", "w", encoding="utf-8") as file:
    file.write("Monday: rain\n")

with open("diary.txt", "a", encoding="utf-8") as file:
    file.write("Tuesday: sun\n")

with open("diary.txt", "a", encoding="utf-8") as file:
    file.write("Wednesday: wind\n")

with open("diary.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

Output:

```text
Monday: rain
Tuesday: sun
Wednesday: wind
```

Now watch what `"w"` does to the same file:

```python
with open("diary.txt", "w", encoding="utf-8") as file:
    file.write("Monday: rain\n")
    file.write("Tuesday: sun\n")

with open("diary.txt", "w", encoding="utf-8") as file:
    file.write("Wednesday: wind\n")

with open("diary.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

Output:

```text
Wednesday: wind
```

Monday and Tuesday are gone. **`"w"` erases first, then writes.** Use `"a"` when you want to keep a growing list.

### Reading line by line

Often you want each line separately, for example to number them. There are three common ways.

**1. `splitlines()`** turns the text into a list of lines, without the `"\n"`:

```python
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("milk\neggs\nbread\n")

with open("shopping.txt", "r", encoding="utf-8") as file:
    lines = file.read().splitlines()

print(lines)
```

Output:

```text
['milk', 'eggs', 'bread']
```

**2. `readlines()`** also gives a list, but **keeps** the `"\n"` at the end of each line:

```python
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("milk\neggs\nbread\n")

with open("shopping.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)
```

Output:

```text
['milk\n', 'eggs\n', 'bread\n']
```

**3. A `for` loop directly on the file** reads one line per turn. Each line still has its `"\n"`, so use `.strip()` to remove it:

```python
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("milk\neggs\nbread\n")

with open("shopping.txt", "r", encoding="utf-8") as file:
    for line in file:
        print("-", line.strip())
```

Output:

```text
- milk
- eggs
- bread
```

If you forget `.strip()`, you get an empty line after each item, because `print` adds its own line break on top of the one already in the line.

For beginners, `read().splitlines()` is usually the simplest choice: you get a clean list and can use everything you know about lists.

```python
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("milk\neggs\nbread\n")

with open("shopping.txt", "r", encoding="utf-8") as file:
    items = file.read().splitlines()

for number, item in enumerate(items, start=1):
    print(f"{number}. {item}")

print(f"Total: {len(items)} items")
```

Output:

```text
1. milk
2. eggs
3. bread
Total: 3 items
```

### Functions that use files

Putting file code inside functions makes it reusable. The file name becomes a **parameter**, so the same function works for any file:

```python
def write_line(file_name, text):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(text + "\n")


def read_lines(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read().splitlines()


write_line("movies.txt", "Spirited Away")
write_line("movies.txt", "Amélie")
print(read_lines("movies.txt"))
```

Output:

```text
['Spirited Away', 'Amélie']
```

### When the file does not exist

Mode `"r"` needs the file to exist. If it does not, Python stops with `FileNotFoundError`:

<!-- error -->
```python
with open("recipes.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

```text
FileNotFoundError: [Errno 2] No such file or directory: 'recipes.txt'
```

Modes `"w"` and `"a"` never have this problem, because they **create** the file if it is missing. A simple trick: if you are about to read a file that might not exist yet, write to it in `"a"` mode first (even an empty string). That creates it without erasing anything:

```python
with open("recipes.txt", "a", encoding="utf-8") as file:
    file.write("")

with open("recipes.txt", "r", encoding="utf-8") as file:
    print(repr(file.read()))
```

Output:

```text
''
```

`repr` shows the string with its quotes, so you can see it is empty. (In module 07 you will learn a cleaner way to handle errors, with `try` and `except`.)

### Where is the file? Relative paths

When you write `open("shopping.txt", ...)`, Python looks for the file in the **folder where the terminal is** when you run the program, not necessarily the folder where the `.py` file is saved.

<!-- no-verify -->
```powershell
PS C:\Users\you\Projects> python lists\shopping.py
```

Here the terminal is in `Projects`, so `shopping.txt` is created in `Projects`, not in `Projects\lists`. To keep things predictable, always `cd` into the program's folder first, then run it:

```powershell
PS C:\Users\you\Projects> cd lists
PS C:\Users\you\Projects\lists> python shopping.py
```

Use `pwd` to check where you are and `ls` to see if the file was created where you expected.

## Common mistakes

### Forgetting the parentheses on `read`

<!-- no-verify -->
```python
with open("shopping.txt", "r", encoding="utf-8") as file:
    content = file.read
print(content)
```

```text
<built-in method read of _io.TextIOWrapper object at 0x7f3a2c1b2e80>
```

No error, but no text either. `file.read` is the method; `file.read()` runs it and gives you the content. **Fix:** `content = file.read()`.

### Using `"w"` when you meant `"a"`

Every time the program runs, the old content disappears and only the last line is left. There is no error message, which makes this mistake sneaky. **Fix:** if you are adding to a list that should grow, use `"a"`.

### Lines glued together

<!-- no-verify -->
```python
file.write(note)
```

Every note ends up on the same line: `buy milkcall grandmapay rent`. **Fix:** `file.write(note + "\n")`.

### Reading a file that does not exist

<!-- error -->
```python
with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

```text
FileNotFoundError: [Errno 2] No such file or directory: 'notes.txt'
```

Either the file was never created, the name is spelled differently (`Notes.txt`, `notes.text`), or the terminal is in a different folder. **Fix:** check with `ls` and `pwd`. If the file should be created on first use, open it with `"a"` before reading.

### Using a file outside the `with` block

<!-- error -->
```python
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("milk\n")

file.write("eggs\n")
```

```text
ValueError: I/O operation on closed file.
```

When the `with` block ends, the file is closed. The variable `file` still exists, but the notebook is back in the drawer. **Fix:** indent the line so it is inside the block, or open the file again.

### Writing a number

<!-- error -->
```python
with open("scores.txt", "w", encoding="utf-8") as file:
    file.write(42)
```

```text
TypeError: write() argument must be str, not int
```

`write` only accepts strings. **Fix:** `file.write(str(42) + "\n")` or `file.write(f"{42}\n")`.

## Exercises

### Predict the output

Read the code, write down what you think it prints, and only then check.

#### Exercise 1: Write then read

```python
with open("pets.txt", "w", encoding="utf-8") as file:
    file.write("cat\n")
    file.write("dog\n")

with open("pets.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

<details>
<summary>Show answer</summary>

Output:

```text
cat
dog
```

Mode `"w"` created the file with two lines, and `read()` returned all of it.

</details>

#### Exercise 2: Write twice

```python
with open("pets.txt", "w", encoding="utf-8") as file:
    file.write("cat\n")

with open("pets.txt", "w", encoding="utf-8") as file:
    file.write("fish\n")

with open("pets.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

<details>
<summary>Show answer</summary>

Output:

```text
fish
```

The second `"w"` erased the file before writing. The cat is gone.

</details>

#### Exercise 3: Append

```python
with open("pets.txt", "w", encoding="utf-8") as file:
    file.write("cat\n")

with open("pets.txt", "a", encoding="utf-8") as file:
    file.write("fish\n")

with open("pets.txt", "r", encoding="utf-8") as file:
    lines = file.read().splitlines()

print(len(lines))
print(lines[-1])
```

<details>
<summary>Show answer</summary>

Output:

```text
2
fish
```

`"a"` kept `cat` and added `fish`. The list has 2 lines, and `lines[-1]` is the last one.

</details>

#### Exercise 4: No line breaks

```python
with open("word.txt", "w", encoding="utf-8") as file:
    for letter in ["s", "u", "n"]:
        file.write(letter)

with open("word.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

<details>
<summary>Show answer</summary>

Output:

```text
sun
```

Without `"\n"`, the letters are written one after the other on the same line.

</details>

### Fix the bug

#### Exercise 5: The list that never grows

This program should keep a list of books, adding one each time it runs. But it always ends up with only the last book. Fix it.

<!-- no-verify -->
```python
def add_book(title):
    with open("books.txt", "w", encoding="utf-8") as file:
        file.write(title + "\n")
```

<details>
<summary>Hint</summary>

Look at the mode. Which mode erases, and which one adds?

</details>

<details>
<summary>Show answer</summary>

```python
def add_book(title):
    with open("books.txt", "a", encoding="utf-8") as file:
        file.write(title + "\n")


add_book("Dom Casmurro")
add_book("The Hobbit")

with open("books.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

Output:

```text
Dom Casmurro
The Hobbit
```

Mode `"w"` erases the file every time. Mode `"a"` adds to the end.

</details>

#### Exercise 6: Empty lines everywhere

This program prints an empty line after each item. Fix it so the list is printed without gaps.

<!-- no-verify -->
```python
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("rice\nbeans\n")

with open("shopping.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line)
```

<details>
<summary>Hint</summary>

Each line read from the file still has its `"\n"`. And `print` adds another one.

</details>

<details>
<summary>Show answer</summary>

```python
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("rice\nbeans\n")

with open("shopping.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

Output:

```text
rice
beans
```

`.strip()` removes the `"\n"` (and any spaces) from the ends of the line.

</details>

#### Exercise 7: The text that never appears

This program should print the content of the file, but it prints something strange instead. Fix it.

<!-- no-verify -->
```python
with open("greeting.txt", "w", encoding="utf-8") as file:
    file.write("Good morning!\n")

with open("greeting.txt", "r", encoding="utf-8") as file:
    print(file)
```

<details>
<summary>Show answer</summary>

```python
with open("greeting.txt", "w", encoding="utf-8") as file:
    file.write("Good morning!\n")

with open("greeting.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

Output:

```text
Good morning!
```

`file` is the open file, not its text. `file.read()` gets the text.

</details>

### Write it

#### Exercise 8: Your favorite foods

Write a program that saves three favorite foods in `foods.txt` (one per line), then reads the file and prints them numbered from 1.

<details>
<summary>Hint</summary>

Write with `"w"` and `"\n"`. Read with `read().splitlines()`. Use `enumerate(..., start=1)`.

</details>

<details>
<summary>Show answer</summary>

```python
with open("foods.txt", "w", encoding="utf-8") as file:
    file.write("feijoada\n")
    file.write("lasagna\n")
    file.write("açaí\n")

with open("foods.txt", "r", encoding="utf-8") as file:
    foods = file.read().splitlines()

for number, food in enumerate(foods, start=1):
    print(f"{number}. {food}")
```

Output:

```text
1. feijoada
2. lasagna
3. açaí
```

</details>

#### Exercise 9: Save a whole list

You have a list in Python. Write a function `save_list(file_name, items)` that writes each item of the list on its own line. Then read the file and print how many lines it has.

<!-- no-verify -->
```python
plants = ["fern", "cactus", "basil", "orchid"]
```

<details>
<summary>Hint</summary>

Open the file once, then use a `for` loop **inside** the `with` block to write each item.

</details>

<details>
<summary>Show answer</summary>

```python
def save_list(file_name, items):
    with open(file_name, "w", encoding="utf-8") as file:
        for item in items:
            file.write(item + "\n")


plants = ["fern", "cactus", "basil", "orchid"]
save_list("plants.txt", plants)

with open("plants.txt", "r", encoding="utf-8") as file:
    lines = file.read().splitlines()

print(f"The file has {len(lines)} lines.")
```

Output:

```text
The file has 4 lines.
```

</details>

#### Exercise 10: Count matching lines

Write a function `count_lines_with(file_name, word)` that returns how many lines of the file contain `word`. Test it with the file below.

<!-- no-verify -->
```python
with open("tasks.txt", "w", encoding="utf-8") as file:
    file.write("buy milk\n")
    file.write("call the bank\n")
    file.write("buy stamps\n")
    file.write("water the plants\n")
```

<details>
<summary>Hint</summary>

Read the lines into a list, start a counter at 0, and use `if word in line:` inside a `for`.

</details>

<details>
<summary>Show answer</summary>

```python
def count_lines_with(file_name, word):
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()
    count = 0
    for line in lines:
        if word in line:
            count = count + 1
    return count


with open("tasks.txt", "w", encoding="utf-8") as file:
    file.write("buy milk\n")
    file.write("call the bank\n")
    file.write("buy stamps\n")
    file.write("water the plants\n")

print(count_lines_with("tasks.txt", "buy"))
print(count_lines_with("tasks.txt", "plants"))
```

Output:

```text
2
1
```

</details>

## Review

#### Review 1: f-strings (module 01)

What does this print?

```python
item = "coffee"
price = 12.5
print(f"One {item} costs R$ {price}")
```

<details>
<summary>Show answer</summary>

Output:

```text
One coffee costs R$ 12.5
```

Inside `{}`, the f-string puts the value of each variable.

</details>

#### Review 2: return vs print (module 03)

What does this print? Pay attention to what the function **returns**.

```python
def double(number):
    print("Calculating...")
    return number * 2


result = double(4)
print(result + 1)
```

<details>
<summary>Show answer</summary>

Output:

```text
Calculating...
9
```

`print` inside the function shows a message. `return` sends `8` back, which is stored in `result`. Then `8 + 1` is `9`.

</details>

#### Review 3: lists and for (module 02)

Write a loop that prints only the items of this list that have more than 4 letters.

<!-- no-verify -->
```python
fruits = ["kiwi", "mango", "fig", "banana"]
```

<details>
<summary>Show answer</summary>

```python
fruits = ["kiwi", "mango", "fig", "banana"]
for fruit in fruits:
    if len(fruit) > 4:
        print(fruit)
```

Output:

```text
mango
banana
```

</details>

## Recap

- A file name is just a string. `open(name, mode, encoding="utf-8")` is what actually opens the file.
- Use `with open(...) as file:` so the file is closed automatically when the block ends.
- `"r"` reads, `"w"` erases and writes, `"a"` adds to the end. When in doubt, `"a"` is the one that never loses data.
- `write` does not add line breaks: add `"\n"` yourself. `file.read().splitlines()` gives you a clean list of lines.
- Opening is not reading: `print(file)` shows the open file, `print(file.read())` shows its text.

**Next:** [project-notebook.md](project-notebook.md)
