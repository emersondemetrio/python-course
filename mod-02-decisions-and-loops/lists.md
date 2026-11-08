# Lists: many values in one place

> **In one sentence:** a list keeps several values together, in order, under one name.

## Why it matters

Real programs rarely deal with just one thing. A shopping app has many products, a music app has many songs, a contact book has many people. Creating one variable for each (`song1`, `song2`, `song3`...) does not work: you never know how many there will be. A list solves this: one name, as many items as you need.

## Analogy

Think of a shopping list on paper. It has a title ("groceries"), items written one below the other, and an order. You can read the first line, cross out an item, add a new one at the bottom, or count how many lines there are.

A Python list is that piece of paper. There is one important difference: Python counts the lines starting from **0**, not from 1.

## The idea, step by step

### Creating a list

Use square brackets `[ ]` and separate the items with commas:

```python
groceries = ["milk", "eggs", "bread", "coffee"]
print(groceries)
```

Output:

```text
['milk', 'eggs', 'bread', 'coffee']
```

A list can hold any type of value: texts, numbers, or even a mix.

```python
temperatures = [22, 25, 19, 30]
empty = []
print(temperatures)
print(empty)
```

Output:

```text
[22, 25, 19, 30]
[]
```

### How many items: len

The same `len()` you used for texts also works for lists:

```python
groceries = ["milk", "eggs", "bread", "coffee"]
print(len(groceries))
```

Output:

```text
4
```

### Reading one item: the index

Each item has a position, called its **index**. The first item is at index **0**.

| Index | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Item | `"milk"` | `"eggs"` | `"bread"` | `"coffee"` |

```python
groceries = ["milk", "eggs", "bread", "coffee"]
print(groceries[0])
print(groceries[2])
```

Output:

```text
milk
bread
```

Why start at 0? Think of the index as "how many steps from the start". The first item is 0 steps away from the start.

A useful consequence: the **last** index is always `len(list) - 1`. A list with 4 items has indexes 0, 1, 2 and 3.

### Negative indexes: counting from the end

Index `-1` means the last item, `-2` the one before it, and so on:

```python
groceries = ["milk", "eggs", "bread", "coffee"]
print(groceries[-1])
print(groceries[-2])
```

Output:

```text
coffee
bread
```

### Changing an item

You can replace an item by assigning to its index:

```python
groceries = ["milk", "eggs", "bread", "coffee"]
groceries[1] = "cheese"
print(groceries)
```

Output:

```text
['milk', 'cheese', 'bread', 'coffee']
```

### Adding items: append

`append` adds an item to the **end** of the list:

```python
groceries = ["milk", "eggs"]
groceries.append("apples")
groceries.append("rice")
print(groceries)
print(len(groceries))
```

Output:

```text
['milk', 'eggs', 'apples', 'rice']
4
```

Notice the dot: `groceries.append(...)`. Functions that belong to a value are called **methods**, and you call them with a dot. You already used one with text: `"hello".upper()`.

### Removing items: remove and pop

`remove` deletes an item by its **value**:

```python
groceries = ["milk", "eggs", "bread"]
groceries.remove("eggs")
print(groceries)
```

Output:

```text
['milk', 'bread']
```

`pop` removes an item by its **position** and gives it back to you. Without a number, it removes the last one:

```python
groceries = ["milk", "eggs", "bread"]
last = groceries.pop()
print(last)
print(groceries)

first = groceries.pop(0)
print(first)
print(groceries)
```

Output:

```text
bread
['milk', 'eggs']
milk
['eggs']
```

### Is it in the list? in

The same `in` you used with text works with lists:

```python
groceries = ["milk", "eggs", "bread"]

print("eggs" in groceries)
print("butter" in groceries)

if "coffee" not in groceries:
    groceries.append("coffee")

print(groceries)
```

Output:

```text
True
False
['milk', 'eggs', 'bread', 'coffee']
```

### Slicing: a piece of the list

A **slice** gives you a new list with part of the items. You write `[start:stop]`. The item at `start` is included, the item at `stop` is **not**.

```python
letters = ["a", "b", "c", "d", "e"]

print(letters[1:3])
print(letters[:2])
print(letters[2:])
```

Output:

```text
['b', 'c']
['a', 'b']
['c', 'd', 'e']
```

- `[1:3]`: from index 1 up to (but not including) index 3.
- `[:2]`: leaving out the start means "from the beginning".
- `[2:]`: leaving out the stop means "until the end".

One way to remember: `[:2]` gives you the first **2** items.

### Lists of numbers: sum, min, max

Python has built-in functions that work on lists of numbers:

```python
temperatures = [22, 25, 19, 30]

print(sum(temperatures))
print(min(temperatures))
print(max(temperatures))
print(sum(temperatures) / len(temperatures))
```

Output:

```text
96
19
30
24.0
```

The last line is the **average**: the total divided by how many there are.

### Putting in order: sorted

`sorted()` gives you a **new** list in order. The original list does not change.

```python
temperatures = [22, 25, 19, 30]
in_order = sorted(temperatures)

print(in_order)
print(temperatures)

names = ["Paula", "ana", "Bruno"]
print(sorted(names))
```

Output:

```text
[19, 22, 25, 30]
[22, 25, 19, 30]
['Bruno', 'Paula', 'ana']
```

Did you notice `'ana'` at the end? When sorting text, Python puts all uppercase letters before lowercase ones. That is one more reason to keep your data consistent.

## Common mistakes

### Asking for an index that does not exist

<!-- error -->
```python
groceries = ["milk", "eggs", "bread"]
print(groceries[3])
```

```text
    print(groceries[3])
          ~~~~~~~~~^^^
IndexError: list index out of range
```

The list has 3 items, so the indexes are 0, 1 and 2. There is no index 3. To get the last item safely, use `groceries[-1]` or `groceries[len(groceries) - 1]`.

### Removing something that is not there

<!-- error -->
```python
groceries = ["milk", "eggs", "bread"]
groceries.remove("butter")
```

```text
    groceries.remove("butter")
    ~~~~~~~~~~~~~~~~^^^^^^^^^^
ValueError: list.remove(x): x not in list
```

`remove` only works if the item exists. Check first:

```python
groceries = ["milk", "eggs", "bread"]

if "butter" in groceries:
    groceries.remove("butter")
else:
    print("butter is not on the list")
```

Output:

```text
butter is not on the list
```

### Forgetting the quotes

<!-- error -->
```python
groceries = ["milk", eggs, "bread"]
```

```text
    groceries = ["milk", eggs, "bread"]
                         ^^^^
NameError: name 'eggs' is not defined
```

Without quotes, Python thinks `eggs` is the name of a variable, and there is no variable with that name. Texts always need quotes: `"eggs"`.

### Printing the result of `.sort()`

Lists also have a method `.sort()`, which puts the list itself in order. But it changes the list and returns **nothing**:

```python
numbers = [3, 1, 2]
print(numbers.sort())
print(numbers)
```

Output:

```text
None
[1, 2, 3]
```

`None` is Python's way of saying "nothing". If you want a sorted copy to print or store, use `sorted(numbers)`.

## Exercises

### Predict the output

#### Exercise 1: Indexes

```python
movies = ["Up", "Coco", "Soul", "Luca", "Elio"]
print(movies[1])
print(movies[-1])
print(movies[1:3])
print(len(movies))
```

<details>
<summary>Show answer</summary>

```text
Coco
Elio
['Coco', 'Soul']
5
```

Index 1 is the **second** item. `-1` is the last. `[1:3]` includes index 1 and 2, but not 3.

</details>

#### Exercise 2: Changing the list

```python
plants = ["fern", "cactus"]
plants.append("basil")
plants[0] = "orchid"
removed = plants.pop()
print(plants)
print(removed)
```

<details>
<summary>Show answer</summary>

```text
['orchid', 'cactus']
basil
```

Step by step: `["fern", "cactus"]`, then `["fern", "cactus", "basil"]`, then `["orchid", "cactus", "basil"]`. Finally `pop()` removes the last item (`"basil"`) and stores it in `removed`.

</details>

#### Exercise 3: Numbers

```python
prices = [10, 4, 25, 1]
print(sorted(prices))
print(max(prices) - min(prices))
print(prices[0] + prices[-1])
```

<details>
<summary>Show answer</summary>

```text
[1, 4, 10, 25]
24
11
```

`max` is 25 and `min` is 1, so the difference is 24. The first item is 10 and the last is 1, so the sum is 11. `sorted` does not change `prices`, so `prices[0]` is still 10.

</details>

### Fix the bug

#### Exercise 4: The last guest

This program should print the last guest, but it crashes. Fix it in two different ways.

<!-- no-verify -->
```python
guests = ["Ana", "Bia", "Caio"]
print(guests[3])
```

<details>
<summary>Show answer</summary>

```python
guests = ["Ana", "Bia", "Caio"]
print(guests[2])
print(guests[-1])
```

Output:

```text
Caio
Caio
```

Three items means indexes 0, 1 and 2. `guests[-1]` is the better fix: it keeps working even if more guests are added later.

</details>

#### Exercise 5: Sorted list

This program should print the scores from lowest to highest, but it prints `None`. Fix it.

<!-- no-verify -->
```python
scores = [8, 3, 10, 6]
print(scores.sort())
```

<details>
<summary>Show answer</summary>

```python
scores = [8, 3, 10, 6]
print(sorted(scores))
```

Output:

```text
[3, 6, 8, 10]
```

`.sort()` sorts the list but returns nothing (`None`). `sorted()` returns a new, sorted list that you can print.

</details>

### Write it

#### Exercise 6: To-do list

1. Create an empty list called `todo`.
2. Add three tasks to it with `append`.
3. Print how many tasks there are, using an f-string: `You have 3 tasks.`
4. Print the first task.

<details>
<summary>Show answer</summary>

```python
todo = []
todo.append("buy coffee")
todo.append("water the plants")
todo.append("call the bank")

print(f"You have {len(todo)} tasks.")
print(todo[0])
```

Output:

```text
You have 3 tasks.
buy coffee
```

</details>

#### Exercise 7: Avoid duplicates

Given `cart = ["apple", "banana"]` and `new_item = "apple"`, add `new_item` to the cart **only** if it is not already there. Otherwise print `"apple is already in the cart"`. Print the cart at the end.

<details>
<summary>Show answer</summary>

```python
cart = ["apple", "banana"]
new_item = "apple"

if new_item not in cart:
    cart.append(new_item)
else:
    print(f"{new_item} is already in the cart")

print(cart)
```

Output:

```text
apple is already in the cart
['apple', 'banana']
```

</details>

#### Exercise 8: Week summary

Given the daily step counts `steps = [4200, 8000, 6500, 10200, 3000, 12000, 7500]`, print:

- the total number of steps in the week
- the best day (the maximum)
- the average per day

<details>
<summary>Show answer</summary>

```python
steps = [4200, 8000, 6500, 10200, 3000, 12000, 7500]

total = sum(steps)
print(f"Total: {total}")
print(f"Best day: {max(steps)}")
print(f"Average: {total / len(steps)}")
```

Output:

```text
Total: 51400
Best day: 12000
Average: 7342.857142857143
```

The average has many decimals. You can round it with `round(total / len(steps))`, which gives `7343`.

</details>

## Review

#### Review 1: Text is also a sequence

What does this print? (Hint: texts have indexes too.)

```python
word = "Python"
print(word[0])
print(word[-1])
print(len(word))
```

<details>
<summary>Show answer</summary>

```text
P
n
6
```

Texts work like lists of characters: index 0 is the first letter, `-1` the last one.

</details>

#### Review 2: Decide with a list

Create a list `vip = ["Ana", "Leo"]` and a variable `name`. Print `"Welcome, <name>! Your table is ready."` if the name is in the VIP list, otherwise `"Welcome, <name>! Please wait to be seated."`.

<details>
<summary>Show answer</summary>

```python
vip = ["Ana", "Leo"]
name = "Leo"

if name in vip:
    print(f"Welcome, {name}! Your table is ready.")
else:
    print(f"Welcome, {name}! Please wait to be seated.")
```

Output:

```text
Welcome, Leo! Your table is ready.
```

</details>

## Recap

- A list is written with `[ ]` and keeps items in order. `len()` tells how many.
- Indexes start at **0**. `-1` is the last item. Asking for an index that does not exist gives `IndexError`.
- `append` adds to the end, `remove` deletes by value, `pop` deletes by position and gives the item back.
- `in` checks if an item is in the list. Slices like `[1:3]` give a piece of the list (the stop is not included).
- `sum`, `min`, `max` and `sorted` work on lists. `sorted` gives a new list; `.sort()` changes the list and returns `None`.

**Next:** [loops.md](loops.md)
