# Teacher's guide: Module 08, Objects
# Every example and exercise answer from this module's lessons, in order.
# Run it from this folder:  python guide.py

import json
from dataclasses import dataclass

print("=" * 50)
print("LESSON: classes.md")

# --------------------------------------------------
print("\n--- Example: an order as a dictionary")
# Start from what she knows: a dictionary. Then show the same thing as a class.
order = {"item": "latte", "size": "large", "price": 4.5}
print(order["item"], order["price"])

print("\n--- Example: the same order as a class")
# Class = recipe, object = the dish. Order(...) cooks one dish from the recipe.


class Order:
    def __init__(self, item, size, price):
        self.item = item
        self.size = size
        self.price = price


order = Order("latte", "large", 4.5)
print(order.item, order.price)

print("\n--- Example: what is self?")
# Ask: when we create `second`, does `first` change? self is "this one object".
first = Order("latte", "large", 4.5)
second = Order("espresso", "small", 2.0)
print(first.item)
print(second.item)

print("\n--- Example: methods, functions that belong to the object")


class Order:
    def __init__(self, item, size, price):
        self.item = item
        self.size = size
        self.price = price

    def describe(self):
        return f"{self.size} {self.item} for ${self.price}"


order = Order("latte", "large", 4.5)
print(order.describe())

print("\n--- Example: methods that change the object")
# Ask her to predict both prints before running.


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

print("\n--- Example: __str__ and __repr__")
# __str__ is for people (print). __repr__ is for programmers (shown inside lists).


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

print("\n--- Example: protecting the object with raise")


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

print("\n--- Example: a status that only moves forward")
# This is the same idea as the ceramic piece lifecycle in the final project.


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

print("\n--- Example: saving objects to and from a dictionary")


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

print("\n--- Example: a shortcut, @dataclass")


@dataclass
class Book:
    title: str
    author: str
    pages: int


book = Book("Dune", "Frank Herbert", 412)
print(book.title)
print(book)

# --------------------------------------------------
print("\n--- Mistake: forgetting self in a method")
# def describe():
#     return "an order"
# order.describe()
# TypeError: Order.describe() takes 0 positional arguments but 1 was given
# Python always passes the object itself as the first argument. Fixed:


class Order:
    def __init__(self, item):
        self.item = item

    def describe(self):
        return "an order"


order = Order("latte")
print(order.describe())

print("\n--- Mistake: forgetting self. when storing an attribute")
# def __init__(self, title):
#     title = title
# print(task.title)
# AttributeError: 'Task' object has no attribute 'title'
# Without self. the value lives only inside __init__. Fixed:


class Task:
    def __init__(self, title):
        self.title = title


task = Task("Buy coffee")
print(task.title)

print("\n--- Mistake: missing an argument when creating the object")
# class Order:
#     def __init__(self, item, price): ...
# order = Order("latte")
# TypeError: Order.__init__() missing 1 required positional argument: 'price'

print("\n--- Mistake: a typo in an attribute name")
# print(order.totl)
# AttributeError: 'Order' object has no attribute 'totl'. Did you mean: 'total'?

print("\n--- Mistake: calling a method without parentheses")
# Shows the method itself instead of running it (same idea as `read` vs `read()`).


class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def complete(self):
        self.done = True


task = Task("Buy coffee")
print(task.complete)
task.complete()
print(task.done)

# --------------------------------------------------
print("\n--- Exercise 1: two plants")
# Ask her to predict before running.


class Plant:
    def __init__(self, name, water_days):
        self.name = name
        self.water_days = water_days


fern = Plant("fern", 3)
cactus = Plant("cactus", 14)
print(cactus.name, cactus.water_days)
print(fern.water_days + cactus.water_days)

print("\n--- Exercise 2: changing state")
# Ask her to predict before running. Each object has its own value.


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

print("\n--- Exercise 3: __str__")
# Ask her to predict before running.


class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year})"


movie = Movie("Amélie", 2001)
print(movie)
print("My favorite: " + str(movie))

print("\n--- Exercise 4: the forgotten self")
# Broken version:  def greet():  ->  TypeError: Person.greet() takes 0 positional
# arguments but 1 was given. Fixed:


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}"


ana = Person("Ana")
print(ana.greet())

print("\n--- Exercise 5: the total that never changes")
# Broken version:  total = self.total + price   (no self.)  -> prints 0
# It does not crash: it creates a local variable and throws it away. Fixed:


class Cart:
    def __init__(self):
        self.total = 0

    def add(self, price):
        self.total = self.total + price


cart = Cart()
cart.add(5)
cart.add(2.5)
print(cart.total)

print("\n--- Exercise 6: a book with a description")


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        return f"{self.title} by {self.author}, {self.pages} pages"


book = Book("Dune", "Frank Herbert", 412)
print(book.describe())

print("\n--- Exercise 7: a bank account with rules")


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

print("\n--- Exercise 8: a recipe with stages")


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

print("\n--- Exercise 9: save and load a contact")


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

# --------------------------------------------------
print("\n--- Review 1: dictionaries (module 06)")
stock = {"flour": 2, "sugar": 0, "eggs": 6}
for name, amount in stock.items():
    if amount == 0:
        print(f"Buy more {name}")

print("\n--- Review 2: exceptions (module 07)")


def parse_age(text):
    try:
        return int(text)
    except ValueError:
        return None


print(parse_age("42"))
print(parse_age("forty"))

print("\n--- Review 3: comprehensions (module 06)")
# The loop version first, then the same thing as a list comprehension.
prices = [10, 25, 8, 40]
expensive = []
for price in prices:
    if price > 20:
        expensive.append(price)
print(expensive)

expensive = [price for price in prices if price > 20]
print(expensive)


print("\n" + "=" * 50)
print("LESSON: inheritance.md")

# --------------------------------------------------
print("\n--- Example: a parent class")


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        return f"{self.name}: ${self.price}"


pen = Product("pen", 1.5)
print(pen.describe())

print("\n--- Example: a child class")
# Food gets everything from Product for free, even with `pass`.


class Food(Product):
    pass


bread = Food("bread", 3.0)
print(bread.describe())

print("\n--- Example: adding something new with super().__init__")


class Food(Product):
    def __init__(self, name, price, expires):
        super().__init__(name, price)
        self.expires = expires


milk = Food("milk", 1.2, "2026-12-01")
print(milk.name, milk.price, milk.expires)

print("\n--- Example: changing a behavior, overriding")


class Food(Product):
    def __init__(self, name, price, expires):
        super().__init__(name, price)
        self.expires = expires

    def describe(self):
        return f"{self.name}: ${self.price} (expires {self.expires})"


items = [Product("pen", 1.5), Food("milk", 1.2, "2026-12-01")]
for item in items:
    print(item.describe())

print("\n--- Example: reusing the parent inside an override")


class Food(Product):
    def __init__(self, name, price, expires):
        super().__init__(name, price)
        self.expires = expires

    def describe(self):
        basic = super().describe()
        return f"{basic} (expires {self.expires})"


print(Food("milk", 1.2, "2026-12-01").describe())

print("\n--- Example: checking the kind of object, isinstance")
# Ask her to predict the three answers. A Food IS a Product, not the other way around.
pen = Product("pen", 1.5)
milk = Food("milk", 1.2, "2026-12-01")
print(isinstance(milk, Food))
print(isinstance(milk, Product))
print(isinstance(pen, Food))

# --------------------------------------------------
print("\n--- Mistake: forgetting to call super().__init__")
# class Food(Product):
#     def __init__(self, name, price, expires):
#         self.expires = expires
# print(milk.name)
# AttributeError: 'Food' object has no attribute 'name'

print("\n--- Mistake: passing self to super().__init__")
# super().__init__(self, name, price)
# TypeError: Product.__init__() takes 3 positional arguments but 4 were given

print("\n--- Mistake: using inheritance for 'has a'")
# class Order(Customer):   # an order is NOT a customer
# Fixed: an order HAS a customer, so it is an attribute.


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

# --------------------------------------------------
print("\n--- Exercise 1: who answers?")
# Ask her to predict before running. Fish has no sound(), so it uses Animal's.


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

print("\n--- Exercise 2: isinstance")
# Ask her to predict before running.


class Vehicle:
    pass


class Bike(Vehicle):
    pass


bike = Bike()
car = Vehicle()
print(isinstance(bike, Vehicle), isinstance(car, Bike))

print("\n--- Exercise 3: the missing title")
# Broken version has no super().__init__(title):
# AttributeError: 'Podcast' object has no attribute 'title'. Fixed:


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

print("\n--- Exercise 4: employees and managers")


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

print("\n--- Exercise 5: inherit or not?")
# Answer (talk it through, no code):
# 1. Book and Ebook: subclass. An ebook IS a book.
# 2. Car and Wheel: attribute. A car HAS wheels: self.wheels = [...]
# 3. Coffee and LargeCoffee: neither. Size is just an attribute: Coffee(size="large").
print("1. subclass   2. attribute   3. neither (size is an attribute)")

# --------------------------------------------------
print("\n--- Review 1: classes (previous file)")
# Ask her to predict: three toggles starting from False.


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

print("\n--- Review 2: modules (module 07)")
# Answer: if Product lives in shop.py, next to this file:
# from shop import Product
print("from shop import Product")
