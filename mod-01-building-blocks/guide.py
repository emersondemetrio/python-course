# ruff: noqa: F811, UP003, UP015
# Teacher's guide: Module 01, Building blocks
# Every example and exercise answer from this module's lessons, in order.
# Run it from this folder:  python guide.py

import os

print("=" * 50)
print("LESSON: data-types.md")

print("\n--- Example: Creating a variable")
# A variable is a name with a value inside. = puts the value in the name.
cups = 3
print(cups)

print("\n--- Example: Using variables in calculations")
price = 12
quantity = 3
total = price * quantity
print(total)

print("\n--- Example: Reassignment, the latest value wins")
# Ask her to predict: a ends up as 0, so c is 5.
a = 2
a = 0
b = 5
c = a + b
print(c)

print("\n--- Example: Using the old value to make the new one")
steps = 10
steps = steps + 5
print(steps)

print("\n--- Example: Names are case sensitive")
name = "Ana"
Name = "Bia"
print(name)
print(Name)

print("\n--- Example: The basic types")
print(type(10))
print(type(10.0))
print(type("10"))
print(type(True))

print("\n--- Example: Arithmetic")
# Highlight: / always gives a float, even 6 / 2.
print(7 + 2)
print(7 * 2)
print(7 / 2)
print(6 / 2)

print("\n--- Example: Type hints do not force a type")
a: int = 10
print(a)
a = "ten"
print(a)

print("\n--- Example: Converting between types")
print(int("42") + 1)
print(float("2.5") * 2)
print(str(7) + "7")
print(int(3.9))  # int() cuts the decimal part, it does not round

print("\n--- Mistake: Using a variable before creating it")
# print(total_cost)
# total_cost = 10
# NameError: name 'total_cost' is not defined
total_cost = 10
print(total_cost)

print("\n--- Mistake: Wrong upper or lower case")
# city = "Lisbon"
# print(City)
# NameError: name 'City' is not defined. Did you mean: 'city'?
city = "Lisbon"
print(city)

print("\n--- Mistake: Turning text that is not a number into a number")
# age = int("thirty")
# ValueError: invalid literal for int() with base 10: 'thirty'
age = int("30")
print(age)

print("\n--- Mistake: Forgetting that quotes make text")
a = "5"
b = "3"
print(a + b)

print("\n--- Exercise 1: Last one wins")
# Ask her to predict before running.
coffee = 1
coffee = 2
coffee = 3
print(coffee)

print("\n--- Exercise 2: Order matters")
# Ask her to predict: y was calculated when x was still 4.
x = 4
y = x + 1
x = 10
print(y)

print("\n--- Exercise 3: What type is it?")
print(type(3))
print(type("3"))
print(type(3.0))
print(type(False))

print("\n--- Exercise 4: Division")
print(10 / 2)
print(10 / 4)

print("\n--- Exercise 5: The missing variable")
# Broken: height is used before it exists.
#   width = 5
#   area = width * height
#   height = 5
width = 5
height = 5
area = width * height
print(area)

print("\n--- Exercise 6: Text that should be a number")
# Broken: "10" + "5" gives "105".
bags = 10
extra = 5
print(bags + extra)

print("\n--- Exercise 7: Pizza for everyone")
slices_per_pizza = 8
pizzas = 3
total_slices = slices_per_pizza * pizzas
print(total_slices)

print("\n--- Exercise 8: Saving money")
savings = 100
savings = savings + 25
savings = savings + 25
savings = savings + 25
print(savings)

print("\n--- Exercise 9: From text to number")
typed = "1990"
year = int(typed)
age = 2026 - year
print(age)

print()
print("=" * 50)
print("LESSON: strings.md")

print("\n--- Example: Quotes")
print("Hello")
print("Hello")  # single quotes 'Hello' work the same way

print("\n--- Example: New lines with \\n")
print("First line\nSecond line")

print("\n--- Example: Joining strings with +")
first = "Maria"
last = "Silva"
print(first + " " + last)

print("\n--- Example: + only joins text with text")
cups = 2
# print("Cups: " + cups)
# TypeError: can only concatenate str (not "int") to str
print("Cups: " + str(cups))

print("\n--- Example: f-strings, filling in the blanks")
name = "Maria"
cups = 2
print(f"{name} ordered {cups} cups.")

print("\n--- Example: Calculations and function calls inside {}")
price = 4.5
cups = 2
print(f"Total: {price * cups}")
print(f"One plus one is {1 + 1}")
print(f"The word 'coffee' has {len('coffee')} letters")

print("\n--- Example: What happens without the f")
name = "Maria"
print("Hello, {name}")
print(f"Hello, {name}")

print("\n--- Example: print with several values")
print("Total:", 9, "reais")

print("\n--- Example: sep")
print("apple", "banana", "pear", sep=", ")
print("apple", "banana", "pear", sep="\n")

print("\n--- Example: end")
print("Loading", end="...")
print("done")

print("\n--- Example: How long is a string?")
print(len("tea"))
print(len("green tea"))  # the space counts

print("\n--- Example: Going through each character")
for letter in "tea":
    print(letter)

print("\n--- Mistake: Joining text and a number with +")
age = 30
# print("I am " + age + " years old")
# TypeError: can only concatenate str (not "int") to str
print("I am " + str(age) + " years old")
print(f"I am {age} years old")

print("\n--- Mistake: Forgetting the f")
city = "Porto"
print("I live in {city}")
print(f"I live in {city}")

print("\n--- Mistake: Quotes that do not match")
# print("Hello')
# SyntaxError: unterminated string literal (detected at line 1)
print("Hello")

print("\n--- Mistake: Missing spaces when joining")
first = "Ana"
last = "Costa"
print(first + last)
print(first + " " + last)

print("\n--- Exercise 1: With and without f")
# Ask her to predict before running.
food = "soup"
print("I like {food}")
print(f"I like {food}")

print("\n--- Exercise 2: Joining text")
a = "5"
b = "5"
print(a + b)
print(f"{a}{b}")

print("\n--- Exercise 3: Separators")
print("a", "b", "c")
print("a", "b", "c", sep="-")
print("a", "b", "c", sep="")

print("\n--- Exercise 4: Math inside braces")
# Only what is inside {} is calculated.
apples = 3
print(f"{apples} apples")
print(f"{apples * 2} apples")
print(f"{apples} * 2 apples")

print("\n--- Exercise 5: The broken receipt")
total = 18
# print("Total: " + total + " reais")
# TypeError: can only concatenate str (not "int") to str
print("Total: " + str(total) + " reais")
print(f"Total: {total} reais")

print("\n--- Exercise 6: Glued words")
greeting = "Good"
time = "morning,"
name = "Ana"
print(greeting + " " + time + " " + name)

print("\n--- Exercise 7: Coffee order")
customer = "Lucas"
drink = "latte"
price = 9.5
print(f"{customer} ordered a {drink} for {price} reais.")

print("\n--- Exercise 8: Three lines, one print")
print("Milk\nEggs\nBread")

print("\n--- Exercise 9: Word length")
word = "pineapple"
print(f"{word} has {len(word)} letters")

print("\n--- Review 1: Which type?")
value = "12"
print(type(value))
value = 12
print(type(value))

print("\n--- Review 2: Total price")
price = 3
quantity = 4
total = price * quantity
print(f"Total: {total}")

print()
print("=" * 50)
print("LESSON: built-in.md")

print("\n--- Example: Calling a function, name plus parentheses")
print(len("coffee"))

print("\n--- Example: The name alone is not a call")
# Same idea as file.read versus file.read() in class 3.
print(len)
print(len("tea"))
word = "tea"
print(word.upper)
print(word.upper())

print("\n--- Example: print()")
print("Pears:", 4, "Price:", 2.5)

print("\n--- Example: input() always gives back text")
# age = input("How old are you? ")      she types: 30
age = "30"
print(type(age))
# age = int(input("How old are you? "))
age = int("30")
print(f"Next year you will be {age + 1}")

print("\n--- Example: len()")
print(len("Lisbon"))
print(len(["milk", "eggs", "bread"]))
print(len(""))

print("\n--- Example: type(), int(), float(), str()")
print(type(2.5))
print(int("8") + 2)
print(float("1.5") + 1)
print(str(8) + "2")

print("\n--- Example: round()")
print(round(3.7))
print(round(3.14159, 2))
print(round(9.876, 1))

print("\n--- Example: enumerate(), numbering items in a loop")
groceries = ["milk", "eggs", "bread"]
for position, item in enumerate(groceries):
    print(position, item)
for number, item in enumerate(groceries, start=1):
    print(f"{number}. {item}")

print("\n--- Example: Keywords versus built-in names")
# return = 5
# SyntaxError: invalid syntax            (return is a keyword)
#
# str = "hello"
# print(str(5))
# TypeError: 'str' object is not callable   (str is a built-in name: don't reuse it)

print("\n--- Mistake: Forgetting the parentheses")
name = "ana"
print(name.upper)
print(name.upper())

print("\n--- Mistake: Doing math with what input() returned")
# cups = input("How many cups? ")       she types: 3
cups = "3"
print(cups * 2)
print(int(cups) * 2)

print("\n--- Mistake: Calling something that is not a function")
total = 10
# print(total())
# TypeError: 'int' object is not callable
print(total)

print("\n--- Mistake: Using a variable called len (or str, list...)")
# len = 3
# print(len("abc"))
# TypeError: 'int' object is not callable
size = 3
print(len("abc"), size)

print("\n--- Exercise 1: Inside out")
# Ask her to predict: the inner call runs first.
print(len("bread") + 1)

print("\n--- Exercise 2: Name or call?")
print(type)
print(type(7))

print("\n--- Exercise 3: Rounding")
print(round(2.71828, 2))
print(round(7.6))

print("\n--- Exercise 4: Counting from 1")
colors = ["red", "blue"]
for n, color in enumerate(colors, start=1):
    print(n, color)

print("\n--- Exercise 5: The doubled order")
# Broken: plates = input(...) is text, so "4" * 2 is "44".
# plates = int(input("How many plates? "))    she types: 4
plates = int("4")
print(plates * 2)

print("\n--- Exercise 6: The broken name")
# Broken: list = ["tea", "coffee"] hides the built-in list().
drinks = ["tea", "coffee"]
print(len(drinks))
items = list("abc")
print(items)

print("\n--- Exercise 7: Name length")
# name = input("What is your name? ")    she types: Carla
name = "Carla"
print(f"{name} has {len(name)} letters")

print("\n--- Exercise 8: Splitting the bill")
# total = float(input("Bill total? "))         she types: 100
# people = int(input("How many people? "))     she types: 3
total = float("100")
people = int("3")
each = total / people
print(f"Each person pays {round(each, 2)}")

print("\n--- Exercise 9: Numbered to-do list")
tasks = ["water the plants", "call mom", "buy coffee"]
for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")

print("\n--- Review 1: Text plus number")
# print("Items: " + 3)   -> TypeError
print("Items: " + str(3))
print(f"Items: {3}")

print("\n--- Review 2: Predict the output")
# b got the value 1 before a changed.
a = 1
b = a
a = 5
print(f"{a} {b}")

print()
print("=" * 50)
print("LESSON: practice.md  (practice set: classes 1 to 3)")

print("\n--- Exercise 1: Fill the blank")
plant = "basil"
print(f"I water the {plant} every day.")

print("\n--- Exercise 2: Where is the f?")
book = "Dom Casmurro"
print("Reading {book}")
print(f"Reading {book}")

print("\n--- Exercise 3: Math in the braces")
price = 5
print(f"Two coffees cost {price * 2} reais")
print(f"Two coffees cost {price} * 2 reais")

print("\n--- Exercise 4: From + to f-string")
# Before: print("You have " + str(3) + " new messages")
messages = 3
print(f"You have {messages} new messages")

print("\n--- Exercise 5: A short introduction")
name = "Ana"
city = "Lisbon"
age = 39
print(f"My name is {name}, I live in {city} and I am {age} years old.")

print("\n--- Exercise 6: Defined but never called")
# Ask her to predict: defining is not calling, so "Hello!" never shows.


def say_hello():
    print("Hello!")


print("Start")
print("End")

print("\n--- Exercise 7: Called twice")


def say_hello():
    print("Hello!")


print("Start")
say_hello()
say_hello()
print("End")

print("\n--- Exercise 8: Parameter and argument")
# person is the PARAMETER (in the def). "Marta" is the ARGUMENT (in the call).


def greet(person):
    print(f"Good evening, {person}")


greet("Marta")
greet("Joel")

print("\n--- Exercise 9: Outside name, inside name")
# file_name (outside) and name (inside) are two names for the same value.
# And "notes.txt" is just text: the file is never opened here.


def show_file_name(name):
    print(f"File: {name}")


file_name = "notes.txt"
show_file_name(file_name)

print("\n--- Exercise 10: return versus print")
# Ask her to predict: only 8 twice. double_return(4) alone shows nothing.


def double_print(n):
    print(n * 2)


def double_return(n):
    return n * 2


double_print(4)
double_return(4)
result = double_return(4)
print(result)

print("\n--- Exercise 11: Your first function")


def welcome(name):
    print(f"Welcome, {name}!")


welcome("Ana")
welcome("Rui")
welcome("Lia")

print("\n--- Exercise 12: A function that returns")


def total_price(price, quantity):
    return price * quantity


total = total_price(5, 3)
print(f"Total: {total}")

print("\n--- Exercise 13: From print to return")
# Broken version prints "Hi, Bia!" and then None:
#   def make_greeting(name):
#       print(f"Hi, {name}!")


def make_greeting(name):
    return f"Hi, {name}!"


message = make_greeting("Bia")
print(message)

print("\n--- Exercise 14: Counting starts at 0")
fruits = ["apple", "banana", "grape"]
print(fruits[0])
print(fruits[2])

print("\n--- Exercise 15: How many?")
fruits = ["apple", "banana", "grape"]
fruits.append("mango")
print(len(fruits))
print(fruits)

print("\n--- Exercise 16: Out of range")
days = ["mon", "tue", "wed"]
# print(days[3])
# IndexError: list index out of range     (3 items: positions 0, 1, 2)
print(days[2])

print("\n--- Exercise 17: Build a list")
shopping = []
shopping.append("rice")
shopping.append("beans")
shopping.append("coffee")
print(shopping)
print(len(shopping))

print("\n--- Exercise 18: One item per turn")
pets = ["cat", "dog", "fish"]
for pet in pets:
    print(f"I have a {pet}")

print("\n--- Exercise 19: What is inside the loop?")
# "done" is not indented, so it runs once, after the loop.
for pet in ["cat", "dog"]:
    print(pet)
print("done")

print("\n--- Exercise 20: enumerate from 0 and from 1")
songs = ["intro", "chorus"]
for i, song in enumerate(songs):
    print(i, song)
for i, song in enumerate(songs, start=1):
    print(i, song)

print("\n--- Exercise 21: Looping over a word")
for letter in "python":
    print(letter)

print("\n--- Exercise 22: Counting with a loop")
prices = [10, 25, 5, 40]
total = 0
for price in prices:
    total = total + price
print(f"Total: {total}")

print("\n--- Exercise 23: Shopping list printer")


def print_list(items):
    for number, item in enumerate(items, start=1):
        print(f"{number}. {item}")


print_list(["milk", "eggs", "bread"])

print("\n--- Exercise 24: Greetings for everyone")


def make_greeting(name):
    return f"Hello, {name}!"


for person in ["Ana", "Rui", "Lia"]:
    print(make_greeting(person))

print("\n--- Exercise 25: Longest word")
words = ["sun", "ocean", "sky"]
total = 0
for word in words:
    print(f"{word}: {len(word)}")
    total = total + len(word)
print(f"Total letters: {total}")

print("\n--- Exercise 26: Notes from a file")
# First the guide creates notes.txt with three lines (she makes it in the editor).
with open("notes.txt", "w") as file:
    file.write("buy coffee\ncall the dentist\nwater the plants\n")

with open("notes.txt", "r") as file:
    content = file.read()

notes = content.splitlines()
for number, note in enumerate(notes, start=1):
    print(f"{number}. {note}")

print("\n--- Exercise 27: Add a note, then show all")
# This is her class 3 program: one function writes, one reads.


def add_note(file_name, note):
    with open(file_name, "a") as file:
        file.write(note + "\n")


def show_notes(file_name):
    with open(file_name, "r") as file:
        notes = file.read().splitlines()
    for number, note in enumerate(notes, start=1):
        print(f"{number}. {note}")


notes_file = "notes.txt"
# new_note = input("New note: ")     she types: pay the rent
new_note = "pay the rent"
add_note(notes_file, new_note)
show_notes(notes_file)

os.remove("notes.txt")
