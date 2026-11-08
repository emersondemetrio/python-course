# ruff: noqa: F811, B018
# Teacher's guide: Module 03, Functions
# Every example and exercise answer from this module's lessons, in order.
# Run it from this folder:  python guide.py

print("=" * 50)
print("LESSON: functions.md")

print("\n--- Example: Defining a function")


def say_hello():
    print("Hello!")
    print("Nice to see you.")


print("\n--- Example: Calling a function")


def say_hello():
    print("Hello!")
    print("Nice to see you.")


say_hello()
say_hello()

print("\n--- Example: Parameters and arguments")


def greet(name):
    print(f"Good evening, {name}!")


greet("Ana")
greet("Bruno")

print("\n--- Example: Parameters and arguments")


def greet(name):
    print(f"Good evening, {name}!")


guest = "Carla"
greet(guest)

print("\n--- Example: More than one parameter")


def describe_pet(animal, pet_name):
    print(f"I have a {animal} called {pet_name}.")


describe_pet("cat", "Mimi")
describe_pet("Mimi", "cat")

print("\n--- Example: Keyword arguments")


def describe_pet(animal, pet_name):
    print(f"I have a {animal} called {pet_name}.")


describe_pet(pet_name="Rex", animal="dog")

print("\n--- Example: Default values")


def make_coffee(size="medium"):
    print(f"Making a {size} coffee.")


make_coffee()
make_coffee("large")

print("\n--- Example: return vs print (the most important part)")


def add_and_show(a, b):
    print(a + b)


def add_and_give(a, b):
    return a + b


add_and_show(2, 3)
result = add_and_give(2, 3)
print(result * 10)

print("\n--- Example: What happens without return: None")


def add_and_show(a, b):
    print(a + b)


result = add_and_show(2, 3)
print(result)

print("\n--- Example: return ends the function")


def check_age(age):
    if age >= 18:
        return "adult"
    return "minor"
    print("This line never runs.")


print(check_age(30))
print(check_age(12))

print("\n--- Example: Functions that call functions")


def price_with_tax(price):
    return price * 1.1


def format_price(price):
    return f"${price:.2f}"


def show_price(item, price):
    final = price_with_tax(price)
    print(f"{item}: {format_price(final)}")


show_price("Book", 20)
show_price("Pen", 3)

print("\n--- Example: Docstrings: explaining what the function does")


def average(numbers):
    """Return the average of a list of numbers."""
    return sum(numbers) / len(numbers)


print(average([8, 6, 10]))

print("\n--- Mistake: Calling a function before defining it")
# greet("Ana")
#
# def greet(name):
#     print(f"Hello, {name}")
# -> NameError: name 'greet' is not defined

print("\n--- Mistake: Forgetting an argument")
# def greet(name):
#     print(f"Hello, {name}")
#
# greet()
# -> TypeError: greet() missing 1 required positional argument: 'name'

print("\n--- Mistake: Using print where you needed return")
# def double(n):
#     print(n * 2)
#
# result = double(5) + 1
# -> TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

print("\n--- Mistake: Using print where you needed return")


def double(n):
    return n * 2


result = double(5) + 1
print(result)

print("\n--- Mistake: Forgetting the parentheses")


def say_hello():
    print("Hello!")


say_hello
print(say_hello)

print("\n--- Exercise 1: Defined but not called")


# Ask her to predict the output before running.
def morning():
    print("Good morning")


def night():
    print("Good night")


night()
night()

print("\n--- Exercise 2: print or return?")


# Ask her to predict the output before running.
def a(x):
    print(x + 1)


def b(x):
    return x + 1


first = a(10)
second = b(10)
print(first)
print(second)

print("\n--- Exercise 3: Default values")


# Ask her to predict the output before running.
def order(drink, size="small", sugar=0):
    return f"{size} {drink} with {sugar} sugar"


print(order("tea"))
print(order("coffee", "large"))
print(order("coffee", sugar=2))

print("\n--- Exercise 4: The total that disappears")


# The broken version is in the lesson; this is the fixed answer.
def add_tip(bill):
    return bill * 1.1


total = add_tip(50)
print(f"Total with tip: {total}")

print("\n--- Exercise 5: Order matters")


# The broken version is in the lesson; this is the fixed answer.
def square(n):
    return n * n


print(square(4))

print("\n--- Exercise 6: Area of a rectangle")


def area(width, height):
    return width * height


first = area(3, 4)
second = area(10, 2)
print(first)
print(second)
print(first + second)

print("\n--- Exercise 7: Greeting with a default")


def welcome(name, language="en"):
    if language == "pt":
        return f"Bem-vindo, {name}!"
    return f"Welcome, {name}!"


print(welcome("Ana"))
print(welcome("Ana", "pt"))

print("\n--- Exercise 8: Count long words")


def count_long(words, min_length):
    count = 0
    for word in words:
        if len(word) >= min_length:
            count += 1
    return count


print(count_long(["sun", "rainbow", "cloud", "sky"], 5))

print("\n--- Exercise 9: From print to return")


def receipt_line(item, price):
    return f"{item}: ${price}"


print(receipt_line("Bread", 4))
print(receipt_line("Milk", 3))
print(receipt_line("Coffee", 12))

print("\n--- Review 1: Function with a loop and a list")


def numbered(items):
    result = []
    for number, item in enumerate(items, start=1):
        result.append(f"{number}. {item}")
    return result


print(numbered(["milk", "eggs", "bread"]))

print("\n--- Review 2: Decision inside a function")


def water_state(temperature):
    if temperature <= 0:
        return "ice"
    elif temperature < 100:
        return "water"
    else:
        return "steam"


for t in [-5, 25, 100]:
    print(t, water_state(t))


print("=" * 50)
print("LESSON: scope.md")

print("\n--- Example: Local variables: created inside, live inside")
# def make_tea():
#     kettle = "hot"
#     print(f"The kettle is {kettle}.")
#
# make_tea()
# print(kettle)
# -> NameError: name 'kettle' is not defined

print("\n--- Example: Local variables: created inside, live inside")


def make_tea():
    kettle = "hot"
    return kettle


result = make_tea()
print(result)

print("\n--- Example: Global variables: created outside")
store_name = "Corner Café"


def welcome():
    print(f"Welcome to {store_name}!")


welcome()

print("\n--- Example: Same name, different variables")
message = "I am global"


def show():
    message = "I am local"
    print(message)


show()
print(message)

print("\n--- Example: Changing a global from inside a function: avoid it")
# visits = 0
#
# def add_visit():
#     visits = visits + 1
#
# add_visit()
# -> UnboundLocalError: cannot access local variable 'visits'
#    where it is not associated with a value

print("\n--- Example: Changing a global from inside a function: avoid it")


def add_visit(visits):
    return visits + 1


visits = 0
visits = add_visit(visits)
visits = add_visit(visits)
print(visits)

print("\n--- Example: Why closed boxes are better")
prices = [10, 20, 30]
total = 0


def calculate():
    for p in prices:
        print(p)


calculate()
print(total)

print("\n--- Example: Why closed boxes are better")


def calculate_total(prices):
    total = 0
    for p in prices:
        total += p
    return total


cart = [10, 20, 30]
print(calculate_total(cart))
print(calculate_total([5, 5]))

print("\n--- Example: One function controls the flow: main()")


def ask_name():
    return "Ana"  # in a real program: input("Your name: ")


def build_greeting(name):
    return f"Hello, {name}! Welcome back."


def show(message):
    print(message)


def main():
    name = ask_name()
    greeting = build_greeting(name)
    show(greeting)


main()

print("\n--- Example: A peek ahead: `if __name__ == '__main__':`")


def main():
    print("Program started")


if __name__ == "__main__":
    main()

print("\n--- Mistake: Trying to use a local variable outside its function")
# def calculate():
#     result = 2 + 2
#
# calculate()
# print(result)
# -> NameError: name 'result' is not defined

print("\n--- Mistake: Changing a global inside a function")
# count = 0
#
# def increase():
#     count += 1
#
# increase()
# -> UnboundLocalError: cannot access local variable 'count' where it is not associated with a value

print("\n--- Exercise 1: Same name")
# Ask her to predict the output before running.
color = "blue"


def paint():
    color = "red"
    return color


print(paint())
print(color)

print("\n--- Exercise 2: Passing values along")


# Ask her to predict the output before running.
def step_one(n):
    return n + 1


def step_two(n):
    return n * 10


def main():
    value = 4
    value = step_one(value)
    value = step_two(value)
    print(value)


main()

print("\n--- Exercise 3: Will it crash?")
# Ask her to predict the output before running.
# This code stops with an error on purpose, so it is shown as a comment:
# def make_list():
#     items = ["a", "b"]
#     return len(items)
#
# size = make_list()
# print(size)
# print(items)
# -> NameError: name 'items' is not defined

print("\n--- Exercise 4: The counter")


# The broken version is in the lesson; this is the fixed answer.
def like(likes):
    return likes + 1


likes = 0
likes = like(likes)
likes = like(likes)
likes = like(likes)
print(likes)

print("\n--- Exercise 5: A tiny program with main")


def get_items():
    return ["notebook", "pen", "eraser"]


def format_items(items):
    lines = []
    for number, item in enumerate(items, start=1):
        lines.append(f"{number}. {item}")
    return lines


def show(lines):
    for line in lines:
        print(line)


def main():
    items = get_items()
    lines = format_items(items)
    show(lines)


main()

print("\n--- Exercise 6: Remove the globals")


def calculate_pay(hours, rate):
    return hours * rate


def pay_message(name, pay):
    return f"{name} earned {pay} dollars."


def main():
    pay = calculate_pay(6, 20)
    print(pay_message("Bruno", pay))


main()

print("\n--- Review 1: return vs print again")


def shout(word):
    print(word.upper())


def whisper(word):
    return word.lower()


shout("hello")
whisper("HELLO")
print(whisper("BYE"))

print("\n--- Review 2: Loop inside a function")


def total_length(words):
    total = 0
    for word in words:
        total += len(word)
    return total


print(total_length(["sun", "moon"]))


print("=" * 50)
print("LESSON: reading-errors.md")

print("\n--- Example: The anatomy of a traceback")
# def total_price(prices):
#     total = 0
#     for price in prices:
#         total = total + price
#     return total
#
# cart = [10, 20, "5"]
# print(total_price(cart))
# -> TypeError: unsupported operand type(s) for +: 'int' and 'str'

print("\n--- SyntaxError: Python cannot even read the code")
# print("Hello"
# -> SyntaxError: '(' was never closed

print("\n--- IndentationError: the spaces are wrong")
# name = "Ana"
#     print(name)
# -> IndentationError: unexpected indent

print("\n--- NameError: Python does not know this name")
# message = "Hi"
# print(mesage)
# -> NameError: name 'mesage' is not defined. Did you mean: 'message'?

print("\n--- TypeError: the value has the wrong type for this operation")
# age = 39
# print("Age: " + age)
# -> TypeError: can only concatenate str (not "int") to str

print("\n--- IndexError: that position does not exist")
# days = ["Mon", "Tue", "Wed"]
# print(days[3])
# -> IndexError: list index out of range

print("\n--- ValueError: right type, wrong value")
# quantity = int("three")
# -> ValueError: invalid literal for int() with base 10: 'three'

print("\n--- Example: Print debugging: make the invisible visible")


def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers) + 1


print(average([4, 6, 8]))

print("\n--- Example: Print debugging: make the invisible visible")


def average(numbers):
    total = 0
    for n in numbers:
        total += n
        print(f"DEBUG n={n} total={total}")
    print(f"DEBUG len={len(numbers)}")
    return total / len(numbers) + 1


print(average([4, 6, 8]))

print("\n--- Exercise 1: The receipt")
item = "Coffee"
price = 4
print(f"{item} costs {price} dollars")

print("\n--- Exercise 2: The missing friend")
friends = ["Ana", "Leo"]
for friend in friends:
    print(f"Hi, {friend}!")

print("\n--- Exercise 3: Two steps away")


def get_discount(code):
    if code == "SAVE10":
        return 10
    return 0


def final_price(price, code):
    return price - get_discount(code)


print(final_price(100, "SAVE20"))
print(final_price(100, "SAVE10"))

print("\n--- Exercise 4: Wrong count")
words = ["banana", "apple", "berry", "bread"]
count = 0

for word in words:
    if word.startswith("b"):
        count += 1

print(count)

print("\n--- Exercise 5: Three bugs")


def greet(name):
    return f"Hello, {name}!"


guests = ["Ana", "Bia", "Caio"]
for guest in guests:
    print(greet(guest))

print("\n--- Exercise 6: Make each error on purpose")
# print("hi"          -> SyntaxError: '(' was never closed
# print(nothing)      -> NameError: name 'nothing' is not defined
# "a" + 1             -> TypeError: can only concatenate str (not "int") to str
# [1, 2][5]           -> IndexError: list index out of range
# int("hello")        -> ValueError: invalid literal for int() with base 10: 'hello'

print("\n--- Review 1: Predict and explain")


def label(price):
    print(f"Price: {price}")


result = label(9)
print(result)

print("\n--- Review 2: A safe division")


def safe_divide(a, b):
    if b == 0:
        return None
    return a / b


print(safe_divide(10, 2))
print(safe_divide(10, 0))


print("=" * 50)
print("LESSON: functions.md")

print("\n--- Example: Defining a function")


def say_hello():
    print("Hello!")
    print("Nice to see you.")


print("\n--- Example: Calling a function")


def say_hello():
    print("Hello!")
    print("Nice to see you.")


say_hello()
say_hello()

print("\n--- Example: Parameters and arguments")


def greet(name):
    print(f"Good evening, {name}!")


greet("Ana")
greet("Bruno")

print("\n--- Example: Parameters and arguments")


def greet(name):
    print(f"Good evening, {name}!")


guest = "Carla"
greet(guest)

print("\n--- Example: More than one parameter")


def describe_pet(animal, pet_name):
    print(f"I have a {animal} called {pet_name}.")


describe_pet("cat", "Mimi")
describe_pet("Mimi", "cat")

print("\n--- Example: Keyword arguments")


def describe_pet(animal, pet_name):
    print(f"I have a {animal} called {pet_name}.")


describe_pet(pet_name="Rex", animal="dog")

print("\n--- Example: Default values")


def make_coffee(size="medium"):
    print(f"Making a {size} coffee.")


make_coffee()
make_coffee("large")

print("\n--- Example: return vs print (the most important part)")


def add_and_show(a, b):
    print(a + b)


def add_and_give(a, b):
    return a + b


add_and_show(2, 3)
result = add_and_give(2, 3)
print(result * 10)

print("\n--- Example: What happens without return: None")


def add_and_show(a, b):
    print(a + b)


result = add_and_show(2, 3)
print(result)

print("\n--- Example: return ends the function")


def check_age(age):
    if age >= 18:
        return "adult"
    return "minor"
    print("This line never runs.")


print(check_age(30))
print(check_age(12))

print("\n--- Example: Functions that call functions")


def price_with_tax(price):
    return price * 1.1


def format_price(price):
    return f"${price:.2f}"


def show_price(item, price):
    final = price_with_tax(price)
    print(f"{item}: {format_price(final)}")


show_price("Book", 20)
show_price("Pen", 3)

print("\n--- Example: Docstrings: explaining what the function does")


def average(numbers):
    """Return the average of a list of numbers."""
    return sum(numbers) / len(numbers)


print(average([8, 6, 10]))

print("\n--- Mistake: Calling a function before defining it")
# greet("Ana")
#
# def greet(name):
#     print(f"Hello, {name}")
# -> NameError: name 'greet' is not defined

print("\n--- Mistake: Forgetting an argument")
# def greet(name):
#     print(f"Hello, {name}")
#
# greet()
# -> TypeError: greet() missing 1 required positional argument: 'name'

print("\n--- Mistake: Using print where you needed return")
# def double(n):
#     print(n * 2)
#
# result = double(5) + 1
# -> TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

print("\n--- Mistake: Using print where you needed return")


def double(n):
    return n * 2


result = double(5) + 1
print(result)

print("\n--- Mistake: Forgetting the parentheses")


def say_hello():
    print("Hello!")


say_hello
print(say_hello)

print("\n--- Exercise 1: Defined but not called")


# Ask her to predict the output before running.
def morning():
    print("Good morning")


def night():
    print("Good night")


night()
night()

print("\n--- Exercise 2: print or return?")


# Ask her to predict the output before running.
def a(x):
    print(x + 1)


def b(x):
    return x + 1


first = a(10)
second = b(10)
print(first)
print(second)

print("\n--- Exercise 3: Default values")


# Ask her to predict the output before running.
def order(drink, size="small", sugar=0):
    return f"{size} {drink} with {sugar} sugar"


print(order("tea"))
print(order("coffee", "large"))
print(order("coffee", sugar=2))

print("\n--- Exercise 4: The total that disappears")


# The broken version is in the lesson; this is the fixed answer.
def add_tip(bill):
    return bill * 1.1


total = add_tip(50)
print(f"Total with tip: {total}")

print("\n--- Exercise 5: Order matters")


# The broken version is in the lesson; this is the fixed answer.
def square(n):
    return n * n


print(square(4))

print("\n--- Exercise 6: Area of a rectangle")


def area(width, height):
    return width * height


first = area(3, 4)
second = area(10, 2)
print(first)
print(second)
print(first + second)

print("\n--- Exercise 7: Greeting with a default")


def welcome(name, language="en"):
    if language == "pt":
        return f"Bem-vindo, {name}!"
    return f"Welcome, {name}!"


print(welcome("Ana"))
print(welcome("Ana", "pt"))

print("\n--- Exercise 8: Count long words")


def count_long(words, min_length):
    count = 0
    for word in words:
        if len(word) >= min_length:
            count += 1
    return count


print(count_long(["sun", "rainbow", "cloud", "sky"], 5))

print("\n--- Exercise 9: From print to return")


def receipt_line(item, price):
    return f"{item}: ${price}"


print(receipt_line("Bread", 4))
print(receipt_line("Milk", 3))
print(receipt_line("Coffee", 12))

print("\n--- Review 1: Function with a loop and a list")


def numbered(items):
    result = []
    for number, item in enumerate(items, start=1):
        result.append(f"{number}. {item}")
    return result


print(numbered(["milk", "eggs", "bread"]))

print("\n--- Review 2: Decision inside a function")


def water_state(temperature):
    if temperature <= 0:
        return "ice"
    elif temperature < 100:
        return "water"
    else:
        return "steam"


for t in [-5, 25, 100]:
    print(t, water_state(t))
