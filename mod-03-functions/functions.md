# Functions: naming a piece of work

> **In one sentence:** a function is a block of code with a name, which runs only when you call it, and can receive values and give a result back.

## Why it matters

Without functions, programs become long, repetitive lists of instructions. If you need to calculate a discount in five places, you write the same lines five times, and when the rule changes you must remember to fix all five.

With a function, you write the logic **once**, give it a clear name (`apply_discount`), and use it wherever you need. Functions also make code easier to read: `total = apply_discount(price)` tells you what happens without showing how.

You have been using functions since your first day: `print()`, `len()`, `input()`. Now you will write your own.

## Analogy

A function is like a **recipe card** in a kitchen.

- Writing the card ("Pancakes: mix flour, eggs and milk, then fry") does not make any pancakes. That is **defining** the function.
- Making pancakes by following the card is **calling** the function. You can do it as many times as you want.
- The card says "you need: flour, eggs, milk". Those blanks are the **parameters**.
- The actual flour and eggs you bring today are the **arguments**.
- The plate of pancakes at the end is the **return value**.

## The idea, step by step

### Defining a function

```python
def say_hello():
    print("Hello!")
    print("Nice to see you.")
```

The parts:

| Part | Meaning |
|---|---|
| `def` | "I am defining a function" |
| `say_hello` | the name you chose (same rules as variable names: lowercase, words joined with `_`) |
| `()` | where the parameters go; empty here, but the parentheses are still required |
| `:` | starts the block |
| indented lines | the **body** of the function: what it does |

If you run the code above, **nothing appears**. That is expected. You wrote the recipe card, but nobody cooked yet.

### Calling a function

To run the function, write its name followed by parentheses:

```python
def say_hello():
    print("Hello!")
    print("Nice to see you.")

say_hello()
say_hello()
```

Output:

```text
Hello!
Nice to see you.
Hello!
Nice to see you.
```

Two calls, so the body ran twice. **Defining is not calling.** The `def` only teaches Python what `say_hello` means. The line `say_hello()` actually runs it.

Python reads the file from top to bottom, so a function must be defined **before** the line that calls it.

### Parameters and arguments

A function becomes much more useful when it can work with different values.

```python
def greet(name):
    print(f"Good evening, {name}!")

greet("Ana")
greet("Bruno")
```

Output:

```text
Good evening, Ana!
Good evening, Bruno!
```

Two words that people often mix up:

- **Parameter**: the name in the `def`, inside the parentheses. Here, `name`. It is an empty slot waiting for a value. It is like a variable that only exists inside the function.
- **Argument**: the actual value you pass when you **call** the function. Here, `"Ana"` and then `"Bruno"`.

When you call `greet("Ana")`, Python does something like `name = "Ana"` and then runs the body.

The argument can also be a variable:

```python
def greet(name):
    print(f"Good evening, {name}!")

guest = "Carla"
greet(guest)
```

Output:

```text
Good evening, Carla!
```

Here, `guest` is a variable outside the function. Its value, `"Carla"`, is the argument. Inside the function, that value is called `name`. The two names do not need to match.

### More than one parameter

Separate parameters with commas. The arguments are matched **in order**:

```python
def describe_pet(animal, pet_name):
    print(f"I have a {animal} called {pet_name}.")

describe_pet("cat", "Mimi")
describe_pet("Mimi", "cat")
```

Output:

```text
I have a cat called Mimi.
I have a Mimi called cat.
```

The second call shows what happens if you swap the order: Python does not know what you meant, it only follows the positions.

### Keyword arguments

You can say exactly which parameter gets which value by writing its name. Then the order does not matter:

```python
def describe_pet(animal, pet_name):
    print(f"I have a {animal} called {pet_name}.")

describe_pet(pet_name="Rex", animal="dog")
```

Output:

```text
I have a dog called Rex.
```

### Default values

A parameter can have a **default value**, used when you do not pass an argument for it:

```python
def make_coffee(size="medium"):
    print(f"Making a {size} coffee.")

make_coffee()
make_coffee("large")
```

Output:

```text
Making a medium coffee.
Making a large coffee.
```

You already used a default value without knowing: `print` has a parameter `sep` whose default is a space `" "`. When you wrote `print("a", "b", sep="-")`, you passed a keyword argument to change it.

### return vs print (the most important part)

Read this section slowly.

- `print` **shows** a value on the screen, for a human to read. The program cannot use it afterwards.
- `return` **gives** a value back to the code that called the function. The program can store it, calculate with it, or pass it to another function.

Compare these two functions:

```python
def add_and_show(a, b):
    print(a + b)

def add_and_give(a, b):
    return a + b

add_and_show(2, 3)
result = add_and_give(2, 3)
print(result * 10)
```

Output:

```text
5
50
```

`add_and_show` printed 5, and that was the end of it. `add_and_give` printed nothing, but it gave 5 back, so we could store it in `result` and multiply it by 10.

An analogy: you ask a friend to calculate a restaurant bill.

- With `print`, your friend says the number out loud. You heard it, but you did not write it down. If you need it for the next calculation, it is gone.
- With `return`, your friend hands you a piece of paper with the number. You can keep it and use it.

When the function's job is to **calculate** something, use `return`. Leave the `print` for the place that decides to show the result. Most functions you write should return, not print.

### What happens without return: None

If a function has no `return`, it gives back a special value called `None`, which means "nothing".

```python
def add_and_show(a, b):
    print(a + b)

result = add_and_show(2, 3)
print(result)
```

Output:

```text
5
None
```

The `5` comes from the `print` **inside** the function. Then `result` is `None`, because the function did not return anything. This is the most common surprise for beginners.

### return ends the function

When Python reaches `return`, it leaves the function immediately. Lines after it never run:

```python
def check_age(age):
    if age >= 18:
        return "adult"
    return "minor"
    print("This line never runs.")

print(check_age(30))
print(check_age(12))
```

Output:

```text
adult
minor
```

This also shows that a function can have more than one `return`, each one in a different path.

### Functions that call functions

A function can use other functions, including ones you wrote:

```python
def price_with_tax(price):
    return price * 1.1

def format_price(price):
    return f"${price:.2f}"

def show_price(item, price):
    final = price_with_tax(price)
    print(f"{item}: {format_price(final)}")

show_price("Book", 20)
show_price("Pen", 3)
```

Output:

```text
Book: $22.00
Pen: $3.30
```

`{price:.2f}` inside an f-string means "show this number with 2 decimal places".

Each function does one small job. `show_price` combines them. This is how bigger programs are built.

### Docstrings: explaining what the function does

A text right below the `def`, between triple quotes, is a **docstring**. It explains what the function does, for whoever reads the code later (including you, in three months).

```python
def average(numbers):
    """Return the average of a list of numbers."""
    return sum(numbers) / len(numbers)

print(average([8, 6, 10]))
```

Output:

```text
8.0
```

In Cursor, if you hover your mouse over `average(...)`, the docstring appears in a small box.

## Common mistakes

### Calling a function before defining it

<!-- error -->
```python
greet("Ana")

def greet(name):
    print(f"Hello, {name}")
```

```text
    greet("Ana")
    ^^^^^
NameError: name 'greet' is not defined
```

Python reads from top to bottom. On line 1, it has not seen the `def` yet. Move the call below the definition.

### Forgetting an argument

<!-- error -->
```python
def greet(name):
    print(f"Hello, {name}")

greet()
```

```text
    greet()
    ~~~~~^^
TypeError: greet() missing 1 required positional argument: 'name'
```

The function has a parameter `name` without a default value, so you must pass something. Fix: `greet("Ana")`.

### Using print where you needed return

<!-- error -->
```python
def double(n):
    print(n * 2)

result = double(5) + 1
```

```text
    result = double(5) + 1
             ~~~~~~~~~~^~~
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
```

The error says you tried to add `None` and a number. Why `None`? Because `double` prints but does not return. Fix: change `print(n * 2)` to `return n * 2`.

```python
def double(n):
    return n * 2

result = double(5) + 1
print(result)
```

Output:

```text
11
```

### Forgetting the parentheses

<!-- no-verify -->
```python
def say_hello():
    print("Hello!")

say_hello
print(say_hello)
```

```console
PS C:\Users\you\Projects> python hello.py
<function say_hello at 0x000001A2B3C4D5E0>
```

Without parentheses, you are only **mentioning** the function, not calling it. The line `say_hello` alone does nothing, and printing it shows a description of the function (the strange number is where it lives in memory, and changes every time). Write `say_hello()`.

The same thing happens with methods. If you write `my_file.read` instead of `my_file.read()`, you get a description of the method, not the content.

## Exercises

### Predict the output

#### Exercise 1: Defined but not called

```python
def morning():
    print("Good morning")

def night():
    print("Good night")

night()
night()
```

<details>
<summary>Show answer</summary>

```text
Good night
Good night
```

`morning` was defined but never called, so its body never ran. `night` was called twice.

</details>

#### Exercise 2: print or return?

```python
def a(x):
    print(x + 1)

def b(x):
    return x + 1

first = a(10)
second = b(10)
print(first)
print(second)
```

<details>
<summary>Show answer</summary>

```text
11
None
11
```

The first `11` is printed **inside** `a`, when it is called. `a` returns nothing, so `first` is `None`. `b` prints nothing, but returns 11, which goes into `second`.

</details>

#### Exercise 3: Default values

```python
def order(drink, size="small", sugar=0):
    return f"{size} {drink} with {sugar} sugar"

print(order("tea"))
print(order("coffee", "large"))
print(order("coffee", sugar=2))
```

<details>
<summary>Show answer</summary>

```text
small tea with 0 sugar
large coffee with 0 sugar
small coffee with 2 sugar
```

Missing arguments use the default. In the last call, `sugar=2` is a keyword argument, so `size` keeps its default.

</details>

### Fix the bug

#### Exercise 4: The total that disappears

This program should print `Total with tip: 55.0`, but it prints something else. Fix the function (do not change the last two lines).

<!-- no-verify -->
```python
def add_tip(bill):
    print(bill * 1.1)

total = add_tip(50)
print(f"Total with tip: {total}")
```

<details>
<summary>Show answer</summary>

```python
def add_tip(bill):
    return bill * 1.1

total = add_tip(50)
print(f"Total with tip: {total}")
```

Output:

```text
Total with tip: 55.00000000000001
```

The fix is `return` instead of `print`. Surprised by the long number? Computers store decimal numbers in a way that sometimes creates tiny errors. Use `round(bill * 1.1, 2)` to get `55.0`. This is a famous quirk of almost every programming language, not a mistake in your code.

</details>

#### Exercise 5: Order matters

This crashes. Find out why without running it, then fix it.

<!-- no-verify -->
```python
print(square(4))

def square(n):
    return n * n
```

<details>
<summary>Show answer</summary>

```python
def square(n):
    return n * n

print(square(4))
```

Output:

```text
16
```

The function was called before it was defined, which gives `NameError: name 'square' is not defined`.

</details>

### Write it

#### Exercise 6: Area of a rectangle

Write a function `area(width, height)` that **returns** the area. Use it to print the area of a 3 by 4 rectangle and of a 10 by 2 rectangle, and then the sum of both areas.

<details>
<summary>Show answer</summary>

```python
def area(width, height):
    return width * height

first = area(3, 4)
second = area(10, 2)
print(first)
print(second)
print(first + second)
```

Output:

```text
12
20
32
```

Because `area` returns, you can add the two results. With `print` inside the function, the last line would be impossible.

</details>

#### Exercise 7: Greeting with a default

Write a function `welcome(name, language="en")` that returns `"Welcome, <name>!"` when the language is `"en"` and `"Bem-vindo, <name>!"` when it is `"pt"`. Print the result for `"Ana"` in both languages.

<details>
<summary>Show answer</summary>

```python
def welcome(name, language="en"):
    if language == "pt":
        return f"Bem-vindo, {name}!"
    return f"Welcome, {name}!"

print(welcome("Ana"))
print(welcome("Ana", "pt"))
```

Output:

```text
Welcome, Ana!
Bem-vindo, Ana!
```

</details>

#### Exercise 8: Count long words

Write a function `count_long(words, min_length)` that receives a list of words and a number, and **returns** how many words have at least `min_length` letters.

<details>
<summary>Hint</summary>

Inside the function: a counter, a `for` loop, an `if`, and a `return` after the loop (not inside it).

</details>

<details>
<summary>Show answer</summary>

```python
def count_long(words, min_length):
    count = 0
    for word in words:
        if len(word) >= min_length:
            count += 1
    return count

print(count_long(["sun", "rainbow", "cloud", "sky"], 5))
```

Output:

```text
2
```

If the `return` were indented inside the `for`, the function would stop after checking only the first word.

</details>

#### Exercise 9: From print to return

This function prints a receipt line. Rewrite it so it **returns** the text instead, then print three lines using it.

<!-- no-verify -->
```python
def receipt_line(item, price):
    print(f"{item}: ${price}")
```

<details>
<summary>Show answer</summary>

```python
def receipt_line(item, price):
    return f"{item}: ${price}"

print(receipt_line("Bread", 4))
print(receipt_line("Milk", 3))
print(receipt_line("Coffee", 12))
```

Output:

```text
Bread: $4
Milk: $3
Coffee: $12
```

Now the function only **builds** the text, and the caller decides what to do with it: print it, save it to a file, or add it to a list.

</details>

## Review

#### Review 1: Function with a loop and a list

Write a function `numbered(items)` that receives a list and **returns a new list** with each item numbered from 1, like `"1. milk"`.

<details>
<summary>Show answer</summary>

```python
def numbered(items):
    result = []
    for number, item in enumerate(items, start=1):
        result.append(f"{number}. {item}")
    return result

print(numbered(["milk", "eggs", "bread"]))
```

Output:

```text
['1. milk', '2. eggs', '3. bread']
```

</details>

#### Review 2: Decision inside a function

Write a function `water_state(temperature)` that returns `"ice"`, `"water"` or `"steam"` (0 or below, between 1 and 99, 100 or above). Test it with -5, 25 and 100.

<details>
<summary>Show answer</summary>

```python
def water_state(temperature):
    if temperature <= 0:
        return "ice"
    elif temperature < 100:
        return "water"
    else:
        return "steam"

for t in [-5, 25, 100]:
    print(t, water_state(t))
```

Output:

```text
-5 ice
25 water
100 steam
```

</details>

## Recap

- `def name(parameters):` **defines** a function; nothing runs yet. `name(arguments)` **calls** it.
- A **parameter** is the name in the `def`; an **argument** is the value you pass in the call.
- Arguments match parameters by position, or by name (`size="large"`). Parameters can have default values.
- `print` shows a value on the screen; `return` gives it back so the program can use it. Functions that calculate should `return`.
- A function without `return` gives back `None`. `return` ends the function immediately.

**Next:** [scope.md](scope.md)
