# Teacher's guide: Module 06, Data structures
# Every example and exercise answer from this module's lessons, in order.
# Run it from this folder:  python guide.py
# ruff: noqa: UP015, UP034, B033, E501

import json
import os

print("=" * 50)
print("LESSON: dictionaries.md")

print("\n--- Example: Creating a dictionary")
prices = {"espresso": 5.0, "latte": 8.5, "tea": 4.0}
print(prices)

contact = {
    "name": "Ana",
    "phone": "555-0101",
    "city": "Lisbon",
}
print(contact)

print("\n--- Example: Reading a value")
prices = {"espresso": 5.0, "latte": 8.5, "tea": 4.0}
print(prices["latte"])
print(f"A tea costs {prices['tea']}")

print("\n--- Example: Adding and changing values")
prices = {"espresso": 5.0, "latte": 8.5}
prices["latte"] = 9.0  # the key exists: change the value
prices["cappuccino"] = 8.0  # the key is new: add a pair
print(prices)

prices = {"espresso": 5.0, "latte": 8.5, "tea": 4.0}
del prices["tea"]
print(prices)

print("\n--- Example: Checking if a key exists with in")
prices = {"espresso": 5.0, "latte": 8.5}
print("latte" in prices)
print("mocha" in prices)
print(8.5 in prices)

print("\n--- Example: Reading safely with .get()")
prices = {"espresso": 5.0, "latte": 8.5}
print(prices.get("latte"))
print(prices.get("mocha"))
print(prices.get("mocha", 0))
print(prices.get("mocha", "not on the menu"))

print("\n--- Example: Looping over a dictionary")
prices = {"espresso": 5.0, "latte": 8.5, "tea": 4.0}
for drink in prices:
    print(drink)

prices = {"espresso": 5.0, "latte": 8.5, "tea": 4.0}
for drink, price in prices.items():
    print(f"{drink}: {price}")

prices = {"espresso": 5.0, "latte": 8.5, "tea": 4.0}
print(list(prices.keys()))
print(list(prices.values()))
print(sum(prices.values()))
print(len(prices))

print("\n--- Example: The counting pattern")
orders = ["latte", "tea", "latte", "espresso", "latte", "tea"]
counts = {}
for drink in orders:
    counts[drink] = counts.get(drink, 0) + 1
print(counts)

print("\n--- Example: A list of dictionaries: records")
books = [
    {"title": "Dune", "author": "Frank Herbert", "pages": 412},
    {"title": "Emma", "author": "Jane Austen", "pages": 474},
    {"title": "Ubik", "author": "Philip K. Dick", "pages": 202},
]

for book in books:
    print(f"{book['title']} by {book['author']}, {book['pages']} pages")

books = [
    {"title": "Dune", "pages": 412},
    {"title": "Emma", "pages": 474},
    {"title": "Ubik", "pages": 202},
]

for book in books:
    if book["pages"] < 300:
        print(f"Short read: {book['title']}")

books = [{"title": "Dune", "pages": 412}]
books.append({"title": "Emma", "pages": 474})
print(len(books))

print("\n--- Example: Nested dictionaries")
recipe = {
    "name": "Pancakes",
    "minutes": 20,
    "ingredients": {"flour": "200 g", "milk": "300 ml", "eggs": "2"},
}
print(recipe["ingredients"]["milk"])
print(len(recipe["ingredients"]))

print("\n--- Mistake: Asking for a key that does not exist")
# Breaks on purpose (do not run):
# prices = {"espresso": 5.0, "latte": 8.5}
# print(prices["mocha"])
# KeyError: 'mocha'

prices = {"espresso": 5.0, "latte": 8.5}
print(prices.get("mocha", "not on the menu"))

print("\n--- Mistake: Using a position instead of a key")
# Breaks on purpose (do not run):
# prices = {"espresso": 5.0, "latte": 8.5}
# print(prices[0])
# KeyError: 0

print("\n--- Mistake: Forgetting .items() in the loop")
# Breaks on purpose (do not run):
# prices = {"espresso": 5.0, "latte": 8.5}
# for drink, price in prices:
#     print(drink, price)
# ValueError: too many values to unpack (expected 2)

prices = {"espresso": 5.0, "latte": 8.5}
for drink, price in prices.items():
    print(drink, price)

print("\n--- Mistake: Forgetting the quotes around a key")
# Breaks on purpose (do not run):
# contact = {"name": "Ana", "phone": "555-0101"}
# print(contact[name])
# NameError: name 'name' is not defined

# Ask her to predict the output before running.
print("\n--- Exercise 1: Reading values")
plant = {"name": "Fern", "water_days": 3, "sun": "shade"}
print(plant["name"])
print(plant["water_days"] + 1)
print("sun" in plant)
print("Fern" in plant)

# Ask her to predict the output before running.
print("\n--- Exercise 2: Replace or add?")
stock = {"apples": 4, "pears": 2}
stock["apples"] = 10
stock["plums"] = 5
stock["pears"] = stock["pears"] + 1
print(stock)
print(len(stock))

# Ask her to predict the output before running.
print("\n--- Exercise 3: .get() with and without a default")
grades = {"Ana": 9, "Bruno": 7}
print(grades.get("Ana"))
print(grades.get("Carla"))
print(grades.get("Carla", 0))

print("\n--- Exercise 4: The broken menu")
# Starting code given in the exercise (not run):
# menu = {"juice": 6.0, "water": 3.0}
# for item, price in menu:
#     print(f"{item} costs {price}")

menu = {"juice": 6.0, "water": 3.0}
for item, price in menu.items():
    print(f"{item} costs {price}")

print("\n--- Exercise 5: The missing city")
# Starting code given in the exercise (not run):
# contact = {"name": "Bruno", "phone": "555-0199"}
# print(contact["city"])

contact = {"name": "Bruno", "phone": "555-0199"}
print(contact.get("city", "unknown"))

print("\n--- Exercise 6: Your favorite movies")
movies = {"Up": 2009, "Coco": 2017, "Amelie": 2001}
for title, year in movies.items():
    print(f"{title} ({year})")

print("\n--- Exercise 7: Counting colors")
colors = ["blue", "red", "blue", "green", "blue", "red"]
counts = {}
for color in colors:
    counts[color] = counts.get(color, 0) + 1
print(counts)

print("\n--- Exercise 8: The cheapest product")
products = [
    {"name": "Notebook", "price": 12.5},
    {"name": "Pencil", "price": 1.5},
    {"name": "Mug", "price": 9.0},
]
for product in products:
    if product["price"] < 10:
        print(product["name"])

print("\n--- Exercise 9: Total of an order")


def order_total(prices, order):
    total = 0
    for item in order:
        total = total + prices[item]
    return total


prices = {"espresso": 5.0, "latte": 8.5, "tea": 4.0}
order = ["latte", "tea", "latte"]
print(order_total(prices, order))

print("\n--- Review 1: Lists and enumerate (module 02)")
tasks = ["wash dishes", "buy bread", "call mom"]
for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")

print("\n--- Review 2: Reading a file into a list (module 04)")
# The guide creates groceries.txt first, so the answer can run.
with open("groceries.txt", "w", encoding="utf-8") as file:
    file.write("milk\neggs\nbread\n")

with open("groceries.txt", "r", encoding="utf-8") as file:
    content = file.read()

items = content.splitlines()
print(f"There are {len(items)} items.")

os.remove("groceries.txt")


print("=" * 50)
print("LESSON: tuples-and-sets.md")

print("\n--- Example: Creating a tuple")
birthday = (14, "March")
print(birthday)
print(birthday[0])
print(birthday[1])
print(len(birthday))

print("\n--- Example: Tuples cannot change")
# Breaks on purpose (do not run):
# birthday = (14, "March")
# birthday[0] = 15
# TypeError: 'tuple' object does not support item assignment

birthday = (14, "March")
birthday = (15, "March")
print(birthday)

print("\n--- Example: Unpacking")
point = (38.7, -9.1)
latitude, longitude = point
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")

for number, fruit in enumerate(["apple", "pear"]):
    print(number, fruit)


def min_and_max(numbers):
    return min(numbers), max(numbers)


lowest, highest = min_and_max([12, 3, 27, 8])
print(lowest, highest)

print("\n--- Example: A tuple with one item needs a comma")
not_a_tuple = ("tea")  # fmt: skip
a_tuple = ("tea",)
print(type(not_a_tuple))
print(type(a_tuple))

print("\n--- Example: Creating a set")
numbers = {3, 1, 2, 3, 1}
print(numbers)
print(len(numbers))

fruits = {"pear", "apple", "banana"}
print(sorted(fruits))

print("\n--- Example: Removing duplicates from a list")
visitors = ["Ana", "Bruno", "Ana", "Carla", "Bruno", "Ana"]
unique = set(visitors)
print(len(visitors))
print(len(unique))
print(sorted(unique))

print("\n--- Example: Adding to a set and checking with in")
tags = {"python", "beginner"}
tags.add("tutorial")
tags.add("python")
print(len(tags))
print("python" in tags)
print("java" in tags)

print("\n--- Example: Comparing two sets")
ana = {"basil", "mint", "rosemary"}
bruno = {"mint", "parsley", "basil"}

print(sorted(ana & bruno))
print(sorted(ana | bruno))
print(sorted(ana - bruno))
print(sorted(bruno - ana))

print("\n--- Example: {} is a dictionary, not a set")
empty_dict = {}
empty_set = set()
print(type(empty_dict))
print(type(empty_set))

print("\n--- Mistake: Trying to change a tuple")
# Breaks on purpose (do not run):
# size = (20, 30)
# size.append(40)
# AttributeError: 'tuple' object has no attribute 'append'

print("\n--- Mistake: Unpacking the wrong number of values")
# Breaks on purpose (do not run):
# date = (14, "March", 2024)
# day, month = date
# ValueError: too many values to unpack (expected 2)

print("\n--- Mistake: Using a position in a set")
# Breaks on purpose (do not run):
# colors = {"red", "blue"}
# print(colors[0])
# TypeError: 'set' object is not subscriptable

print("\n--- Mistake: Expecting {} to be an empty set")
# Breaks on purpose (do not run):
# seen = {}
# seen.add("tea")
# AttributeError: 'dict' object has no attribute 'add'

# Ask her to predict the output before running.
print("\n--- Exercise 1: Tuple basics")
recipe = ("Soup", 30, "easy")
name, minutes, level = recipe
print(name)
print(minutes * 2)
print(len(recipe))

# Ask her to predict the output before running.
print("\n--- Exercise 2: How many unique?")
answers = ["yes", "no", "yes", "yes", "maybe", "no"]
print(len(answers))
print(len(set(answers)))

# Ask her to predict the output before running.
print("\n--- Exercise 3: Comparing groups")
monday = {"Ana", "Bruno", "Carla"}
tuesday = {"Carla", "Davi"}
print(sorted(monday & tuesday))
print(sorted(monday | tuesday))
print(sorted(tuesday - monday))

print("\n--- Exercise 4: The one-item tuple")
# Starting code given in the exercise (not run):
# colors = ("green")
# print(type(colors))

colors = ("green",)
print(type(colors))

print("\n--- Exercise 5: Collecting unique cities")
# Starting code given in the exercise (not run):
# cities = {}
# for city in ["Porto", "Lisbon", "Porto"]:
#     cities.add(city)
# print(sorted(cities))

cities = set()
for city in ["Porto", "Lisbon", "Porto"]:
    cities.add(city)
print(sorted(cities))

print("\n--- Exercise 6: Unique words")
sentence = "the cat saw the dog and the dog saw the cat"
words = sentence.split()
print(len(words))
print(len(set(words)))

print("\n--- Exercise 7: A function that returns two values")


def split_name(full_name):
    parts = full_name.split()
    return parts[0], parts[-1]


first, last = split_name("Ana Souza")
print(first)
print(last)

print("\n--- Exercise 8: What is missing from the shopping?")
plan = {"milk", "eggs", "bread", "coffee"}
cart = {"eggs", "coffee", "chocolate"}
print(sorted(plan - cart))

print("\n--- Review 1: Dictionaries (previous file)")
ages = {"Ana": 30, "Bruno": 25}
ages["Ana"] = ages["Ana"] + 1
print(ages.get("Bruno", 0) + ages.get("Carla", 0))
print(ages["Ana"])

print("\n--- Review 2: Functions with return (module 03)")


def double_print(n):
    print(n * 2)


def double_return(n):
    return n * 2


a = double_print(5)
b = double_return(5)
print(a)
print(b)


print("=" * 50)
print("LESSON: json.md")

print("\n--- Example: Packing: from Python to JSON text with json.dumps()")
contact = {"name": "Ana", "favorite": True, "nickname": None}
text = json.dumps(contact)
print(text)
print(type(text))

print("\n--- Example: Making it readable with indent")
contact = {"name": "Ana", "tags": ["work", "family"]}
print(json.dumps(contact, indent=4))

print("\n--- Example: Unpacking: from JSON text to Python with json.loads()")
text = '{"title": "Dune", "pages": 412, "read": false}'
book = json.loads(text)
print(book["title"])
print(book["pages"] + 1)
print(book["read"])
print(type(book))

print("\n--- Example: Saving to a file with json.dump()")
books = [
    {"title": "Dune", "pages": 412},
    {"title": "Emma", "pages": 474},
]

with open("books.json", "w", encoding="utf-8") as file:
    json.dump(books, file, indent=4)

print("Saved!")

print("\n--- Example: Loading from a file with json.load()")
with open("books.json", "w", encoding="utf-8") as file:
    json.dump([{"title": "Dune", "pages": 412}], file)

with open("books.json", "r", encoding="utf-8") as file:
    books = json.load(file)

for book in books:
    print(f"{book['title']}: {book['pages']} pages")

print("\n--- Example: Accents and special characters: ensure_ascii=False")
print(json.dumps({"city": "São Paulo"}))
print(json.dumps({"city": "São Paulo"}, ensure_ascii=False))

print("\n--- Example: The load-or-start-empty pattern")
FILE = "contacts.json"


def load_contacts():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_contacts(contacts):
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4, ensure_ascii=False)


contacts = load_contacts()
print(f"Loaded {len(contacts)} contacts")

contacts.append({"name": "José", "phone": "555-0123"})
save_contacts(contacts)

print(f"Now there are {len(load_contacts())} contacts")

print("\n--- Mistake: Confusing dump with dumps (and load with loads)")
# Breaks on purpose (do not run):
# import json
#
# text = '{"name": "Ana"}'
# data = json.load(text)
# AttributeError: 'str' object has no attribute 'read'

print("\n--- Mistake: Single quotes in JSON text")
# Breaks on purpose (do not run):
# import json
#
# data = json.loads("{'name': 'Ana'}")
# json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

print("\n--- Mistake: Loading a file that does not exist")
# Breaks on purpose (do not run):
# import json
#
# with open("missing.json", "r", encoding="utf-8") as file:
#     data = json.load(file)
# FileNotFoundError: [Errno 2] No such file or directory: 'missing.json'

print("\n--- Mistake: Saving something JSON does not understand")
# Breaks on purpose (do not run):
# import json
#
# tags = {"python", "beginner"}
# print(json.dumps(tags))
# TypeError: Object of type set is not JSON serializable

# Ask her to predict the output before running.
print("\n--- Exercise 1: Python to JSON")
plant = {"name": "Fern", "indoor": True, "sold": False, "price": None}
print(json.dumps(plant))

# Ask her to predict the output before running.
print("\n--- Exercise 2: JSON to Python")
text = '{"temps": [21, 24, 19], "city": "Porto"}'
weather = json.loads(text)
print(weather["city"])
print(max(weather["temps"]))
print(len(weather))

print("\n--- Exercise 3: The wrong function")
# Starting code given in the exercise (not run):
# import json
#
# order = {"drink": "latte", "size": "large"}
# print(json.dump(order))

order = {"drink": "latte", "size": "large"}
print(json.dumps(order))

print("\n--- Exercise 4: Unreadable accents")
# Starting code given in the exercise (not run):
# import json
#
# dish = {"dish": "Feijoada com farofa", "country": "Brasil", "note": "Delicioso, não?"}
# print(json.dumps(dish))

dish = {"dish": "Feijoada com farofa", "country": "Brasil", "note": "Delicioso, não?"}
print(json.dumps(dish, ensure_ascii=False))

print("\n--- Exercise 5: Save and load a to-do list")
tasks = [
    {"title": "Water the plants", "done": True},
    {"title": "Pay the bills", "done": False},
    {"title": "Call the dentist", "done": False},
]

with open("todo.json", "w", encoding="utf-8") as file:
    json.dump(tasks, file, indent=4)

with open("todo.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

for task in loaded:
    if task["done"]:
        mark = "x"
    else:
        mark = " "
    print(f"[{mark}] {task['title']}")

print("\n--- Exercise 6: A growing guest book")
# In the lesson the name comes from input(). Here we simulate two runs: Ana, then Bruno.
FILE = "guests.json"


def load_guests():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_guests(guests):
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(guests, file, indent=4, ensure_ascii=False)


for name in ["Ana", "Bruno"]:
    guests = load_guests()
    # name = input("Your name: ")
    guests.append(name)
    save_guests(guests)
    print(f"Thank you, {name}! We have {len(guests)} guests.")

# (console)
# PS C:\Users\you\Projects> python guests.py
# Your name: Ana
# Thank you, Ana! We have 1 guests.
# PS C:\Users\you\Projects> python guests.py
# Your name: Bruno
# Thank you, Bruno! We have 2 guests.

print("\n--- Review 1: Records (dictionaries)")
pets = [
    {"name": "Rex", "kind": "dog"},
    {"name": "Mia", "kind": "cat"},
    {"name": "Bob", "kind": "dog"},
]
dogs = 0
for pet in pets:
    if pet["kind"] == "dog":
        dogs = dogs + 1
print(dogs)


# Clean up the files this lesson created.
for leftover in ["books.json", "contacts.json", "todo.json", "guests.json"]:
    os.remove(leftover)


print("=" * 50)
print("LESSON: comprehensions.md")

print("\n--- Example: From a loop to a comprehension")
prices = [10, 25, 4]
doubled = []
for price in prices:
    doubled.append(price * 2)
print(doubled)

prices = [10, 25, 4]
doubled = [price * 2 for price in prices]
print(doubled)

# Shown only, not run:
# doubled = []                    # 1. the empty list...
# for price in prices:            # 2. ...the loop...
#     doubled.append(price * 2)   # 3. ...and what gets added
#
# doubled = [price * 2 for price in prices]
# #          ^ 3.       ^ 2.               the [] is 1.

print("\n--- Example: More examples")
names = ["ana", "bruno", "carla"]
print([name.upper() for name in names])
print([len(name) for name in names])
print([f"Hello, {name}!" for name in names])

squares = [n * n for n in range(1, 6)]
print(squares)

print("\n--- Example: Filtering with if")
temps = [18, 25, 31, 22, 29]
hot = []
for t in temps:
    if t > 24:
        hot.append(t)
print(hot)

temps = [18, 25, 31, 22, 29]
hot = [t for t in temps if t > 24]
print(hot)

products = [
    {"name": "Notebook", "price": 12.5},
    {"name": "Pencil", "price": 1.5},
    {"name": "Mug", "price": 9.0},
]
cheap_names = [p["name"] for p in products if p["price"] < 10]
print(cheap_names)

print("\n--- Example: Set and dictionary comprehensions (briefly)")
words = ["Apple", "apple", "APPLE", "pear"]
unique = {w.lower() for w in words}
print(sorted(unique))

names = ["ana", "bruno", "carla"]
lengths = {name: len(name) for name in names}
print(lengths)

menu = {"espresso": 5.0, "latte": 8.0}
new_menu = {drink: price * 1.1 for drink, price in menu.items()}
print(new_menu)

print("\n--- Example: When NOT to use a comprehension")
# Don't do this (not run):
# # Do not do this: it builds a useless list of None values just to print.
# [print(name) for name in names]
#
# # Do this:
# for name in names:
#     print(name)

print("\n--- Mistake: Putting the if in the wrong place")
# Breaks on purpose (do not run):
# temps = [18, 25, 31]
# hot = [if t > 24 t for t in temps]
# SyntaxError: invalid syntax

print("\n--- Mistake: Using a variable that is not the loop variable")
# Breaks on purpose (do not run):
# prices = [10, 25, 4]
# doubled = [p * 2 for price in prices]
# NameError: name 'p' is not defined

print("\n--- Mistake: Forgetting .items() in a dictionary comprehension")
# Breaks on purpose (do not run):
# menu = {"espresso": 5.0, "latte": 8.0}
# cheap = {d: p for d, p in menu if p < 6}
# ValueError: too many values to unpack (expected 2)

# Ask her to predict the output before running.
print("\n--- Exercise 1: Read the comprehension")
numbers = [1, 2, 3, 4, 5, 6]
print([n * 10 for n in numbers])
print([n for n in numbers if n % 2 == 0])
print([n + 1 for n in numbers if n > 4])

# Ask her to predict the output before running.
print("\n--- Exercise 2: Dictionary comprehension")
stock = {"apples": 0, "pears": 4, "plums": 0, "figs": 2}
available = {fruit: amount for fruit, amount in stock.items() if amount > 0}
print(available)

print("\n--- Exercise 3: Wrong order")
# Starting code given in the exercise (not run):
# items = ["bread", "chocolate", "milk"]
# short = [for item in items item.upper() if len(item) <= 5]
# print(short)

items = ["bread", "chocolate", "milk"]
short = [item.upper() for item in items if len(item) <= 5]
print(short)

print("\n--- Exercise 4: Loop to comprehension")
# Starting code given in the exercise (not run):
# cities = ["lisbon", "porto", "faro"]
# titles = []
# for city in cities:
#     titles.append(city.title())
# print(titles)

cities = ["lisbon", "porto", "faro"]
titles = [city.title() for city in cities]
print(titles)

print("\n--- Exercise 5: Comprehension to loop")
# Starting code given in the exercise (not run):
# words = ["sun", "moonlight", "sky", "rainbow"]
# long_words = [w for w in words if len(w) > 3]
# print(long_words)

words = ["sun", "moonlight", "sky", "rainbow"]
long_words = []
for w in words:
    if len(w) > 3:
        long_words.append(w)
print(long_words)

print("\n--- Exercise 6: Titles of unread books")
books = [
    {"title": "Dune", "read": True},
    {"title": "Emma", "read": False},
    {"title": "Ubik", "read": False},
]
to_read = [book["title"] for book in books if not book["read"]]
print(to_read)

print("\n--- Review 2: Sets (tuples and sets)")
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(sorted(a & b))
print(sorted(a - b))
print(len(a | b))
