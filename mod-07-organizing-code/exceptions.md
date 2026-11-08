# Exceptions

> **In one sentence:** an exception is Python's way of saying "something went wrong here", and `try`/`except` lets you decide what to do when it happens instead of letting the program crash.

## Why it matters

Since your very first program, you have seen errors like `TypeError`, `KeyError` and `FileNotFoundError`. Those are **exceptions**. Until now, every exception made your program stop. But many of them are not bugs in your code: the user typed letters where you expected a number, or a file does not exist yet. A good program expects these situations and handles them gracefully. In this lesson you learn to **catch** exceptions, and also to **raise** your own, which is the honest way for a function to say "I cannot do this".

## Analogy

Think of a waiter taking an order. A customer asks for the fish, but the fish is sold out. The waiter does not faint in the middle of the restaurant (that is a crash). He also does not bring an empty plate pretending it is fish (that is returning a fake value). He comes back and says: "Sorry, we are out of fish." That is **raising** an exception: telling the truth about the problem.

Then the customer decides what to do: order the chicken, or leave. That is **catching** the exception: the part of the program that knows what to do next.

## The idea, step by step

### What an exception looks like

<!-- no-verify -->
```python
print("Start")
number = int("twelve")
print("End")
```

```text
Start
Traceback (most recent call last):
  File "example.py", line 2, in <module>
    number = int("twelve")
ValueError: invalid literal for int() with base 10: 'twelve'
```

Read it from the **bottom up**:

- The last line has the **type** of the exception (`ValueError`) and a message.
- Above it, the line of code where it happened, and its line number.
- `"End"` was never printed: the program stopped at the exception.

### Catching an exception with `try` and `except`

Put the risky code inside `try:`. If an exception happens there, Python jumps to `except:` instead of crashing.

```python
text = "twelve"
try:
    number = int(text)
    print(f"You typed {number}")
except ValueError:
    print(f"'{text}' is not a number")
print("The program continues")
```

Output:

```text
'twelve' is not a number
The program continues
```

How it flows:

1. Python runs the lines inside `try` one by one.
2. `int(text)` raises `ValueError`. Python **stops** the `try` block right there (so `You typed...` is never printed).
3. It looks for an `except` that matches `ValueError`, and runs it.
4. The program continues after the whole `try`/`except`.

If nothing goes wrong, the `except` block is simply skipped:

```python
text = "12"
try:
    number = int(text)
    print(f"You typed {number}")
except ValueError:
    print(f"'{text}' is not a number")
```

Output:

```text
You typed 12
```

### A classic use: asking until the input is valid

Combine `try`/`except` with `while True` (module 02) to keep asking until the user types something valid:

<!-- no-verify -->
```python
while True:
    text = input("How many cups? ")
    try:
        cups = int(text)
        break
    except ValueError:
        print("Please type a whole number, like 2.")

print(f"OK, {cups} cups.")
```

```console
PS C:\Users\you\Projects> python cups.py
How many cups? two
Please type a whole number, like 2.
How many cups? 2
OK, 2 cups.
```

`break` only runs if `int(text)` worked, because when it fails, Python jumps to `except` before reaching `break`.

### Catch specific exceptions

Always name the exception you expect. Different problems deserve different answers:

```python
prices = {"latte": 8.5}

for item in ["latte", "mocha"]:
    try:
        print(f"{item}: {prices[item]}")
    except KeyError:
        print(f"{item}: not on the menu")
```

Output:

```text
latte: 8.5
mocha: not on the menu
```

You can have several `except` blocks for several kinds of problems:

```python
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
```

Output:

```text
not a number
age cannot be zero
2.0
```

### Never catch everything blindly

You may see code like this:

<!-- no-verify -->
```python
try:
    total = price * quantity
except:
    print("Something went wrong")
```

An `except:` with no name catches **every** exception, including the ones caused by your own typos. If you wrote `quantiy` by mistake, you would get "Something went wrong" instead of a clear `NameError` telling you the line and the name. Your bug becomes invisible. Catch only what you expect and know how to handle.

### `else` and `finally`

Two optional extra blocks:

- `else:` runs only if **no** exception happened in `try`.
- `finally:` runs **always**, exception or not. It is used for cleanup.

```python
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
```

Output:

```text
7: valid, doubled is 14
  (checked)
seven: invalid
  (checked)
```

You will not need these often. `with open(...)` already does the cleanup of files for you, which is one reason we use it.

### Raising your own exceptions with `raise`

Now the other side. When **your** function receives something it cannot handle, it should not pretend everything is fine. It should `raise` an exception.

Remember the `divide` function many people write when starting out:

```python
def divide(a, b):
    if b == 0:
        print("[error] cannot divide by zero")
        return 0
    return a / b

print(divide(0, 5))
print(divide(5, 0))
```

Output:

```text
0.0
[error] cannot divide by zero
0
```

Look at the two results: `0.0` and `0`. The first is a correct answer (zero divided by five really is zero). The second is a **fake** answer: five divided by zero is not zero. Whoever calls `divide` cannot tell them apart. If this number goes into a bill or a report, the error spreads silently. The printed message helps a human reading the screen, but not the code that received the `0`.

The honest version raises an exception:

```python
def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b

print(divide(10, 4))

try:
    print(divide(5, 0))
except ValueError as error:
    print(f"Problem: {error}")
```

Output:

```text
2.5
Problem: cannot divide by zero
```

Now there is no fake value. Either you get a real result, or you get an exception that cannot be ignored by accident. And the **caller** decides what to do: show a message, ask again, use a default. The function's only job is to tell the truth.

`except ValueError as error:` gives the exception a name (`error`), so you can print its message.

(Python already raises `ZeroDivisionError` when you divide by zero. We raise our own here to show how `raise` works and to give a clearer message.)

### Your own kind of exception (briefly)

For bigger programs, you can create your own exception type with a name that describes your problem. It takes two lines:

```python
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
```

Output:

```text
One chicken, coming up!
Sorry: fish is sold out
```

`class OutOfStock(Exception): pass` creates a new kind of exception. You will understand `class` properly in module 08; for now, copy the pattern. The benefit: `except OutOfStock` catches exactly this problem and nothing else.

## Common mistakes

### Catching the wrong exception type

<!-- error -->
```python
prices = {"latte": 8.5}
try:
    print(prices["mocha"])
except ValueError:
    print("Not on the menu")
```

```text
Traceback (most recent call last):
KeyError: 'mocha'
```

A missing key raises `KeyError`, not `ValueError`, so the `except` did not match and the program still crashed. Read the last line of the traceback to learn the exact type, then catch that one.

### Putting too much code inside `try`

<!-- no-verify -->
```python
try:
    text = input("Quantity: ")
    quantity = int(text)
    total = quantity * pricee
    print(total)
except NameError:
    print("Invalid quantity")
```

The typo `pricee` raises `NameError`, and the program says "Invalid quantity", which is a lie. Keep only the line that can fail for the reason you expect inside `try` (here, `int(text)`), and catch the matching exception (`ValueError`).

### Returning a fake value instead of raising

<!-- no-verify -->
```python
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
```

The average of no numbers is not 0, it does not exist. A report would show "average: 0" and look normal. Prefer `raise ValueError("cannot average an empty list")` and let the caller decide.

### Forgetting the parentheses with `as`

<!-- error -->
```python
try:
    int("x")
except ValueError, TypeError:
    print("bad")
```

```text
    except ValueError, TypeError:
           ^^^^^^^^^^^^^^^^^^^^^
SyntaxError: multiple exception types must be parenthesized
```

To catch two types in one `except`, put them in parentheses: `except (ValueError, TypeError):`.

## Exercises

### Predict the output

#### Exercise 1: Where does it stop?

<!-- no-verify -->
```python
try:
    print("A")
    x = int("3")
    print("B")
    y = int("three")
    print("C")
except ValueError:
    print("D")
print("E")
```

<details>
<summary>Show answer</summary>

```python
try:
    print("A")
    x = int("3")
    print("B")
    y = int("three")
    print("C")
except ValueError:
    print("D")
print("E")
```

Output:

```text
A
B
D
E
```

`int("3")` works. `int("three")` fails, so Python jumps straight to `except` and `C` is never printed.

</details>

#### Exercise 2: `else` and `finally`

<!-- no-verify -->
```python
for text in ["5", "five"]:
    try:
        n = int(text)
    except ValueError:
        print("bad")
    else:
        print("good", n)
    finally:
        print("done")
```

<details>
<summary>Show answer</summary>

```python
for text in ["5", "five"]:
    try:
        n = int(text)
    except ValueError:
        print("bad")
    else:
        print("good", n)
    finally:
        print("done")
```

Output:

```text
good 5
done
bad
done
```

</details>

### Fix the bug

#### Exercise 3: The fake zero

Rewrite this function so that, instead of returning `0` for an empty list, it raises a `ValueError` with a clear message. Then call it with `[]` inside a `try` and print the message.

<!-- no-verify -->
```python
def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)
```

<details>
<summary>Show answer</summary>

```python
def average(numbers):
    if len(numbers) == 0:
        raise ValueError("cannot average an empty list")
    return sum(numbers) / len(numbers)

print(average([4, 6]))
try:
    print(average([]))
except ValueError as error:
    print(f"Problem: {error}")
```

Output:

```text
5.0
Problem: cannot average an empty list
```

</details>

#### Exercise 4: The wrong catch

This should print `unknown city` for Paris, but it crashes. Fix it.

<!-- no-verify -->
```python
temps = {"Lisbon": 22, "Oslo": 9}
try:
    print(temps["Paris"])
except ValueError:
    print("unknown city")
```

<details>
<summary>Show answer</summary>

```python
temps = {"Lisbon": 22, "Oslo": 9}
try:
    print(temps["Paris"])
except KeyError:
    print("unknown city")
```

Output:

```text
unknown city
```

</details>

### Write it

#### Exercise 5: Safe conversion

Write a function `to_number(text)` that returns the text converted to a `float`, or `None` if it cannot be converted. Test it with `"3.5"`, `"7"` and `"abc"`.

<details>
<summary>Show answer</summary>

```python
def to_number(text):
    try:
        return float(text)
    except ValueError:
        return None

print(to_number("3.5"))
print(to_number("7"))
print(to_number("abc"))
```

Output:

```text
3.5
7.0
None
```

Is returning `None` here a "fake value"? Not really: the name and purpose of the function say "try to convert, give me nothing if you cannot", and `None` clearly means "nothing", unlike `0`, which looks like a real number.

</details>

#### Exercise 6: Load a file safely

Write a function `read_notes(filename)` that returns the content of a text file, or the string `"(no notes yet)"` if the file does not exist. Use `try`/`except FileNotFoundError`.

<details>
<summary>Show answer</summary>

```python
def read_notes(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "(no notes yet)"

print(read_notes("notes.txt"))
```

Output:

```text
(no notes yet)
```

</details>

## Review

#### Review 1: Modules (previous file)

What does `if __name__ == "__main__":` protect, and when does the code inside it run?

<details>
<summary>Show answer</summary>

It protects code that should only run when the file is executed directly, like `python prices.py`. When another file imports it with `import prices`, `__name__` is `"prices"`, not `"__main__"`, so that code does not run.

</details>

#### Review 2: Dictionaries (module 06)

Rewrite this without `try`/`except`, using `.get()`:

<!-- no-verify -->
```python
stock = {"apples": 3}
try:
    amount = stock["pears"]
except KeyError:
    amount = 0
print(amount)
```

<details>
<summary>Show answer</summary>

```python
stock = {"apples": 3}
amount = stock.get("pears", 0)
print(amount)
```

Output:

```text
0
```

Both work. For a simple default value, `.get()` is shorter and clearer.

</details>

## Recap

- An exception is an error object. Read the traceback from the bottom: type, message, line.
- `try:` risky code, `except SomeError:` what to do if it fails. Keep `try` small and name the exception.
- Never use a bare `except:`; it hides your own bugs.
- `raise ValueError("message")` is the honest way for a function to say "I cannot do this". Do not return fake values like `0`.
- `except SomeError as error:` lets you print the message. Custom exceptions: `class MyError(Exception): pass`.

**Next:** [uv and ruff](uv-and-ruff.md)
