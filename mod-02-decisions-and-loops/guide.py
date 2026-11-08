# Teacher's guide: Module 02, Decisions and loops
# Every example and exercise answer from this module's lessons, in order.
# Run it from this folder:  python guide.py

print("=" * 50)
print("LESSON: conditionals.md")

print("\n--- Example: True and False")
is_raining = True
print(is_raining)
print(type(is_raining))

print("\n--- Example: Comparisons create True or False")
print(10 > 3)
print(10 == 3)
print("apple" == "apple")
print("apple" == "Apple")

print("\n--- Example: if: do something only when the condition is true")
temperature = 32

if temperature > 30:
    print("It is hot today.")
    print("Drink some water.")

print("Have a nice day!")

print("\n--- Example: if: do something only when the condition is true")
temperature = 20

if temperature > 30:
    print("It is hot today.")
    print("Drink some water.")

print("Have a nice day!")

print("\n--- Example: else: what to do otherwise")
is_raining = False

if is_raining:
    print("Take an umbrella.")
else:
    print("Take sunglasses.")

print("\n--- Example: elif: more than two paths")
score = 75

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 50:
    print("Okay")
else:
    print("Needs practice")

print("\n--- Example: Two ifs are not the same as if/elif")
level = "error"

if level == "error":
    print("Something went wrong")
if level == "error" or level == "warning":
    print("Check the logs")

print("\n--- Example: Two ifs are not the same as if/elif")
level = "error"

if level == "error":
    print("Something went wrong")
elif level == "error" or level == "warning":
    print("Check the logs")

print("\n--- Example: in: is it inside?")
print("a" in "banana")
print("z" in "banana")
print("nan" in "banana")

print("\n--- Example: in: is it inside?")
email = "ana@example.com"

if "@" in email:
    print("Looks like an email.")
else:
    print("This is not an email.")

print("\n--- Example: in: is it inside?")
password = "sunshine"

if "1" not in password:
    print("Your password should contain a number.")

print("\n--- Example: and, or, not: combining conditions")
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter.")

print("\n--- Example: and, or, not: combining conditions")
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend!")
else:
    print("Workday.")

print("\n--- Example: and, or, not: combining conditions")
is_raining = False

if not is_raining:
    print("Let's go for a walk.")

print("\n--- Example: The classic `or` bug")
day = "Monday"

if day == "Saturday" or "Sunday":
    print("Weekend!")

print("\n--- Example: The classic `or` bug")
day = "Monday"

if day == "Saturday" or day == "Sunday":
    print("Weekend!")
else:
    print("Workday.")

print("\n--- Mistake: Using `=` instead of `==`")
# temperature = 30
# if temperature = 30:
#     print("Hot")
# -> SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

print("\n--- Mistake: Using `=` instead of `==`")
temperature = 30
if temperature == 30:
    print("Hot")

print("\n--- Mistake: Forgetting the colon")
# age = 20
# if age >= 18
#     print("Adult")
# -> SyntaxError: expected ':'

print("\n--- Mistake: Forgetting to indent")
# age = 20
# if age >= 18:
# print("Adult")
# -> IndentationError: expected an indented block after 'if' statement on line 2

print("\n--- Mistake: Uppercase and lowercase")
answer = "Yes"

if answer == "yes":
    print("Great!")
else:
    print("Okay, maybe later.")

print("\n--- Mistake: Uppercase and lowercase")
answer = "Yes"

if answer.lower() == "yes":
    print("Great!")
else:
    print("Okay, maybe later.")

print("\n--- Exercise 1: Coffee size")
# Ask her to predict the output before running.
size = "large"

if size == "small":
    print("That will be 3 dollars.")
elif size == "medium":
    print("That will be 4 dollars.")
else:
    print("That will be 5 dollars.")

print("\n--- Exercise 2: Two ifs")
# Ask her to predict the output before running.
stock = 0

if stock == 0:
    print("Out of stock")
if stock < 5:
    print("Order more")
print("Done")

print("\n--- Exercise 3: True or False?")
# Ask her to predict the output before running.
print(7 >= 7)
print("cat" in "concatenate")
print(not (3 > 1))
print(10 != 10 or 2 < 3)

print("\n--- Exercise 4: The weekend checker")
# The broken version is in the lesson; this is the fixed answer.
day = "Tuesday"

if day == "Saturday" or day == "Sunday":
    print("Weekend!")
else:
    print("Workday.")

print("\n--- Exercise 5: Only one message")
# The broken version is in the lesson; this is the fixed answer.
price = 150

if price > 100:
    print("Expensive")
elif price > 50:
    print("Medium")
else:
    print("Cheap")

print("\n--- Exercise 6: Even or odd")
number = 7

if number % 2 == 0:
    print("even")
else:
    print("odd")

print("\n--- Exercise 7: Free shipping")
total = 42

if total >= 50:
    print("Free shipping!")
else:
    print("Shipping costs 8 dollars.")
    print(f"Spend {50 - total} more dollars to get free shipping.")

print("\n--- Exercise 8: Water state")
temperature = 100

if temperature <= 0:
    print("ice")
elif temperature < 100:
    print("water")
else:
    print("steam")

print("\n--- Review 1: Mixing types")
age = 39
print(f"Next year I will be {age + 1}.")
print("Next year I will be " + str(age + 1) + ".")

print("\n--- Review 2: Long name")
name = "Gabriela"

if len(name) > 6:
    print(f"{name} is a long name")
else:
    print(f"{name} is a short name")


print("=" * 50)
print("LESSON: lists.md")

print("\n--- Example: Creating a list")
groceries = ["milk", "eggs", "bread", "coffee"]
print(groceries)

print("\n--- Example: Creating a list")
temperatures = [22, 25, 19, 30]
empty = []
print(temperatures)
print(empty)

print("\n--- Example: How many items: len")
groceries = ["milk", "eggs", "bread", "coffee"]
print(len(groceries))

print("\n--- Example: Reading one item: the index")
groceries = ["milk", "eggs", "bread", "coffee"]
print(groceries[0])
print(groceries[2])

print("\n--- Example: Negative indexes: counting from the end")
groceries = ["milk", "eggs", "bread", "coffee"]
print(groceries[-1])
print(groceries[-2])

print("\n--- Example: Changing an item")
groceries = ["milk", "eggs", "bread", "coffee"]
groceries[1] = "cheese"
print(groceries)

print("\n--- Example: Adding items: append")
groceries = ["milk", "eggs"]
groceries.append("apples")
groceries.append("rice")
print(groceries)
print(len(groceries))

print("\n--- Example: Removing items: remove and pop")
groceries = ["milk", "eggs", "bread"]
groceries.remove("eggs")
print(groceries)

print("\n--- Example: Removing items: remove and pop")
groceries = ["milk", "eggs", "bread"]
last = groceries.pop()
print(last)
print(groceries)

first = groceries.pop(0)
print(first)
print(groceries)

print("\n--- Example: Is it in the list? in")
groceries = ["milk", "eggs", "bread"]

print("eggs" in groceries)
print("butter" in groceries)

if "coffee" not in groceries:
    groceries.append("coffee")

print(groceries)

print("\n--- Example: Slicing: a piece of the list")
letters = ["a", "b", "c", "d", "e"]

print(letters[1:3])
print(letters[:2])
print(letters[2:])

print("\n--- Example: Lists of numbers: sum, min, max")
temperatures = [22, 25, 19, 30]

print(sum(temperatures))
print(min(temperatures))
print(max(temperatures))
print(sum(temperatures) / len(temperatures))

print("\n--- Example: Putting in order: sorted")
temperatures = [22, 25, 19, 30]
in_order = sorted(temperatures)

print(in_order)
print(temperatures)

names = ["Paula", "ana", "Bruno"]
print(sorted(names))

print("\n--- Mistake: Asking for an index that does not exist")
# groceries = ["milk", "eggs", "bread"]
# print(groceries[3])
# -> IndexError: list index out of range

print("\n--- Mistake: Removing something that is not there")
# groceries = ["milk", "eggs", "bread"]
# groceries.remove("butter")
# -> ValueError: list.remove(x): x not in list

print("\n--- Mistake: Removing something that is not there")
groceries = ["milk", "eggs", "bread"]

if "butter" in groceries:
    groceries.remove("butter")
else:
    print("butter is not on the list")

print("\n--- Mistake: Forgetting the quotes")
# groceries = ["milk", eggs, "bread"]
# -> NameError: name 'eggs' is not defined

print("\n--- Mistake: Printing the result of `.sort()`")
numbers = [3, 1, 2]
print(numbers.sort())
print(numbers)

print("\n--- Exercise 1: Indexes")
# Ask her to predict the output before running.
movies = ["Up", "Coco", "Soul", "Luca", "Elio"]
print(movies[1])
print(movies[-1])
print(movies[1:3])
print(len(movies))

print("\n--- Exercise 2: Changing the list")
# Ask her to predict the output before running.
plants = ["fern", "cactus"]
plants.append("basil")
plants[0] = "orchid"
removed = plants.pop()
print(plants)
print(removed)

print("\n--- Exercise 3: Numbers")
# Ask her to predict the output before running.
prices = [10, 4, 25, 1]
print(sorted(prices))
print(max(prices) - min(prices))
print(prices[0] + prices[-1])

print("\n--- Exercise 4: The last guest")
# The broken version is in the lesson; this is the fixed answer.
guests = ["Ana", "Bia", "Caio"]
print(guests[2])
print(guests[-1])

print("\n--- Exercise 5: Sorted list")
# The broken version is in the lesson; this is the fixed answer.
scores = [8, 3, 10, 6]
print(sorted(scores))

print("\n--- Exercise 6: To-do list")
todo = []
todo.append("buy coffee")
todo.append("water the plants")
todo.append("call the bank")

print(f"You have {len(todo)} tasks.")
print(todo[0])

print("\n--- Exercise 7: Avoid duplicates")
cart = ["apple", "banana"]
new_item = "apple"

if new_item not in cart:
    cart.append(new_item)
else:
    print(f"{new_item} is already in the cart")

print(cart)

print("\n--- Exercise 8: Week summary")
steps = [4200, 8000, 6500, 10200, 3000, 12000, 7500]

total = sum(steps)
print(f"Total: {total}")
print(f"Best day: {max(steps)}")
print(f"Average: {total / len(steps)}")

print("\n--- Review 1: Text is also a sequence")
word = "Python"
print(word[0])
print(word[-1])
print(len(word))

print("\n--- Review 2: Decide with a list")
vip = ["Ana", "Leo"]
name = "Leo"

if name in vip:
    print(f"Welcome, {name}! Your table is ready.")
else:
    print(f"Welcome, {name}! Please wait to be seated.")


print("=" * 50)
print("LESSON: loops.md")

print("\n--- Example: for: once for each item")
groceries = ["milk", "eggs", "bread"]

for item in groceries:
    print(item)

print("Done!")

print("\n--- Example: Doing more inside the loop")
prices = [12, 45, 8, 60]

for price in prices:
    if price > 40:
        print(f"{price} dollars: expensive")
    else:
        print(f"{price} dollars: fine")

print("\n--- Example: Looping over a text")
for letter in "hello":
    print(letter)

print("\n--- Example: range: repeating a number of times")
for number in range(5):
    print(number)

print("\n--- Example: range: repeating a number of times")
for number in range(1, 6):
    print(number)

print("\n--- Example: range: repeating a number of times")
for number in range(0, 21, 5):
    print(number)

print("\n--- Example: enumerate: the item and its position")
groceries = ["milk", "eggs", "bread"]

for index, item in enumerate(groceries):
    print(index, item)

print("\n--- Example: enumerate: the item and its position")
groceries = ["milk", "eggs", "bread"]

for number, item in enumerate(groceries, start=1):
    print(f"{number}. {item}")

print("\n--- Example: Counting: the counter pattern")
scores = [7, 4, 9, 5, 10, 3]
passed = 0

for score in scores:
    if score >= 6:
        passed = passed + 1

print(f"{passed} students passed.")

print("\n--- Example: Adding up: the accumulator pattern")
cart = [12.50, 3.00, 8.25]
total = 0

for price in cart:
    total += price

print(f"Total: {total}")

print("\n--- Example: Building a new list")
names = ["ana", "bruno", "carla"]
capitalized = []

for name in names:
    capitalized.append(name.capitalize())

print(capitalized)

print("\n--- Example: Building a new list")
temperatures = [18, 25, 31, 22, 35]
hot_days = []

for temperature in temperatures:
    if temperature > 30:
        hot_days.append(temperature)

print(hot_days)

print("\n--- Example: while: repeat while a condition is true")
countdown = 3

while countdown > 0:
    print(countdown)
    countdown = countdown - 1

print("Go!")

print("\n--- Example: break: leave the loop early")
emails = ["ana@mail.com", "bruno.mail.com", "carla@mail.com"]

for email in emails:
    if "@" not in email:
        print(f"Invalid email found: {email}")
        break
    print(f"{email} is fine")

print("\n--- Example: The infinite loop, and how to stop it")
# This loop never ends, so it is shown as a comment (stop it with Ctrl+C):
# count = 1
#
# while count > 0:
#     print(count)
#     count = count + 1   # count only grows, so it is always > 0

print("\n--- Example: The infinite loop, and how to stop it")
typed = ["hello", "quit"]  # what she types in the lesson
while True:
    # answer = input("Type 'quit' to exit: ")
    answer = typed.pop(0)
    if answer == "quit":
        break
    print(f"You typed: {answer}")

print("Bye!")

print("\n--- Mistake: Forgetting to indent the block")
# for item in ["a", "b"]:
# print(item)
# -> IndentationError: expected an indented block after 'for' statement on line 1

print("\n--- Mistake: Resetting the total inside the loop")
cart = [10, 20, 30]

for price in cart:
    total = 0
    total += price

print(total)

print("\n--- Mistake: Resetting the total inside the loop")
cart = [10, 20, 30]
total = 0

for price in cart:
    total += price

print(total)

print("\n--- Mistake: Printing inside the loop when you meant after")
cart = [10, 20, 30]
total = 0

for price in cart:
    total += price
    print(total)

print("\n--- Mistake: Off by one with range")
for day in range(1, 7):
    print(f"Day {day}")

print("\n--- Exercise 1: Simple for")
# Ask her to predict the output before running.
colors = ["red", "green", "blue"]

for color in colors:
    print(f"I like {color}")
print("That's all")

print("\n--- Exercise 2: Counter")
# Ask her to predict the output before running.
words = ["sun", "moon", "sky", "star", "sea"]
count = 0

for word in words:
    if len(word) == 3:
        count += 1

print(count)

print("\n--- Exercise 3: range and while")
# Ask her to predict the output before running.
for i in range(2, 5):
    print(i)

n = 10
while n > 4:
    n = n - 3
print(n)

print("\n--- Exercise 4: The numbered menu")
# The broken version is in the lesson; this is the fixed answer.
menu = ["Espresso", "Latte", "Tea"]

for number, drink in enumerate(menu, start=1):
    print(f"{number}. {drink}")

print("\n--- Exercise 5: Counting expensive items")
# The broken version is in the lesson; this is the fixed answer.
prices = [25, 10, 30, 40, 5]
expensive = 0

for price in prices:
    if price > 20:
        expensive += 1

print(expensive)

print("\n--- Exercise 6: Shopping list")
groceries = ["rice", "beans", "tomatoes", "onions"]

for number, item in enumerate(groceries, start=1):
    print(f"{number}. {item}")

print(f"{len(groceries)} items in total")

print("\n--- Exercise 7: Total without sum")
expenses = [35.0, 12.5, 80.0, 7.5]
total = 0

for expense in expenses:
    total += expense

print(f"Total spent: {total}")

print("\n--- Exercise 8: Short words")
words = ["tea", "coffee", "milk", "water", "ice"]
short = []

for word in words:
    if len(word) <= 4:
        short.append(word)

print(short)

print("\n--- Exercise 9: Multiplication table")
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

print("\n--- Review 1: Vowels")
text = "programming is fun"
vowels = 0

for letter in text:
    if letter in "aeiou":
        vowels += 1

print(vowels)

print("\n--- Review 2: Grades report")
grades = [9, 4, 7, 10, 5]

for grade in grades:
    if grade >= 6:
        print(f"{grade}: passed")
    else:
        print(f"{grade}: failed")

print(f"Average: {sum(grades) / len(grades)}")


print("=" * 50)
print("LESSON: conditionals.md")

print("\n--- Example: True and False")
is_raining = True
print(is_raining)
print(type(is_raining))

print("\n--- Example: Comparisons create True or False")
print(10 > 3)
print(10 == 3)
print("apple" == "apple")
print("apple" == "Apple")

print("\n--- Example: if: do something only when the condition is true")
temperature = 32

if temperature > 30:
    print("It is hot today.")
    print("Drink some water.")

print("Have a nice day!")

print("\n--- Example: if: do something only when the condition is true")
temperature = 20

if temperature > 30:
    print("It is hot today.")
    print("Drink some water.")

print("Have a nice day!")

print("\n--- Example: else: what to do otherwise")
is_raining = False

if is_raining:
    print("Take an umbrella.")
else:
    print("Take sunglasses.")

print("\n--- Example: elif: more than two paths")
score = 75

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 50:
    print("Okay")
else:
    print("Needs practice")

print("\n--- Example: Two ifs are not the same as if/elif")
level = "error"

if level == "error":
    print("Something went wrong")
if level == "error" or level == "warning":
    print("Check the logs")

print("\n--- Example: Two ifs are not the same as if/elif")
level = "error"

if level == "error":
    print("Something went wrong")
elif level == "error" or level == "warning":
    print("Check the logs")

print("\n--- Example: in: is it inside?")
print("a" in "banana")
print("z" in "banana")
print("nan" in "banana")

print("\n--- Example: in: is it inside?")
email = "ana@example.com"

if "@" in email:
    print("Looks like an email.")
else:
    print("This is not an email.")

print("\n--- Example: in: is it inside?")
password = "sunshine"

if "1" not in password:
    print("Your password should contain a number.")

print("\n--- Example: and, or, not: combining conditions")
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter.")

print("\n--- Example: and, or, not: combining conditions")
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend!")
else:
    print("Workday.")

print("\n--- Example: and, or, not: combining conditions")
is_raining = False

if not is_raining:
    print("Let's go for a walk.")

print("\n--- Example: The classic `or` bug")
day = "Monday"

if day == "Saturday" or "Sunday":
    print("Weekend!")

print("\n--- Example: The classic `or` bug")
day = "Monday"

if day == "Saturday" or day == "Sunday":
    print("Weekend!")
else:
    print("Workday.")

print("\n--- Mistake: Using `=` instead of `==`")
# temperature = 30
# if temperature = 30:
#     print("Hot")
# -> SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

print("\n--- Mistake: Using `=` instead of `==`")
temperature = 30
if temperature == 30:
    print("Hot")

print("\n--- Mistake: Forgetting the colon")
# age = 20
# if age >= 18
#     print("Adult")
# -> SyntaxError: expected ':'

print("\n--- Mistake: Forgetting to indent")
# age = 20
# if age >= 18:
# print("Adult")
# -> IndentationError: expected an indented block after 'if' statement on line 2

print("\n--- Mistake: Uppercase and lowercase")
answer = "Yes"

if answer == "yes":
    print("Great!")
else:
    print("Okay, maybe later.")

print("\n--- Mistake: Uppercase and lowercase")
answer = "Yes"

if answer.lower() == "yes":
    print("Great!")
else:
    print("Okay, maybe later.")

print("\n--- Exercise 1: Coffee size")
# Ask her to predict the output before running.
size = "large"

if size == "small":
    print("That will be 3 dollars.")
elif size == "medium":
    print("That will be 4 dollars.")
else:
    print("That will be 5 dollars.")

print("\n--- Exercise 2: Two ifs")
# Ask her to predict the output before running.
stock = 0

if stock == 0:
    print("Out of stock")
if stock < 5:
    print("Order more")
print("Done")

print("\n--- Exercise 3: True or False?")
# Ask her to predict the output before running.
print(7 >= 7)
print("cat" in "concatenate")
print(not (3 > 1))
print(10 != 10 or 2 < 3)

print("\n--- Exercise 4: The weekend checker")
# The broken version is in the lesson; this is the fixed answer.
day = "Tuesday"

if day == "Saturday" or day == "Sunday":
    print("Weekend!")
else:
    print("Workday.")

print("\n--- Exercise 5: Only one message")
# The broken version is in the lesson; this is the fixed answer.
price = 150

if price > 100:
    print("Expensive")
elif price > 50:
    print("Medium")
else:
    print("Cheap")

print("\n--- Exercise 6: Even or odd")
number = 7

if number % 2 == 0:
    print("even")
else:
    print("odd")

print("\n--- Exercise 7: Free shipping")
total = 42

if total >= 50:
    print("Free shipping!")
else:
    print("Shipping costs 8 dollars.")
    print(f"Spend {50 - total} more dollars to get free shipping.")

print("\n--- Exercise 8: Water state")
temperature = 100

if temperature <= 0:
    print("ice")
elif temperature < 100:
    print("water")
else:
    print("steam")

print("\n--- Review 1: Mixing types")
age = 39
print(f"Next year I will be {age + 1}.")
print("Next year I will be " + str(age + 1) + ".")

print("\n--- Review 2: Long name")
name = "Gabriela"

if len(name) > 6:
    print(f"{name} is a long name")
else:
    print(f"{name} is a short name")
