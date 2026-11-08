# Dictionaries

> **In one sentence:** a dictionary stores pairs of **keys** and **values**, so you can find a value by its name instead of by its position.

## Why it matters

With a list, you find things by position: "give me item number 2". That works when order is what matters, but most of the time you want to find things by name: "what is Ana's phone number?", "how much does a latte cost?". Dictionaries do exactly that, and they are everywhere in Python. Almost every program you write from now on will use one.

## Analogy

Think of a real dictionary, the book. You do not read it from the first page until you find the word "coffee". You go straight to the word, and next to it you find its meaning. The word is the **key**, the meaning is the **value**.

Another picture: the menu at a café. On the left, the name of the drink. On the right, the price. You look for "latte" and read the price next to it. A Python dictionary is that menu.

## The idea, step by step

### Creating a dictionary

A dictionary uses curly braces `{}`. Inside, each pair is written as `key: value`, and pairs are separated by commas.

```python
prices = {"espresso": 5.0, "latte": 8.5, "tea": 4.0}
print(prices)
```

Output:

```text
{'espresso': 5.0, 'latte': 8.5, 'tea': 4.0}
```

The keys here are strings (`"espresso"`), and the values are floats (`5.0`). Keys are usually strings, but values can be anything: numbers, strings, lists, even other dictionaries.

When a dictionary gets long, write one pair per line. It is the same dictionary, just easier to read:

```python
contact = {
    "name": "Ana",
    "phone": "555-0101",
    "city": "Lisbon",
}
print(contact)
```

Output:

```text
{'name': 'Ana', 'phone': '555-0101', 'city': 'Lisbon'}
```

The comma after the last pair is optional. Many programmers leave it there so that adding a new line later is easier.

### Reading a value

To read a value, write the dictionary name and the key in square brackets. It looks like reading a list, but instead of a position you give the key.

```python
prices = {"espresso": 5.0, "latte": 8.5, "tea": 4.0}
print(prices["latte"])
print(f"A tea costs {prices['tea']}")
```

Output:

```text
8.5
A tea costs 4.0
```

Notice the quotes inside the f-string: the f-string uses double quotes, so the key uses single quotes. If you use double quotes in both places, Python gets confused about where the string ends (in older versions of Python this is an error).

### Adding and changing values

You use the same square brackets to add a new pair or change an existing one. If the key already exists, the value is replaced. If it does not exist, a new pair is created.

```python
prices = {"espresso": 5.0, "latte": 8.5}
prices["latte"] = 9.0       # the key exists: change the value
prices["cappuccino"] = 8.0  # the key is new: add a pair
print(prices)
```

Output:

```text
{'espresso': 5.0, 'latte': 9.0, 'cappuccino': 8.0}
```

Keys are unique. A dictionary can never have two `"latte"` keys. Writing to an existing key always replaces its value.

To remove a pair, use `del`:

```python
prices = {"espresso": 5.0, "latte": 8.5, "tea": 4.0}
del prices["tea"]
print(prices)
```

Output:

```text
{'espresso': 5.0, 'latte': 8.5}
```

### Checking if a key exists with `in`

The `in` operator, which you already used with lists, checks if a **key** is in the dictionary. It answers `True` or `False`.

```python
prices = {"espresso": 5.0, "latte": 8.5}
print("latte" in prices)
print("mocha" in prices)
print(8.5 in prices)
```

Output:

```text
True
False
False
```

The last line is `False` because `in` only looks at the keys, never at the values.

### Reading safely with `.get()`

If you ask for a key that does not exist with square brackets, your program crashes (you will see this in Common mistakes). The method `.get()` asks politely: if the key exists, you get its value; if not, you get `None`, or a default value that you choose.

```python
prices = {"espresso": 5.0, "latte": 8.5}
print(prices.get("latte"))
print(prices.get("mocha"))
print(prices.get("mocha", 0))
print(prices.get("mocha", "not on the menu"))
```

Output:

```text
8.5
None
0
not on the menu
```

A good rule: use `prices["latte"]` when you are sure the key exists, and `prices.get("latte", something)` when it might not.

### Looping over a dictionary

A `for` loop over a dictionary goes through its **keys**:

```python
prices = {"espresso": 5.0, "latte": 8.5, "tea": 4.0}
for drink in prices:
    print(drink)
```

Output:

```text
espresso
latte
tea
```

Most of the time you want both the key and the value. Use `.items()`, which gives you pairs, and unpack them into two variables, just like you did with `enumerate()`:

```python
prices = {"espresso": 5.0, "latte": 8.5, "tea": 4.0}
for drink, price in prices.items():
    print(f"{drink}: {price}")
```

Output:

```text
espresso: 5.0
latte: 8.5
tea: 4.0
```

If you only want the keys or only the values, there are `.keys()` and `.values()`. Wrapping them with `list()` makes them easy to print:

```python
prices = {"espresso": 5.0, "latte": 8.5, "tea": 4.0}
print(list(prices.keys()))
print(list(prices.values()))
print(sum(prices.values()))
print(len(prices))
```

Output:

```text
['espresso', 'latte', 'tea']
[5.0, 8.5, 4.0]
17.5
3
```

`len()` tells you how many **pairs** the dictionary has.

### The counting pattern

A very common job: count how many times each thing appears. A dictionary is perfect for this. The key is the thing, the value is the count.

```python
orders = ["latte", "tea", "latte", "espresso", "latte", "tea"]
counts = {}
for drink in orders:
    counts[drink] = counts.get(drink, 0) + 1
print(counts)
```

Output:

```text
{'latte': 3, 'tea': 2, 'espresso': 1}
```

Read the line inside the loop slowly: "the count for this drink is whatever it was before (or 0 if this is the first time), plus 1". The `.get(drink, 0)` is what avoids a crash the first time a drink appears.

### A list of dictionaries: records

One dictionary describes **one** thing, like one contact. When you have many contacts, put the dictionaries inside a list. Each dictionary is called a **record**. This is how most real data looks, and it is very close to a table: each dictionary is a row, each key is a column.

```python
books = [
    {"title": "Dune", "author": "Frank Herbert", "pages": 412},
    {"title": "Emma", "author": "Jane Austen", "pages": 474},
    {"title": "Ubik", "author": "Philip K. Dick", "pages": 202},
]

for book in books:
    print(f"{book['title']} by {book['author']}, {book['pages']} pages")
```

Output:

```text
Dune by Frank Herbert, 412 pages
Emma by Jane Austen, 474 pages
Ubik by Philip K. Dick, 202 pages
```

To find one record, loop and check a key:

```python
books = [
    {"title": "Dune", "pages": 412},
    {"title": "Emma", "pages": 474},
    {"title": "Ubik", "pages": 202},
]

for book in books:
    if book["pages"] < 300:
        print(f"Short read: {book['title']}")
```

Output:

```text
Short read: Ubik
```

To add a new record, use `.append()`, exactly as with any list:

```python
books = [{"title": "Dune", "pages": 412}]
books.append({"title": "Emma", "pages": 474})
print(len(books))
```

Output:

```text
2
```

### Nested dictionaries

A value can be another dictionary. This is useful when one thing has a group of details inside it.

```python
recipe = {
    "name": "Pancakes",
    "minutes": 20,
    "ingredients": {"flour": "200 g", "milk": "300 ml", "eggs": "2"},
}
print(recipe["ingredients"]["milk"])
print(len(recipe["ingredients"]))
```

Output:

```text
300 ml
3
```

Read `recipe["ingredients"]["milk"]` from left to right: first get the `"ingredients"` dictionary, then, inside it, get `"milk"`.

### When to use a dictionary, when to use a list

- Use a **list** when you have many things of the same kind and order matters, or when you just go through them one by one: a shopping list, the steps of a recipe.
- Use a **dictionary** when you want to find something by a name, or when one thing has several named properties: the price of each drink, the details of one contact.
- Use a **list of dictionaries** when you have many things, each with several properties: all your contacts, all your books.

## Common mistakes

### Asking for a key that does not exist

<!-- error -->
```python
prices = {"espresso": 5.0, "latte": 8.5}
print(prices["mocha"])
```

```text
Traceback (most recent call last):
KeyError: 'mocha'
```

`KeyError` means "there is no such key in this dictionary". Check the spelling first: keys are case sensitive, so `"Latte"` and `"latte"` are different keys. If the key may really be missing, use `.get()` or check with `in` before reading:

```python
prices = {"espresso": 5.0, "latte": 8.5}
print(prices.get("mocha", "not on the menu"))
```

Output:

```text
not on the menu
```

### Using a position instead of a key

<!-- error -->
```python
prices = {"espresso": 5.0, "latte": 8.5}
print(prices[0])
```

```text
Traceback (most recent call last):
KeyError: 0
```

Dictionaries do not have positions like lists. `prices[0]` means "the value for the key `0`", and there is no such key. Use the key name: `prices["espresso"]`.

### Forgetting `.items()` in the loop

<!-- error -->
```python
prices = {"espresso": 5.0, "latte": 8.5}
for drink, price in prices:
    print(drink, price)
```

```text
Traceback (most recent call last):
ValueError: too many values to unpack (expected 2)
```

Looping directly over a dictionary gives you only the keys, one string at a time. Python then tries to split the string `"espresso"` into two variables and fails. Add `.items()` to get key and value together:

```python
prices = {"espresso": 5.0, "latte": 8.5}
for drink, price in prices.items():
    print(drink, price)
```

Output:

```text
espresso 5.0
latte 8.5
```

### Forgetting the quotes around a key

<!-- error -->
```python
contact = {"name": "Ana", "phone": "555-0101"}
print(contact[name])
```

```text
Traceback (most recent call last):
NameError: name 'name' is not defined
```

Without quotes, `name` is a variable, and there is no variable called `name`. The key is the string `"name"`, so it needs quotes: `contact["name"]`.

## Exercises

### Predict the output

#### Exercise 1: Reading values

What does this print? Write your answer before opening it.

<!-- no-verify -->
```python
plant = {"name": "Fern", "water_days": 3, "sun": "shade"}
print(plant["name"])
print(plant["water_days"] + 1)
print("sun" in plant)
print("Fern" in plant)
```

<details>
<summary>Show answer</summary>

```python
plant = {"name": "Fern", "water_days": 3, "sun": "shade"}
print(plant["name"])
print(plant["water_days"] + 1)
print("sun" in plant)
print("Fern" in plant)
```

Output:

```text
Fern
4
True
False
```

`"Fern"` is a value, not a key, and `in` only checks keys.

</details>

#### Exercise 2: Replace or add?

<!-- no-verify -->
```python
stock = {"apples": 4, "pears": 2}
stock["apples"] = 10
stock["plums"] = 5
stock["pears"] = stock["pears"] + 1
print(stock)
print(len(stock))
```

<details>
<summary>Show answer</summary>

```python
stock = {"apples": 4, "pears": 2}
stock["apples"] = 10
stock["plums"] = 5
stock["pears"] = stock["pears"] + 1
print(stock)
print(len(stock))
```

Output:

```text
{'apples': 10, 'pears': 3, 'plums': 5}
3
```

`"apples"` already existed, so its value was replaced. `"plums"` was new, so it was added at the end.

</details>

#### Exercise 3: `.get()` with and without a default

<!-- no-verify -->
```python
grades = {"Ana": 9, "Bruno": 7}
print(grades.get("Ana"))
print(grades.get("Carla"))
print(grades.get("Carla", 0))
```

<details>
<summary>Show answer</summary>

```python
grades = {"Ana": 9, "Bruno": 7}
print(grades.get("Ana"))
print(grades.get("Carla"))
print(grades.get("Carla", 0))
```

Output:

```text
9
None
0
```

</details>

### Fix the bug

#### Exercise 4: The broken menu

This program should print every drink with its price, but it crashes. Fix it.

<!-- no-verify -->
```python
menu = {"juice": 6.0, "water": 3.0}
for item, price in menu:
    print(f"{item} costs {price}")
```

<details>
<summary>Hint</summary>

Looping over a dictionary gives you only the keys. What method gives you key and value together?

</details>

<details>
<summary>Show answer</summary>

```python
menu = {"juice": 6.0, "water": 3.0}
for item, price in menu.items():
    print(f"{item} costs {price}")
```

Output:

```text
juice costs 6.0
water costs 3.0
```

</details>

#### Exercise 5: The missing city

This program crashes with a `KeyError`. Change one line so it prints `unknown` when the city is missing.

<!-- no-verify -->
```python
contact = {"name": "Bruno", "phone": "555-0199"}
print(contact["city"])
```

<details>
<summary>Show answer</summary>

```python
contact = {"name": "Bruno", "phone": "555-0199"}
print(contact.get("city", "unknown"))
```

Output:

```text
unknown
```

</details>

### Write it

#### Exercise 6: Your favorite movies

Create a dictionary where each key is a movie title and each value is the year it came out (use at least three movies). Then loop over it and print one line per movie, like `Up (2009)`.

<details>
<summary>Show answer</summary>

```python
movies = {"Up": 2009, "Coco": 2017, "Amelie": 2001}
for title, year in movies.items():
    print(f"{title} ({year})")
```

Output:

```text
Up (2009)
Coco (2017)
Amelie (2001)
```

</details>

#### Exercise 7: Counting colors

Given the list below, use a dictionary to count how many times each color appears, then print the dictionary.

<!-- no-verify -->
```python
colors = ["blue", "red", "blue", "green", "blue", "red"]
```

<details>
<summary>Hint</summary>

Start with an empty dictionary `counts = {}`. Inside the loop, use `counts.get(color, 0) + 1`.

</details>

<details>
<summary>Show answer</summary>

```python
colors = ["blue", "red", "blue", "green", "blue", "red"]
counts = {}
for color in colors:
    counts[color] = counts.get(color, 0) + 1
print(counts)
```

Output:

```text
{'blue': 3, 'red': 2, 'green': 1}
```

</details>

#### Exercise 8: The cheapest product

Below is a list of products. Write a loop that prints only the names of the products that cost less than 10.

<!-- no-verify -->
```python
products = [
    {"name": "Notebook", "price": 12.5},
    {"name": "Pencil", "price": 1.5},
    {"name": "Mug", "price": 9.0},
]
```

<details>
<summary>Show answer</summary>

```python
products = [
    {"name": "Notebook", "price": 12.5},
    {"name": "Pencil", "price": 1.5},
    {"name": "Mug", "price": 9.0},
]
for product in products:
    if product["price"] < 10:
        print(product["name"])
```

Output:

```text
Pencil
Mug
```

</details>

#### Exercise 9: Total of an order

Write a function `order_total(prices, order)` that receives a dictionary of prices and a list of items, and **returns** the total. Test it with the data below.

<!-- no-verify -->
```python
prices = {"espresso": 5.0, "latte": 8.5, "tea": 4.0}
order = ["latte", "tea", "latte"]
```

<details>
<summary>Show answer</summary>

```python
def order_total(prices, order):
    total = 0
    for item in order:
        total = total + prices[item]
    return total

prices = {"espresso": 5.0, "latte": 8.5, "tea": 4.0}
order = ["latte", "tea", "latte"]
print(order_total(prices, order))
```

Output:

```text
21.0
```

The function uses `return`, so whoever calls it decides what to do with the result. Here we print it.

</details>

## Review

#### Review 1: Lists and `enumerate` (module 02)

What does this print?

<!-- no-verify -->
```python
tasks = ["wash dishes", "buy bread", "call mom"]
for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")
```

<details>
<summary>Show answer</summary>

```python
tasks = ["wash dishes", "buy bread", "call mom"]
for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")
```

Output:

```text
1. wash dishes
2. buy bread
3. call mom
```

</details>

#### Review 2: Reading a file into a list (module 04)

You have a file `groceries.txt` with one item per line. Write a few lines that open it, read it, and turn its content into a list using `.splitlines()`. Then print how many items there are.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
with open("groceries.txt", "r", encoding="utf-8") as file:
    content = file.read()

items = content.splitlines()
print(f"There are {len(items)} items.")
```

`.read()` gives you one long string, and `.splitlines()` cuts it at every line break, giving you a list.

</details>

## Recap

- A dictionary stores `key: value` pairs inside `{}`. You find values by key, not by position.
- `d[key]` reads (and crashes with `KeyError` if the key is missing). `d.get(key, default)` reads safely.
- `d[key] = value` adds a new pair or replaces an existing value. `in` checks keys only.
- Loop with `for key, value in d.items():`.
- A list of dictionaries is how you store many records, like rows in a table.

**Next:** [Tuples and sets](tuples-and-sets.md)
