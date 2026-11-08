# Conditionals: making decisions

> **In one sentence:** a conditional lets your program run some lines only when a condition is true.

## Why it matters

Almost every useful program makes decisions. A shopping app shows "free shipping" only if the total is high enough. A login screen lets you in only if the password matches. Without conditionals, a program does the exact same thing every time, no matter what.

## Analogy

Think about leaving home in the morning. You look out the window and think: "**If** it is raining, I take an umbrella. **Otherwise**, I take sunglasses."

You do not take both, and you do not skip the decision. You check one thing (is it raining?), and the answer decides what you do. That is exactly what `if` and `else` do in Python.

## The idea, step by step

### True and False

Python has a type of value with only two options: `True` and `False`. This type is called **bool** (short for *boolean*, named after the mathematician George Boole).

Notice the capital letters: `True` and `False`, not `true` and `false`.

```python
is_raining = True
print(is_raining)
print(type(is_raining))
```

Output:

```text
True
<class 'bool'>
```

### Comparisons create True or False

When you compare two values, Python answers with `True` or `False`.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | is equal to | `5 == 5` | `True` |
| `!=` | is not equal to | `5 != 3` | `True` |
| `>` | is greater than | `5 > 3` | `True` |
| `<` | is less than | `5 < 3` | `False` |
| `>=` | is greater than or equal to | `5 >= 5` | `True` |
| `<=` | is less than or equal to | `3 <= 2` | `False` |

```python
print(10 > 3)
print(10 == 3)
print("apple" == "apple")
print("apple" == "Apple")
```

Output:

```text
True
False
True
False
```

The last one is `False` because Python treats uppercase and lowercase letters as different. `"apple"` and `"Apple"` are not the same text.

> **Important:** `=` and `==` are different things.
> - `=` **stores** a value in a variable: `age = 30` ("age now holds 30").
> - `==` **asks** a question: `age == 30` ("is age equal to 30?").

### if: do something only when the condition is true

```python
temperature = 32

if temperature > 30:
    print("It is hot today.")
    print("Drink some water.")

print("Have a nice day!")
```

Output:

```text
It is hot today.
Drink some water.
Have a nice day!
```

Three things to notice:

1. The line with `if` ends with a colon `:`.
2. The lines that belong to the `if` are **indented** (moved to the right by 4 spaces). This is called the **block** of the `if`.
3. `print("Have a nice day!")` is not indented, so it is **outside** the `if`. It always runs.

Now change the temperature to `20` and run it again:

```python
temperature = 20

if temperature > 30:
    print("It is hot today.")
    print("Drink some water.")

print("Have a nice day!")
```

Output:

```text
Have a nice day!
```

The condition was `False`, so Python skipped the whole block.

### Indentation is not decoration

In many languages, indentation is only to make code pretty. In Python, indentation **is the structure**. It tells Python which lines belong to which block. Use 4 spaces (Cursor does this automatically when you press Tab after a `:`).

### else: what to do otherwise

```python
is_raining = False

if is_raining:
    print("Take an umbrella.")
else:
    print("Take sunglasses.")
```

Output:

```text
Take sunglasses.
```

`else` has no condition. It means "in every other case". It also ends with `:` and has its own indented block.

Notice `if is_raining:`. Since `is_raining` is already `True` or `False`, you do not need to write `if is_raining == True:`. Both work, but the short form is the usual one.

### elif: more than two paths

`elif` means "else, if". Use it when there are several options.

```python
score = 75

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 50:
    print("Okay")
else:
    print("Needs practice")
```

Output:

```text
Good
```

Python checks the conditions **from top to bottom** and runs **only the first one that is true**. Then it jumps past the whole `if`/`elif`/`else` group. Even though `75 >= 50` is also true, "Okay" is never printed, because Python already found a match.

### Two ifs are not the same as if/elif

This is a very common source of bugs. Compare:

```python
level = "error"

if level == "error":
    print("Something went wrong")
if level == "error" or level == "warning":
    print("Check the logs")
```

Output:

```text
Something went wrong
Check the logs
```

Two separate `if`s are two separate questions. Python asks both, so both blocks can run.

```python
level = "error"

if level == "error":
    print("Something went wrong")
elif level == "error" or level == "warning":
    print("Check the logs")
```

Output:

```text
Something went wrong
```

With `elif`, they become **one** decision. Once the first one matches, the rest is skipped.

Rule of thumb: if only **one** of the options should happen, use `if`/`elif`/`else`.

### in: is it inside?

The word `in` checks if something is inside something else. It works with text and, as you will see in the next file, with lists.

```python
print("a" in "banana")
print("z" in "banana")
print("nan" in "banana")
```

Output:

```text
True
False
True
```

```python
email = "ana@example.com"

if "@" in email:
    print("Looks like an email.")
else:
    print("This is not an email.")
```

Output:

```text
Looks like an email.
```

You can also use `not in`:

```python
password = "sunshine"

if "1" not in password:
    print("Your password should contain a number.")
```

Output:

```text
Your password should contain a number.
```

### and, or, not: combining conditions

| Word | True when... | Example |
|---|---|---|
| `and` | **both** sides are true | `age >= 18 and has_ticket` |
| `or` | **at least one** side is true | `day == "Saturday" or day == "Sunday"` |
| `not` | the condition is false (it flips it) | `not is_raining` |

```python
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter.")
```

Output:

```text
You can enter.
```

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend!")
else:
    print("Workday.")
```

Output:

```text
Weekend!
```

```python
is_raining = False

if not is_raining:
    print("Let's go for a walk.")
```

Output:

```text
Let's go for a walk.
```

### The classic `or` bug

This code looks right when you read it in English, but it is wrong:

```python
day = "Monday"

if day == "Saturday" or "Sunday":
    print("Weekend!")
```

Output:

```text
Weekend!
```

Monday is not the weekend, so why did it print? Python reads the condition as two separate pieces:

- `day == "Saturday"` is `False`
- `"Sunday"` alone... is just a text. And Python treats any non-empty text as "true enough".

So the whole thing is `False or "Sunday"`, which counts as true. The fix is to **repeat the comparison** on both sides:

```python
day = "Monday"

if day == "Saturday" or day == "Sunday":
    print("Weekend!")
else:
    print("Workday.")
```

Output:

```text
Workday.
```

## Common mistakes

### Using `=` instead of `==`

<!-- error -->
```python
temperature = 30
if temperature = 30:
    print("Hot")
```

```text
    if temperature = 30:
       ^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

`=` stores a value; it cannot ask a question. Python even suggests the fix. Use `==`:

```python
temperature = 30
if temperature == 30:
    print("Hot")
```

Output:

```text
Hot
```

### Forgetting the colon

<!-- error -->
```python
age = 20
if age >= 18
    print("Adult")
```

```text
    if age >= 18
                ^
SyntaxError: expected ':'
```

Every `if`, `elif` and `else` line ends with `:`. The fix is `if age >= 18:`.

### Forgetting to indent

<!-- error -->
```python
age = 20
if age >= 18:
print("Adult")
```

```text
    print("Adult")
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 2
```

After a `:`, Python expects at least one indented line. Move `print` 4 spaces to the right.

### Uppercase and lowercase

```python
answer = "Yes"

if answer == "yes":
    print("Great!")
else:
    print("Okay, maybe later.")
```

Output:

```text
Okay, maybe later.
```

No error, but the wrong result: `"Yes"` is not equal to `"yes"`. A common fix is to make the text lowercase first with `.lower()`:

```python
answer = "Yes"

if answer.lower() == "yes":
    print("Great!")
else:
    print("Okay, maybe later.")
```

Output:

```text
Great!
```

### The `or` shortcut

Writing `if x == "a" or "b":` is always true. Write `if x == "a" or x == "b":`. (See "The classic `or` bug" above.)

## Exercises

### Predict the output

Read the code and write down what it prints **before** running it. Then run it to check.

#### Exercise 1: Coffee size

```python
size = "large"

if size == "small":
    print("That will be 3 dollars.")
elif size == "medium":
    print("That will be 4 dollars.")
else:
    print("That will be 5 dollars.")
```

<details>
<summary>Show answer</summary>

```text
That will be 5 dollars.
```

`size` is `"large"`. It is not `"small"` and not `"medium"`, so Python falls into `else`.

</details>

#### Exercise 2: Two ifs

```python
stock = 0

if stock == 0:
    print("Out of stock")
if stock < 5:
    print("Order more")
print("Done")
```

<details>
<summary>Show answer</summary>

```text
Out of stock
Order more
Done
```

These are two separate `if`s, so Python checks both. `0 == 0` is true and `0 < 5` is also true. `Done` is outside both blocks, so it always prints.

</details>

#### Exercise 3: True or False?

```python
print(7 >= 7)
print("cat" in "concatenate")
print(not (3 > 1))
print(10 != 10 or 2 < 3)
```

<details>
<summary>Show answer</summary>

```text
True
True
False
True
```

- `7 >= 7`: 7 is equal to 7, so "greater than or equal" is true.
- `"cat"` appears inside "con**cat**enate".
- `3 > 1` is true, and `not` flips it to false.
- `10 != 10` is false, but `2 < 3` is true, and `or` only needs one side.

</details>

### Fix the bug

#### Exercise 4: The weekend checker

This program prints "Weekend!" even on a Tuesday. Find the problem and fix it.

<!-- no-verify -->
```python
day = "Tuesday"

if day == "Saturday" or "Sunday":
    print("Weekend!")
else:
    print("Workday.")
```

<details>
<summary>Hint</summary>

Read the condition out loud the way Python reads it: two separate pieces joined by `or`.

</details>

<details>
<summary>Show answer</summary>

```python
day = "Tuesday"

if day == "Saturday" or day == "Sunday":
    print("Weekend!")
else:
    print("Workday.")
```

Output:

```text
Workday.
```

`"Sunday"` on its own is a non-empty text, which counts as true. You must repeat `day ==` on the right side of `or`.

</details>

#### Exercise 5: Only one message

This program should print only **one** message, but for a price of 150 it prints two. Fix it.

<!-- no-verify -->
```python
price = 150

if price > 100:
    print("Expensive")
if price > 50:
    print("Medium")
else:
    print("Cheap")
```

<details>
<summary>Show answer</summary>

```python
price = 150

if price > 100:
    print("Expensive")
elif price > 50:
    print("Medium")
else:
    print("Cheap")
```

Output:

```text
Expensive
```

Changing the second `if` to `elif` turns the two questions into one decision. Only the first true condition runs.

</details>

### Write it

#### Exercise 6: Even or odd

Create a variable `number` with any whole number. Print `"even"` if it is even and `"odd"` if it is odd.

<details>
<summary>Hint</summary>

The `%` operator gives the remainder of a division. `7 % 2` is `1`, `8 % 2` is `0`. Even numbers have remainder 0 when divided by 2.

</details>

<details>
<summary>Show answer</summary>

```python
number = 7

if number % 2 == 0:
    print("even")
else:
    print("odd")
```

Output:

```text
odd
```

</details>

#### Exercise 7: Free shipping

A store gives free shipping for orders of 50 dollars or more. Create a variable `total` and print `"Free shipping!"` or `"Shipping costs 8 dollars."`. Then, in the second case, also print how much more the customer needs to spend to get free shipping, using an f-string.

<details>
<summary>Show answer</summary>

```python
total = 42

if total >= 50:
    print("Free shipping!")
else:
    print("Shipping costs 8 dollars.")
    print(f"Spend {50 - total} more dollars to get free shipping.")
```

Output:

```text
Shipping costs 8 dollars.
Spend 8 more dollars to get free shipping.
```

Note that `>=` is the right operator here: an order of exactly 50 should get free shipping.

</details>

#### Exercise 8: Water state

Create a variable `temperature` (in Celsius). Print:

- `"ice"` if it is 0 or below
- `"water"` if it is between 1 and 99
- `"steam"` if it is 100 or above

<details>
<summary>Show answer</summary>

```python
temperature = 100

if temperature <= 0:
    print("ice")
elif temperature < 100:
    print("water")
else:
    print("steam")
```

Output:

```text
steam
```

Because `elif` is only checked when the first condition was false, you do not need to write `temperature > 0 and temperature < 100`. By the time Python reaches the `elif`, it already knows the temperature is above 0.

</details>

## Review

These exercises bring back ideas from module 01.

#### Review 1: Mixing types

What does this print?

```python
age = 39
print(f"Next year I will be {age + 1}.")
print("Next year I will be " + str(age + 1) + ".")
```

<details>
<summary>Show answer</summary>

```text
Next year I will be 40.
Next year I will be 40.
```

Same result, two ways. The f-string calculates `age + 1` inside the braces and turns it into text for you. With `+`, you must convert the number to text yourself with `str()`.

</details>

#### Review 2: Long name

Write a program with a variable `name`. If the name has more than 6 letters, print `"<name> is a long name"`, otherwise print `"<name> is a short name"`.

<details>
<summary>Hint</summary>

The built-in function `len()` tells you how many characters a text has.

</details>

<details>
<summary>Show answer</summary>

```python
name = "Gabriela"

if len(name) > 6:
    print(f"{name} is a long name")
else:
    print(f"{name} is a short name")
```

Output:

```text
Gabriela is a long name
```

</details>

## Recap

- `True` and `False` are values of type `bool`. Comparisons like `5 > 3` produce them.
- `=` stores a value; `==` asks "is it equal?".
- `if` runs its indented block only when the condition is true. `else` covers every other case. `elif` adds more paths.
- In `if`/`elif`/`else`, only the **first** true condition runs. Two separate `if`s can both run.
- `and` needs both sides true, `or` needs one, `not` flips. Always write the full comparison on both sides of `or`.

**Next:** [lists.md](lists.md)
