# Reading errors: Python is trying to help

> **In one sentence:** an error message tells you what went wrong and on which line, and you read it from the bottom up.

## Why it matters

Errors are not a sign that you are bad at programming. Professional programmers see errors many times a day. What changes with experience is not the number of errors, it is how fast you understand them.

The good news: Python's error messages are some of the clearest of any language. Most of the time, the answer is written right there on the screen. You only need to know where to look.

## Analogy

An error message is like the **note a mechanic leaves on your car**. It does not say "your car is bad". It says: "Problem: flat tire. Where: front left wheel." The **what** and the **where** are all you need to start fixing it.

In Python, the **what** is the last line of the message, and the **where** is the line number just above it.

## The idea, step by step

### The anatomy of a traceback

When a program crashes, Python prints a **traceback**: the path the program took until it hit the problem. Here is a program saved as `shop.py`:

<!-- error -->
```python
def total_price(prices):
    total = 0
    for price in prices:
        total = total + price
    return total

cart = [10, 20, "5"]
print(total_price(cart))
```

```text
Traceback (most recent call last):
  File "C:\Users\you\Projects\shop.py", line 8, in <module>
    print(total_price(cart))
          ~~~~~~~~~~~^^^^^^
  File "C:\Users\you\Projects\shop.py", line 4, in total_price
    total = total + price
            ~~~~~~^~~~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

It looks scary. Read it **from the bottom up**:

1. **Last line: what happened.** `TypeError: unsupported operand type(s) for +: 'int' and 'str'`. In plain words: "you tried to use `+` between a number (`int`) and a text (`str`), and I don't know how to do that."
2. **Just above: where it happened.** `line 4, in total_price`, the line `total = total + price`. The little `~~~^~~~` marks point at the exact part of the line.
3. **Further up: how we got there.** Line 8 called `total_price(cart)`. That is useful when the problem is in what you **passed** to the function.

Now you can reason: on line 4, `price` was a text. Where did a text come from? From the list on line 7: `"5"` has quotes. Fix: `cart = [10, 20, 5]`.

"most recent call last" means the most recent step is at the bottom. That is why you start reading there.

### The error type is a big clue

The word before the `:` on the last line is the **type** of error. Each type points to a different kind of problem.

#### SyntaxError: Python cannot even read the code

The code breaks the writing rules of Python, so **nothing runs**, not even the lines before the mistake.

<!-- error -->
```python
print("Hello"
```

```text
    print("Hello"
         ^
SyntaxError: '(' was never closed
```

Look for missing or extra parentheses, quotes, colons and commas. The `^` shows where Python got confused, which is sometimes a bit after the real mistake. If the line looks fine, check the line **above** it.

#### IndentationError: the spaces are wrong

<!-- error -->
```python
name = "Ana"
    print(name)
```

```text
    print(name)
IndentationError: unexpected indent
```

A line is indented where it should not be (or not indented where it should be, after a `:`). Check that each block uses the same number of spaces.

#### NameError: Python does not know this name

<!-- error -->
```python
message = "Hi"
print(mesage)
```

```text
    print(mesage)
          ^^^^^^
NameError: name 'mesage' is not defined. Did you mean: 'message'?
```

Usually a typo, a variable used before it was created, a local variable used outside its function, or a text without quotes. Python even suggests the name you probably meant.

#### TypeError: the value has the wrong type for this operation

<!-- error -->
```python
age = 39
print("Age: " + age)
```

```text
    print("Age: " + age)
          ~~~~~~~~^~~~~
TypeError: can only concatenate str (not "int") to str
```

You mixed types that do not work together. Here, the fix is `"Age: " + str(age)`, or better, `f"Age: {age}"`. A `TypeError` also appears when you call a function with the wrong number of arguments.

#### IndexError: that position does not exist

<!-- error -->
```python
days = ["Mon", "Tue", "Wed"]
print(days[3])
```

```text
    print(days[3])
          ~~~~^^^
IndexError: list index out of range
```

Remember: 3 items means indexes 0, 1 and 2.

#### ValueError: right type, wrong value

<!-- error -->
```python
quantity = int("three")
```

```text
    quantity = int("three")
               ^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'three'
```

`int()` accepts a text, so the **type** is fine. But the text `"three"` cannot be turned into a number, so the **value** is wrong. This happens a lot with `input()`, when the user types letters where you expected a number.

### Summary table

| Error | In plain words | First thing to check |
|---|---|---|
| `SyntaxError` | "I can't read this" | Parentheses, quotes, colons, commas |
| `IndentationError` | "The spaces are wrong" | Indentation after `:` and inside blocks |
| `NameError` | "I don't know this name" | Typos, order of lines, missing quotes |
| `TypeError` | "These types don't go together" | Mixing text and numbers, number of arguments, `None` |
| `IndexError` | "That position doesn't exist" | List length, starting at 0 |
| `ValueError` | "Right type, wrong value" | What was typed or passed to `int()` |

### Print debugging: make the invisible visible

Some bugs do not crash. The program runs, but the result is wrong. Then the question is: "what is actually inside my variables?" The simplest tool is to **print** them.

```python
def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers) + 1

print(average([4, 6, 8]))
```

Output:

```text
7.0
```

The average of 4, 6 and 8 should be 6. Add temporary prints to see what happens:

```python
def average(numbers):
    total = 0
    for n in numbers:
        total += n
        print(f"DEBUG n={n} total={total}")
    print(f"DEBUG len={len(numbers)}")
    return total / len(numbers) + 1

print(average([4, 6, 8]))
```

Output:

```text
DEBUG n=4 total=4
DEBUG n=6 total=10
DEBUG n=8 total=18
DEBUG len=3
7.0
```

The total (18) and the length (3) are right, so the problem must be in the `return` line: there is an extra `+ 1`. Remove it, and remove the debug prints when you are done.

Tips:

- Start debug prints with something easy to spot, like `DEBUG`.
- Print the **name** and the **value**: `f"total={total}"`, not just `total`.
- Print just before the line where things go wrong.

### The debugger: pause the program and look around

Cursor (like VS Code) has a **debugger**: a tool that runs your program step by step and shows every variable as it changes. It is like watching a movie in slow motion instead of only seeing the last scene.

How to use it:

1. Make sure the **Python extension** is installed in Cursor (Extensions panel, search "Python").
2. Open your `.py` file.
3. Click in the narrow space **to the left of a line number**. A red dot appears. That is a **breakpoint**: "pause here".
4. Press **F5** (or open the Run and Debug panel and click the green play button). If Cursor asks, choose **Python File**.
5. The program runs and pauses **before** executing the line with the red dot. That line is highlighted.
6. On the left, the **Variables** panel shows every variable and its current value.
7. Use the small toolbar at the top:

| Button | Key | What it does |
|---|---|---|
| Continue | F5 | Run until the next breakpoint (or the end) |
| Step Over | F10 | Run the current line and stop at the next one |
| Step Into | F11 | If the line calls one of your functions, go inside it |
| Stop | Shift+F5 | Stop the program |

Try it with the `average` example above: put a breakpoint on the line `total += n`, press F5, then press F10 several times and watch `n` and `total` change in the Variables panel.

When to use each tool:

- **Error message** first: it often tells you everything.
- **Print debugging** for a quick look at one or two values.
- **Debugger** when you need to follow the program step by step, especially inside loops and functions.

## Common mistakes

### Reading only the first line of the traceback

The top of the traceback is the oldest step, often far from the problem. Always start from the **last** line, then go up.

### Fixing the line the arrow points to, when the problem is earlier

In the `shop.py` example, the crash was on line 4, but the real mistake was the `"5"` on line 7. The traceback tells you where the program **noticed** the problem. Sometimes you need to ask "where did this value come from?" and look further up.

### Changing many things at once

When something is broken, change **one** thing, save (Ctrl+S), run again. If you change five things at once and it works, you will not know which change fixed it. If it still fails, you will not know which change made it worse.

### Forgetting to save before running

If you fixed the code but the error is the same, check the tab in Cursor: a white dot means the file is not saved. Python runs the file on disk, not what you see on the screen.

## Exercises

### Read the error

For these exercises, do not run anything. Read the code and the error, and answer: **what** is the problem, **which line**, and **how** would you fix it?

#### Exercise 1: The receipt

<!-- no-verify -->
```python
item = "Coffee"
price = 4
print(item + " costs " + price + " dollars")
```

```text
  File "receipt.py", line 3, in <module>
    print(item + " costs " + price + " dollars")
          ~~~~~~~~~~~~~~~~~^~~~~~~
TypeError: can only concatenate str (not "int") to str
```

<details>
<summary>Show answer</summary>

**What:** a number (`price`) is being joined with `+` to texts. **Line:** 3. **Fix:** use an f-string, or convert the number.

```python
item = "Coffee"
price = 4
print(f"{item} costs {price} dollars")
```

Output:

```text
Coffee costs 4 dollars
```

</details>

#### Exercise 2: The missing friend

<!-- no-verify -->
```python
friends = ["Ana", "Leo"]
for friend in friends:
    print(f"Hi, {freind}!")
```

```text
  File "hello.py", line 3, in <module>
    print(f"Hi, {freind}!")
                 ^^^^^^
NameError: name 'freind' is not defined. Did you mean: 'friend'?
```

<details>
<summary>Show answer</summary>

**What:** a typo, `freind` instead of `friend`. **Line:** 3. Python even suggests the fix.

```python
friends = ["Ana", "Leo"]
for friend in friends:
    print(f"Hi, {friend}!")
```

Output:

```text
Hi, Ana!
Hi, Leo!
```

</details>

#### Exercise 3: Two steps away

<!-- no-verify -->
```python
def get_discount(code):
    if code == "SAVE10":
        return 10

def final_price(price, code):
    return price - get_discount(code)

print(final_price(100, "SAVE20"))
```

```text
  File "store.py", line 8, in <module>
    print(final_price(100, "SAVE20"))
          ~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "store.py", line 6, in final_price
    return price - get_discount(code)
           ~~~~~~^~~~~~~~~~~~~~~~~~~~
TypeError: unsupported operand type(s) for -: 'int' and 'NoneType'
```

<details>
<summary>Hint</summary>

`NoneType` is the type of `None`. Which function returned `None`, and why?

</details>

<details>
<summary>Show answer</summary>

**What:** on line 6, the code subtracts `None` from a number. `get_discount("SAVE20")` returned `None`, because the code is not `"SAVE10"` and the function has no `return` for that case. **Fix:** return 0 when the code is not valid.

```python
def get_discount(code):
    if code == "SAVE10":
        return 10
    return 0

def final_price(price, code):
    return price - get_discount(code)

print(final_price(100, "SAVE20"))
print(final_price(100, "SAVE10"))
```

Output:

```text
100
90
```

The crash was on line 6, but the real mistake was in `get_discount`. That is why you sometimes read further up.

</details>

### Find the bug

#### Exercise 4: Wrong count

This should count the words that start with "b" and print `3`, but it prints `1`. There is no error message. Use print debugging (or the debugger) to find the problem, then fix it.

<!-- no-verify -->
```python
words = ["banana", "apple", "berry", "bread"]

for word in words:
    count = 0
    if word.startswith("b"):
        count += 1

print(count)
```

<details>
<summary>Hint</summary>

Add `print(f"DEBUG word={word} count={count}")` as the last line inside the loop.

</details>

<details>
<summary>Show answer</summary>

```python
words = ["banana", "apple", "berry", "bread"]
count = 0

for word in words:
    if word.startswith("b"):
        count += 1

print(count)
```

Output:

```text
3
```

The debug print would show `count` going back to 0 on every word. The counter must be created before the loop.

</details>

#### Exercise 5: Three bugs

This program has three bugs. Fix one at a time: run it, read the error, fix, save, run again.

<!-- no-verify -->
```python
def greet(name)
    return f"Hello, {name}!"

guests = ["Ana", "Bia", "Caio"]
for i in range(4):
    print(greet(guest[i]))
```

<details>
<summary>Show answer</summary>

1. `SyntaxError: expected ':'` on line 1: the `def` line needs a colon.
2. `NameError: name 'guest' is not defined`: the list is called `guests`.
3. `IndexError: list index out of range`: the list has 3 items, but `range(4)` goes up to index 3. Better: loop over the list directly.

```python
def greet(name):
    return f"Hello, {name}!"

guests = ["Ana", "Bia", "Caio"]
for guest in guests:
    print(greet(guest))
```

Output:

```text
Hello, Ana!
Hello, Bia!
Hello, Caio!
```

</details>

### Write it

#### Exercise 6: Make each error on purpose

Create a file `errors.py` and write the smallest code you can that causes each error: `SyntaxError`, `NameError`, `TypeError`, `IndexError` and `ValueError`. Run each one (comment the others out with `#`) and read the message.

<details>
<summary>Show answer</summary>

One possible set (run one at a time):

<!-- no-verify -->
```python
# print("hi"          -> SyntaxError: '(' was never closed
# print(nothing)      -> NameError: name 'nothing' is not defined
# "a" + 1             -> TypeError: can only concatenate str (not "int") to str
# [1, 2][5]           -> IndexError: list index out of range
# int("hello")        -> ValueError: invalid literal for int() with base 10: 'hello'
```

Causing errors on purpose is a great way to lose your fear of them. Once you have seen an error, you recognize it next time.

</details>

## Review

#### Review 1: Predict and explain

What does this print? Then explain why the second line is `None`.

```python
def label(price):
    print(f"Price: {price}")

result = label(9)
print(result)
```

<details>
<summary>Show answer</summary>

```text
Price: 9
None
```

`label` prints but does not return, so it gives back `None`.

</details>

#### Review 2: A safe division

Write a function `safe_divide(a, b)` that returns `a / b`, but returns `None` when `b` is 0 (instead of crashing with `ZeroDivisionError`). Test it with `(10, 2)` and `(10, 0)`.

<details>
<summary>Show answer</summary>

```python
def safe_divide(a, b):
    if b == 0:
        return None
    return a / b

print(safe_divide(10, 2))
print(safe_divide(10, 0))
```

Output:

```text
5.0
None
```

Why `None` and not `0`? Because 0 could be a real answer (`0 / 5` is 0). `None` clearly says "there is no answer". In module 07 you will learn an even better way: raising your own error with `raise`.

</details>

## Recap

- Read a traceback **from the bottom up**: last line = what happened; line above = where.
- The error type is a clue: `SyntaxError` (can't read), `IndentationError` (spaces), `NameError` (unknown name), `TypeError` (types don't match), `IndexError` (position doesn't exist), `ValueError` (wrong value).
- The line that crashed is not always the line with the mistake; ask where the bad value came from.
- For wrong results without a crash, print the variables (`f"DEBUG total={total}"`) or use the debugger: breakpoint, F5, F10, F11.
- Change one thing at a time, and save before running.

**Next:** [Module 04: Files](../module-04-files/README.md)
