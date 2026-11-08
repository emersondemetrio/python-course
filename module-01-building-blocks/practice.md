# Practice set: classes 1 to 3

> **In one sentence:** small, step-by-step exercises to make what you already saw in class stick: interpolation, functions, lists and `for` loops.

## How to use this file

You have already met everything here in class. Lists and loops get their full lessons in module 02, and functions in module 03. This file is **review and practice**, not new material.

- Go in order. The exercises get a little harder each time.
- For **Predict the output**, write your answer on paper (or in your notes) **before** running anything. This is the best test of whether you really understand.
- For the other exercises, write the code in a file inside your `Projects` folder, save with `Ctrl+S`, and run it with `python file.py`.
- Open the **Hint** only if you are stuck for more than a few minutes. Open the **Answer** only after trying.
- If an answer surprises you, do not just read it: type it, run it, and change something to see what happens.

---

## Part 1: Interpolation (f-strings)

#### Exercise 1: Fill the blank (predict the output)

```python
plant = "basil"
print(f"I water the {plant} every day.")
```

<details>
<summary>Show answer</summary>

```text
I water the basil every day.
```

</details>

#### Exercise 2: Where is the f? (predict the output)

```python
book = "Dom Casmurro"
print("Reading {book}")
print(f"Reading {book}")
```

<details>
<summary>Show answer</summary>

```text
Reading {book}
Reading Dom Casmurro
```

Without the `f`, `{book}` is just characters, not the variable.

</details>

#### Exercise 3: Math in the braces (predict the output)

```python
price = 5
print(f"Two coffees cost {price * 2} reais")
print(f"Two coffees cost {price} * 2 reais")
```

<details>
<summary>Show answer</summary>

```text
Two coffees cost 10 reais
Two coffees cost 5 * 2 reais
```

Only what is inside `{}` is calculated.

</details>

#### Exercise 4: From + to f-string (write it)

Rewrite this line using an f-string, so it does not need `str()`:

<!-- no-verify -->
```python
print("You have " + str(3) + " new messages")
```

<details>
<summary>Show answer</summary>

```python
messages = 3
print(f"You have {messages} new messages")
```

```text
You have 3 new messages
```

</details>

#### Exercise 5: A short introduction (write it)

Create three variables: `name`, `city` and `age` (use your own data). Print one sentence with all three, using a single f-string. Example:

```text
My name is Ana, I live in Lisbon and I am 39 years old.
```

<details>
<summary>Show answer</summary>

```python
name = "Ana"
city = "Lisbon"
age = 39
print(f"My name is {name}, I live in {city} and I am {age} years old.")
```

```text
My name is Ana, I live in Lisbon and I am 39 years old.
```

</details>

---

## Part 2: Functions

Remember the two moments of a function:

- **Defining** (`def name(parameter):`) writes the recipe down. Nothing runs yet.
- **Calling** (`name(argument)`) cooks the recipe.

The name in the definition is a **parameter**. The value you pass in the call is an **argument**.

#### Exercise 6: Defined but never called (predict the output)

```python
def say_hello():
    print("Hello!")

print("Start")
print("End")
```

<details>
<summary>Show answer</summary>

```text
Start
End
```

`say_hello` was defined, but nobody called it, so `Hello!` never appears.

</details>

#### Exercise 7: Called twice (predict the output)

```python
def say_hello():
    print("Hello!")

print("Start")
say_hello()
say_hello()
print("End")
```

<details>
<summary>Show answer</summary>

```text
Start
Hello!
Hello!
End
```

Each call runs the function's code once, at the moment of the call.

</details>

#### Exercise 8: Parameter and argument (predict the output)

```python
def greet(person):
    print(f"Good evening, {person}")

greet("Marta")
greet("Joel")
```

<details>
<summary>Show answer</summary>

```text
Good evening, Marta
Good evening, Joel
```

`person` is the parameter. In the first call it receives the argument `"Marta"`; in the second, `"Joel"`.

</details>

#### Exercise 9: Outside name, inside name (predict the output)

```python
def show_file_name(name):
    print(f"File: {name}")

file_name = "notes.txt"
show_file_name(file_name)
```

<details>
<summary>Hint</summary>

When the function is called, the parameter `name` receives whatever value `file_name` holds.

</details>

<details>
<summary>Show answer</summary>

```text
File: notes.txt
```

`file_name` (outside) and `name` (inside) are two different names, but at the moment of the call they hold the same value. Also note: `"notes.txt"` is only **text with a file name**. Nothing was opened.

</details>

#### Exercise 10: return versus print (predict the output)

```python
def double_print(n):
    print(n * 2)

def double_return(n):
    return n * 2

double_print(4)
double_return(4)
result = double_return(4)
print(result)
```

<details>
<summary>Show answer</summary>

```text
8
8
```

- `double_print(4)` shows `8` itself.
- `double_return(4)` gives `8` back, but nobody uses it, so nothing appears.
- `result = double_return(4)` stores the `8`, and `print(result)` shows it.

`print` **shows**, `return` **hands back**.

</details>

#### Exercise 11: Your first function (write it)

Write a function `welcome(name)` that **prints** `Welcome, <name>!`. Call it three times with three different names.

<details>
<summary>Show answer</summary>

```python
def welcome(name):
    print(f"Welcome, {name}!")

welcome("Ana")
welcome("Rui")
welcome("Lia")
```

```text
Welcome, Ana!
Welcome, Rui!
Welcome, Lia!
```

</details>

#### Exercise 12: A function that returns (write it)

Write a function `total_price(price, quantity)` that **returns** the price times the quantity. Then use it to print:

```text
Total: 15
```

<details>
<summary>Hint</summary>

Inside the function, use `return`, not `print`. Then call it and put the result inside an f-string.

</details>

<details>
<summary>Show answer</summary>

```python
def total_price(price, quantity):
    return price * quantity

total = total_price(5, 3)
print(f"Total: {total}")
```

```text
Total: 15
```

You could also call it directly inside the braces: `print(f"Total: {total_price(5, 3)}")`.

</details>

#### Exercise 13: From print to return (fix it)

This function prints the greeting, but we want to **store** it in a variable and use it later. Change it so it returns the text, and print the variable at the end.

<!-- no-verify -->
```python
def make_greeting(name):
    print(f"Hi, {name}!")

message = make_greeting("Bia")
print(message)
```

Right now it prints `Hi, Bia!` and then `None`. Why `None`?

<details>
<summary>Show answer</summary>

A function without `return` gives back `None` ("nothing"). So `message` received `None`.

```python
def make_greeting(name):
    return f"Hi, {name}!"

message = make_greeting("Bia")
print(message)
```

```text
Hi, Bia!
```

</details>

---

## Part 3: Lists

#### Exercise 14: Counting starts at 0 (predict the output)

```python
fruits = ["apple", "banana", "grape"]
print(fruits[0])
print(fruits[2])
```

<details>
<summary>Show answer</summary>

```text
apple
grape
```

Positions (indexes) start at `0`. The third item is at position `2`.

</details>

#### Exercise 15: How many? (predict the output)

```python
fruits = ["apple", "banana", "grape"]
fruits.append("mango")
print(len(fruits))
print(fruits)
```

<details>
<summary>Show answer</summary>

```text
4
['apple', 'banana', 'grape', 'mango']
```

`.append()` adds an item at the end.

</details>

#### Exercise 16: Out of range (fix it)

This crashes with `IndexError: list index out of range`. Why? Fix it so it prints the last item.

<!-- error -->
```python
days = ["mon", "tue", "wed"]
print(days[3])
```

```text
IndexError: list index out of range
```

<details>
<summary>Show answer</summary>

The list has 3 items, at positions `0`, `1` and `2`. There is no position `3`.

```python
days = ["mon", "tue", "wed"]
print(days[2])
```

```text
wed
```

</details>

#### Exercise 17: Build a list (write it)

Create an empty list called `shopping`, add `"rice"`, `"beans"` and `"coffee"` with `.append()`, and print the list and its size.

<details>
<summary>Show answer</summary>

```python
shopping = []
shopping.append("rice")
shopping.append("beans")
shopping.append("coffee")
print(shopping)
print(len(shopping))
```

```text
['rice', 'beans', 'coffee']
3
```

</details>

---

## Part 4: for loops

#### Exercise 18: One item per turn (predict the output)

```python
pets = ["cat", "dog", "fish"]
for pet in pets:
    print(f"I have a {pet}")
```

<details>
<summary>Show answer</summary>

```text
I have a cat
I have a dog
I have a fish
```

In each turn of the loop, `pet` holds the next item of the list.

</details>

#### Exercise 19: What is inside the loop? (predict the output)

```python
for pet in ["cat", "dog"]:
    print(pet)
print("done")
```

<details>
<summary>Show answer</summary>

```text
cat
dog
done
```

`print("done")` is not indented, so it is outside the loop and runs only once, at the end.

</details>

#### Exercise 20: enumerate from 0 and from 1 (predict the output)

```python
songs = ["intro", "chorus"]
for i, song in enumerate(songs):
    print(i, song)
for i, song in enumerate(songs, start=1):
    print(i, song)
```

<details>
<summary>Show answer</summary>

```text
0 intro
1 chorus
1 intro
2 chorus
```

</details>

#### Exercise 21: Looping over a word (write it)

Print each letter of the word `"python"` on its own line.

<details>
<summary>Show answer</summary>

```python
for letter in "python":
    print(letter)
```

```text
p
y
t
h
o
n
```

</details>

#### Exercise 22: Counting with a loop (write it)

Given `prices = [10, 25, 5, 40]`, use a `for` loop to add all the prices into a variable `total`, and print `Total: 80`.

<details>
<summary>Hint</summary>

Start with `total = 0` **before** the loop. Inside the loop, do `total = total + price`.

</details>

<details>
<summary>Show answer</summary>

```python
prices = [10, 25, 5, 40]
total = 0
for price in prices:
    total = total + price
print(f"Total: {total}")
```

```text
Total: 80
```

The `print` is outside the loop, so it shows only the final total.

</details>

---

## Part 5: Putting it together

#### Exercise 23: Shopping list printer (write it)

Write a function `print_list(items)` that receives a list and prints each item numbered from 1. Call it with `["milk", "eggs", "bread"]`.

```text
1. milk
2. eggs
3. bread
```

<details>
<summary>Show answer</summary>

```python
def print_list(items):
    for number, item in enumerate(items, start=1):
        print(f"{number}. {item}")

print_list(["milk", "eggs", "bread"])
```

```text
1. milk
2. eggs
3. bread
```

</details>

#### Exercise 24: Greetings for everyone (write it)

Write a function `make_greeting(name)` that **returns** `"Hello, <name>!"`. Then loop over the list `["Ana", "Rui", "Lia"]` and print the greeting for each person.

<details>
<summary>Show answer</summary>

```python
def make_greeting(name):
    return f"Hello, {name}!"

for person in ["Ana", "Rui", "Lia"]:
    print(make_greeting(person))
```

```text
Hello, Ana!
Hello, Rui!
Hello, Lia!
```

</details>

#### Exercise 25: Longest word (write it)

Given `words = ["sun", "ocean", "sky"]`, print each word with its length, like `sun: 3`. Then print the total number of letters.

<details>
<summary>Show answer</summary>

```python
words = ["sun", "ocean", "sky"]
total = 0
for word in words:
    print(f"{word}: {len(word)}")
    total = total + len(word)
print(f"Total letters: {total}")
```

```text
sun: 3
ocean: 5
sky: 3
Total letters: 11
```

</details>

#### Exercise 26: Notes from a file (write it)

Create a file called `notes.txt` next to your script, with three lines:

```text
buy coffee
call the dentist
water the plants
```

Write a program that reads the file and prints the notes numbered from 1:

```console
PS C:\Users\you\Projects> python notes.py
1. buy coffee
2. call the dentist
3. water the plants
```

<details>
<summary>Hint</summary>

Open with `with open("notes.txt", "r") as file:` and read with `file.read()` (with parentheses!). Then `.splitlines()` turns the text into a list with one item per line. After that, it is the same as Exercise 23.

</details>

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
with open("notes.txt", "r") as file:
    content = file.read()

notes = content.splitlines()
for number, note in enumerate(notes, start=1):
    print(f"{number}. {note}")
```

Remember: `"notes.txt"` is just text with the file's name. `open()` opens the file, and `read()` gets what is inside it.

</details>

#### Exercise 27: Add a note, then show all (write it)

Extend Exercise 26 with two functions:

- `add_note(file_name, note)`: appends the note as a new line at the end of the file.
- `show_notes(file_name)`: prints all notes numbered from 1.

Then ask the user for a new note with `input()`, add it, and show all notes.

```console
PS C:\Users\you\Projects> python notes.py
New note: pay the rent
1. buy coffee
2. call the dentist
3. water the plants
4. pay the rent
```

<details>
<summary>Hint</summary>

To add without erasing, open the file with mode `"a"` (append) and write `note + "\n"` so each note ends with a new line.

</details>

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
def add_note(file_name, note):
    with open(file_name, "a") as file:
        file.write(note + "\n")

def show_notes(file_name):
    with open(file_name, "r") as file:
        notes = file.read().splitlines()
    for number, note in enumerate(notes, start=1):
        print(f"{number}. {note}")

notes_file = "notes.txt"
new_note = input("New note: ")
add_note(notes_file, new_note)
show_notes(notes_file)
```

Notice how the last three lines tell the whole story of the program: which file, ask, add, show. The details live inside the functions.

</details>

---

## Recap

- f-strings fill values into text: `f"Total: {price * 2}"`. No `f`, no filling.
- Defining a function writes the recipe; calling it (`name()`) runs it.
- Parameters are the names in the definition; arguments are the values in the call.
- `print` shows a value; `return` hands it back so you can store and reuse it.
- List positions start at 0, and `for` visits one item per turn; `enumerate(..., start=1)` numbers them for people.

**Next:** [Module 02: Decisions and loops](../module-02-decisions-and-loops/README.md)
