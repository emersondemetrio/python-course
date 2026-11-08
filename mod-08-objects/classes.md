# Classes and objects

> **In one sentence:** a class is a template that describes what some kind of thing knows (its data) and what it can do (its behavior), and an object is one real thing made from that template.

## Why it matters

Until now, you kept data in one place (variables, lists, dictionaries) and behavior in another (functions). When a program grows, you start passing the same dictionary to ten different functions, and it gets hard to know which functions belong to which data. A class puts the data and the functions that work on that data in the same box. Most Python programs you will read, and the libraries you will use, are built from classes.

## Analogy

Think of a **recipe** and a **dish**. The recipe for a chocolate cake says what ingredients a cake has and what steps to follow. It is not a cake: you cannot eat it. When you follow the recipe, you get a cake. If you follow it three times, you get three cakes. They come from the same recipe, but each one is its own cake: you can put candles on one and leave the others plain.

A **class** is the recipe. An **object** is a cake. Python programmers also say "an object is an **instance** of a class", which just means "one cake made from that recipe".

## The idea, step by step

### From dictionary to class

You already know how to describe a coffee order with a dictionary:

```python
order = {"item": "latte", "size": "large", "price": 4.5}
print(order["item"], order["price"])
```

Output:

```text
latte 4.5
```

Here is the same thing as a class:

```python
class Order:
    def __init__(self, item, size, price):
        self.item = item
        self.size = size
        self.price = price

order = Order("latte", "large", 4.5)
print(order.item, order.price)
```

Output:

```text
latte 4.5
```

Line by line:

- `class Order:` starts the recipe. Class names use **CapitalizedWords** (this style is called *CamelCase*), so you can tell a class from a function at a glance.
- `def __init__(self, item, size, price):` is a special function inside the class. Python runs it automatically every time you create a new object. Its name is "init" (short for *initialize*) with two underscores on each side. Programmers read `__init__` as "dunder init" (dunder = **d**ouble **under**score).
- `self.item = item` stores the value inside the object. A value stored inside an object is called an **attribute**.
- `Order("latte", "large", 4.5)` creates a new object. You call the class like a function. Notice you do NOT pass `self`: Python does that for you.
- `order.item` reads an attribute with a dot, instead of `order["item"]` with brackets.

### What is `self`?

`self` is the object that is being built or used right now. When you write `Order("latte", "large", 4.5)`, Python creates an empty object and passes it to `__init__` as `self`. So `self.item = item` means "put the item inside **this** object".

Two objects, each with its own data:

```python
class Order:
    def __init__(self, item, size, price):
        self.item = item
        self.size = size
        self.price = price

first = Order("latte", "large", 4.5)
second = Order("espresso", "small", 2.0)
print(first.item)
print(second.item)
```

Output:

```text
latte
espresso
```

Same recipe, two different cakes.

### Methods: functions that belong to the object

A function written inside a class is called a **method**. Its first parameter is always `self`, so it can read the object's attributes.

```python
class Order:
    def __init__(self, item, size, price):
        self.item = item
        self.size = size
        self.price = price

    def describe(self):
        return f"{self.size} {self.item} for ${self.price}"

order = Order("latte", "large", 4.5)
print(order.describe())
```

Output:

```text
large latte for $4.5
```

You define `describe(self)` with `self`, but you call it as `order.describe()` with nothing inside the parentheses. Python fills in `self` with `order`.

### Methods that change the object

A method can also change the object's attributes. Here a to-do task can be marked as done:

```python
class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def complete(self):
        self.done = True

task = Task("Buy coffee")
print(task.done)
task.complete()
print(task.done)
```

Output:

```text
False
True
```

Notice `self.done = False` in `__init__`: an attribute does not have to come from a parameter. You can give it a starting value.

### Making objects print nicely: `__str__` and `__repr__`

If you print an object without preparing it, you get something unhelpful, like `<__main__.Task object at 0x7f3a2c1b9e50>` (the numbers change every time). You can tell Python how to show your object with two more special methods:

- `__str__`: the friendly text for people. Used by `print()` and `str()`.
- `__repr__`: the precise text for programmers. Used when you look at the object inside a list, or in the interactive Python prompt.

```python
class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def __str__(self):
        mark = "x" if self.done else " "
        return f"[{mark}] {self.title}"

    def __repr__(self):
        return f"Task({self.title!r})"

task = Task("Buy coffee")
print(task)
print([task])
```

Output:

```text
[ ] Buy coffee
[Task('Buy coffee')]
```

The `!r` inside the f-string means "show this value the way a programmer would type it", so the text gets quotes around it.

### Protecting the object with `raise`

An object is a good place to put rules. If something does not make sense, the method can refuse with `raise`, just like you learned in module 07.

```python
class Order:
    def __init__(self, item, price):
        if price <= 0:
            raise ValueError("price must be greater than zero")
        self.item = item
        self.price = price

order = Order("latte", 4.5)
print(order.price)

try:
    Order("free coffee", 0)
except ValueError as error:
    print("Could not create order:", error)
```

Output:

```text
4.5
Could not create order: price must be greater than zero
```

Now it is impossible to create an order with a wrong price. Anyone who uses your class gets this protection for free.

### A status that only moves forward

Many real things go through stages in a fixed order. A delivery order is **placed**, then **paid**, then **shipped**, then **delivered**. It should never go backwards, and it should never skip a stage. A class is perfect for this.

```python
class Order:
    STAGES = ["placed", "paid", "shipped", "delivered"]

    def __init__(self, item):
        self.item = item
        self.status = "placed"

    def advance(self):
        position = Order.STAGES.index(self.status)
        if position == len(Order.STAGES) - 1:
            raise ValueError(f"order is already {self.status}")
        self.status = Order.STAGES[position + 1]

order = Order("coffee beans")
print(order.status)
order.advance()
print(order.status)
order.advance()
order.advance()
print(order.status)

try:
    order.advance()
except ValueError as error:
    print("Error:", error)
```

Output:

```text
placed
paid
delivered
Error: order is already delivered
```

What is new here:

- `STAGES = [...]` is written directly in the class, not inside `__init__`. It is a **class attribute**: one value shared by all orders. Every order uses the same list of stages, so it does not need its own copy. You read it with `Order.STAGES`.
- `advance()` finds the current position in the list and moves to the next one. There is no way to go back or jump ahead, because the only way to change the status is through `advance()`.

The final project uses exactly this idea for ceramic pieces.

### Saving objects: to and from a dictionary

JSON (module 06) does not know about your classes. It only knows dictionaries, lists, text, numbers, `True`/`False` and `None`. So to save an object, you turn it into a dictionary. To load it, you build an object from the dictionary.

```python
import json

class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def to_dict(self):
        return {"title": self.title, "done": self.done}

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["done"])

task = Task("Water the plants")
text = json.dumps(task.to_dict())
print(text)

loaded = Task.from_dict(json.loads(text))
print(loaded.title, loaded.done)
```

Output:

```text
{"title": "Water the plants", "done": false}
Water the plants False
```

- `to_dict` is a normal method.
- `from_dict` has `@classmethod` written above it. That line is a **decorator** (a label that changes how the function works). Here it means: "this method belongs to the class, not to one object". It receives the class itself as `cls` instead of an object as `self`, because there is no object yet: we are about to create one. `cls(...)` is the same as `Task(...)`.

### Class or dictionary?

You do not need a class for everything. A simple rule:

- Use a **dictionary** when you just need to hold a few values together and pass them around (for example, a row of settings, or data you just read from JSON).
- Use a **class** when the data has **rules** (a price must be positive, a status must follow an order) or **behavior** (it can be completed, advanced, described).

If you find yourself writing many functions that all receive the same kind of dictionary, that is a sign it wants to be a class.

### A shortcut: `@dataclass`

Writing `__init__` with many `self.x = x` lines gets repetitive. Python has a shortcut in the standard library called **dataclass**:

```python
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int

book = Book("Dune", "Frank Herbert", 412)
print(book.title)
print(book)
```

Output:

```text
Dune
Book(title='Dune', author='Frank Herbert', pages=412)
```

The `@dataclass` decorator writes `__init__` and `__repr__` for you, based on the list of attributes. The `: str` and `: int` parts are **type hints** (notes about what kind of value is expected; Python does not enforce them). You can still add your own methods. Learn normal classes first; use dataclasses once you are comfortable.

## Common mistakes

### Forgetting `self` in a method

<!-- error -->
```python
class Order:
    def __init__(self, item):
        self.item = item

    def describe():
        return "an order"

order = Order("latte")
order.describe()
```

```text
TypeError: Order.describe() takes 0 positional arguments but 1 was given
```

Python always passes the object as the first argument to a method. The method was defined with no parameters, so there is nowhere to put it. The message says "1 was given" even though the parentheses look empty: that "1" is the hidden `self`. Fix: always write `self` as the first parameter.

```python
class Order:
    def __init__(self, item):
        self.item = item

    def describe(self):
        return "an order"

order = Order("latte")
print(order.describe())
```

```text
an order
```

### Forgetting `self.` when storing an attribute

<!-- error -->
```python
class Task:
    def __init__(self, title):
        title = title

task = Task("Buy coffee")
print(task.title)
```

```text
AttributeError: 'Task' object has no attribute 'title'
```

`title = title` only creates a normal variable inside `__init__`, which disappears when `__init__` ends. Nothing was stored in the object. Fix: `self.title = title`.

```python
class Task:
    def __init__(self, title):
        self.title = title

task = Task("Buy coffee")
print(task.title)
```

```text
Buy coffee
```

### Missing an argument when creating the object

<!-- error -->
```python
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

order = Order("latte")
```

```text
TypeError: Order.__init__() missing 1 required positional argument: 'price'
```

Creating an object calls `__init__`, so you must pass every parameter after `self`. Fix: `Order("latte", 4.5)`, or give the parameter a default value: `def __init__(self, item, price=0):`.

### A typo in an attribute name

<!-- error -->
```python
class Order:
    def __init__(self, item, total):
        self.item = item
        self.total = total

order = Order("latte", 4.5)
print(order.totl)
```

```text
AttributeError: 'Order' object has no attribute 'totl'. Did you mean: 'total'?
```

Python reads the attribute name exactly as you typed it. Recent versions of Python even suggest the name you probably meant. Fix the spelling: `order.total`.

### Calling a method without parentheses

<!-- no-verify -->
```python
task = Task("Buy coffee")
print(task.complete)
```

```console
<bound method Task.complete of <__main__.Task object at 0x7f3a2c1b9e50>>
```

There is no error, which makes this one sneaky. Without `()`, you are not calling the method, you are just pointing at it (you saw the same thing with `read` and `read()` when working with files). Nothing happens to the task. Fix: `task.complete()`.

## Exercises

### Predict the output

#### Exercise 1: Two plants

```python
class Plant:
    def __init__(self, name, water_days):
        self.name = name
        self.water_days = water_days

fern = Plant("fern", 3)
cactus = Plant("cactus", 14)
print(cactus.name, cactus.water_days)
print(fern.water_days + cactus.water_days)
```

<details>
<summary>Show answer</summary>

```text
cactus 14
17
```

Each object keeps its own attributes. `fern.water_days` is 3 and `cactus.water_days` is 14.

</details>

#### Exercise 2: Changing state

```python
class Counter:
    def __init__(self):
        self.value = 0

    def add(self):
        self.value = self.value + 1

a = Counter()
b = Counter()
a.add()
a.add()
b.add()
print(a.value, b.value)
```

<details>
<summary>Show answer</summary>

```text
2 1
```

`a` and `b` are separate objects. Calling `add()` on `a` does not touch `b`.

</details>

#### Exercise 3: `__str__`

```python
class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year})"

movie = Movie("Amélie", 2001)
print(movie)
print("My favorite: " + str(movie))
```

<details>
<summary>Show answer</summary>

```text
Amélie (2001)
My favorite: Amélie (2001)
```

Both `print()` and `str()` use `__str__`.

</details>

### Fix the bug

#### Exercise 4: The forgotten self

This should print `Hello, I am Ana`, but it crashes. Fix it.

<!-- error -->
```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet():
        return f"Hello, I am {self.name}"

ana = Person("Ana")
print(ana.greet())
```

```text
TypeError: Person.greet() takes 0 positional arguments but 1 was given
```

<details>
<summary>Hint</summary>

Every method needs a first parameter to receive the object.

</details>

<details>
<summary>Show answer</summary>

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}"

ana = Person("Ana")
print(ana.greet())
```

```text
Hello, I am Ana
```

`greet` needs `self` so it can read `self.name`.

</details>

#### Exercise 5: The total that never changes

This shopping cart should print `7.5`, but it prints `0`. Find the bug.

```python
class Cart:
    def __init__(self):
        self.total = 0

    def add(self, price):
        total = self.total + price

cart = Cart()
cart.add(5)
cart.add(2.5)
print(cart.total)
```

```text
0
```

<details>
<summary>Show answer</summary>

```python
class Cart:
    def __init__(self):
        self.total = 0

    def add(self, price):
        self.total = self.total + price

cart = Cart()
cart.add(5)
cart.add(2.5)
print(cart.total)
```

```text
7.5
```

`total = ...` created a temporary variable inside the method. To change the object, you must write `self.total = ...`.

</details>

### Write it

#### Exercise 6: A book with a description

Write a class `Book` with attributes `title`, `author` and `pages`, and a method `describe()` that returns text like `Dune by Frank Herbert, 412 pages`. Create one book and print its description.

<details>
<summary>Show answer</summary>

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

book = Book("Dune", "Frank Herbert", 412)
print(book.describe())
```

```text
Dune by Frank Herbert, 412 pages
```

</details>

#### Exercise 7: A bank account with rules

Write a class `Account` that starts with a `balance` of 0. Add:

- `deposit(amount)`: adds to the balance. If `amount` is 0 or less, `raise ValueError("deposit must be positive")`.
- `withdraw(amount)`: subtracts from the balance. If there is not enough money, `raise ValueError("not enough money")`.

Test it: deposit 100, withdraw 30, print the balance, then try to withdraw 500 and print the error message.

<details>
<summary>Show answer</summary>

```python
class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("not enough money")
        self.balance = self.balance - amount

account = Account()
account.deposit(100)
account.withdraw(30)
print(account.balance)

try:
    account.withdraw(500)
except ValueError as error:
    print("Error:", error)
```

```text
70
Error: not enough money
```

</details>

#### Exercise 8: A recipe with stages

A cake goes through these stages in order: `"mixing"`, `"baking"`, `"cooling"`, `"ready"`. Write a class `Cake` with a `name` and a `stage` that starts at `"mixing"`, and a method `next_stage()` that moves to the next stage. If the cake is already `"ready"`, it must `raise ValueError("cake is already ready")`. Add a `__str__` that returns text like `Carrot cake: baking`.

<details>
<summary>Hint</summary>

Look at the `Order` example with `STAGES` and `.index()`.

</details>

<details>
<summary>Show answer</summary>

```python
class Cake:
    STAGES = ["mixing", "baking", "cooling", "ready"]

    def __init__(self, name):
        self.name = name
        self.stage = "mixing"

    def next_stage(self):
        position = Cake.STAGES.index(self.stage)
        if position == len(Cake.STAGES) - 1:
            raise ValueError("cake is already ready")
        self.stage = Cake.STAGES[position + 1]

    def __str__(self):
        return f"{self.name}: {self.stage}"

cake = Cake("Carrot cake")
cake.next_stage()
print(cake)
cake.next_stage()
cake.next_stage()
print(cake)

try:
    cake.next_stage()
except ValueError as error:
    print("Error:", error)
```

```text
Carrot cake: baking
Carrot cake: ready
Error: cake is already ready
```

</details>

#### Exercise 9: Save and load a contact

Write a class `Contact` with `name` and `phone`. Add `to_dict()` and a `@classmethod` called `from_dict(cls, data)`. Then turn a contact into JSON text, print it, load it back into a new object and print the name.

<details>
<summary>Show answer</summary>

```python
import json

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def to_dict(self):
        return {"name": self.name, "phone": self.phone}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["phone"])

contact = Contact("Bruno", "555-0101")
text = json.dumps(contact.to_dict())
print(text)

copy = Contact.from_dict(json.loads(text))
print(copy.name)
```

```text
{"name": "Bruno", "phone": "555-0101"}
Bruno
```

</details>

## Review

#### Review 1: Dictionaries (module 06)

What does this print?

```python
stock = {"flour": 2, "sugar": 0, "eggs": 6}
for name, amount in stock.items():
    if amount == 0:
        print(f"Buy more {name}")
```

<details>
<summary>Show answer</summary>

```text
Buy more sugar
```

`.items()` gives you each key and value as a pair. Only `sugar` has 0.

</details>

#### Review 2: Exceptions (module 07)

What does this print?

```python
def parse_age(text):
    try:
        return int(text)
    except ValueError:
        return None

print(parse_age("42"))
print(parse_age("forty"))
```

<details>
<summary>Show answer</summary>

```text
42
None
```

`int("forty")` raises `ValueError`, which is caught, so the function returns `None`.

</details>

#### Review 3: Comprehensions (module 06)

Rewrite this loop as a list comprehension and print the result.

```python
prices = [10, 25, 8, 40]
expensive = []
for price in prices:
    if price > 20:
        expensive.append(price)
print(expensive)
```

<details>
<summary>Show answer</summary>

```python
prices = [10, 25, 8, 40]
expensive = [price for price in prices if price > 20]
print(expensive)
```

```text
[25, 40]
```

</details>

## Recap

- A **class** is a template (the recipe); an **object** is one thing made from it (the cake).
- `__init__` runs when you create an object; `self.name = value` stores an **attribute** in that object.
- A **method** is a function inside a class; its first parameter is always `self`, but you never pass it yourself.
- `__str__` controls what `print()` shows; methods can protect the object with `raise`.
- Use a class when the data has rules or behavior; a dictionary is fine for just holding values.

**Next:** [inheritance.md](inheritance.md)
