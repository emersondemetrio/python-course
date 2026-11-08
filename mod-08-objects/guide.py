"""Teacher's guide for module 08: Objects.

Every example and every exercise answer from this module's lessons, ready to
show in class. Each item prints its own code and then runs it.

Usage (from this folder):
    uv run guide.py                  list sections and items
    uv run guide.py classes          run every item in a section
    uv run guide.py classes.ex07     run one item
    uv run guide.py all              run everything
"""

# Lesson code is copied as-is: long SQL lines and the unused variables in the
# "Common mistakes" items are intentional.
# ruff: noqa: E501, F841

import builtins
import contextlib
import inspect
import os
import sys
import tempfile
import textwrap

SECTIONS: dict[str, dict[str, tuple]] = {}


def item(section, name, note="", run=True):
    """Register a function as a guide item: `section.name`, with a teaching note.

    Use run=False for code that should only be shown (servers, network, API keys,
    third-party libraries): the guide prints it without executing it.
    """

    def register(fn):
        SECTIONS.setdefault(section, {})[name] = (fn, note, run)
        return fn

    return register


@contextlib.contextmanager
def typed(*answers):
    """Simulate a person typing `answers` into input(), echoing them like a terminal."""
    queue = list(answers)
    original = builtins.input

    def fake_input(prompt=""):
        value = queue.pop(0)
        print(f"{prompt}{value}")
        return value

    builtins.input = fake_input
    try:
        yield
    finally:
        builtins.input = original


@contextlib.contextmanager
def scratch_folder():
    """Run file examples inside a throwaway folder, so nothing is left behind."""
    previous = os.getcwd()
    with tempfile.TemporaryDirectory() as folder:
        os.chdir(folder)
        try:
            yield folder
        finally:
            os.chdir(previous)


def show(section, name):
    fn, note, run = SECTIONS[section][name]
    source = inspect.getsource(fn)
    body = source.split(":\n", 1)[1] if source.lstrip().startswith(("@", "def")) else source
    body = textwrap.dedent(body.split('"""', 2)[-1] if fn.__doc__ else body).strip("\n")
    title = fn.__doc__.strip() if fn.__doc__ else name
    print(f"\n=== {section}.{name}: {title}")
    if note:
        print(f"Teacher note: {note}")
    print("--- code")
    print(body)
    if not run:
        print("--- (shown only: run it in a project, see the lesson)")
        return
    print("--- output")
    try:
        fn()
    except Exception as error:  # noqa: BLE001 - broken-on-purpose examples show their error
        print(f"{type(error).__name__}: {error}")


def main(args):
    if not args:
        for section, items in SECTIONS.items():
            print(f"{section}: {', '.join(items)}")
        return
    target = args[0]
    if target == "all":
        for section, items in SECTIONS.items():
            for name in items:
                show(section, name)
        return
    section, _, name = target.partition(".")
    if section not in SECTIONS or (name and name not in SECTIONS[section]):
        print(f"Unknown item: {target}. Run without arguments to see the list.")
        sys.exit(1)
    for each in [name] if name else SECTIONS[section]:
        show(section, each)


# --- classes ---------------------------------------------------------------


@item("classes", "dict_version", "Start from what she knows: a dictionary.")
def classes_dict_version():
    """From dictionary to class"""
    order = {"item": "latte", "size": "large", "price": 4.5}
    print(order["item"], order["price"])


@item("classes", "class_version", "Same data as a class. Compare order['item'] with order.item.")
def classes_class_version():
    """From dictionary to class"""

    class Order:
        def __init__(self, item, size, price):
            self.item = item
            self.size = size
            self.price = price

    order = Order("latte", "large", 4.5)
    print(order.item, order.price)


@item("classes", "what_is_self", "Same recipe, two cakes: each object keeps its own data.")
def classes_what_is_self():
    """What is self?"""

    class Order:
        def __init__(self, item, size, price):
            self.item = item
            self.size = size
            self.price = price

    first = Order("latte", "large", 4.5)
    second = Order("espresso", "small", 2.0)
    print(first.item)
    print(second.item)


@item("classes", "methods", "Defined with self, called with empty parentheses.")
def classes_methods():
    """Methods: functions that belong to the object"""

    class Order:
        def __init__(self, item, size, price):
            self.item = item
            self.size = size
            self.price = price

        def describe(self):
            return f"{self.size} {self.item} for ${self.price}"

    order = Order("latte", "large", 4.5)
    print(order.describe())


@item("classes", "methods_change_state", "done starts as False without coming from a parameter.")
def classes_methods_change_state():
    """Methods that change the object"""

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


@item("classes", "str_and_repr", "First print without __str__ to show the ugly default text.")
def classes_str_and_repr():
    """Making objects print nicely: __str__ and __repr__"""

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


@item(
    "classes", "protect_with_raise", "The class refuses bad data: nobody can create a free order."
)
def classes_protect_with_raise():
    """Protecting the object with raise"""

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


@item(
    "classes", "status_moves_forward", "The same idea as the ceramics stages in the final project."
)
def classes_status_moves_forward():
    """A status that only moves forward"""

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


@item("classes", "to_and_from_dict", "JSON only knows dicts; cls is the class itself.")
def classes_to_and_from_dict():
    """Saving objects: to and from a dictionary"""
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


@item("classes", "dataclass", "Optional shortcut. Teach plain classes first.")
def classes_dataclass():
    """A shortcut: @dataclass"""
    from dataclasses import dataclass

    @dataclass
    class Book:
        title: str
        author: str
        pages: int

    book = Book("Dune", "Frank Herbert", 412)
    print(book.title)
    print(book)


@item(
    "classes",
    "mistake_no_self_param",
    "Ask why it says 1 was given. In a normal file the message names the class directly (no <locals>).",
)
def classes_mistake_no_self_param():
    """Forgetting self in a method"""

    class Order:
        def __init__(self, item):
            self.item = item

        def describe():
            return "an order"

    order = Order("latte")
    order.describe()


@item("classes", "mistake_no_self_param_fix", "The fixed version.")
def classes_mistake_no_self_param_fix():
    """Forgetting self in a method (fixed)"""

    class Order:
        def __init__(self, item):
            self.item = item

        def describe(self):
            return "an order"

    order = Order("latte")
    print(order.describe())


@item("classes", "mistake_no_self_dot", "title = title only makes a local variable.")
def classes_mistake_no_self_dot():
    """Forgetting self. when storing an attribute"""

    class Task:
        def __init__(self, title):
            title = title

    task = Task("Buy coffee")
    print(task.title)


@item("classes", "mistake_no_self_dot_fix", "The fixed version.")
def classes_mistake_no_self_dot_fix():
    """Forgetting self. when storing an attribute (fixed)"""

    class Task:
        def __init__(self, title):
            self.title = title

    task = Task("Buy coffee")
    print(task.title)


@item(
    "classes",
    "mistake_missing_argument",
    "Creating an object calls __init__. In a normal file the message names the class directly (no <locals>).",
)
def classes_mistake_missing_argument():
    """Missing an argument when creating the object"""

    class Order:
        def __init__(self, item, price):
            self.item = item
            self.price = price

    order = Order("latte")


@item("classes", "mistake_attribute_typo", "Point out the 'Did you mean' hint.")
def classes_mistake_attribute_typo():
    """A typo in an attribute name"""

    class Order:
        def __init__(self, item, total):
            self.item = item
            self.total = total

    order = Order("latte", 4.5)
    print(order.totl)


@item(
    "classes",
    "mistake_no_parentheses",
    "No error: it only points at the method, like read vs read().",
)
def classes_mistake_no_parentheses():
    """Calling a method without parentheses"""

    class Task:
        def __init__(self, title):
            self.title = title
            self.done = False

        def complete(self):
            self.done = True

    task = Task("Buy coffee")
    print(task.complete)
    print(task.done)


@item("classes", "ex01", "Ask her to predict the output before running.")
def classes_ex01():
    """Exercise 1: Two plants"""

    class Plant:
        def __init__(self, name, water_days):
            self.name = name
            self.water_days = water_days

    fern = Plant("fern", 3)
    cactus = Plant("cactus", 14)
    print(cactus.name, cactus.water_days)
    print(fern.water_days + cactus.water_days)


@item("classes", "ex02", "Ask her to predict the output before running.")
def classes_ex02():
    """Exercise 2: Changing state"""

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


@item("classes", "ex03", "Ask her to predict the output before running.")
def classes_ex03():
    """Exercise 3: __str__"""

    class Movie:
        def __init__(self, title, year):
            self.title = title
            self.year = year

        def __str__(self):
            return f"{self.title} ({self.year})"

    movie = Movie("Amélie", 2001)
    print(movie)
    print("My favorite: " + str(movie))


@item(
    "classes",
    "ex04",
    "Answer: the fixed code. In a normal file the message names the class directly (no <locals>).",
)
def classes_ex04():
    """Exercise 4: The forgotten self"""

    class Person:
        def __init__(self, name):
            self.name = name

        def greet(self):
            return f"Hello, I am {self.name}"

    ana = Person("Ana")
    print(ana.greet())


@item("classes", "ex05", "Answer: the fixed code. Show the broken version first.")
def classes_ex05():
    """Exercise 5: The total that never changes"""

    class Cart:
        def __init__(self):
            self.total = 0

        def add(self, price):
            self.total = self.total + price

    cart = Cart()
    cart.add(5)
    cart.add(2.5)
    print(cart.total)


@item("classes", "ex06", "Answer to Exercise 6.")
def classes_ex06():
    """Exercise 6: A book with a description"""

    class Book:
        def __init__(self, title, author, pages):
            self.title = title
            self.author = author
            self.pages = pages

        def describe(self):
            return f"{self.title} by {self.author}, {self.pages} pages"

    book = Book("Dune", "Frank Herbert", 412)
    print(book.describe())


@item("classes", "ex07", "Answer to Exercise 7.")
def classes_ex07():
    """Exercise 7: A bank account with rules"""

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


@item("classes", "ex08", "Answer to Exercise 8.")
def classes_ex08():
    """Exercise 8: A recipe with stages"""

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


@item("classes", "ex09", "Answer to Exercise 9.")
def classes_ex09():
    """Exercise 9: Save and load a contact"""
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


@item("classes", "review01", "Ask her to predict the output before running.")
def classes_review01():
    """Review 1: Dictionaries (module 06)"""
    stock = {"flour": 2, "sugar": 0, "eggs": 6}
    for name, amount in stock.items():
        if amount == 0:
            print(f"Buy more {name}")


@item("classes", "review02", "Ask her to predict the output before running.")
def classes_review02():
    """Review 2: Exceptions (module 07)"""

    def parse_age(text):
        try:
            return int(text)
        except ValueError:
            return None

    print(parse_age("42"))
    print(parse_age("forty"))


@item("classes", "review03", "Answer to Review 3.")
def classes_review03():
    """Review 3: Comprehensions (module 06)"""
    prices = [10, 25, 8, 40]
    expensive = [price for price in prices if price > 20]
    print(expensive)


# --- inheritance -----------------------------------------------------------


@item("inheritance", "a_parent_class", "A normal class: nothing new yet.")
def inheritance_a_parent_class():
    """A parent class"""

    class Product:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def describe(self):
            return f"{self.name}: ${self.price}"

    pen = Product("pen", 1.5)
    print(pen.describe())


@item("inheritance", "a_child_class", "Food has only pass, yet it can describe() itself.")
def inheritance_a_child_class():
    """A child class"""

    class Product:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def describe(self):
            return f"{self.name}: ${self.price}"

    class Food(Product):
        pass

    bread = Food("bread", 3.0)
    print(bread.describe())


@item(
    "inheritance", "super_init", "Parent stores name and price first, then the child adds expires."
)
def inheritance_super_init():
    """Adding something new with super().__init__"""

    class Product:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def describe(self):
            return f"{self.name}: ${self.price}"

    class Food(Product):
        def __init__(self, name, price, expires):
            super().__init__(name, price)
            self.expires = expires

    milk = Food("milk", 1.2, "2026-12-01")
    print(milk.name, milk.price, milk.expires)


@item("inheritance", "overriding", "The loop does not care which class each item is.")
def inheritance_overriding():
    """Changing a behavior: overriding"""

    class Product:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def describe(self):
            return f"{self.name}: ${self.price}"

    class Food(Product):
        def __init__(self, name, price, expires):
            super().__init__(name, price)
            self.expires = expires

        def describe(self):
            return f"{self.name}: ${self.price} (expires {self.expires})"

    items = [Product("pen", 1.5), Food("milk", 1.2, "2026-12-01")]
    for item in items:
        print(item.describe())


@item("inheritance", "reuse_parent_method", "Change the parent's text and food follows.")
def inheritance_reuse_parent_method():
    """Reusing the parent inside an override"""

    class Product:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def describe(self):
            return f"{self.name}: ${self.price}"

    class Food(Product):
        def __init__(self, name, price, expires):
            super().__init__(name, price)
            self.expires = expires

        def describe(self):
            basic = super().describe()
            return f"{basic} (expires {self.expires})"

    print(Food("milk", 1.2, "2026-12-01").describe())


@item("inheritance", "isinstance", "A Food is also a Product, but not the other way around.")
def inheritance_isinstance():
    """Checking the kind of object: isinstance"""

    class Product:
        pass

    class Food(Product):
        pass

    pen = Product()
    milk = Food()
    print(isinstance(milk, Food))
    print(isinstance(milk, Product))
    print(isinstance(pen, Food))


@item("inheritance", "mistake_no_super_init", "The child's __init__ replaced the parent's one.")
def inheritance_mistake_no_super_init():
    """Forgetting to call super().__init__"""

    class Product:
        def __init__(self, name, price):
            self.name = name
            self.price = price

    class Food(Product):
        def __init__(self, name, price, expires):
            self.expires = expires

    milk = Food("milk", 1.2, "2026-12-01")
    print(milk.name)


@item(
    "inheritance",
    "mistake_self_in_super",
    "super() already passes self. In a normal file the message names the class directly (no <locals>).",
)
def inheritance_mistake_self_in_super():
    """Passing self to super().__init__"""

    class Product:
        def __init__(self, name, price):
            self.name = name
            self.price = price

    class Food(Product):
        def __init__(self, name, price, expires):
            super().__init__(self, name, price)
            self.expires = expires

    milk = Food("milk", 1.2, "2026-12-01")


@item("inheritance", "mistake_has_a", "Runs fine: the problem is the design, not an error.")
def inheritance_mistake_has_a():
    """Using inheritance for 'has a'"""

    class Customer:
        def __init__(self, name):
            self.name = name

    class Order(Customer):  # an order is NOT a customer
        def __init__(self, name, item):
            super().__init__(name)
            self.item = item

    order = Order("Ana", "latte")
    print(order.name, order.item)


@item("inheritance", "mistake_has_a_fix", "An order HAS a customer: store it as an attribute.")
def inheritance_mistake_has_a_fix():
    """Using inheritance for 'has a' (fixed)"""

    class Customer:
        def __init__(self, name):
            self.name = name

    class Order:
        def __init__(self, customer, item):
            self.customer = customer
            self.item = item

    ana = Customer("Ana")
    order = Order(ana, "latte")
    print(order.customer.name, order.item)


@item("inheritance", "ex01", "Ask her to predict the output before running.")
def inheritance_ex01():
    """Exercise 1: Who answers?"""

    class Animal:
        def sound(self):
            return "..."

    class Dog(Animal):
        def sound(self):
            return "Woof"

    class Fish(Animal):
        pass

    for pet in [Dog(), Fish()]:
        print(pet.sound())


@item("inheritance", "ex02", "Ask her to predict the output before running.")
def inheritance_ex02():
    """Exercise 2: isinstance"""

    class Vehicle:
        pass

    class Bike(Vehicle):
        pass

    bike = Bike()
    car = Vehicle()
    print(isinstance(bike, Vehicle), isinstance(car, Bike))


@item("inheritance", "ex03", "Answer: the fixed code. Show the broken version first.")
def inheritance_ex03():
    """Exercise 3: The missing title"""

    class Media:
        def __init__(self, title):
            self.title = title

    class Podcast(Media):
        def __init__(self, title, minutes):
            super().__init__(title)
            self.minutes = minutes

        def describe(self):
            return f"Podcast: {self.title}, {self.minutes} min"

    episode = Podcast("Coffee Talk", 45)
    print(episode.describe())


@item("inheritance", "ex04", "Answer to Exercise 4.")
def inheritance_ex04():
    """Exercise 4: Employees and managers"""

    class Employee:
        def __init__(self, name, salary):
            self.name = name
            self.salary = salary

        def yearly(self):
            return self.salary * 12

    class Manager(Employee):
        def __init__(self, name, salary, bonus):
            super().__init__(name, salary)
            self.bonus = bonus

        def yearly(self):
            return super().yearly() + self.bonus

    print(Employee("Bia", 3000).yearly())
    print(Manager("Caio", 5000, 10000).yearly())


@item("inheritance", "ex05", "Answer to Exercise 5, shown as code. Ask for the reasons.")
def inheritance_ex05():
    """Exercise 5: Inherit or not?"""

    class Book:
        def __init__(self, title):
            self.title = title

    class Ebook(Book):  # 1. subclass: an ebook IS a book
        def __init__(self, title, size_mb):
            super().__init__(title)
            self.size_mb = size_mb

    class Wheel:
        pass

    class Car:  # 2. attribute: a car HAS wheels
        def __init__(self):
            self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]

    class Coffee:  # 3. neither: a large coffee is a coffee with another value
        def __init__(self, size):
            self.size = size

    print(Ebook("Dune", 2.5).title)
    print(len(Car().wheels))
    print(Coffee("large").size)


@item("inheritance", "review01", "Ask her to predict the output before running.")
def inheritance_review01():
    """Review 1: Classes (previous file)"""

    class Lamp:
        def __init__(self):
            self.on = False

        def toggle(self):
            self.on = not self.on

    lamp = Lamp()
    lamp.toggle()
    lamp.toggle()
    lamp.toggle()
    print(lamp.on)


@item(
    "inheritance",
    "review02",
    "Needs a shop.py file next to it: shown only. shop is the file name without .py.",
    run=False,
)
def inheritance_review02():
    """Review 2: Modules (module 07)"""
    from shop import Product  # noqa: F401


if __name__ == "__main__":
    main(sys.argv[1:])
