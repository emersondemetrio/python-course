"""Teacher's guide for module 02: Decisions and loops.

Every example and every exercise answer from this module's lessons, ready to
show in class. Each item prints its own code and then runs it.

Usage (from this folder):
    uv run guide.py                  list sections and items
    uv run guide.py loops            run every item in a section
    uv run guide.py conditionals.ex03     run one item
    uv run guide.py all              run everything
"""

# Lesson code is shown exactly as taught, so a few style rules are relaxed here.
# ruff: noqa: F841, F821, F823, B007, E741

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


# --------------------------------------------------------------------------
# Items: one section per lesson file, in reading order.

# ==========================================================================
# conditionals.md


@item(
    "conditionals",
    "true_and_false",
    "Run it and talk through each line.",
)
def conditionals_true_and_false():
    """True and False"""
    is_raining = True
    print(is_raining)
    print(type(is_raining))


@item(
    "conditionals",
    "comparisons",
    "Highlight: The last one is `False` because Python treats uppercase and lowercase "
    "letters as different.",
)
def conditionals_comparisons():
    """Comparisons create True or False"""
    print(10 > 3)
    print(10 == 3)
    print("apple" == "apple")
    print("apple" == "Apple")


@item(
    "conditionals",
    "if_true",
    "Highlight: Three things to notice:",
)
def conditionals_if_true():
    """if: do something only when the condition is true"""
    temperature = 32

    if temperature > 30:
        print("It is hot today.")
        print("Drink some water.")

    print("Have a nice day!")


@item(
    "conditionals",
    "if_false",
    "Highlight: The condition was `False`, so Python skipped the whole block.",
)
def conditionals_if_false():
    """if: do something only when the condition is true"""
    temperature = 20

    if temperature > 30:
        print("It is hot today.")
        print("Drink some water.")

    print("Have a nice day!")


@item(
    "conditionals",
    "if_else",
    "Highlight: `else` has no condition.",
)
def conditionals_if_else():
    """else: what to do otherwise"""
    is_raining = False

    if is_raining:
        print("Take an umbrella.")
    else:
        print("Take sunglasses.")


@item(
    "conditionals",
    "elif",
    "Highlight: Python checks the conditions from top to bottom and runs only the "
    "first one that is true.",
)
def conditionals_elif():
    """elif: more than two paths"""
    score = 75

    if score >= 90:
        print("Excellent")
    elif score >= 70:
        print("Good")
    elif score >= 50:
        print("Okay")
    else:
        print("Needs practice")


@item(
    "conditionals",
    "two_ifs",
    "Highlight: Two separate `if`s are two separate questions.",
)
def conditionals_two_ifs():
    """Two ifs are not the same as if/elif"""
    level = "error"

    if level == "error":
        print("Something went wrong")
    if level == "error" or level == "warning":
        print("Check the logs")


@item(
    "conditionals",
    "if_elif",
    "Highlight: With `elif`, they become one decision.",
)
def conditionals_if_elif():
    """Two ifs are not the same as if/elif"""
    level = "error"

    if level == "error":
        print("Something went wrong")
    elif level == "error" or level == "warning":
        print("Check the logs")


@item(
    "conditionals",
    "in_text",
    "Highlight: You can also use `not in`:",
)
def conditionals_in_text():
    """in: is it inside?"""
    print("a" in "banana")
    print("z" in "banana")
    print("nan" in "banana")


@item(
    "conditionals",
    "in_email",
    "Highlight: You can also use `not in`:",
)
def conditionals_in_email():
    """in: is it inside?"""
    email = "ana@example.com"

    if "@" in email:
        print("Looks like an email.")
    else:
        print("This is not an email.")


@item(
    "conditionals",
    "not_in",
    "Run it and talk through each line.",
)
def conditionals_not_in():
    """in: is it inside?"""
    password = "sunshine"

    if "1" not in password:
        print("Your password should contain a number.")


@item(
    "conditionals",
    "and",
    "Run it and talk through each line.",
)
def conditionals_and():
    """and, or, not: combining conditions"""
    age = 25
    has_ticket = True

    if age >= 18 and has_ticket:
        print("You can enter.")


@item(
    "conditionals",
    "or",
    "Run it and talk through each line.",
)
def conditionals_or():
    """and, or, not: combining conditions"""
    day = "Sunday"

    if day == "Saturday" or day == "Sunday":
        print("Weekend!")
    else:
        print("Workday.")


@item(
    "conditionals",
    "not",
    "Run it and talk through each line.",
)
def conditionals_not():
    """and, or, not: combining conditions"""
    is_raining = False

    if not is_raining:
        print("Let's go for a walk.")


@item(
    "conditionals",
    "or_bug",
    "Highlight: Monday is not the weekend, so why did it print?",
)
def conditionals_or_bug():
    """The classic or bug"""
    day = "Monday"

    if day == "Saturday" or "Sunday":
        print("Weekend!")


@item(
    "conditionals",
    "or_bug_fixed",
    "Run it and talk through each line.",
)
def conditionals_or_bug_fixed():
    """The classic or bug"""
    day = "Monday"

    if day == "Saturday" or day == "Sunday":
        print("Weekend!")
    else:
        print("Workday.")


@item(
    "conditionals",
    "mistake_single_equals",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def conditionals_mistake_single_equals():
    """Using = instead of =="""
    code = """\
    temperature = 30
    if temperature = 30:
        print("Hot")
    """
    exec(textwrap.dedent(code), {})


@item(
    "conditionals",
    "mistake_single_equals_fixed",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def conditionals_mistake_single_equals_fixed():
    """Using = instead of =="""
    temperature = 30
    if temperature == 30:
        print("Hot")


@item(
    "conditionals",
    "mistake_no_colon",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def conditionals_mistake_no_colon():
    """Forgetting the colon"""
    code = """\
    age = 20
    if age >= 18
        print("Adult")
    """
    exec(textwrap.dedent(code), {})


@item(
    "conditionals",
    "mistake_no_indent",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def conditionals_mistake_no_indent():
    """Forgetting to indent"""
    code = """\
    age = 20
    if age >= 18:
    print("Adult")
    """
    exec(textwrap.dedent(code), {})


@item(
    "conditionals",
    "mistake_case",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def conditionals_mistake_case():
    """Uppercase and lowercase"""
    answer = "Yes"

    if answer == "yes":
        print("Great!")
    else:
        print("Okay, maybe later.")


@item(
    "conditionals",
    "mistake_case_fixed",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def conditionals_mistake_case_fixed():
    """Uppercase and lowercase"""
    answer = "Yes"

    if answer.lower() == "yes":
        print("Great!")
    else:
        print("Okay, maybe later.")


@item(
    "conditionals",
    "ex01",
    "Ask her to predict the output before running.",
)
def conditionals_ex01():
    """Exercise 1: Coffee size"""
    size = "large"

    if size == "small":
        print("That will be 3 dollars.")
    elif size == "medium":
        print("That will be 4 dollars.")
    else:
        print("That will be 5 dollars.")


@item(
    "conditionals",
    "ex02",
    "Ask her to predict the output before running.",
)
def conditionals_ex02():
    """Exercise 2: Two ifs"""
    stock = 0

    if stock == 0:
        print("Out of stock")
    if stock < 5:
        print("Order more")
    print("Done")


@item(
    "conditionals",
    "ex03",
    "Ask her to predict the output before running.",
)
def conditionals_ex03():
    """Exercise 3: True or False?"""
    print(7 >= 7)
    print("cat" in "concatenate")
    print(not (3 > 1))
    print(10 != 10 or 2 < 3)


@item(
    "conditionals",
    "ex04_bug",
    "The broken version from the lesson. Run it, then ask her what is wrong.",
)
def conditionals_ex04_bug():
    """Exercise 4: The weekend checker (the buggy version)"""
    day = "Tuesday"

    if day == "Saturday" or "Sunday":
        print("Weekend!")
    else:
        print("Workday.")


@item(
    "conditionals",
    "ex04",
    "The fixed version. Ask her to explain what changed and why.",
)
def conditionals_ex04():
    """Exercise 4: The weekend checker"""
    day = "Tuesday"

    if day == "Saturday" or day == "Sunday":
        print("Weekend!")
    else:
        print("Workday.")


@item(
    "conditionals",
    "ex05_bug",
    "The broken version from the lesson. Run it, then ask her what is wrong.",
)
def conditionals_ex05_bug():
    """Exercise 5: Only one message (the buggy version)"""
    price = 150

    if price > 100:
        print("Expensive")
    if price > 50:
        print("Medium")
    else:
        print("Cheap")


@item(
    "conditionals",
    "ex05",
    "The fixed version. Ask her to explain what changed and why.",
)
def conditionals_ex05():
    """Exercise 5: Only one message"""
    price = 150

    if price > 100:
        print("Expensive")
    elif price > 50:
        print("Medium")
    else:
        print("Cheap")


@item(
    "conditionals",
    "ex06",
    "Let her write it first; show this only to compare.",
)
def conditionals_ex06():
    """Exercise 6: Even or odd"""
    number = 7

    if number % 2 == 0:
        print("even")
    else:
        print("odd")


@item(
    "conditionals",
    "ex07",
    "Let her write it first; show this only to compare.",
)
def conditionals_ex07():
    """Exercise 7: Free shipping"""
    total = 42

    if total >= 50:
        print("Free shipping!")
    else:
        print("Shipping costs 8 dollars.")
        print(f"Spend {50 - total} more dollars to get free shipping.")


@item(
    "conditionals",
    "ex08",
    "Let her write it first; show this only to compare.",
)
def conditionals_ex08():
    """Exercise 8: Water state"""
    temperature = 100

    if temperature <= 0:
        print("ice")
    elif temperature < 100:
        print("water")
    else:
        print("steam")


@item(
    "conditionals",
    "review01",
    "Review exercise: ask which earlier lesson it uses. Let her try before showing this.",
)
def conditionals_review01():
    """Review 1: Mixing types"""
    age = 39
    print(f"Next year I will be {age + 1}.")
    print("Next year I will be " + str(age + 1) + ".")


@item(
    "conditionals",
    "review02",
    "Review exercise: ask which earlier lesson it uses. Let her try before showing this.",
)
def conditionals_review02():
    """Review 2: Long name"""
    name = "Gabriela"

    if len(name) > 6:
        print(f"{name} is a long name")
    else:
        print(f"{name} is a short name")


# ==========================================================================
# lists.md


@item(
    "lists",
    "create",
    "Highlight: A list can hold any type of value: texts, numbers, or even a mix.",
)
def lists_create():
    """Creating a list"""
    groceries = ["milk", "eggs", "bread", "coffee"]
    print(groceries)


@item(
    "lists",
    "create_numbers",
    "Run it and talk through each line.",
)
def lists_create_numbers():
    """Creating a list"""
    temperatures = [22, 25, 19, 30]
    empty = []
    print(temperatures)
    print(empty)


@item(
    "lists",
    "len",
    "Run it and talk through each line.",
)
def lists_len():
    """How many items: len"""
    groceries = ["milk", "eggs", "bread", "coffee"]
    print(len(groceries))


@item(
    "lists",
    "index",
    "Highlight: Why start at 0?",
)
def lists_index():
    """Reading one item: the index"""
    groceries = ["milk", "eggs", "bread", "coffee"]
    print(groceries[0])
    print(groceries[2])


@item(
    "lists",
    "negative_index",
    "Run it and talk through each line.",
)
def lists_negative_index():
    """Negative indexes: counting from the end"""
    groceries = ["milk", "eggs", "bread", "coffee"]
    print(groceries[-1])
    print(groceries[-2])


@item(
    "lists",
    "change_item",
    "Run it and talk through each line.",
)
def lists_change_item():
    """Changing an item"""
    groceries = ["milk", "eggs", "bread", "coffee"]
    groceries[1] = "cheese"
    print(groceries)


@item(
    "lists",
    "append",
    "Highlight: Notice the dot: `groceries.append(...)`.",
)
def lists_append():
    """Adding items: append"""
    groceries = ["milk", "eggs"]
    groceries.append("apples")
    groceries.append("rice")
    print(groceries)
    print(len(groceries))


@item(
    "lists",
    "remove",
    "Highlight: `pop` removes an item by its position and gives it back to you.",
)
def lists_remove():
    """Removing items: remove and pop"""
    groceries = ["milk", "eggs", "bread"]
    groceries.remove("eggs")
    print(groceries)


@item(
    "lists",
    "pop",
    "Run it and talk through each line.",
)
def lists_pop():
    """Removing items: remove and pop"""
    groceries = ["milk", "eggs", "bread"]
    last = groceries.pop()
    print(last)
    print(groceries)

    first = groceries.pop(0)
    print(first)
    print(groceries)


@item(
    "lists",
    "in",
    "Run it and talk through each line.",
)
def lists_in():
    """Is it in the list? in"""
    groceries = ["milk", "eggs", "bread"]

    print("eggs" in groceries)
    print("butter" in groceries)

    if "coffee" not in groceries:
        groceries.append("coffee")

    print(groceries)


@item(
    "lists",
    "slicing",
    "Run it and talk through each line.",
)
def lists_slicing():
    """Slicing: a piece of the list"""
    letters = ["a", "b", "c", "d", "e"]

    print(letters[1:3])
    print(letters[:2])
    print(letters[2:])


@item(
    "lists",
    "sum_min_max",
    "Highlight: The last line is the average: the total divided by how many there are.",
)
def lists_sum_min_max():
    """Lists of numbers: sum, min, max"""
    temperatures = [22, 25, 19, 30]

    print(sum(temperatures))
    print(min(temperatures))
    print(max(temperatures))
    print(sum(temperatures) / len(temperatures))


@item(
    "lists",
    "sorted",
    "Highlight: Did you notice `'ana'` at the end?",
)
def lists_sorted():
    """Putting in order: sorted"""
    temperatures = [22, 25, 19, 30]
    in_order = sorted(temperatures)

    print(in_order)
    print(temperatures)

    names = ["Paula", "ana", "Bruno"]
    print(sorted(names))


@item(
    "lists",
    "mistake_index_error",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def lists_mistake_index_error():
    """Asking for an index that does not exist"""
    groceries = ["milk", "eggs", "bread"]
    print(groceries[3])


@item(
    "lists",
    "mistake_remove_missing",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def lists_mistake_remove_missing():
    """Removing something that is not there"""
    groceries = ["milk", "eggs", "bread"]
    groceries.remove("butter")


@item(
    "lists",
    "mistake_remove_missing_fixed",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def lists_mistake_remove_missing_fixed():
    """Removing something that is not there"""
    groceries = ["milk", "eggs", "bread"]

    if "butter" in groceries:
        groceries.remove("butter")
    else:
        print("butter is not on the list")


@item(
    "lists",
    "mistake_no_quotes",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def lists_mistake_no_quotes():
    """Forgetting the quotes"""
    groceries = ["milk", eggs, "bread"]


@item(
    "lists",
    "mistake_print_sort",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def lists_mistake_print_sort():
    """Printing the result of .sort()"""
    numbers = [3, 1, 2]
    print(numbers.sort())
    print(numbers)


@item(
    "lists",
    "ex01",
    "Ask her to predict the output before running.",
)
def lists_ex01():
    """Exercise 1: Indexes"""
    movies = ["Up", "Coco", "Soul", "Luca", "Elio"]
    print(movies[1])
    print(movies[-1])
    print(movies[1:3])
    print(len(movies))


@item(
    "lists",
    "ex02",
    "Ask her to predict the output before running.",
)
def lists_ex02():
    """Exercise 2: Changing the list"""
    plants = ["fern", "cactus"]
    plants.append("basil")
    plants[0] = "orchid"
    removed = plants.pop()
    print(plants)
    print(removed)


@item(
    "lists",
    "ex03",
    "Ask her to predict the output before running.",
)
def lists_ex03():
    """Exercise 3: Numbers"""
    prices = [10, 4, 25, 1]
    print(sorted(prices))
    print(max(prices) - min(prices))
    print(prices[0] + prices[-1])


@item(
    "lists",
    "ex04_bug",
    "The broken version from the lesson. Run it, then ask her what is wrong.",
)
def lists_ex04_bug():
    """Exercise 4: The last guest (the buggy version)"""
    guests = ["Ana", "Bia", "Caio"]
    print(guests[3])


@item(
    "lists",
    "ex04",
    "The fixed version. Ask her to explain what changed and why.",
)
def lists_ex04():
    """Exercise 4: The last guest"""
    guests = ["Ana", "Bia", "Caio"]
    print(guests[2])
    print(guests[-1])


@item(
    "lists",
    "ex05_bug",
    "The broken version from the lesson. Run it, then ask her what is wrong.",
)
def lists_ex05_bug():
    """Exercise 5: Sorted list (the buggy version)"""
    scores = [8, 3, 10, 6]
    print(scores.sort())


@item(
    "lists",
    "ex05",
    "The fixed version. Ask her to explain what changed and why.",
)
def lists_ex05():
    """Exercise 5: Sorted list"""
    scores = [8, 3, 10, 6]
    print(sorted(scores))


@item(
    "lists",
    "ex06",
    "Let her write it first; show this only to compare.",
)
def lists_ex06():
    """Exercise 6: To-do list"""
    todo = []
    todo.append("buy coffee")
    todo.append("water the plants")
    todo.append("call the bank")

    print(f"You have {len(todo)} tasks.")
    print(todo[0])


@item(
    "lists",
    "ex07",
    "Let her write it first; show this only to compare.",
)
def lists_ex07():
    """Exercise 7: Avoid duplicates"""
    cart = ["apple", "banana"]
    new_item = "apple"

    if new_item not in cart:
        cart.append(new_item)
    else:
        print(f"{new_item} is already in the cart")

    print(cart)


@item(
    "lists",
    "ex08",
    "Let her write it first; show this only to compare.",
)
def lists_ex08():
    """Exercise 8: Week summary"""
    steps = [4200, 8000, 6500, 10200, 3000, 12000, 7500]

    total = sum(steps)
    print(f"Total: {total}")
    print(f"Best day: {max(steps)}")
    print(f"Average: {total / len(steps)}")


@item(
    "lists",
    "review01",
    "Review exercise: ask which earlier lesson it uses. Let her try before showing this.",
)
def lists_review01():
    """Review 1: Text is also a sequence"""
    word = "Python"
    print(word[0])
    print(word[-1])
    print(len(word))


@item(
    "lists",
    "review02",
    "Review exercise: ask which earlier lesson it uses. Let her try before showing this.",
)
def lists_review02():
    """Review 2: Decide with a list"""
    vip = ["Ana", "Leo"]
    name = "Leo"

    if name in vip:
        print(f"Welcome, {name}! Your table is ready.")
    else:
        print(f"Welcome, {name}! Please wait to be seated.")


# ==========================================================================
# loops.md


@item(
    "loops",
    "for_list",
    'Highlight: How to read it: "for each `item` in `groceries`, print the item."',
)
def loops_for_list():
    """for: once for each item"""
    groceries = ["milk", "eggs", "bread"]

    for item in groceries:
        print(item)

    print("Done!")


@item(
    "loops",
    "if_inside_for",
    "Highlight: Look at the indentation: `if` is inside the `for` (4 spaces), and "
    "`print` is inside the `if` (8 spaces).",
)
def loops_if_inside_for():
    """Doing more inside the loop"""
    prices = [12, 45, 8, 60]

    for price in prices:
        if price > 40:
            print(f"{price} dollars: expensive")
        else:
            print(f"{price} dollars: fine")


@item(
    "loops",
    "for_text",
    "Run it and talk through each line.",
)
def loops_for_text():
    """Looping over a text"""
    for letter in "hello":
        print(letter)


@item(
    "loops",
    "range",
    "Highlight: `range(5)` gives 5 numbers, starting at 0 and stopping before 5.",
)
def loops_range():
    """range: repeating a number of times"""
    for number in range(5):
        print(number)


@item(
    "loops",
    "range_start_stop",
    'Highlight: `range(1, 6)` means "from 1, up to but not including 6".',
)
def loops_range_start_stop():
    """range: repeating a number of times"""
    for number in range(1, 6):
        print(number)


@item(
    "loops",
    "range_step",
    "Run it and talk through each line.",
)
def loops_range_step():
    """range: repeating a number of times"""
    for number in range(0, 21, 5):
        print(number)


@item(
    "loops",
    "enumerate",
    "Highlight: Notice the two variables, separated by a comma: `index, item`.",
)
def loops_enumerate():
    """enumerate: the item and its position"""
    groceries = ["milk", "eggs", "bread"]

    for index, item in enumerate(groceries):
        print(index, item)


@item(
    "loops",
    "enumerate_start",
    "Run it and talk through each line.",
)
def loops_enumerate_start():
    """enumerate: the item and its position"""
    groceries = ["milk", "eggs", "bread"]

    for number, item in enumerate(groceries, start=1):
        print(f"{number}. {item}")


@item(
    "loops",
    "counter",
    "Highlight: The counter is created before the loop (so it starts at 0 only once) "
    "and printed after the loop (when all the counting is done).",
)
def loops_counter():
    """Counting: the counter pattern"""
    scores = [7, 4, 9, 5, 10, 3]
    passed = 0

    for score in scores:
        if score >= 6:
            passed = passed + 1

    print(f"{passed} students passed.")


@item(
    "loops",
    "accumulator",
    "Highlight: This is what `sum()` does for you.",
)
def loops_accumulator():
    """Adding up: the accumulator pattern"""
    cart = [12.50, 3.00, 8.25]
    total = 0

    for price in cart:
        total += price

    print(f"Total: {total}")


@item(
    "loops",
    "build_list",
    "Highlight: You can also build a list with only some of the items (this is called filtering):",
)
def loops_build_list():
    """Building a new list"""
    names = ["ana", "bruno", "carla"]
    capitalized = []

    for name in names:
        capitalized.append(name.capitalize())

    print(capitalized)


@item(
    "loops",
    "build_filtered_list",
    "Run it and talk through each line.",
)
def loops_build_filtered_list():
    """Building a new list"""
    temperatures = [18, 25, 31, 22, 35]
    hot_days = []

    for temperature in temperatures:
        if temperature > 30:
            hot_days.append(temperature)

    print(hot_days)


@item(
    "loops",
    "while",
    "Highlight: Each time the block runs, `countdown` goes down by 1.",
)
def loops_while():
    """while: repeat while a condition is true"""
    countdown = 3

    while countdown > 0:
        print(countdown)
        countdown = countdown - 1

    print("Go!")


@item(
    "loops",
    "break",
    'Highlight: `"carla@mail.com"` was never checked, because `break` ended the loop.',
)
def loops_break():
    """break: leave the loop early"""
    emails = ["ana@mail.com", "bruno.mail.com", "carla@mail.com"]

    for email in emails:
        if "@" not in email:
            print(f"Invalid email found: {email}")
            break
        print(f"{email} is fine")


@item(
    "loops",
    "infinite_loop",
    "Never ends: shown only. Run it from a file in class and practice stopping it with Ctrl+C.",
    run=False,
)
def loops_infinite_loop():
    """The infinite loop, and how to stop it"""
    count = 1

    while count > 0:
        print(count)
        count = count + 1  # count only grows, so it is always > 0


@item(
    "loops",
    "while_true_menu",
    "An infinite loop on purpose, with a break. input() is simulated: she types hello, then quit.",
)
def loops_while_true_menu():
    """The infinite loop, and how to stop it"""
    with typed("hello", "quit"):
        while True:
            answer = input("Type 'quit' to exit: ")
            if answer == "quit":
                break
            print(f"You typed: {answer}")

        print("Bye!")


@item(
    "loops",
    "mistake_no_indent",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def loops_mistake_no_indent():
    """Forgetting to indent the block"""
    code = """\
    for item in ["a", "b"]:
    print(item)
    """
    exec(textwrap.dedent(code), {})


@item(
    "loops",
    "mistake_reset_total",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def loops_mistake_reset_total():
    """Resetting the total inside the loop"""
    cart = [10, 20, 30]

    for price in cart:
        total = 0
        total += price

    print(total)


@item(
    "loops",
    "mistake_reset_total_fixed",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def loops_mistake_reset_total_fixed():
    """Resetting the total inside the loop"""
    cart = [10, 20, 30]
    total = 0

    for price in cart:
        total += price

    print(total)


@item(
    "loops",
    "mistake_print_inside",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def loops_mistake_print_inside():
    """Printing inside the loop when you meant after"""
    cart = [10, 20, 30]
    total = 0

    for price in cart:
        total += price
        print(total)


@item(
    "loops",
    "mistake_off_by_one",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def loops_mistake_off_by_one():
    """Off by one with range"""
    for day in range(1, 7):
        print(f"Day {day}")


@item(
    "loops",
    "ex01",
    "Ask her to predict the output before running.",
)
def loops_ex01():
    """Exercise 1: Simple for"""
    colors = ["red", "green", "blue"]

    for color in colors:
        print(f"I like {color}")
    print("That's all")


@item(
    "loops",
    "ex02",
    "Ask her to predict the output before running.",
)
def loops_ex02():
    """Exercise 2: Counter"""
    words = ["sun", "moon", "sky", "star", "sea"]
    count = 0

    for word in words:
        if len(word) == 3:
            count += 1

    print(count)


@item(
    "loops",
    "ex03",
    "Ask her to predict the output before running.",
)
def loops_ex03():
    """Exercise 3: range and while"""
    for i in range(2, 5):
        print(i)

    n = 10
    while n > 4:
        n = n - 3
    print(n)


@item(
    "loops",
    "ex04_bug",
    "The broken version from the lesson. Run it, then ask her what is wrong.",
)
def loops_ex04_bug():
    """Exercise 4: The numbered menu (the buggy version)"""
    menu = ["Espresso", "Latte", "Tea"]

    for number, drink in enumerate(menu):
        print(f"{number}. {drink}")


@item(
    "loops",
    "ex04",
    "The fixed version. Ask her to explain what changed and why.",
)
def loops_ex04():
    """Exercise 4: The numbered menu"""
    menu = ["Espresso", "Latte", "Tea"]

    for number, drink in enumerate(menu, start=1):
        print(f"{number}. {drink}")


@item(
    "loops",
    "ex05_bug",
    "The broken version from the lesson. Run it, then ask her what is wrong.",
)
def loops_ex05_bug():
    """Exercise 5: Counting expensive items (the buggy version)"""
    prices = [25, 10, 30, 40, 5]

    for price in prices:
        expensive = 0
        if price > 20:
            expensive += 1

    print(expensive)


@item(
    "loops",
    "ex05",
    "The fixed version. Ask her to explain what changed and why.",
)
def loops_ex05():
    """Exercise 5: Counting expensive items"""
    prices = [25, 10, 30, 40, 5]
    expensive = 0

    for price in prices:
        if price > 20:
            expensive += 1

    print(expensive)


@item(
    "loops",
    "ex06",
    "Let her write it first; show this only to compare.",
)
def loops_ex06():
    """Exercise 6: Shopping list"""
    groceries = ["rice", "beans", "tomatoes", "onions"]

    for number, item in enumerate(groceries, start=1):
        print(f"{number}. {item}")

    print(f"{len(groceries)} items in total")


@item(
    "loops",
    "ex07",
    "Let her write it first; show this only to compare.",
)
def loops_ex07():
    """Exercise 7: Total without sum"""
    expenses = [35.0, 12.5, 80.0, 7.5]
    total = 0

    for expense in expenses:
        total += expense

    print(f"Total spent: {total}")


@item(
    "loops",
    "ex08",
    "Let her write it first; show this only to compare.",
)
def loops_ex08():
    """Exercise 8: Short words"""
    words = ["tea", "coffee", "milk", "water", "ice"]
    short = []

    for word in words:
        if len(word) <= 4:
            short.append(word)

    print(short)


@item(
    "loops",
    "ex09",
    "Let her write it first; show this only to compare.",
)
def loops_ex09():
    """Exercise 9: Multiplication table"""
    for i in range(1, 11):
        print(f"7 x {i} = {7 * i}")


@item(
    "loops",
    "review01",
    "Review exercise: ask which earlier lesson it uses. Let her try before showing this.",
)
def loops_review01():
    """Review 1: Vowels"""
    text = "programming is fun"
    vowels = 0

    for letter in text:
        if letter in "aeiou":
            vowels += 1

    print(vowels)


@item(
    "loops",
    "review02",
    "Review exercise: ask which earlier lesson it uses. Let her try before showing this.",
)
def loops_review02():
    """Review 2: Grades report"""
    grades = [9, 4, 7, 10, 5]

    for grade in grades:
        if grade >= 6:
            print(f"{grade}: passed")
        else:
            print(f"{grade}: failed")

    print(f"Average: {sum(grades) / len(grades)}")


if __name__ == "__main__":
    main(sys.argv[1:])
