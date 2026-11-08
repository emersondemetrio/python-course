# Scope: where variables live

> **In one sentence:** a variable created inside a function exists only inside that function, so functions should receive what they need as parameters and give results back with `return`.

## Why it matters

As programs grow, you will have many variables with similar names in different places. If any part of the program could change any variable, a small change in one function could break something far away, and you would never find out why.

**Scope** is Python's rule about which part of the code can see which variable. Understanding it helps you write functions that are like closed boxes: clear inputs, clear outputs, no surprises.

## Analogy

Think of a function as a **kitchen in a restaurant**.

- What happens in the kitchen stays in the kitchen. The cook's bowls and knives (the **local variables**) are not visible from the dining room.
- The order comes in through a window (the **parameters**), and the plate goes out through the same window (the **return value**).
- The kitchen can look at the menu on the wall of the dining room (a **global variable**), but it should not walk out and rearrange the tables.

## The idea, step by step

### Local variables: created inside, live inside

A variable created inside a function is **local**. It is born when the function runs and disappears when the function ends.

<!-- error -->
```python
def make_tea():
    kettle = "hot"
    print(f"The kettle is {kettle}.")

make_tea()
print(kettle)
```

```text
The kettle is hot.
Traceback (most recent call last):
    print(kettle)
          ^^^^^^
NameError: name 'kettle' is not defined
```

Inside `make_tea`, `kettle` exists. Outside, after the function ended, it does not. If you need a value from inside a function, **return** it:

```python
def make_tea():
    kettle = "hot"
    return kettle

result = make_tea()
print(result)
```

Output:

```text
hot
```

Parameters are local too. In `def greet(name):`, the variable `name` only exists while `greet` is running.

### Global variables: created outside

A variable created outside any function, at the top level of the file, is **global**. Functions can **read** it:

```python
store_name = "Corner Café"

def welcome():
    print(f"Welcome to {store_name}!")

welcome()
```

Output:

```text
Welcome to Corner Café!
```

### Same name, different variables

A local variable can have the same name as a global one. They are still two different variables:

```python
message = "I am global"

def show():
    message = "I am local"
    print(message)

show()
print(message)
```

Output:

```text
I am local
I am global
```

Creating `message` inside the function did **not** change the global one. It created a new, local `message` that disappeared at the end of `show`.

### Changing a global from inside a function: avoid it

Here is a classic trap:

<!-- error -->
```python
visits = 0

def add_visit():
    visits = visits + 1

add_visit()
```

```text
    visits = visits + 1
             ^^^^^^
UnboundLocalError: cannot access local variable 'visits' where it is not associated with a value
```

Because the function **assigns** to `visits` (with `=`), Python decides that `visits` is a local variable of this function. Then, on the right side, it tries to read that local `visits`, which has no value yet.

Python has a keyword `global` that makes this work, but experienced programmers avoid it. The better way is to pass the value in and return the new value:

```python
def add_visit(visits):
    return visits + 1

visits = 0
visits = add_visit(visits)
visits = add_visit(visits)
print(visits)
```

Output:

```text
2
```

Now the function is a closed box: it receives a number, returns a number, and does not depend on anything outside.

### Why closed boxes are better

Compare two versions of the same program.

**Version 1:** functions reach out to global variables.

```python
prices = [10, 20, 30]
total = 0

def calculate():
    for p in prices:
        print(p)

calculate()
print(total)
```

Output:

```text
10
20
30
0
```

It is hard to tell what `calculate` needs and what it produces just by looking at its name and its `def` line. And it does not even calculate a total.

**Version 2:** everything goes in through parameters and out through `return`.

```python
def calculate_total(prices):
    total = 0
    for p in prices:
        total += p
    return total

cart = [10, 20, 30]
print(calculate_total(cart))
print(calculate_total([5, 5]))
```

Output:

```text
60
10
```

From the line `def calculate_total(prices):` alone, you know what it needs. You can use it with any list. You can test it by itself. This is the habit to build: **values in through parameters, results out through return.**

### One function controls the flow: main()

When a program has several functions, it helps to have **one** function that controls the whole flow, calling the others in order. By convention, it is called `main`.

```python
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
```

Output:

```text
Hello, Ana! Welcome back.
```

Reading `main` is like reading a table of contents: ask the name, build the greeting, show it. Each step is a function with one job, and the values travel between them through returns and arguments. Nothing is stored in global variables.

Notice that the file only **defines** functions, and the very last line calls `main()`. That one line starts everything.

### A peek ahead: `if __name__ == "__main__":`

In many Python programs you will see this at the end:

```python
def main():
    print("Program started")

if __name__ == "__main__":
    main()
```

Output:

```text
Program started
```

For now, read it as: "if this file is the one being run, call `main()`". It matters when you split a program into several files (module 07). Until then, a plain `main()` at the bottom is fine.

## Common mistakes

### Trying to use a local variable outside its function

<!-- error -->
```python
def calculate():
    result = 2 + 2

calculate()
print(result)
```

```text
    print(result)
          ^^^^^^
NameError: name 'result' is not defined
```

`result` only existed inside `calculate`. Return it and store it: `result = calculate()` (with `return 2 + 2` in the function).

### Changing a global inside a function

<!-- error -->
```python
count = 0

def increase():
    count += 1

increase()
```

```text
    count += 1
    ^^^^^
UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
```

Pass the value as a parameter and return the new one: `def increase(count): return count + 1`, then `count = increase(count)`.

### Calling main twice, or forgetting to call it

If you define `main()` but never call it, the program runs and prints nothing. If you call it in two places, everything happens twice. There should be exactly one `main()` call, at the bottom of the file.

## Exercises

### Predict the output

#### Exercise 1: Same name

```python
color = "blue"

def paint():
    color = "red"
    return color

print(paint())
print(color)
```

<details>
<summary>Show answer</summary>

```text
red
blue
```

The `color` inside `paint` is a separate, local variable. The global `color` was never changed.

</details>

#### Exercise 2: Passing values along

```python
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
```

<details>
<summary>Show answer</summary>

```text
50
```

4, then `step_one` gives 5, then `step_two` gives 50.

</details>

#### Exercise 3: Will it crash?

Which line crashes, and with which error?

<!-- no-verify -->
```python
def make_list():
    items = ["a", "b"]
    return len(items)

size = make_list()
print(size)
print(items)
```

<details>
<summary>Show answer</summary>

It prints `2`, then crashes on the last line with `NameError: name 'items' is not defined`. `items` is local to `make_list`. The function returned only its length, not the list.

</details>

### Fix the bug

#### Exercise 4: The counter

Rewrite this so it works **without** using `global`, and prints `3`.

<!-- no-verify -->
```python
likes = 0

def like():
    likes = likes + 1

like()
like()
like()
print(likes)
```

<details>
<summary>Show answer</summary>

```python
def like(likes):
    return likes + 1

likes = 0
likes = like(likes)
likes = like(likes)
likes = like(likes)
print(likes)
```

Output:

```text
3
```

</details>

### Write it

#### Exercise 5: A tiny program with main

Write a program with three functions and a `main`:

- `get_items()` returns the list `["notebook", "pen", "eraser"]`
- `format_items(items)` returns a new list with each item numbered from 1 (`"1. notebook"`)
- `show(lines)` prints each line
- `main()` calls them in order

<details>
<summary>Show answer</summary>

```python
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
```

Output:

```text
1. notebook
2. pen
3. eraser
```

Each function does one job, and `main` shows the whole story in three lines.

</details>

#### Exercise 6: Remove the globals

This program works, but every function depends on global variables. Rewrite it so each function receives what it needs and returns its result. Keep the output the same.

<!-- no-verify -->
```python
name = "Bruno"
hours = 6
rate = 20
pay = 0

def calculate_pay():
    global pay
    pay = hours * rate

def show_pay():
    print(f"{name} earned {pay} dollars.")

calculate_pay()
show_pay()
```

<details>
<summary>Show answer</summary>

```python
def calculate_pay(hours, rate):
    return hours * rate

def pay_message(name, pay):
    return f"{name} earned {pay} dollars."

def main():
    pay = calculate_pay(6, 20)
    print(pay_message("Bruno", pay))

main()
```

Output:

```text
Bruno earned 120 dollars.
```

Now you can use `calculate_pay` for anyone, with any numbers, without touching global variables.

</details>

## Review

#### Review 1: return vs print again

Without running it, how many lines does this print, and what are they?

```python
def shout(word):
    print(word.upper())

def whisper(word):
    return word.lower()

shout("hello")
whisper("HELLO")
print(whisper("BYE"))
```

<details>
<summary>Show answer</summary>

```text
HELLO
bye
```

Two lines. `shout` prints by itself. The first `whisper` call returns `"hello"`, but nobody stores or prints it, so it is lost. The last line prints what `whisper` returned.

</details>

#### Review 2: Loop inside a function

Write a function `total_length(words)` that returns the total number of letters in a list of words. Test it with `["sun", "moon"]` (should be 7).

<details>
<summary>Show answer</summary>

```python
def total_length(words):
    total = 0
    for word in words:
        total += len(word)
    return total

print(total_length(["sun", "moon"]))
```

Output:

```text
7
```

</details>

## Recap

- Variables created inside a function (including parameters) are **local**: they disappear when the function ends.
- Variables created outside functions are **global**: functions can read them, but should not change them.
- If a function assigns to a name, Python treats that name as local, which causes `UnboundLocalError` when you try to update a global.
- Build functions as closed boxes: values in through **parameters**, results out through **return**.
- A `main()` function controls the flow by calling the others in order; call it once, at the bottom of the file.

**Next:** [reading-errors.md](reading-errors.md)
