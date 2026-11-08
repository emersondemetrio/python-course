# What Python is and how to run it

> **In one sentence:** Python is a program that reads the instructions you write in a `.py` file and carries them out, one line at a time, from top to bottom.

## Why it matters

Before learning what to write, you need to know where to write it, how to run it, and what to do when Python complains. These three things happen in every single exercise of this course, so it is worth getting comfortable with them now.

## Analogy

Think of a recipe and a cook.

- The **recipe** is your `.py` file: a list of instructions written in a language the cook understands.
- The **cook** is the Python **interpreter**: a program that reads the recipe line by line and does what it says.

Writing a recipe does not make dinner. Someone has to read it and cook. In the same way, **writing code does not run it**. You have to ask Python to read the file.

And if the recipe says "add 2 cups of slat", the cook stops and says "I don't know what slat is". That is an **error message**. It is not an insult, it is the cook telling you exactly where they got confused.

## The idea, step by step

### Python is a language and a program

The word "Python" means two things:

- A **programming language**: a set of words and rules to write instructions.
- A **program** installed on your computer, called the **interpreter**, that reads those instructions and runs them.

When you type `python` in the terminal, you are starting the interpreter.

### Your first file

Create a file called `hello.py` in your `Projects` folder, with this line:

```python
print("Hello, world!")
```

Output:

```text
Hello, world!
```

`print` is an instruction that shows something on the screen. The text goes inside parentheses and quotes.

The `.py` at the end of the name is the **extension**. It tells the computer (and your editor) that this is a Python file, the same way `.jpg` means a photo and `.txt` means plain text.

### Save, then run

Writing in the editor changes the file **only in the editor's memory** until you save it. In Cursor and VS Code, a white dot on the tab means "there are unsaved changes".

1. Save with **Ctrl + S** (Cmd + S on macOS).
2. In the terminal, go to the folder of the file.
3. Run it:

```powershell
PS C:\Users\ana\Projects> python hello.py
Hello, world!
```

If you forget to save, Python runs the **old** version of the file, and you will wonder why your change "did not work".

### Top to bottom, one line at a time

Python reads your file from the first line to the last, in order.

```python
print("First")
print("Second")
print("Third")
```

Output:

```text
First
Second
Third
```

Change the order of the lines, and the order of the output changes too.

### The interactive mode (REPL)

If you type `python` **without** a file name, Python opens its **interactive mode**, also called the **REPL** (Read, Evaluate, Print, Loop). It reads one line, runs it, shows the result, and waits for the next one.

```console
PS C:\Users\ana> python
Python 3.13.0 (main, Oct  7 2024, 05:02:14) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 3
5
>>> print("Hi")
Hi
>>> exit()
PS C:\Users\ana>
```

The `>>>` is Python's own prompt. It means "type a Python line".

| | REPL (`python`) | File (`python hello.py`) |
|---|---|---|
| Good for | Quick experiments, checking one thing | Real programs |
| Code is saved? | No, it disappears when you exit | Yes, it is in the file |
| How to leave | `exit()` or Ctrl + Z then Enter (Windows), Ctrl + D (macOS/Linux) | It ends by itself |

In this course you will mostly write **files**. Use the REPL as a scratch pad.

### Syntax: the grammar of Python

**Syntax** is the set of rules for how code must be written: where the parentheses go, where the quotes go, which words are special. Python is strict about it. A missing quote or parenthesis means Python cannot even start running your file.

```python
print("Coffee")
print("Tea")
```

Output:

```text
Coffee
Tea
```

Every opening `(` needs a closing `)`. Every opening `"` needs a closing `"`.

### Comments: notes for humans

A line that starts with `#` is a **comment**. Python ignores it completely. Comments are notes for you and for other people reading the code.

```python
# This program greets the user
print("Good morning!")  # a comment can also go at the end of a line
```

Output:

```text
Good morning!
```

The colors and italics your editor uses for comments are only there to help you read. They do not change what the code does.

### Reading an error message

When something is wrong, Python stops and shows an error. It looks scary, but it follows a pattern:

```text
Traceback (most recent call last):
  File "C:\Users\ana\Projects\hello.py", line 2, in <module>
    pront("Hello")
    ^^^^^
NameError: name 'pront' is not defined. Did you mean: 'print'?
```

Read it **from the bottom up**:

1. **Last line:** the type of error (`NameError`) and a description. Python even suggests the fix here: "Did you mean: 'print'?"
2. **Above it:** the line of code that caused the problem, with `^^^^^` pointing to the exact spot.
3. **Above that:** the file name and the **line number** (`line 2`).

Errors are information, not failure. Every programmer sees dozens of them every day.

## Common mistakes

### Forgetting to close the quotes

<!-- error -->
```python
print("Hello)
```

```text
SyntaxError: unterminated string literal (detected at line 1)
```

**Why:** the text started with `"` but never ended, so Python does not know where the text stops.

**Fix:** close the quotes.

```python
print("Hello")
```

```text
Hello
```

### Forgetting to close the parenthesis

<!-- error -->
```python
print("Hello"
```

```text
SyntaxError: '(' was never closed
```

**Why:** every `(` needs a matching `)`.

**Fix:** `print("Hello")`.

### A typo in a name

<!-- error -->
```python
pront("Hello")
```

```text
NameError: name 'pront' is not defined. Did you mean: 'print'?
```

**Why:** Python only knows the words it knows. `pront` means nothing to it.

**Fix:** read the suggestion in the last line, and write `print`.

### Capital letters

<!-- error -->
```python
Print("Hello")
```

```text
NameError: name 'Print' is not defined. Did you mean: 'print'?
```

**Why:** Python is **case sensitive**: `Print` and `print` are different names.

**Fix:** use lowercase, `print`.

### Running before saving

You change `print("Hello")` to `print("Goodbye")`, run the file, and still see `Hello`.

**Why:** the change was not saved. Look for the white dot on the editor tab.

**Fix:** Ctrl + S, then run again.

## Exercises

### Predict the output

#### Exercise 1: Order matters

What does this print?

```python
print("Lunch")
print("Breakfast")
print("Dinner")
```

<details>
<summary>Show answer</summary>

```text
Lunch
Breakfast
Dinner
```

Python runs the lines in the order they are written, not in the order that makes sense to us.

</details>

#### Exercise 2: Comments

What does this print?

```python
# print("one")
print("two")
# print("three")
print("four")
```

<details>
<summary>Show answer</summary>

```text
two
four
```

Lines starting with `#` are comments, so Python skips them.

</details>

#### Exercise 3: Reading an error

Look at this error:

```text
Traceback (most recent call last):
  File "C:\Users\ana\Projects\shop.py", line 4, in <module>
    prnt("Milk")
    ^^^^
NameError: name 'prnt' is not defined. Did you mean: 'print'?
```

Answer: in which file is the problem, on which line, and how do you fix it?

<details>
<summary>Show answer</summary>

- File: `shop.py`
- Line: 4
- Fix: change `prnt` to `print`.

Reading from the bottom up gives you everything you need.

</details>

### Fix the bug

#### Exercise 4: Three small problems

This file has three mistakes, one per line. Fix them.

<!-- no-verify -->
```python
print("Apples)
Print("Bananas")
print("Cherries"
```

<details>
<summary>Show answer</summary>

```python
print("Apples")
print("Bananas")
print("Cherries")
```

Output:

```text
Apples
Bananas
Cherries
```

Line 1 was missing the closing quote, line 2 had a capital `P`, line 3 was missing the closing parenthesis. Note: Python stops at the **first** error it finds, so you would see these errors one at a time.

</details>

### Write it

#### Exercise 5: About me

Create a file called `about_me.py` that prints three lines: your name, your city, and your favorite food. Add a comment at the top explaining what the program does. Then run it from the terminal.

<details>
<summary>Show answer</summary>

```python
# Prints a short introduction about me
print("My name is Ana")
print("I live in Lisbon")
print("I love pasta")
```

Output:

```text
My name is Ana
I live in Lisbon
I love pasta
```

To run it: save with Ctrl + S, go to the folder in the terminal, and type `python about_me.py`.

</details>

#### Exercise 6: REPL vs file

1. Open the REPL (type `python` alone) and calculate `7 * 6`. Then leave the REPL.
2. Create a file `multiply.py` with `print(7 * 6)` and run it.

What is the difference between what you had to type in each case?

<details>
<summary>Show answer</summary>

In the REPL:

```console
>>> 7 * 6
42
>>> exit()
```

In the file:

```python
print(7 * 6)
```

```text
42
```

The REPL shows the result of an expression automatically. In a file, nothing is shown unless you use `print`. Also, the REPL code is gone after `exit()`, while the file stays saved.

</details>

## Review

#### Review 1: From the terminal

You are in `C:\Users\ana` and your file `hello.py` is in `C:\Users\ana\Projects`. Write the two commands to run it.

<details>
<summary>Show answer</summary>

```powershell
cd Projects
python hello.py
```

See [terminal.md](terminal.md) if this was hard.

</details>

#### Review 2: Not recognized

You type `python hello.py` and the terminal says `The term 'python' is not recognized`. Is the problem in your file?

<details>
<summary>Show answer</summary>

No. The terminal cannot find the Python program itself. The problem is the **PATH**. Your file was never even opened.

</details>

## Recap

- Python is a **language** and also a **program** (the interpreter) that runs `.py` files.
- **Writing is not running.** Save with Ctrl + S, then run with `python file.py`.
- Python reads the file **top to bottom**, one line at a time.
- `python` alone opens the **REPL** (`>>>`), good for quick experiments. Leave with `exit()`.
- Read errors **from the bottom up**: error type, the line of code, the line number.

**Next:** [software-engineering.md](software-engineering.md)
