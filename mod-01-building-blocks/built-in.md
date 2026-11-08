# Built-in functions

> **In one sentence:** built-in functions are tools that come with Python, ready to use, and you use one by writing its name followed by parentheses.

## Why it matters

You do not have to build everything yourself. Python ships with dozens of ready-made functions for the most common jobs: showing text, reading what the user types, counting, converting, rounding. Knowing the main ones saves you a lot of work, and understanding how to **call** them prevents one of the most common beginner confusions.

## Analogy

Think of a kitchen that came with appliances already installed: a blender, a toaster, a kettle. You did not build them, you just use them. Each appliance has a **name** ("the blender") and you **use** it by pressing the button and putting something in.

- Saying "the blender" is not the same as turning it on. In Python, writing `len` only **names** the tool.
- Writing `len("coffee")` **presses the button**: it calls the function with `"coffee"` inside, and you get a result back.

## The idea, step by step

### What "built-in" means

A **built-in** function is one that exists as soon as Python starts. You do not need to define it with `def` or import anything. `print` is the one you have used the most.

The ones in this file:

| Function | What it does | Example | Result |
|---|---|---|---|
| `print()` | shows values on the screen | `print("hi")` | `hi` appears |
| `input()` | asks the user to type something | `input("Name? ")` | the typed text, as `str` |
| `len()` | counts items or characters | `len("tea")` | `3` |
| `type()` | tells the type of a value | `type(3)` | `<class 'int'>` |
| `int()` `float()` `str()` | convert to another type | `int("5")` | `5` |
| `round()` | rounds a number | `round(3.7)` | `4` |
| `enumerate()` | numbers the items of a list in a loop | see below | |

### Calling a function: name plus parentheses

To **call** (run) a function, write its name and then `()`. What goes inside the parentheses is the information you give it, called an **argument**.

```python
print(len("coffee"))
```

Output:

```text
6
```

Here two functions are called. Python works from the inside out: first `len("coffee")` gives `6`, then `print(6)` shows it.

### The name alone is not a call

If you write the name **without** parentheses, you are only referring to the function, not running it. Printing it shows Python's description of the tool:

```python
print(len)
print(len("tea"))
```

Output:

```text
<built-in function len>
3
```

The first line did not count anything: it just described the `len` tool. This is exactly what happened in class with `read` and `read()`: without parentheses you see a description of the method, with parentheses it actually reads the file.

The same applies to **methods**, which are functions attached to a value with a dot. `.upper()` turns text into capital letters:

<!-- no-verify -->
```python
word = "tea"
print(word.upper)
print(word.upper())
```

```text
<built-in method upper of str object at 0x7f3a1c2b5e30>
TEA
```

(The `0x7f...` number is a memory address and changes every time.) Whenever you see a strange `<built-in ...>` or `<bound method ...>` on your screen, the first thing to check is: **did I forget the parentheses?**

### `print()`

You know `print` well. It can receive several arguments, separated by commas:

```python
print("Pears:", 4, "Price:", 2.5)
```

Output:

```text
Pears: 4 Price: 2.5
```

### `input()` always gives back text

`input()` shows a message, waits for the user to type and press Enter, and returns what they typed **as a string**, even if they typed digits.

<!-- no-verify -->
```python
age = input("How old are you? ")
print(type(age))
```

```console
PS C:\Users\you\Projects> python age.py
How old are you? 30
<class 'str'>
```

So if you want to do math with it, convert it first:

<!-- no-verify -->
```python
age = int(input("How old are you? "))
print(f"Next year you will be {age + 1}")
```

```console
PS C:\Users\you\Projects> python age.py
How old are you? 30
Next year you will be 31
```

Notice the nesting again: `input(...)` runs first and gives `"30"`, then `int("30")` gives `30`.

### `len()`

`len()` counts characters in a string and items in a list:

```python
print(len("Lisbon"))
print(len(["milk", "eggs", "bread"]))
print(len(""))
```

Output:

```text
6
3
0
```

### `type()`, `int()`, `float()`, `str()`

You met these in [data-types.md](data-types.md). A quick reminder:

```python
print(type(2.5))
print(int("8") + 2)
print(float("1.5") + 1)
print(str(8) + "2")
```

Output:

```text
<class 'float'>
10
2.5
82
```

### `round()`

`round()` rounds a number. With a second argument, it keeps that many decimal places:

```python
print(round(3.7))
print(round(3.14159, 2))
print(round(9.876, 1))
```

Output:

```text
4
3.14
9.9
```

### `enumerate()`: numbering items in a loop

When you loop over a list, `enumerate()` gives you the **position** and the **item** together. Positions start at `0`:

```python
groceries = ["milk", "eggs", "bread"]
for position, item in enumerate(groceries):
    print(position, item)
```

Output:

```text
0 milk
1 eggs
2 bread
```

People usually count from 1, so you can tell `enumerate` where to start:

```python
groceries = ["milk", "eggs", "bread"]
for number, item in enumerate(groceries, start=1):
    print(f"{number}. {item}")
```

Output:

```text
1. milk
2. eggs
3. bread
```

Lists and loops get their own full lessons in module 02.

### Keywords versus built-in names

Python has two kinds of special words, and they behave differently.

**Keywords** are part of Python's grammar: `def`, `return`, `for`, `in`, `if`, `else`, `True`, `False`, `None`, and a few more. You **cannot** use them as names.

<!-- error -->
```python
return = 5
```

```text
SyntaxError: invalid syntax
```

**Built-in names** like `print`, `len`, `str`, `int`, `list` and `input` are **not** keywords. Python lets you reuse them as variable names, but that hides the original tool, so it is a bad idea:

<!-- error -->
```python
str = "hello"
print(str(5))
```

```text
TypeError: 'str' object is not callable
```

After `str = "hello"`, the name `str` points to the text `"hello"`, not to the conversion tool anymore, so `str(5)` tries to "call" a piece of text. **Rule of thumb:** never name your variables `str`, `list`, `len`, `print`, `input`, `type`, `int` or `sum`.

## Common mistakes

### Forgetting the parentheses

```python
name = "ana"
print(name.upper)
```

You will not see `ANA`, but a line like `<built-in method upper of str object at 0x...>`. **Fix:** `print(name.upper())`.

### Doing math with what `input()` returned

<!-- no-verify -->
```python
cups = input("How many cups? ")
print(cups * 2)
```

```console
How many cups? 3
33
```

`cups` is the text `"3"`, and text times 2 repeats it. **Fix:** `cups = int(input("How many cups? "))`.

### Calling something that is not a function

<!-- error -->
```python
total = 10
print(total())
```

```text
TypeError: 'int' object is not callable
```

Only functions can be called with `()`. `total` is a number. **Fix:** `print(total)`.

### Using a variable called `len` (or `str`, `list`...)

<!-- error -->
```python
len = 3
print(len("abc"))
```

```text
TypeError: 'int' object is not callable
```

**Fix:** pick another name, such as `size` or `length`.

## Exercises

### Predict the output

#### Exercise 1: Inside out

```python
print(len("bread") + 1)
```

<details>
<summary>Show answer</summary>

```text
6
```

`len("bread")` is `5`, plus 1 is `6`, and `print` shows it.

</details>

#### Exercise 2: Name or call?

```python
print(type)
print(type(7))
```

<details>
<summary>Show answer</summary>

```text
<class 'type'>
<class 'int'>
```

The first line only names the tool `type` (Python describes it as a class). The second line calls it with `7`.

</details>

#### Exercise 3: Rounding

```python
print(round(2.71828, 2))
print(round(7.6))
```

<details>
<summary>Show answer</summary>

```text
2.72
8
```

</details>

#### Exercise 4: Counting from 1

```python
colors = ["red", "blue"]
for n, color in enumerate(colors, start=1):
    print(n, color)
```

<details>
<summary>Show answer</summary>

```text
1 red
2 blue
```

</details>

### Fix the bug

#### Exercise 5: The doubled order

The user types `4` and the program prints `44` instead of `8`. Fix it.

<!-- no-verify -->
```python
plates = input("How many plates? ")
print(plates * 2)
```

<details>
<summary>Hint</summary>

What type does `input()` always return?

</details>

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
plates = int(input("How many plates? "))
print(plates * 2)
```

```console
How many plates? 4
8
```

</details>

#### Exercise 6: The broken name

Why does this crash, and how do you fix it?

<!-- no-verify -->
```python
list = ["tea", "coffee"]
print(len(list))
items = list("abc")
```

<details>
<summary>Show answer</summary>

`list` is a built-in name. After `list = ["tea", "coffee"]`, it no longer points to the tool that creates lists, so `list("abc")` fails with `TypeError: 'list' object is not callable`. Rename the variable:

```python
drinks = ["tea", "coffee"]
print(len(drinks))
items = list("abc")
print(items)
```

```text
2
['a', 'b', 'c']
```

</details>

### Write it

#### Exercise 7: Name length

Ask the user for their name with `input()` and print how many letters it has, like this:

```console
What is your name? Carla
Carla has 5 letters
```

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
name = input("What is your name? ")
print(f"{name} has {len(name)} letters")
```

</details>

#### Exercise 8: Splitting the bill

Ask for the bill total and the number of people (both with `input()`), and print how much each person pays, rounded to 2 decimal places.

```console
Bill total? 100
How many people? 3
Each person pays 33.33
```

<details>
<summary>Hint</summary>

The total can have cents, so convert it with `float()`. The number of people is whole, so use `int()`. Then use `round(value, 2)`.

</details>

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
total = float(input("Bill total? "))
people = int(input("How many people? "))
each = total / people
print(f"Each person pays {round(each, 2)}")
```

</details>

#### Exercise 9: Numbered to-do list

Create a list with three tasks and print it numbered from 1, in the format `1. task`.

<details>
<summary>Show answer</summary>

```python
tasks = ["water the plants", "call mom", "buy coffee"]
for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")
```

```text
1. water the plants
2. call mom
3. buy coffee
```

</details>

## Review

These revisit [data-types.md](data-types.md) and [strings.md](strings.md).

#### Review 1: Text plus number

Fix this line in two different ways:

<!-- no-verify -->
```python
print("Items: " + 3)
```

<details>
<summary>Show answer</summary>

```python
print("Items: " + str(3))
print(f"Items: {3}")
```

```text
Items: 3
Items: 3
```

</details>

#### Review 2: Predict the output

```python
a = 1
b = a
a = 5
print(f"{a} {b}")
```

<details>
<summary>Show answer</summary>

```text
5 1
```

`b` received the value `a` had at that moment (`1`). Changing `a` afterwards does not change `b`.

</details>

## Recap

- Built-in functions come with Python: `print`, `input`, `len`, `type`, `int`, `float`, `str`, `round`, `enumerate`.
- A function runs only when you **call** it: name **plus** parentheses. The name alone just describes the tool.
- `input()` always returns a `str`. Convert it before doing math.
- `enumerate(list, start=1)` gives you a number and an item in each turn of a loop.
- Keywords (`def`, `return`, `for`...) cannot be names. Built-in names (`str`, `list`, `len`...) can, but you should never reuse them.

**Next:** [practice.md](practice.md)
