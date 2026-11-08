"""Teacher's guide for module 03: Functions.

Every example and every exercise answer from this module's lessons, ready to
show in class. Each item prints its own code and then runs it.

Usage (from this folder):
    uv run guide.py                  list sections and items
    uv run guide.py scope            run every item in a section
    uv run guide.py functions.ex03     run one item
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
# functions.md


@item(
    "functions",
    "define",
    "Highlight: The parts:",
)
def functions_define():
    """Defining a function"""

    def say_hello():
        print("Hello!")
        print("Nice to see you.")


@item(
    "functions",
    "call",
    "Highlight: Two calls, so the body ran twice.",
)
def functions_call():
    """Calling a function"""

    def say_hello():
        print("Hello!")
        print("Nice to see you.")

    say_hello()
    say_hello()


@item(
    "functions",
    "parameter",
    "Highlight: Two words that people often mix up:",
)
def functions_parameter():
    """Parameters and arguments"""

    def greet(name):
        print(f"Good evening, {name}!")

    greet("Ana")
    greet("Bruno")


@item(
    "functions",
    "argument_from_variable",
    "Highlight: Here, `guest` is a variable outside the function.",
)
def functions_argument_from_variable():
    """Parameters and arguments"""

    def greet(name):
        print(f"Good evening, {name}!")

    guest = "Carla"
    greet(guest)


@item(
    "functions",
    "two_parameters",
    "Highlight: The second call shows what happens if you swap the order: Python does "
    "not know what you meant, it only follows the positions.",
)
def functions_two_parameters():
    """More than one parameter"""

    def describe_pet(animal, pet_name):
        print(f"I have a {animal} called {pet_name}.")

    describe_pet("cat", "Mimi")
    describe_pet("Mimi", "cat")


@item(
    "functions",
    "keyword_arguments",
    "Run it and talk through each line.",
)
def functions_keyword_arguments():
    """Keyword arguments"""

    def describe_pet(animal, pet_name):
        print(f"I have a {animal} called {pet_name}.")

    describe_pet(pet_name="Rex", animal="dog")


@item(
    "functions",
    "default_value",
    "Highlight: You already used a default value without knowing: `print` has a "
    'parameter `sep` whose default is a space `" "`.',
)
def functions_default_value():
    """Default values"""

    def make_coffee(size="medium"):
        print(f"Making a {size} coffee.")

    make_coffee()
    make_coffee("large")


@item(
    "functions",
    "return_vs_print",
    "Highlight: `add_and_show` printed 5, and that was the end of it.",
)
def functions_return_vs_print():
    """return vs print (the most important part)"""

    def add_and_show(a, b):
        print(a + b)

    def add_and_give(a, b):
        return a + b

    add_and_show(2, 3)
    result = add_and_give(2, 3)
    print(result * 10)


@item(
    "functions",
    "no_return_gives_none",
    "Highlight: The `5` comes from the `print` inside the function.",
)
def functions_no_return_gives_none():
    """What happens without return: None"""

    def add_and_show(a, b):
        print(a + b)

    result = add_and_show(2, 3)
    print(result)


@item(
    "functions",
    "return_ends",
    "Highlight: This also shows that a function can have more than one `return`, each "
    "one in a different path.",
)
def functions_return_ends():
    """return ends the function"""

    def check_age(age):
        if age >= 18:
            return "adult"
        return "minor"
        print("This line never runs.")

    print(check_age(30))
    print(check_age(12))


@item(
    "functions",
    "calling_other_functions",
    'Highlight: `{price:.2f}` inside an f-string means "show this number with 2 decimal places".',
)
def functions_calling_other_functions():
    """Functions that call functions"""

    def price_with_tax(price):
        return price * 1.1

    def format_price(price):
        return f"${price:.2f}"

    def show_price(item, price):
        final = price_with_tax(price)
        print(f"{item}: {format_price(final)}")

    show_price("Book", 20)
    show_price("Pen", 3)


@item(
    "functions",
    "docstring",
    "Highlight: In Cursor, if you hover your mouse over `average(...)`, the docstring "
    "appears in a small box.",
)
def functions_docstring():
    """Docstrings: explaining what the function does"""

    def average(numbers):
        """Return the average of a list of numbers."""
        return sum(numbers) / len(numbers)

    print(average([8, 6, 10]))


@item(
    "functions",
    "mistake_call_before_define",
    "Ask her to predict the error first. Python reads top to bottom: greet does not "
    "exist yet on the first line.",
)
def functions_mistake_call_before_define():
    """Calling a function before defining it"""
    code = """\
    greet("Ana")

    def greet(name):
        print(f"Hello, {name}")
    """
    exec(textwrap.dedent(code), {})


@item(
    "functions",
    "mistake_missing_argument",
    "Ask her to predict the error first. The function expects one argument and got none.",
)
def functions_mistake_missing_argument():
    """Forgetting an argument"""
    code = """\
    def greet(name):
        print(f"Hello, {name}")

    greet()
    """
    exec(textwrap.dedent(code), {})


@item(
    "functions",
    "mistake_print_not_return",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def functions_mistake_print_not_return():
    """Using print where you needed return"""

    def double(n):
        print(n * 2)

    result = double(5) + 1


@item(
    "functions",
    "mistake_print_not_return_fixed",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def functions_mistake_print_not_return_fixed():
    """Using print where you needed return"""

    def double(n):
        return n * 2

    result = double(5) + 1
    print(result)


@item(
    "functions",
    "mistake_no_parentheses",
    "Without parentheses the function is only mentioned, not called. The number is a "
    "memory address and changes every run.",
)
def functions_mistake_no_parentheses():
    """Forgetting the parentheses"""
    code = """\
    def say_hello():
        print("Hello!")

    say_hello
    print(say_hello)
    """
    exec(textwrap.dedent(code), {})


@item(
    "functions",
    "ex01",
    "Ask her to predict the output before running.",
)
def functions_ex01():
    """Exercise 1: Defined but not called"""

    def morning():
        print("Good morning")

    def night():
        print("Good night")

    night()
    night()


@item(
    "functions",
    "ex02",
    "Ask her to predict the output before running.",
)
def functions_ex02():
    """Exercise 2: print or return?"""

    def a(x):
        print(x + 1)

    def b(x):
        return x + 1

    first = a(10)
    second = b(10)
    print(first)
    print(second)


@item(
    "functions",
    "ex03",
    "Ask her to predict the output before running.",
)
def functions_ex03():
    """Exercise 3: Default values"""

    def order(drink, size="small", sugar=0):
        return f"{size} {drink} with {sugar} sugar"

    print(order("tea"))
    print(order("coffee", "large"))
    print(order("coffee", sugar=2))


@item(
    "functions",
    "ex04_bug",
    "The broken version from the lesson. Run it, then ask her what is wrong.",
)
def functions_ex04_bug():
    """Exercise 4: The total that disappears (the buggy version)"""

    def add_tip(bill):
        print(bill * 1.1)

    total = add_tip(50)
    print(f"Total with tip: {total}")


@item(
    "functions",
    "ex04",
    "The fixed version. Ask her to explain what changed and why.",
)
def functions_ex04():
    """Exercise 4: The total that disappears"""

    def add_tip(bill):
        return bill * 1.1

    total = add_tip(50)
    print(f"Total with tip: {total}")


@item(
    "functions",
    "ex05_bug",
    "The broken version from the lesson. Run it, then ask her what is wrong.",
)
def functions_ex05_bug():
    """Exercise 5: Order matters (the buggy version)"""
    print(square(4))

    def square(n):
        return n * n


@item(
    "functions",
    "ex05",
    "The fixed version. Ask her to explain what changed and why.",
)
def functions_ex05():
    """Exercise 5: Order matters"""

    def square(n):
        return n * n

    print(square(4))


@item(
    "functions",
    "ex06",
    "Let her write it first; show this only to compare.",
)
def functions_ex06():
    """Exercise 6: Area of a rectangle"""

    def area(width, height):
        return width * height

    first = area(3, 4)
    second = area(10, 2)
    print(first)
    print(second)
    print(first + second)


@item(
    "functions",
    "ex07",
    "Let her write it first; show this only to compare.",
)
def functions_ex07():
    """Exercise 7: Greeting with a default"""

    def welcome(name, language="en"):
        if language == "pt":
            return f"Bem-vindo, {name}!"
        return f"Welcome, {name}!"

    print(welcome("Ana"))
    print(welcome("Ana", "pt"))


@item(
    "functions",
    "ex08",
    "Let her write it first; show this only to compare.",
)
def functions_ex08():
    """Exercise 8: Count long words"""

    def count_long(words, min_length):
        count = 0
        for word in words:
            if len(word) >= min_length:
                count += 1
        return count

    print(count_long(["sun", "rainbow", "cloud", "sky"], 5))


@item(
    "functions",
    "ex09",
    "Let her write it first; show this only to compare.",
)
def functions_ex09():
    """Exercise 9: From print to return"""

    def receipt_line(item, price):
        return f"{item}: ${price}"

    print(receipt_line("Bread", 4))
    print(receipt_line("Milk", 3))
    print(receipt_line("Coffee", 12))


@item(
    "functions",
    "review01",
    "Review exercise: ask which earlier lesson it uses. Let her try before showing this.",
)
def functions_review01():
    """Review 1: Function with a loop and a list"""

    def numbered(items):
        result = []
        for number, item in enumerate(items, start=1):
            result.append(f"{number}. {item}")
        return result

    print(numbered(["milk", "eggs", "bread"]))


@item(
    "functions",
    "review02",
    "Review exercise: ask which earlier lesson it uses. Let her try before showing this.",
)
def functions_review02():
    """Review 2: Decision inside a function"""

    def water_state(temperature):
        if temperature <= 0:
            return "ice"
        elif temperature < 100:
            return "water"
        else:
            return "steam"

    for t in [-5, 25, 100]:
        print(t, water_state(t))


# ==========================================================================
# scope.md


@item(
    "scope",
    "local",
    "Ask her to predict the error first. kettle only exists while make_tea runs.",
)
def scope_local():
    """Local variables: created inside, live inside"""

    def make_tea():
        kettle = "hot"
        print(f"The kettle is {kettle}.")

    make_tea()
    print(kettle)


@item(
    "scope",
    "local_returned",
    "Highlight: Parameters are local too.",
)
def scope_local_returned():
    """Local variables: created inside, live inside"""

    def make_tea():
        kettle = "hot"
        return kettle

    result = make_tea()
    print(result)


@item(
    "scope",
    "global_read",
    "Run it and talk through each line.",
)
def scope_global_read():
    """Global variables: created outside"""
    store_name = "Corner Café"

    def welcome():
        print(f"Welcome to {store_name}!")

    welcome()


@item(
    "scope",
    "same_name",
    "Highlight: Creating `message` inside the function did not change the global one.",
)
def scope_same_name():
    """Same name, different variables"""
    message = "I am global"

    def show():
        message = "I am local"
        print(message)

    show()
    print(message)


@item(
    "scope",
    "change_global",
    "Highlight: Because the function assigns to `visits` (with `=`), Python decides "
    "that `visits` is a local variable of this function.",
)
def scope_change_global():
    """Changing a global from inside a function: avoid it"""
    visits = 0

    def add_visit():
        visits = visits + 1

    add_visit()


@item(
    "scope",
    "change_global_fixed",
    "Highlight: Now the function is a closed box: it receives a number, returns a "
    "number, and does not depend on anything outside.",
)
def scope_change_global_fixed():
    """Changing a global from inside a function: avoid it"""

    def add_visit(visits):
        return visits + 1

    visits = 0
    visits = add_visit(visits)
    visits = add_visit(visits)
    print(visits)


@item(
    "scope",
    "open_box",
    "Highlight: It is hard to tell what `calculate` needs and what it produces just "
    "by looking at its name and its `def` line.",
)
def scope_open_box():
    """Why closed boxes are better"""
    prices = [10, 20, 30]
    total = 0

    def calculate():
        for p in prices:
            print(p)

    calculate()
    print(total)


@item(
    "scope",
    "closed_box",
    "Highlight: From the line `def calculate_total(prices):` alone, you know what it needs.",
)
def scope_closed_box():
    """Why closed boxes are better"""

    def calculate_total(prices):
        total = 0
        for p in prices:
            total += p
        return total

    cart = [10, 20, 30]
    print(calculate_total(cart))
    print(calculate_total([5, 5]))


@item(
    "scope",
    "main",
    "Highlight: Reading `main` is like reading a table of contents: ask the name, "
    "build the greeting, show it.",
)
def scope_main():
    """One function controls the flow: main()"""

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


@item(
    "scope",
    "name_main",
    'Highlight: For now, read it as: "if this file is the one being run, call `main()`".',
)
def scope_name_main():
    """A peek ahead: if __name__ == '__main__':"""

    def main():
        print("Program started")

    if __name__ == "__main__":
        main()


@item(
    "scope",
    "mistake_local_outside",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def scope_mistake_local_outside():
    """Trying to use a local variable outside its function"""

    def calculate():
        result = 2 + 2

    calculate()
    print(result)


@item(
    "scope",
    "mistake_change_global",
    "Ask her to predict the error first, then read the last line of the traceback together.",
)
def scope_mistake_change_global():
    """Changing a global inside a function"""
    count = 0

    def increase():
        count += 1

    increase()


@item(
    "scope",
    "ex01",
    "Ask her to predict the output before running.",
)
def scope_ex01():
    """Exercise 1: Same name"""
    color = "blue"

    def paint():
        color = "red"
        return color

    print(paint())
    print(color)


@item(
    "scope",
    "ex02",
    "Ask her to predict the output before running.",
)
def scope_ex02():
    """Exercise 2: Passing values along"""

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


@item(
    "scope",
    "ex03",
    "Ask her to predict the output before running.",
)
def scope_ex03():
    """Exercise 3: Will it crash?"""

    def make_list():
        items = ["a", "b"]
        return len(items)

    size = make_list()
    print(size)
    print(items)


@item(
    "scope",
    "ex04_bug",
    "The broken version from the lesson. Run it, then ask her what is wrong.",
)
def scope_ex04_bug():
    """Exercise 4: The counter (the buggy version)"""
    likes = 0

    def like():
        likes = likes + 1

    like()
    like()
    like()
    print(likes)


@item(
    "scope",
    "ex04",
    "The fixed version. Ask her to explain what changed and why.",
)
def scope_ex04():
    """Exercise 4: The counter"""

    def like(likes):
        return likes + 1

    likes = 0
    likes = like(likes)
    likes = like(likes)
    likes = like(likes)
    print(likes)


@item(
    "scope",
    "ex05",
    "Let her write it first; show this only to compare.",
)
def scope_ex05():
    """Exercise 5: A tiny program with main"""

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


@item(
    "scope",
    "ex06",
    "Let her write it first; show this only to compare.",
)
def scope_ex06():
    """Exercise 6: Remove the globals"""

    def calculate_pay(hours, rate):
        return hours * rate

    def pay_message(name, pay):
        return f"{name} earned {pay} dollars."

    def main():
        pay = calculate_pay(6, 20)
        print(pay_message("Bruno", pay))

    main()


@item(
    "scope",
    "review01",
    "Review exercise: ask which earlier lesson it uses. Let her try before showing this.",
)
def scope_review01():
    """Review 1: return vs print again"""

    def shout(word):
        print(word.upper())

    def whisper(word):
        return word.lower()

    shout("hello")
    whisper("HELLO")
    print(whisper("BYE"))


@item(
    "scope",
    "review02",
    "Review exercise: ask which earlier lesson it uses. Let her try before showing this.",
)
def scope_review02():
    """Review 2: Loop inside a function"""

    def total_length(words):
        total = 0
        for word in words:
            total += len(word)
        return total

    print(total_length(["sun", "moon"]))


# ==========================================================================
# reading-errors.md


@item(
    "reading_errors",
    "traceback",
    "Highlight: It looks scary.",
)
def reading_errors_traceback():
    """The anatomy of a traceback"""

    def total_price(prices):
        total = 0
        for price in prices:
            total = total + price
        return total

    cart = [10, 20, "5"]
    print(total_price(cart))


@item(
    "reading_errors",
    "syntax_error",
    "Highlight: Look for missing or extra parentheses, quotes, colons and commas.",
)
def reading_errors_syntax_error():
    """The error type is a big clue"""
    code = """\
    print("Hello"
    """
    exec(textwrap.dedent(code), {})


@item(
    "reading_errors",
    "indentation_error",
    "Highlight: A line is indented where it should not be (or not indented where it "
    "should be, after a `:`).",
)
def reading_errors_indentation_error():
    """The error type is a big clue"""
    code = """\
    name = "Ana"
        print(name)
    """
    exec(textwrap.dedent(code), {})


@item(
    "reading_errors",
    "name_error",
    "Ask her to find the typo. In her terminal Python also adds: Did you mean: 'message'?",
)
def reading_errors_name_error():
    """The error type is a big clue"""
    message = "Hi"
    print(mesage)


@item(
    "reading_errors",
    "type_error",
    "Highlight: You mixed types that do not work together.",
)
def reading_errors_type_error():
    """The error type is a big clue"""
    age = 39
    print("Age: " + age)


@item(
    "reading_errors",
    "index_error",
    "Highlight: Remember: 3 items means indexes 0, 1 and 2.",
)
def reading_errors_index_error():
    """The error type is a big clue"""
    days = ["Mon", "Tue", "Wed"]
    print(days[3])


@item(
    "reading_errors",
    "value_error",
    "Highlight: `int()` accepts a text, so the type is fine.",
)
def reading_errors_value_error():
    """The error type is a big clue"""
    quantity = int("three")


@item(
    "reading_errors",
    "average_bug",
    "Highlight: The average of 4, 6 and 8 should be 6.",
)
def reading_errors_average_bug():
    """Print debugging: make the invisible visible"""

    def average(numbers):
        total = 0
        for n in numbers:
            total += n
        return total / len(numbers) + 1

    print(average([4, 6, 8]))


@item(
    "reading_errors",
    "print_debugging",
    "Highlight: The total (18) and the length (3) are right, so the problem must be "
    "in the `return` line: there is an extra `+ 1`.",
)
def reading_errors_print_debugging():
    """Print debugging: make the invisible visible"""

    def average(numbers):
        total = 0
        for n in numbers:
            total += n
            print(f"DEBUG n={n} total={total}")
        print(f"DEBUG len={len(numbers)}")
        return total / len(numbers) + 1

    print(average([4, 6, 8]))


@item(
    "reading_errors",
    "debugger",
    "Do this live in Cursor with the average_bug example saved as a file.",
    run=False,
)
def reading_errors_debugger():
    """The debugger, step by step"""
    # 1. Install the Python extension in Cursor (Extensions panel, search "Python").
    # 2. Save the average example in a file and open it.
    # 3. Click left of the line number of `total += n`: a red dot (breakpoint) appears.
    # 4. Press F5 and choose "Python File" if asked.
    # 5. The program pauses BEFORE that line. Look at the Variables panel.
    # 6. Press F10 (Step Over) several times and watch n and total change.
    # 7. F11 steps into a function, F5 continues, Shift+F5 stops.
    # Ask her: which tool first? Error message, then print debugging, then the debugger.


@item(
    "reading_errors",
    "ex01",
    "Ask her to predict the output before running.",
)
def reading_errors_ex01():
    """Exercise 1: The receipt"""
    item = "Coffee"
    price = 4
    print(f"{item} costs {price} dollars")


@item(
    "reading_errors",
    "ex02",
    "Ask her to predict the output before running.",
)
def reading_errors_ex02():
    """Exercise 2: The missing friend"""
    friends = ["Ana", "Leo"]
    for friend in friends:
        print(f"Hi, {friend}!")


@item(
    "reading_errors",
    "ex03",
    "Ask her to predict the output before running.",
)
def reading_errors_ex03():
    """Exercise 3: Two steps away"""

    def get_discount(code):
        if code == "SAVE10":
            return 10
        return 0

    def final_price(price, code):
        return price - get_discount(code)

    print(final_price(100, "SAVE20"))
    print(final_price(100, "SAVE10"))


@item(
    "reading_errors",
    "ex04_bug",
    "The broken version from the lesson. Run it, then ask her what is wrong.",
)
def reading_errors_ex04_bug():
    """Exercise 4: Wrong count (the buggy version)"""
    words = ["banana", "apple", "berry", "bread"]

    for word in words:
        count = 0
        if word.startswith("b"):
            count += 1

    print(count)


@item(
    "reading_errors",
    "ex04",
    "The fixed version. Ask her to explain what changed and why.",
)
def reading_errors_ex04():
    """Exercise 4: Wrong count"""
    words = ["banana", "apple", "berry", "bread"]
    count = 0

    for word in words:
        if word.startswith("b"):
            count += 1

    print(count)


@item(
    "reading_errors",
    "ex05_bug",
    "The broken version from the lesson. Run it, then ask her what is wrong.",
)
def reading_errors_ex05_bug():
    """Exercise 5: Three bugs (the buggy version)"""
    code = """\
    def greet(name)
        return f"Hello, {name}!"

    guests = ["Ana", "Bia", "Caio"]
    for i in range(4):
        print(greet(guest[i]))
    """
    exec(textwrap.dedent(code), {})


@item(
    "reading_errors",
    "ex05",
    "The fixed version. Ask her to explain what changed and why.",
)
def reading_errors_ex05():
    """Exercise 5: Three bugs"""

    def greet(name):
        return f"Hello, {name}!"

    guests = ["Ana", "Bia", "Caio"]
    for guest in guests:
        print(greet(guest))


@item(
    "reading_errors",
    "ex06",
    "Let her write it first; show this only to compare.",
)
def reading_errors_ex06():
    """Exercise 6: Make each error on purpose"""
    # print("hi"          -> SyntaxError: '(' was never closed
    # print(nothing)      -> NameError: name 'nothing' is not defined
    # "a" + 1             -> TypeError: can only concatenate str (not "int") to str
    # [1, 2][5]           -> IndexError: list index out of range
    # int("hello")        -> ValueError: invalid literal for int() with base 10: 'hello'


@item(
    "reading_errors",
    "review01",
    "Review exercise: ask which earlier lesson it uses. Let her try before showing this.",
)
def reading_errors_review01():
    """Review 1: Predict and explain"""

    def label(price):
        print(f"Price: {price}")

    result = label(9)
    print(result)


@item(
    "reading_errors",
    "review02",
    "Review exercise: ask which earlier lesson it uses. Let her try before showing this.",
)
def reading_errors_review02():
    """Review 2: A safe division"""

    def safe_divide(a, b):
        if b == 0:
            return None
        return a / b

    print(safe_divide(10, 2))
    print(safe_divide(10, 0))


if __name__ == "__main__":
    main(sys.argv[1:])
