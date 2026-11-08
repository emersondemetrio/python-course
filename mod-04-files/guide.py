# Teacher's guide: Module 04, Files
# Every example and exercise answer from this module's lessons, in order.
# Run it from this folder:  python guide.py
# ruff: noqa: UP015

import os

print("=" * 50)
print("LESSON: files.md")

print("\n--- Example: a file name is just a string")
# This line does NOT open, create or read anything. It is the name on the cover.
file_name = "shopping.txt"
print(file_name)

print("\n--- Example: creating a file with open and mode w")
# Read the line slowly with her: open, mode, encoding, "as file", the indented block.
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("milk\n")
    file.write("eggs\n")
    file.write("bread\n")

print("Saved!")

print("\n--- Example: reading the whole file with read()")
# Point at the parentheses in read(). They are what makes it run.
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("milk\n")
    file.write("eggs\n")

with open("shopping.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)

print("\n--- Example: opening is not reading")
# Ask her to predict: will this print "milk"? It prints a description of the open file.
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("milk\n")

with open("shopping.txt", "r", encoding="utf-8") as file:
    print(file)

print("\n--- Example: forgetting the parentheses on read")
# The number at the end changes every run. file.read is the method, file.read() runs it.
with open("shopping.txt", "r", encoding="utf-8") as file:
    print(file.read)

print("\n--- Example: write does not add line breaks")
# Ask her to predict before running: the words get glued together.
with open("colors.txt", "w", encoding="utf-8") as file:
    file.write("red")
    file.write("green")
    file.write("blue")

with open("colors.txt", "r", encoding="utf-8") as file:
    print(file.read())

print("\n--- Example: adding \\n at the end of each line")
with open("colors.txt", "w", encoding="utf-8") as file:
    file.write("red\n")
    file.write("green\n")
    file.write("blue\n")

with open("colors.txt", "r", encoding="utf-8") as file:
    print(file.read())

print("\n--- Example: adding without erasing, mode a")
with open("diary.txt", "w", encoding="utf-8") as file:
    file.write("Monday: rain\n")

with open("diary.txt", "a", encoding="utf-8") as file:
    file.write("Tuesday: sun\n")

with open("diary.txt", "a", encoding="utf-8") as file:
    file.write("Wednesday: wind\n")

with open("diary.txt", "r", encoding="utf-8") as file:
    print(file.read())

print("\n--- Example: what mode w does to the same file")
# Ask her what happens to Monday and Tuesday. "w" erases first, then writes.
with open("diary.txt", "w", encoding="utf-8") as file:
    file.write("Monday: rain\n")
    file.write("Tuesday: sun\n")

with open("diary.txt", "w", encoding="utf-8") as file:
    file.write("Wednesday: wind\n")

with open("diary.txt", "r", encoding="utf-8") as file:
    print(file.read())

print("\n--- Example: splitlines() gives a list without \\n")
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("milk\neggs\nbread\n")

with open("shopping.txt", "r", encoding="utf-8") as file:
    lines = file.read().splitlines()

print(lines)

print("\n--- Example: readlines() keeps the \\n")
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("milk\neggs\nbread\n")

with open("shopping.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)

print("\n--- Example: a for loop directly on the file, with strip()")
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("milk\neggs\nbread\n")

with open("shopping.txt", "r", encoding="utf-8") as file:
    for line in file:
        print("-", line.strip())

print("\n--- Example: numbered list with read().splitlines()")
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("milk\neggs\nbread\n")

with open("shopping.txt", "r", encoding="utf-8") as file:
    items = file.read().splitlines()

for number, item in enumerate(items, start=1):
    print(f"{number}. {item}")

print(f"Total: {len(items)} items")

print("\n--- Example: functions that use files")
# The file name is a PARAMETER, so the same function works for any file.


def write_line(file_name, text):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(text + "\n")


def read_lines(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read().splitlines()


write_line("movies.txt", "Spirited Away")
write_line("movies.txt", "Amélie")
print(read_lines("movies.txt"))

print("\n--- Example: when the file does not exist")
# Mode "r" needs the file to exist. This would crash, so it is not run here:
# with open("recipes.txt", "r", encoding="utf-8") as file:
#     print(file.read())
# FileNotFoundError: [Errno 2] No such file or directory: 'recipes.txt'
#
# The trick: open it in "a" mode first. It creates the file without erasing anything.
with open("recipes.txt", "a", encoding="utf-8") as file:
    file.write("")

with open("recipes.txt", "r", encoding="utf-8") as file:
    print(repr(file.read()))

print("\n--- Example: where is the file? (terminal, not Python)")
# PS C:\Users\you\Projects> python lists\shopping.py
#   -> shopping.txt is created in Projects, not in Projects\lists.
# Always cd into the program's folder first:
# PS C:\Users\you\Projects> cd lists
# PS C:\Users\you\Projects\lists> python shopping.py
# Use pwd to check where you are and ls to see if the file was created.
print("(terminal commands: see the comments in guide.py)")

print("\n--- Mistake: forgetting the parentheses on read")
# content = file.read     -> prints <built-in method read of ...>, no error, no text.
with open("shopping.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)

print("\n--- Mistake: using w when you meant a")
# No error message: the old content silently disappears. Use "a" for a growing list.
print("(no code: explain it with the diary example above)")

print("\n--- Mistake: lines glued together")
# file.write(note)          -> buy milkcall grandmapay rent
# file.write(note + "\n")   -> one note per line
with open("colors.txt", "w", encoding="utf-8") as file:
    for note in ["buy milk", "call grandma", "pay rent"]:
        file.write(note + "\n")
with open("colors.txt", "r", encoding="utf-8") as file:
    print(file.read())

print("\n--- Mistake: reading a file that does not exist")
# with open("notes.txt", "r", encoding="utf-8") as file:
#     print(file.read())
# FileNotFoundError: [Errno 2] No such file or directory: 'notes.txt'
# Fix: check with ls and pwd. Or open it with "a" before reading.
print("(not run: it would crash)")

print("\n--- Mistake: using a file outside the with block")
# with open("shopping.txt", "w", encoding="utf-8") as file:
#     file.write("milk\n")
#
# file.write("eggs\n")
# ValueError: I/O operation on closed file.
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("milk\n")
    file.write("eggs\n")
print("Fixed: both lines are inside the block.")

print("\n--- Mistake: writing a number")
# with open("scores.txt", "w", encoding="utf-8") as file:
#     file.write(42)
# TypeError: write() argument must be str, not int
with open("scores.txt", "w", encoding="utf-8") as file:
    file.write(str(42) + "\n")
with open("scores.txt", "r", encoding="utf-8") as file:
    print(file.read())

print("\n--- Exercise 1: write then read")
# Ask her to predict before running.
with open("pets.txt", "w", encoding="utf-8") as file:
    file.write("cat\n")
    file.write("dog\n")

with open("pets.txt", "r", encoding="utf-8") as file:
    print(file.read())

print("\n--- Exercise 2: write twice")
# Ask her to predict before running. The second "w" erases the cat.
with open("pets.txt", "w", encoding="utf-8") as file:
    file.write("cat\n")

with open("pets.txt", "w", encoding="utf-8") as file:
    file.write("fish\n")

with open("pets.txt", "r", encoding="utf-8") as file:
    print(file.read())

print("\n--- Exercise 3: append")
# Ask her to predict before running.
with open("pets.txt", "w", encoding="utf-8") as file:
    file.write("cat\n")

with open("pets.txt", "a", encoding="utf-8") as file:
    file.write("fish\n")

with open("pets.txt", "r", encoding="utf-8") as file:
    lines = file.read().splitlines()

print(len(lines))
print(lines[-1])

print("\n--- Exercise 4: no line breaks")
# Ask her to predict before running.
with open("word.txt", "w", encoding="utf-8") as file:
    for letter in ["s", "u", "n"]:
        file.write(letter)

with open("word.txt", "r", encoding="utf-8") as file:
    print(file.read())

print("\n--- Exercise 5: the list that never grows (fixed)")
# The bug was mode "w". The fix is mode "a".


def add_book(title):
    with open("books.txt", "a", encoding="utf-8") as file:
        file.write(title + "\n")


add_book("Dom Casmurro")
add_book("The Hobbit")

with open("books.txt", "r", encoding="utf-8") as file:
    print(file.read())

print("\n--- Exercise 6: empty lines everywhere (fixed)")
# The bug was print(line). Each line still has its \n, and print adds another.
with open("shopping.txt", "w", encoding="utf-8") as file:
    file.write("rice\nbeans\n")

with open("shopping.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

print("\n--- Exercise 7: the text that never appears (fixed)")
# The bug was print(file). file is the open file, file.read() is its text.
with open("greeting.txt", "w", encoding="utf-8") as file:
    file.write("Good morning!\n")

with open("greeting.txt", "r", encoding="utf-8") as file:
    print(file.read())

print("\n--- Exercise 8: your favorite foods")
with open("foods.txt", "w", encoding="utf-8") as file:
    file.write("feijoada\n")
    file.write("lasagna\n")
    file.write("açaí\n")

with open("foods.txt", "r", encoding="utf-8") as file:
    foods = file.read().splitlines()

for number, food in enumerate(foods, start=1):
    print(f"{number}. {food}")

print("\n--- Exercise 9: save a whole list")
# Open the file once, then loop INSIDE the with block.


def save_list(file_name, items):
    with open(file_name, "w", encoding="utf-8") as file:
        for item in items:
            file.write(item + "\n")


plants = ["fern", "cactus", "basil", "orchid"]
save_list("plants.txt", plants)

with open("plants.txt", "r", encoding="utf-8") as file:
    lines = file.read().splitlines()

print(f"The file has {len(lines)} lines.")

print("\n--- Exercise 10: count matching lines")


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

print("\n--- Review 1: f-strings (module 01)")
# Ask her to predict before running.
item = "coffee"
price = 12.5
print(f"One {item} costs R$ {price}")

print("\n--- Review 2: return vs print (module 03)")
# Ask her to predict before running. Pay attention to what the function RETURNS.


def double(number):
    print("Calculating...")
    return number * 2


result = double(4)
print(result + 1)

print("\n--- Review 3: lists and for (module 02)")
fruits = ["kiwi", "mango", "fig", "banana"]
for fruit in fruits:
    if len(fruit) > 4:
        print(fruit)

# Clean up the files this lesson created.
for name in [
    "shopping.txt",
    "colors.txt",
    "diary.txt",
    "movies.txt",
    "recipes.txt",
    "scores.txt",
    "pets.txt",
    "word.txt",
    "books.txt",
    "greeting.txt",
    "foods.txt",
    "plants.txt",
    "tasks.txt",
]:
    os.remove(name)


print()
print("=" * 50)
print("LESSON: project-notebook.md")

# Terminal setup (not Python):
# cd ~\Projects
# mkdir notes
# cd notes
# cursor .

print("\n--- Step 1: a constant for the file name")
# CAPITALS mean "constant": set once, never changed. It does not create anything yet.
NOTES_FILE = "notes.txt"
print(NOTES_FILE)

print("\n--- Step 2: a function that saves one note")
# "a" so the list grows. + "\n" puts each note on its own line.


def save_note(file_name, note):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(note + "\n")


save_note("notes.txt", "buy coffee")
save_note("notes.txt", "call the dentist")

with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.read())

os.remove("notes.txt")

print("\n--- Step 3: a function that reads all notes")
# The first with creates the file if it is missing. The function RETURNS, it does not print.


def read_notes(file_name):
    with open(file_name, "a", encoding="utf-8") as file:
        file.write("")
    with open(file_name, "r", encoding="utf-8") as file:
        return file.read().splitlines()


print(read_notes("notes.txt"))
save_note("notes.txt", "buy coffee")
print(read_notes("notes.txt"))

os.remove("notes.txt")

print("\n--- Step 4: a function that shows the notes")
# It receives a LIST, not a file name, and only prints.


def show_notes(notes):
    print("Your notes:")
    for number, note in enumerate(notes, start=1):
        print(f"{number}. {note}")


show_notes(["buy coffee", "call the dentist", "water the plants"])

print("\n--- Step 5: a function that asks for a note")
# In the lesson:
# def ask_note():
#     return input("Write a note: ")
# Here the typed text is fixed so the guide runs by itself.


def ask_note():
    # return input("Write a note: ")
    return "buy coffee"


print(ask_note())

print("\n--- Step 6: main(), the head chef")
# Read main() aloud: ask, save, read, show. The last line is the CALL.


def main():
    note = ask_note()
    save_note(NOTES_FILE, note)
    notes = read_notes(NOTES_FILE)
    show_notes(notes)


main()

print("\n--- The complete program, run a second time")
# Running it again: the note from the first run is still there.


def ask_note():
    # return input("Write a note: ")
    return "call the dentist"


main()

os.remove("notes.txt")

print("\n--- Parameter or argument?")
# In def save_note(file_name, note), file_name is a PARAMETER.
# In save_note(NOTES_FILE, note), NOTES_FILE is an ARGUMENT. Same value at that moment.
print("Parameter: file_name. Argument:", NOTES_FILE)

print("\n--- Mistake: defining but never calling main()")
# def main():
#     note = ask_note()
#     save_note(NOTES_FILE, note)
# Nothing happens when you run it. Fix: add main() at the end, without indentation.
print("(no output: that is the problem)")

print("\n--- Mistake: calling a function before it is defined")
# main()
#
#
# def main():
#     print("Hello")
# NameError: name 'main' is not defined. Did you mean: 'min'?
# Python reads top to bottom. Fix: all the defs first, main() at the very end.
print("(not run: it would crash)")

print("\n--- Mistake: forgetting to save the file before running")
# The old behavior appears. Look for the dot on the editor tab. Ctrl+S, then run.
print("(no code)")

print("\n--- Mistake: printing instead of returning")
# def read_notes(file_name):
#     with open(file_name, "r", encoding="utf-8") as file:
#         print(file.read().splitlines())
#
# notes = read_notes(NOTES_FILE)   -> notes is None
# show_notes(None)
# TypeError: 'NoneType' object is not iterable
# Fix: return the list, and let show_notes do the printing.
print("(not run: it would crash)")

print("\n--- Exercise 1: what gets saved?")
# Ask her to predict before running. notes.txt does not exist at the start.
save_note("notes.txt", "pay rent")
save_note("notes.txt", "buy bread")
notes = read_notes("notes.txt")
print(len(notes))
print(notes[0])

os.remove("notes.txt")

print("\n--- Exercise 2: the notebook with amnesia")
# The bug: "a" was changed to "w". "w" erases the file every time. Change it back to "a".
print('The mode changed from "a" to "w". Fix: use "a".')

print("\n--- Exercise 3: show the count")
# The count line is AFTER the loop, not inside it.


def show_notes(notes):
    print("Your notes:")
    for number, note in enumerate(notes, start=1):
        print(f"{number}. {note}")
    print(f"You have {len(notes)} notes.")


show_notes(["buy coffee", "call the dentist"])

print("\n--- Exercise 4: ignore empty notes")
# The decision lives in main(). save_note stays simple.
# (Back to the show_notes without the count line, as in the lesson.)


def show_notes(notes):
    print("Your notes:")
    for number, note in enumerate(notes, start=1):
        print(f"{number}. {note}")


save_note(NOTES_FILE, "buy coffee")


def ask_note():
    # return input("Write a note: ")
    print("Write a note: ")
    return "   "


def main():
    note = ask_note()
    if note.strip() == "":
        print("Empty note, nothing saved.")
    else:
        save_note(NOTES_FILE, note)
    notes = read_notes(NOTES_FILE)
    show_notes(notes)


main()

os.remove("notes.txt")

print("\n--- Exercise 5: a menu that keeps going (challenge)")
# input always returns a string: compare with "1", not 1.
# The choices below simulate a person typing 1, then 2, then 0.
choices = ["1", "2", "0"]


def show_menu():
    print("1) Add a note")
    print("2) Show notes")
    print("0) Exit")


def ask_note():
    # return input("Write a note: ")
    print("Write a note: buy coffee")
    return "buy coffee"


def main():
    while True:
        show_menu()
        # choice = input("Choose: ")
        choice = choices.pop(0)
        print("Choose:", choice)
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

os.remove("notes.txt")

print("\n--- Review 1: parameter or argument? (module 03)")
# name and time_of_day are parameters. "Ana" and "evening" are arguments.


def greet(name, time_of_day):
    print(f"Good {time_of_day}, {name}!")


greet("Ana", "evening")

print("\n--- Review 2: concatenation vs interpolation (module 01)")
# Ask her which line crashes. The third one is not run here:
# print("You have " + count + " notes")
# TypeError: can only concatenate str (not "int") to str
count = 3
print(f"You have {count} notes")
print("You have " + str(count) + " notes")
