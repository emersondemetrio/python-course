# Loops: doing things again and again

> **In one sentence:** a loop runs the same block of code several times, for example once for every item of a list.

## Why it matters

Imagine printing a list of 500 contacts with one `print` per contact. You would need 500 lines, and the program would break the day you add contact number 501. A loop says: "for **each** contact, print it". Three lines, and it works for any number of contacts.

Computers are great at repetition. Loops are how you ask them to repeat.

## Analogy

Think of washing dishes after dinner. You do not have a separate plan for each plate. You have **one** routine (scrub, rinse, put on the rack), and you repeat it **for each** dish in the sink. When the sink is empty, you stop.

- The sink is the **list**.
- The routine is the **block** of the loop.
- "The dish in my hands right now" is the **loop variable**.

## The idea, step by step

### for: once for each item

```python
groceries = ["milk", "eggs", "bread"]

for item in groceries:
    print(item)

print("Done!")
```

Output:

```text
milk
eggs
bread
Done!
```

How to read it: "**for** each `item` **in** `groceries`, print the item."

What happens behind the scenes:

1. Python takes the first item (`"milk"`), puts it in the variable `item`, and runs the block.
2. It takes the second item (`"eggs"`), puts it in `item`, and runs the block again.
3. Same for `"bread"`.
4. No more items, so the loop ends and Python continues with `print("Done!")`.

Like `if`, the `for` line ends with `:` and the block is indented. `print("Done!")` is not indented, so it runs once, after the loop.

You choose the name of the loop variable. Pick a name that describes **one** item: `for item in groceries`, `for name in names`, `for price in prices`.

### Doing more inside the loop

The block can have several lines, and it can use f-strings, `if`, anything you already know:

```python
prices = [12, 45, 8, 60]

for price in prices:
    if price > 40:
        print(f"{price} dollars: expensive")
    else:
        print(f"{price} dollars: fine")
```

Output:

```text
12 dollars: fine
45 dollars: expensive
8 dollars: fine
60 dollars: expensive
```

Look at the indentation: `if` is inside the `for` (4 spaces), and `print` is inside the `if` (8 spaces).

### Looping over a text

A text is a sequence of characters, so you can loop over it too:

```python
for letter in "hello":
    print(letter)
```

Output:

```text
h
e
l
l
o
```

### range: repeating a number of times

Sometimes you do not have a list, you just want to repeat something a few times. `range` creates a sequence of numbers:

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

`range(5)` gives **5 numbers**, starting at 0 and stopping **before** 5. Same rule as indexes and slices.

You can choose where to start:

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

`range(1, 6)` means "from 1, up to but not including 6". You can also give a third number, the **step**:

```python
for number in range(0, 21, 5):
    print(number)
```

Output:

```text
0
5
10
15
20
```

### enumerate: the item and its position

When you need to number items, use `enumerate`. It gives you two things at each step: the position **and** the item.

```python
groceries = ["milk", "eggs", "bread"]

for index, item in enumerate(groceries):
    print(index, item)
```

Output:

```text
0 milk
1 eggs
2 bread
```

Notice the two variables, separated by a comma: `index, item`. The first receives the position, the second receives the item.

People usually count from 1, not 0. `enumerate` accepts `start=1`:

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

### Counting: the counter pattern

A **counter** is a variable that starts at 0 and goes up by 1 each time something happens.

```python
scores = [7, 4, 9, 5, 10, 3]
passed = 0

for score in scores:
    if score >= 6:
        passed = passed + 1

print(f"{passed} students passed.")
```

Output:

```text
3 students passed.
```

The counter is created **before** the loop (so it starts at 0 only once) and printed **after** the loop (when all the counting is done).

`passed = passed + 1` can also be written `passed += 1`. They mean the same thing: "take the current value, add 1, store it back".

### Adding up: the accumulator pattern

An **accumulator** is like a counter, but instead of adding 1, it adds each value:

```python
cart = [12.50, 3.00, 8.25]
total = 0

for price in cart:
    total += price

print(f"Total: {total}")
```

Output:

```text
Total: 23.75
```

This is what `sum()` does for you. Writing it by hand is worth it because the same pattern works for things `sum()` cannot do, like adding only some of the items.

### Building a new list

Start with an empty list and `append` inside the loop:

```python
names = ["ana", "bruno", "carla"]
capitalized = []

for name in names:
    capitalized.append(name.capitalize())

print(capitalized)
```

Output:

```text
['Ana', 'Bruno', 'Carla']
```

You can also build a list with only **some** of the items (this is called **filtering**):

```python
temperatures = [18, 25, 31, 22, 35]
hot_days = []

for temperature in temperatures:
    if temperature > 30:
        hot_days.append(temperature)

print(hot_days)
```

Output:

```text
[31, 35]
```

### while: repeat while a condition is true

`for` repeats once per item. `while` repeats **as long as a condition is true**. It is like an `if` that keeps asking again.

```python
countdown = 3

while countdown > 0:
    print(countdown)
    countdown = countdown - 1

print("Go!")
```

Output:

```text
3
2
1
Go!
```

Each time the block runs, `countdown` goes down by 1. When it reaches 0, the condition `countdown > 0` becomes false, and the loop ends.

The line `countdown = countdown - 1` is essential. Without it, `countdown` would stay at 3 forever.

### break: leave the loop early

`break` stops the loop immediately, even if there are items left.

```python
emails = ["ana@mail.com", "bruno.mail.com", "carla@mail.com"]

for email in emails:
    if "@" not in email:
        print(f"Invalid email found: {email}")
        break
    print(f"{email} is fine")
```

Output:

```text
ana@mail.com is fine
Invalid email found: bruno.mail.com
```

`"carla@mail.com"` was never checked, because `break` ended the loop.

### The infinite loop, and how to stop it

If the condition of a `while` never becomes false, the loop never ends. This is called an **infinite loop**:

<!-- no-verify -->
```python
count = 1

while count > 0:
    print(count)
    count = count + 1   # count only grows, so it is always > 0
```

Your terminal will fill with numbers and never stop. **Do not panic.** Click on the terminal and press **Ctrl+C**. This stops the running program. You will see a `KeyboardInterrupt` message, which just means "the user stopped me".

Sometimes an infinite loop is on purpose, with a `break` inside. This is common for menus:

<!-- no-verify -->
```python
while True:
    answer = input("Type 'quit' to exit: ")
    if answer == "quit":
        break
    print(f"You typed: {answer}")

print("Bye!")
```

```console
PS C:\Users\you\Projects> python menu.py
Type 'quit' to exit: hello
You typed: hello
Type 'quit' to exit: quit
Bye!
```

### for or while?

| Use `for` when... | Use `while` when... |
|---|---|
| you have a list (or text, or range) to go through | you do not know how many times it will repeat |
| "do this for each item" | "keep doing this until something happens" |
| example: print every contact | example: keep asking until the password is right |

If you are unsure, start with `for`. It cannot become an infinite loop by accident.

## Common mistakes

### Forgetting to indent the block

<!-- error -->
```python
for item in ["a", "b"]:
print(item)
```

```text
    print(item)
    ^^^^^
IndentationError: expected an indented block after 'for' statement on line 1
```

Just like `if`, the lines inside a `for` must be indented.

### Resetting the total inside the loop

```python
cart = [10, 20, 30]

for price in cart:
    total = 0
    total += price

print(total)
```

Output:

```text
30
```

The total should be 60. The problem: `total = 0` is **inside** the loop, so it resets to 0 on every item. Only the last price survives. Move it before the loop:

```python
cart = [10, 20, 30]
total = 0

for price in cart:
    total += price

print(total)
```

Output:

```text
60
```

### Printing inside the loop when you meant after

```python
cart = [10, 20, 30]
total = 0

for price in cart:
    total += price
    print(total)
```

Output:

```text
10
30
60
```

Because `print` is indented, it runs on every step. If you only want the final result, remove the indentation so `print` runs once, after the loop.

### Off by one with range

```python
for day in range(1, 7):
    print(f"Day {day}")
```

Output:

```text
Day 1
Day 2
Day 3
Day 4
Day 5
Day 6
```

If you wanted 7 days, you need `range(1, 8)`. The stop number is never included.

### Forgetting to change the condition in while

If the variable in the condition never changes, the loop never ends. Every `while` should have a line inside that moves it closer to stopping (like `count = count - 1`). If you get stuck, press **Ctrl+C**.

## Exercises

### Predict the output

#### Exercise 1: Simple for

```python
colors = ["red", "green", "blue"]

for color in colors:
    print(f"I like {color}")
print("That's all")
```

<details>
<summary>Show answer</summary>

```text
I like red
I like green
I like blue
That's all
```

The loop runs once per color. The last `print` is not indented, so it runs once, after the loop.

</details>

#### Exercise 2: Counter

```python
words = ["sun", "moon", "sky", "star", "sea"]
count = 0

for word in words:
    if len(word) == 3:
        count += 1

print(count)
```

<details>
<summary>Show answer</summary>

```text
3
```

`"sun"`, `"sky"` and `"sea"` have 3 letters. `"moon"` and `"star"` have 4.

</details>

#### Exercise 3: range and while

```python
for i in range(2, 5):
    print(i)

n = 10
while n > 4:
    n = n - 3
print(n)
```

<details>
<summary>Show answer</summary>

```text
2
3
4
4
```

`range(2, 5)` gives 2, 3, 4. Then `n` goes 10, 7, 4. When `n` is 4, `4 > 4` is false, so the loop stops and prints 4.

</details>

### Fix the bug

#### Exercise 4: The numbered menu

This should print a menu numbered from 1, but it starts at 0. Fix it.

<!-- no-verify -->
```python
menu = ["Espresso", "Latte", "Tea"]

for number, drink in enumerate(menu):
    print(f"{number}. {drink}")
```

<details>
<summary>Show answer</summary>

```python
menu = ["Espresso", "Latte", "Tea"]

for number, drink in enumerate(menu, start=1):
    print(f"{number}. {drink}")
```

Output:

```text
1. Espresso
2. Latte
3. Tea
```

</details>

#### Exercise 5: Counting expensive items

This program should count how many prices are above 20, but it always prints 1 or 0. Fix it.

<!-- no-verify -->
```python
prices = [25, 10, 30, 40, 5]

for price in prices:
    expensive = 0
    if price > 20:
        expensive += 1

print(expensive)
```

<details>
<summary>Show answer</summary>

```python
prices = [25, 10, 30, 40, 5]
expensive = 0

for price in prices:
    if price > 20:
        expensive += 1

print(expensive)
```

Output:

```text
3
```

The counter must start **before** the loop. Inside the loop, it was reset to 0 on every item.

</details>

### Write it

#### Exercise 6: Shopping list

Given `groceries = ["rice", "beans", "tomatoes", "onions"]`, print each item numbered from 1, and then the line `4 items in total`, using `len()`.

<details>
<summary>Show answer</summary>

```python
groceries = ["rice", "beans", "tomatoes", "onions"]

for number, item in enumerate(groceries, start=1):
    print(f"{number}. {item}")

print(f"{len(groceries)} items in total")
```

Output:

```text
1. rice
2. beans
3. tomatoes
4. onions
4 items in total
```

</details>

#### Exercise 7: Total without sum

Given `expenses = [35.0, 12.5, 80.0, 7.5]`, calculate the total **using a loop** (not `sum`) and print `Total spent: 135.0`.

<details>
<summary>Show answer</summary>

```python
expenses = [35.0, 12.5, 80.0, 7.5]
total = 0

for expense in expenses:
    total += expense

print(f"Total spent: {total}")
```

Output:

```text
Total spent: 135.0
```

</details>

#### Exercise 8: Short words

Given `words = ["tea", "coffee", "milk", "water", "ice"]`, build a new list called `short` with only the words that have **4 letters or fewer**, and print it.

<details>
<summary>Show answer</summary>

```python
words = ["tea", "coffee", "milk", "water", "ice"]
short = []

for word in words:
    if len(word) <= 4:
        short.append(word)

print(short)
```

Output:

```text
['tea', 'milk', 'ice']
```

</details>

#### Exercise 9: Multiplication table

Using `range`, print the multiplication table of 7, from `7 x 1 = 7` to `7 x 10 = 70`.

<details>
<summary>Show answer</summary>

```python
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
```

Output:

```text
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

`range(1, 11)` because the stop is not included.

</details>

## Review

#### Review 1: Vowels

Count how many vowels there are in the text `"programming is fun"`. (This mixes loops, `in` and a counter.)

<details>
<summary>Hint</summary>

Loop over each letter. For each letter, check if it is `in "aeiou"`.

</details>

<details>
<summary>Show answer</summary>

```python
text = "programming is fun"
vowels = 0

for letter in text:
    if letter in "aeiou":
        vowels += 1

print(vowels)
```

Output:

```text
5
```

o, a, i, i, u.

</details>

#### Review 2: Grades report

Given `grades = [9, 4, 7, 10, 5]`, print each grade with a label, like `9: passed` or `4: failed` (6 or more passes). At the end, print the average.

<details>
<summary>Show answer</summary>

```python
grades = [9, 4, 7, 10, 5]

for grade in grades:
    if grade >= 6:
        print(f"{grade}: passed")
    else:
        print(f"{grade}: failed")

print(f"Average: {sum(grades) / len(grades)}")
```

Output:

```text
9: passed
4: failed
7: passed
10: passed
5: failed
Average: 7.0
```

</details>

## Recap

- `for item in my_list:` runs the indented block once for each item. The loop variable holds the current item.
- `range(start, stop)` makes numbers to loop over; the stop is not included. `enumerate(my_list, start=1)` gives position and item.
- Counter: start at 0 before the loop, `+= 1` inside. Accumulator: start at 0 before, `+= value` inside. Print after the loop.
- To build a list, start with `[]` before the loop and `append` inside.
- `while` repeats while a condition is true; something inside must change it. `break` leaves a loop early. **Ctrl+C** stops a program that is stuck.

**Next:** [Module 03: Functions](../module-03-functions/README.md)
