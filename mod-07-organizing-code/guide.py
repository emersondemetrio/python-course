# Teacher's guide: Module 07, Organizing code
# Every example and exercise answer from this module's lessons, in order.
# Run it from this folder:  python guide.py
# ruff: noqa: UP015, E501

import json
import math
import os
import random
from math import floor, pi, sqrt
from random import choice

print("=" * 50)
print("LESSON: modules.md")

print("\n--- Example: Importing a module that comes with Python")
print(math.sqrt(16))
print(math.pi > 3)

print("\n--- Example: Importing only what you need with from")
print(sqrt(25))
print(round(pi, 2))

print("\n--- Example: Your own module")
# Shown only, not run:
# # conversions.py
#
# GRAMS_PER_CUP = 120
#
# def cups_to_grams(cups):
#     return cups * GRAMS_PER_CUP
#
# def celsius_to_fahrenheit(celsius):
#     return celsius * 9 / 5 + 32

# Shown only, not run:
# # main.py
# import conversions
#
# flour = conversions.cups_to_grams(2)
# oven = conversions.celsius_to_fahrenheit(180)
#
# print(f"Flour: {flour} g")
# print(f"Oven: {oven} F")

# (console)
# PS C:\Users\you\Projects\recipes> python main.py
# Flour: 240 g
# Oven: 356.0 F

print("\n--- Example: if __name__ == '__main__':")
# Shown only, not run:
# # conversions.py
# def cups_to_grams(cups):
#     return cups * 120
#
# print("Testing:", cups_to_grams(1))

# (console)
# PS C:\Users\you\Projects\recipes> python main.py
# Testing: 120
# Flour: 240 g

# Shown only, not run:
# # conversions.py
# def cups_to_grams(cups):
#     return cups * 120
#
# if __name__ == "__main__":
#     print("Testing:", cups_to_grams(1))

print(__name__)

# Shown only, not run:
# # main.py
# import conversions
#
# def main():
#     print(f"Flour: {conversions.cups_to_grams(2)} g")
#
# if __name__ == "__main__":
#     main()

print("\n--- Example: Packages: folders of modules")
# Shown only, not run:
# # main.py
# from tools import conversions
# from tools.timers import minutes_to_seconds
#
# print(conversions.cups_to_grams(2))
# print(minutes_to_seconds(3))

print("\n--- Example: Exploring a module with dir() and help()")
names = [n for n in dir(math) if not n.startswith("_")]
print(names[:5])

print("\n--- Mistake: Naming your file like a Python module")
# Shown only, not run:
# # random.py  (your file)
# import random
# print(random.choice(["tea", "coffee"]))

# (console)
# PS C:\Users\you\Projects> python random.py
# AttributeError: module 'random' has no attribute 'choice' (consider renaming 'C:\Users\you\Projects\random.py' since it has the same name as the standard library module named 'random' and prevents importing that standard library module)

print("\n--- Mistake: Running from the wrong folder")
# (console)
# PS C:\Users\you\Projects> python main.py
# C:\Python312\python.exe: can't open file 'C:\\Users\\you\\Projects\\main.py': [Errno 2] No such file or directory

print("\n--- Mistake: Writing .py in the import")
# Breaks on purpose (do not run):
# import json.py
# ModuleNotFoundError: No module named 'json.py'

print("\n--- Mistake: Forgetting the module name")
# Breaks on purpose (do not run):
# import math
# print(sqrt(9))
# NameError: name 'sqrt' is not defined

# Ask her to predict the output before running.
print("\n--- Exercise 1: Two ways to import")
print(math.ceil(2.1))
print(floor(2.9))

# Ask her to predict the output before running.
print("\n--- Exercise 2: What runs on import?")
# Starting code given in the exercise (not run):
# # greetings.py
# def hello(name):
#     return f"Hello, {name}!"
#
# print("greetings loaded")
#
# if __name__ == "__main__":
#     print(hello("tester"))

# Starting code given in the exercise (not run):
# # app.py
# import greetings
#
# print(greetings.hello("Ana"))

# (console)
# PS C:\Users\you\Projects> python app.py
# greetings loaded
# Hello, Ana!

print("\n--- Exercise 3: Missing name")
# Starting code given in the exercise (not run):
# import random
# print(choice(["red", "green", "blue"]))

# Answer, option 1 (the color is random, so it changes each run):
print(choice(["red", "green", "blue"]))

# Answer, option 2:
print(random.choice(["red", "green", "blue"]))

print("\n--- Exercise 4: Your first module")
# Answer (not run here: needs other files, a library or the terminal):
# # prices.py
# def with_tax(price):
#     return price * 1.10
#
# def format_price(price):
#     return f"$ {price:.2f}"

# Answer (not run here: needs other files, a library or the terminal):
# # main.py
# import prices
#
# final = prices.with_tax(10)
# print(prices.format_price(final))

# (console)
# PS C:\Users\you\Projects\shop> python main.py
# $ 11.00

print("\n--- Exercise 5: Add a main()")
# Answer (not run here: needs other files, a library or the terminal):
# # prices.py
# def with_tax(price):
#     return price * 1.10
#
# def format_price(price):
#     return f"$ {price:.2f}"
#
# if __name__ == "__main__":
#     print(format_price(with_tax(100)))

# Answer (not run here: needs other files, a library or the terminal):
# # main.py
# import prices
#
# def main():
#     final = prices.with_tax(10)
#     print(prices.format_price(final))
#
# if __name__ == "__main__":
#     main()

print("\n--- Review 1: JSON (module 06)")


def load_notes():
    if not os.path.exists("notes.json"):
        return []
    with open("notes.json", "r", encoding="utf-8") as file:
        return json.load(file)


print(load_notes())

print("\n--- Review 2: Comprehensions (module 06)")
# Starting code given in the exercise (not run):
# files = ["main.py", "notes.txt", "prices.py", "photo.jpg"]
# python_files = []
# for f in files:
#     if f.endswith(".py"):
#         python_files.append(f)
# print(python_files)

files = ["main.py", "notes.txt", "prices.py", "photo.jpg"]
python_files = [f for f in files if f.endswith(".py")]
print(python_files)


print("=" * 50)
print("LESSON: exceptions.md")

print("\n--- Example: What an exception looks like")
# Breaks on purpose (do not run): "Start" prints, then the program stops.
# print("Start")
# number = int("twelve")
# print("End")
# ValueError: invalid literal for int() with base 10: 'twelve'

print("\n--- Example: Catching an exception with try and except")
text = "twelve"
try:
    number = int(text)
    print(f"You typed {number}")
except ValueError:
    print(f"'{text}' is not a number")
print("The program continues")

text = "12"
try:
    number = int(text)
    print(f"You typed {number}")
except ValueError:
    print(f"'{text}' is not a number")

print("\n--- Example: A classic use: asking until the input is valid")
# In the lesson the text comes from input(). Here we simulate her typing "two", then "2".
typed = ["two", "2"]
while True:
    # text = input("How many cups? ")
    text = typed.pop(0)
    print(f"How many cups? {text}")
    try:
        cups = int(text)
        break
    except ValueError:
        print("Please type a whole number, like 2.")

print(f"OK, {cups} cups.")

# (console)
# PS C:\Users\you\Projects> python cups.py
# How many cups? two
# Please type a whole number, like 2.
# How many cups? 2
# OK, 2 cups.

print("\n--- Example: Catch specific exceptions")
prices = {"latte": 8.5}

for item in ["latte", "mocha"]:
    try:
        print(f"{item}: {prices[item]}")
    except KeyError:
        print(f"{item}: not on the menu")


def read_age(text):
    try:
        age = int(text)
        return 100 / age
    except ValueError:
        return "not a number"
    except ZeroDivisionError:
        return "age cannot be zero"


print(read_age("abc"))
print(read_age("0"))
print(read_age("50"))

print("\n--- Example: Never catch everything blindly")
# Shown only, not run:
# try:
#     total = price * quantity
# except:
#     print("Something went wrong")

print("\n--- Example: else and finally")


def convert(text):
    try:
        number = int(text)
    except ValueError:
        print(f"{text}: invalid")
    else:
        print(f"{text}: valid, doubled is {number * 2}")
    finally:
        print("  (checked)")


convert("7")
convert("seven")

print("\n--- Example: Raising your own exceptions with raise")


def divide(a, b):
    if b == 0:
        print("[error] cannot divide by zero")
        return 0
    return a / b


print(divide(0, 5))
print(divide(5, 0))


def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


print(divide(10, 4))

try:
    print(divide(5, 0))
except ValueError as error:
    print(f"Problem: {error}")

print("\n--- Example: Your own kind of exception (briefly)")


class OutOfStock(Exception):
    pass


def order(item, stock):
    if stock.get(item, 0) == 0:
        raise OutOfStock(f"{item} is sold out")
    stock[item] = stock[item] - 1
    return f"One {item}, coming up!"


stock = {"fish": 0, "chicken": 3}
for item in ["chicken", "fish"]:
    try:
        print(order(item, stock))
    except OutOfStock as error:
        print(f"Sorry: {error}")

print("\n--- Mistake: Catching the wrong exception type")
# Breaks on purpose (do not run):
# prices = {"latte": 8.5}
# try:
#     print(prices["mocha"])
# except ValueError:
#     print("Not on the menu")
# KeyError: 'mocha'

print("\n--- Mistake: Putting too much code inside try")
# Shown only, not run:
# try:
#     text = input("Quantity: ")
#     quantity = int(text)
#     total = quantity * pricee
#     print(total)
# except NameError:
#     print("Invalid quantity")

print("\n--- Mistake: Forgetting the parentheses with as")
# Breaks on purpose (do not run):
# try:
#     int("x")
# except ValueError, TypeError:
#     print("bad")
# SyntaxError: multiple exception types must be parenthesized

# Ask her to predict the output before running.
print("\n--- Exercise 1: Where does it stop?")
try:
    print("A")
    x = int("3")
    print("B")
    y = int("three")
    print("C")
except ValueError:
    print("D")
print("E")

# Ask her to predict the output before running.
print("\n--- Exercise 2: else and finally")
for text in ["5", "five"]:
    try:
        n = int(text)
    except ValueError:
        print("bad")
    else:
        print("good", n)
    finally:
        print("done")

print("\n--- Exercise 3: The fake zero")
# Starting code given in the exercise (not run):
# def average(numbers):
#     if len(numbers) == 0:
#         return 0
#     return sum(numbers) / len(numbers)


def average(numbers):
    if len(numbers) == 0:
        raise ValueError("cannot average an empty list")
    return sum(numbers) / len(numbers)


print(average([4, 6]))
try:
    print(average([]))
except ValueError as error:
    print(f"Problem: {error}")

print("\n--- Exercise 4: The wrong catch")
# Starting code given in the exercise (not run):
# temps = {"Lisbon": 22, "Oslo": 9}
# try:
#     print(temps["Paris"])
# except ValueError:
#     print("unknown city")

temps = {"Lisbon": 22, "Oslo": 9}
try:
    print(temps["Paris"])
except KeyError:
    print("unknown city")

print("\n--- Exercise 5: Safe conversion")


def to_number(text):
    try:
        return float(text)
    except ValueError:
        return None


print(to_number("3.5"))
print(to_number("7"))
print(to_number("abc"))

print("\n--- Exercise 6: Load a file safely")


def read_notes(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "(no notes yet)"


print(read_notes("notes.txt"))

print("\n--- Review 2: Dictionaries (module 06)")
# Starting code given in the exercise (not run):
# stock = {"apples": 3}
# try:
#     amount = stock["pears"]
# except KeyError:
#     amount = 0
# print(amount)

stock = {"apples": 3}
amount = stock.get("pears", 0)
print(amount)


print("=" * 50)
print("LESSON: uv-and-ruff.md")

print("\n--- Example: Installing uv")
# (powershell)
# powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# (bash)
# curl -LsSf https://astral.sh/uv/install.sh | sh

# (console)
# PS C:\Users\you> uv --version
# uv 0.11.32

print("\n--- Example: Installing Python with uv")
# (powershell)
# uv python install

print("\n--- Example: Creating a project: uv init")
# (console)
# PS C:\Users\you\Projects> uv init shop
# Initialized project `shop` at `C:\Users\you\Projects\shop`
# PS C:\Users\you\Projects> cd shop

print("\n--- Example: Running code: uv run")
# (console)
# PS C:\Users\you\Projects\shop> uv run main.py
# Using CPython 3.12.8
# Creating virtual environment at: .venv
# Hello from shop!

print("\n--- Example: Adding and removing libraries: uv add and uv remove")
# (console)
# PS C:\Users\you\Projects\shop> uv add requests
# Resolved 6 packages in 412ms
# Installed 5 packages in 38ms
#  + requests==2.32.3
#  ...

# (powershell)
# uv add --dev pytest

print("\n--- Example: Cloning someone's project: uv sync")
# (console)
# PS C:\Users\you\Projects> git clone https://github.com/someone/shop
# PS C:\Users\you\Projects> cd shop
# PS C:\Users\you\Projects\shop> uv sync

print("\n--- Example: A one-off: uv run --with")
# (powershell)
# uv run --with requests try_requests.py

print("\n--- Example: ruff: checking your code")
# (powershell)
# uv add --dev ruff

# Shown only, not run:
# # prices.py
# import random
#
#
# def with_tax(price):
#     total = price * 1.10
#     return round(price * 1.10, 2)

# (console)
# PS C:\Users\you\Projects\shop> uv run ruff check
# prices.py:2:8: F401 [*] `random` imported but unused
# prices.py:6:5: F841 Local variable `total` is assigned to but never used
# Found 2 errors.
# [*] 1 fixable with the `--fix` option.

# (powershell)
# uv run ruff check --fix

print("\n--- Example: ruff: formatting your code")
# Shown only, not run:
# def area(width,height):
#     return width*height
# items=['cup','plate']

# (powershell)
# uv run ruff format

# Shown only, not run:
# def area(width, height):
#     return width * height
#
#
# items = ["cup", "plate"]

print("\n--- Mistake: uv is not recognized")
# (console)
# PS C:\Users\you> uv --version
# uv : The term 'uv' is not recognized as the name of a cmdlet, function, script file, or operable program.

print("\n--- Mistake: Running with python instead of uv run")
# (console)
# PS C:\Users\you\Projects\shop> python try_requests.py
# ModuleNotFoundError: No module named 'requests'

# Ask her to predict the output before running.
print("\n--- Exercise 2: What changes in pyproject.toml?")
# (powershell)
# uv add requests
# uv add flask
# uv add --dev ruff
# uv remove requests

print("\n--- Exercise 4: The tutorial from the internet")
# (bash)
# python -m venv .venv
# source .venv/bin/activate
# pip install flask
# python app.py

# (powershell)
# uv init site
# cd site
# uv add flask
# uv run app.py

print("\n--- Exercise 5: It worked on my computer")
# (powershell)
# uv run main.py

print("\n--- Exercise 6: A project from zero")
# (powershell)
# uv init notes-app
# cd notes-app
# uv add requests
# uv add --dev ruff pytest
# uv run ruff check
# uv run ruff format

print("\n--- Exercise 7: Format by hand, then check")
# Starting code given in the exercise (not run):
# def total(prices,tax):
#     return sum(prices)*(1+tax)
# basket=[2.5,4.0,1.25]
# print(total(basket,0.1))


# Answer (the same code, formatted the way ruff would):
def total(prices, tax):
    return sum(prices) * (1 + tax)


basket = [2.5, 4.0, 1.25]
print(total(basket, 0.1))

print("\n--- Review 1: Exceptions (previous file)")


def parse_price(text):
    try:
        return float(text)
    except ValueError:
        return None


print(parse_price("4.50"))
print(parse_price("free"))

print("\n--- Review 2: Modules (this module)")
# Answer (not run here: needs other files, a library or the terminal):
# from prices import with_tax

# (powershell)
# uv run main.py


print("=" * 50)
print("LESSON: testing.md")

print("\n--- Example: assert: the smallest possible test")


def with_tax(price):
    return round(price * 1.10, 2)


assert with_tax(10) == 11.0
assert with_tax(0) == 0
print("All checks passed")

# Breaks on purpose (do not run):
# def with_tax(price):
#     return round(price * 1.01, 2)
#
# assert with_tax(10) == 11.0
# print("All checks passed")
# AssertionError

# Breaks on purpose (do not run):
# total = 10 + 10
# assert total == 30, f"expected 30, got {total}"
# AssertionError: expected 30, got 20

print("\n--- Example: pytest: a tool to run many tests")
# (powershell)
# uv add --dev pytest

print("\n--- Example: Writing tests for pytest")
# Shown only, not run:
# # prices.py
# def with_tax(price):
#     return round(price * 1.10, 2)
#
# def apply_discount(price, percent):
#     if percent < 0 or percent > 100:
#         raise ValueError("percent must be between 0 and 100")
#     return price - price * percent / 100

# Shown only, not run:
# # test_prices.py
# from prices import with_tax, apply_discount
#
# def test_with_tax_adds_ten_percent():
#     assert with_tax(10) == 11.0
#
# def test_discount_of_half():
#     assert apply_discount(80, 50) == 40
#
# def test_discount_of_zero_changes_nothing():
#     assert apply_discount(80, 0) == 80

print("\n--- Example: Running the tests")
# (console)
# PS C:\Users\you\Projects\shop> uv run pytest
# ============================= test session starts ==============================
# collected 3 items
#
# test_prices.py ...                                                       [100%]
#
# ============================== 3 passed in 0.02s ===============================

# (console)
# PS C:\Users\you\Projects\shop> uv run pytest -v
# test_prices.py::test_with_tax_adds_ten_percent PASSED                    [ 33%]
# test_prices.py::test_discount_of_half PASSED                             [ 66%]
# test_prices.py::test_discount_of_zero_changes_nothing PASSED             [100%]
#
# ============================== 3 passed in 0.02s ===============================

print("\n--- Example: When a test fails")
# (console)
# PS C:\Users\you\Projects\shop> uv run pytest
# collected 3 items
#
# test_prices.py F..                                                       [100%]
#
# =================================== FAILURES ===================================
# ________________________ test_with_tax_adds_ten_percent ________________________
#
#     def test_with_tax_adds_ten_percent():
# >       assert with_tax(10) == 11.0
# E       assert 10.1 == 11.0
# E        +  where 10.1 = with_tax(10)
#
# test_prices.py:4: AssertionError
# =========================== short test summary info ============================
# FAILED test_prices.py::test_with_tax_adds_ten_percent - assert 10.1 == 11.0
# ========================= 1 failed, 2 passed in 0.02s ==========================

print("\n--- Example: Testing that an error happens: pytest.raises")
# Shown only, not run:
# # test_prices.py
# import pytest
# from prices import apply_discount
#
# def test_discount_above_100_is_an_error():
#     with pytest.raises(ValueError):
#         apply_discount(80, 150)

print("\n--- Example: Many cases at once: parametrize (briefly)")
# Shown only, not run:
# import pytest
# from prices import apply_discount
#
# @pytest.mark.parametrize("price, percent, expected", [
#     (100, 10, 90),
#     (100, 50, 50),
#     (80, 25, 60),
#     (80, 0, 80),
# ])
# def test_apply_discount(price, percent, expected):
#     assert apply_discount(price, percent) == expected

print("\n--- Mistake: The test file or function does not start with test_")
# (console)
# PS C:\Users\you\Projects\shop> uv run pytest
# collected 0 items
#
# ============================ no tests ran in 0.01s =============================

print("\n--- Mistake: Comparing with = instead of ==")
# Breaks on purpose (do not run):
# assert 1 + 1 = 2
# SyntaxError: invalid syntax

print("\n--- Mistake: Calling the function outside pytest.raises")
# Shown only, not run:
# def test_discount_above_100_is_an_error():
#     result = apply_discount(80, 150)
#     with pytest.raises(ValueError):
#         print(result)

print("\n--- Mistake: pytest is not recognized")
# (console)
# PS C:\Users\you\Projects\shop> pytest
# pytest : The term 'pytest' is not recognized as the name of a cmdlet, function, script file, or operable program.

# Ask her to predict the output before running.
print("\n--- Exercise 1: Which asserts pass?")
# Starting code given in the exercise (not run):
# assert 2 * 3 == 6
# assert "tea".upper() == "Tea"
# assert len([1, 2, 3]) == 3
# assert 10 / 4 == 2
#
# Answer: line 2 and line 4 fail. "tea".upper() is "TEA", and 10 / 4 is 2.5.
# In a real run Python stops at the first failing assert (line 2).

# Ask her to predict the output before running.
print("\n--- Exercise 2: Read the report")
# (console)
# test_temps.py .F.                                                        [100%]
# ...
# FAILED test_temps.py::test_freezing_point - assert 0.0 == 32
# ========================= 1 failed, 2 passed in 0.01s ==========================

print("\n--- Exercise 3: Invisible tests")
# Starting code given in the exercise (not run):
# # checks.py
# from prices import with_tax
#
# def tax_of_ten():
#     assert with_tax(10) == 11.0

# Answer (not run here: needs other files, a library or the terminal):
# # test_prices.py
# from prices import with_tax
#
# def test_tax_of_ten():
#     assert with_tax(10) == 11.0

print("\n--- Exercise 4: Tests with plain assert")


def count_vowels(text):
    total = 0
    for letter in text.lower():
        if letter in "aeiou":
            total = total + 1
    return total


assert count_vowels("banana") == 3
assert count_vowels("") == 0
assert count_vowels("APPLE") == 2
print("ok")

print("\n--- Exercise 5: Your first pytest file")
# Answer (not run here: needs other files, a library or the terminal):
# # convert.py
# def celsius_to_fahrenheit(c):
#     return c * 9 / 5 + 32

# Answer (not run here: needs other files, a library or the terminal):
# # test_convert.py
# from convert import celsius_to_fahrenheit
#
# def test_water_freezes():
#     assert celsius_to_fahrenheit(0) == 32
#
# def test_water_boils():
#     assert celsius_to_fahrenheit(100) == 212
#
# def test_body_temperature():
#     assert round(celsius_to_fahrenheit(37), 1) == 98.6

# (console)
# PS C:\Users\you\Projects\temps> uv run pytest -v
# test_convert.py::test_water_freezes PASSED                               [ 33%]
# test_convert.py::test_water_boils PASSED                                 [ 66%]
# test_convert.py::test_body_temperature PASSED                            [100%]
#
# ============================== 3 passed in 0.01s ===============================

print("\n--- Exercise 6: Testing an error")
# Answer (not run here: needs other files, a library or the terminal):
# # test_divide.py
# import pytest
# from calc import divide
#
# def test_divide_normal():
#     assert divide(10, 4) == 2.5
#
# def test_divide_by_zero_is_an_error():
#     with pytest.raises(ValueError):
#         divide(5, 0)

print("\n--- Review 1: Exceptions (this module)")


def check_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return "ok"


for age in [30, -2]:
    try:
        print(check_age(age))
    except ValueError as error:
        print(f"error: {error}")
