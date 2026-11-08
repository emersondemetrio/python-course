# Teacher's guide: Module 00, The workbench
# Every example and exercise answer from this module's lessons, in order.
# Run it from this folder:  python guide.py
#
# Most of this module happens in the terminal, not in Python.
# Terminal commands are shown as comments: type them in the terminal with her.

print("=" * 50)
print("LESSON: terminal.md")

# The whole lesson is terminal practice. Do it live in PowerShell.
#
# Paths:
#   C:\Users\ana\Projects\hello.py        (Windows)
#   /Users/ana/Projects/hello.py          (macOS)
#
# Commands, in the order of the lesson:
#   pwd              where am I?
#   ls               what is in here?
#   cd Projects      go into a folder
#   cd ..            go up one level
#   cd .             "right here" (changes nothing)
#   Tab              completes folder and file names
#   clear / Ctrl+L   clears the screen
#   history          shows past commands
#   echo "Hi"        shows text (like print in Python)
#   cat notes.txt    shows the content of a file
#   python hello.py  runs a Python file
#
# PATH: the list of folders where the terminal looks for programs.
# "The term 'python' is not recognized" means Python is not in the PATH.

print("\n--- Exercise 1: Where am I?")
# Starting at C:\Users\ana:  cd Projects / cd course / cd .. / pwd
# Ask her to say the answer before you show it.
print(r"C:\Users\ana\Projects")

print("\n--- Exercise 2: Up, up, up")
# From C:\Users\ana\Projects\course\week1, run:  cd ..\..
print(r"C:\Users\ana\Projects")

print("\n--- Exercise 3: The dot")
# From C:\Users\ana\Projects, run:  cd .  then  pwd
print(r"C:\Users\ana\Projects")

print("\n--- Exercise 4: The file that does not exist")
# PS C:\Users\ana> python hello.py   -> No such file or directory
# Fix: go to the folder where the file is first.
#   cd Projects
#   python hello.py

print("\n--- Exercise 5: Two words")
# cd python course   fails because of the space.
#   1. cd "python course"
#   2. Better: rename the folder to python-course and run  cd python-course

print("\n--- Exercise 6: A full trip")
#   pwd
#   ls
#   cd Projects
#   cat notes.txt
#   cd ..

print("\n--- Exercise 7: Practice on your own computer")
# Let her do it without looking:
#   pwd
#   cd Doc        (press Tab: it becomes cd .\Documents\)
#   cd ..
#   clear         (or Ctrl + L)
#   history

print()
print("=" * 50)
print("LESSON: python.md")

print("\n--- Example: Your first file")
print("Hello, world!")

print("\n--- Example: Top to bottom, one line at a time")
# Python runs one line after the other, in order.
print("First")
print("Second")
print("Third")

print("\n--- Example: Syntax")
print("Coffee")
print("Tea")

print("\n--- Example: Comments")
# This program greets the user
print("Good morning!")  # a comment can also go at the end of a line

print("\n--- Example: Reading an error message")
# Read the error from the bottom up:
#   Traceback (most recent call last):
#     File "C:\Users\ana\Projects\hello.py", line 2, in <module>
#       pront("Hello")
#       ^^^^^
#   NameError: name 'pront' is not defined. Did you mean: 'print'?
# Last line: WHAT went wrong. "line 2": WHERE.

print("\n--- Mistake: Forgetting to close the quotes")
# print("Hello)
# SyntaxError: unterminated string literal (detected at line 1)
print("Hello")

print("\n--- Mistake: Forgetting to close the parenthesis")
# print("Hello"
# SyntaxError: '(' was never closed
print("Hello")

print("\n--- Mistake: A typo in a name")
# pront("Hello")
# NameError: name 'pront' is not defined. Did you mean: 'print'?
print("Hello")

print("\n--- Mistake: Capital letters")
# Print("Hello")
# NameError: name 'Print' is not defined. Did you mean: 'print'?
print("Hello")

print("\n--- Mistake: Running before saving")
# The white dot on the editor tab means "not saved".
# Python runs what is saved on disk, not what is on the screen. Ctrl + S first.

print("\n--- Exercise 1: Order matters")
# Ask her to predict before running.
print("Lunch")
print("Breakfast")
print("Dinner")

print("\n--- Exercise 2: Comments")
# Ask her to predict before running: comment lines do not run.
# print("one")
print("two")
# print("three")
print("four")

print("\n--- Exercise 3: Reading an error")
# NameError: name 'prnt' is not defined. Did you mean: 'print'?   (line 4)
# Answer: line 4 has a typo, prnt instead of print.

print("\n--- Exercise 4: Three small problems")
# Broken version:
#   print("Apples)
#   Print("Bananas")
#   print("Cherries"
print("Apples")
print("Bananas")
print("Cherries")

print("\n--- Exercise 5: About me")
# Prints a short introduction about me
print("My name is Ana")
print("I live in Lisbon")
print("I love pasta")

print("\n--- Exercise 6: REPL vs file")
# In the REPL, typing 7 * 6 shows 42 by itself.
# In a file, you need print to see it.
print(7 * 6)

print("\n--- Review 1: From the terminal")
#   cd Projects
#   python hello.py

print("\n--- Review 2: Not recognized")
# "The term 'python' is not recognized": the problem is the PATH, not the file.

print()
print("=" * 50)
print("LESSON: software-engineering.md")

# All projects live in one place:
#   C:\Users\ana\Projects        (Windows)
#   /Users/ana/Projects          (macOS)
# Names: lowercase, no spaces, no accents, no special characters.
# Open the editor from the terminal:  cursor .   (the dot is "this folder")

print("\n--- Exercise 1: Good name or bad name?")
print("shopping_list.py   OK")
print("Minhas Receitas    space and capitals  -> recipes")
print("café.py            accent              -> coffee.py")
print("class-03           OK")
print("2nd try.py         space, starts with a number -> second_try.py")

print("\n--- Exercise 2: What does cursor . open?")
print(r"C:\Users\ana\Projects\python-course\class-02")

print("\n--- Exercise 3: Markdown preview")
# # Groceries / - eggs / - **milk**
# A big title "Groceries", then a list: eggs (normal) and milk (bold).

print("\n--- Exercise 4: The messy folder")
# Before:                     After:
# Projects/                   Projects/
# ├── Aula 1/                 ├── class-01/
# │   └── Olá Mundo.py        │   └── hello_world.py
# └── anotações python.md     └── notes/
#                                 └── python.md

print("\n--- Exercise 5: Set up your workbench")
#   cd ~
#   mkdir Projects
#   cd Projects
#   mkdir python-course
#   cd python-course
#   mkdir notes
#   cursor .

print("\n--- Exercise 6: Your first notes file")
# notes/terminal.md, in her own words. Check it with the Markdown preview.

print("\n--- Review 1: Where does cd .. take you?")
# From C:\Users\ana\Projects\python-course\notes:  cd ..\..

print("\n--- Review 2: White dot")
# She did not save. Ctrl + S, then run again.
