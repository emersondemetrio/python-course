# Tuples and sets

> **In one sentence:** a **tuple** is a small group of values that never changes, and a **set** is a bag of values with no duplicates and no order.

## Why it matters

Lists and dictionaries cover most of what you need. Tuples and sets cover two special jobs that come up all the time. Tuples are for small, fixed groups, like a date (day, month) or a point on a map (latitude, longitude). Sets are for answering questions like "which items are unique?", "what do these two groups have in common?" and "is this thing in the group?". You have already used tuples without knowing it: `enumerate()` and `.items()` give you tuples.

## Analogy

A **tuple** is like a printed label on a jar: "Strawberry jam, 2024". Once it is printed, you do not edit it. If something changes, you print a new label.

A **set** is like a guest list at the door of a party. Each name is either on the list or not. Writing a name twice does not invite the person twice. And the list has no "first" or "second" guest; it only answers "is this person invited?".

## The idea, step by step

### Creating a tuple

A tuple uses parentheses `()` instead of square brackets. You read items by position, exactly like a list.

```python
birthday = (14, "March")
print(birthday)
print(birthday[0])
print(birthday[1])
print(len(birthday))
```

Output:

```text
(14, 'March')
14
March
2
```

### Tuples cannot change

This is the big difference from a list. Once a tuple exists, you cannot change, add or remove items. Python calls this **immutable** (it cannot mutate, it cannot change).

<!-- error -->
```python
birthday = (14, "March")
birthday[0] = 15
```

```text
Traceback (most recent call last):
TypeError: 'tuple' object does not support item assignment
```

Why would you want something that cannot change? Because it protects you. A date, a pair of coordinates or the size of a sheet of paper should not change by accident in the middle of your program. If you need a different value, create a new tuple:

```python
birthday = (14, "March")
birthday = (15, "March")
print(birthday)
```

Output:

```text
(15, 'March')
```

This works because we did not change the old tuple: we made the variable `birthday` point to a brand new one.

### Unpacking

You can split a tuple into separate variables in one line. This is called **unpacking**.

```python
point = (38.7, -9.1)
latitude, longitude = point
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
```

Output:

```text
Latitude: 38.7
Longitude: -9.1
```

The number of variables on the left must match the number of items in the tuple. You already did this in loops:

```python
for number, fruit in enumerate(["apple", "pear"]):
    print(number, fruit)
```

Output:

```text
0 apple
1 pear
```

`enumerate()` gives you tuples like `(0, "apple")`, and the `for` unpacks each one into `number` and `fruit`.

A function can also return a tuple, which is a neat way to give back two values at once:

```python
def min_and_max(numbers):
    return min(numbers), max(numbers)

lowest, highest = min_and_max([12, 3, 27, 8])
print(lowest, highest)
```

Output:

```text
3 27
```

`return min(numbers), max(numbers)` creates a tuple. The parentheses are optional when you write values separated by commas.

### A tuple with one item needs a comma

This one surprises everyone. Parentheses alone do not make a tuple; the **comma** does.

```python
not_a_tuple = ("tea")
a_tuple = ("tea",)
print(type(not_a_tuple))
print(type(a_tuple))
```

Output:

```text
<class 'str'>
<class 'tuple'>
```

`("tea")` is just the string `"tea"` with parentheses around it, like `(2 + 3)` in math. Add a comma to make a one-item tuple.

### Creating a set

A set uses curly braces `{}`, like a dictionary, but with single values instead of `key: value` pairs.

```python
numbers = {3, 1, 2, 3, 1}
print(numbers)
print(len(numbers))
```

Output:

```text
{1, 2, 3}
3
```

The duplicates disappeared. A set keeps each value only once.

Sets have **no order**. When you print a set of words, Python may show them in a different order each time you run the program. To get a stable order, use `sorted()`, which gives you a sorted list:

```python
fruits = {"pear", "apple", "banana"}
print(sorted(fruits))
```

Output:

```text
['apple', 'banana', 'pear']
```

Because there is no order, you also cannot use positions: `fruits[0]` is an error.

### Removing duplicates from a list

This is the most common use of a set. Turn the list into a set with `set()`:

```python
visitors = ["Ana", "Bruno", "Ana", "Carla", "Bruno", "Ana"]
unique = set(visitors)
print(len(visitors))
print(len(unique))
print(sorted(unique))
```

Output:

```text
6
3
['Ana', 'Bruno', 'Carla']
```

### Adding to a set and checking with `in`

```python
tags = {"python", "beginner"}
tags.add("tutorial")
tags.add("python")
print(len(tags))
print("python" in tags)
print("java" in tags)
```

Output:

```text
3
True
False
```

Adding `"python"` a second time did nothing, because it was already there.

### Comparing two sets

Sets can answer questions about two groups at once. Imagine two friends and the herbs they grow:

```python
ana = {"basil", "mint", "rosemary"}
bruno = {"mint", "parsley", "basil"}

print(sorted(ana & bruno))
print(sorted(ana | bruno))
print(sorted(ana - bruno))
print(sorted(bruno - ana))
```

Output:

```text
['basil', 'mint']
['basil', 'mint', 'parsley', 'rosemary']
['rosemary']
['parsley']
```

- `&` (**intersection**): what both have.
- `|` (**union**): everything, from both, without duplicates.
- `-` (**difference**): what the first has and the second does not.

### `{}` is a dictionary, not a set

Because both use curly braces, empty braces are a dictionary. To create an empty set, use `set()`:

```python
empty_dict = {}
empty_set = set()
print(type(empty_dict))
print(type(empty_set))
```

Output:

```text
<class 'dict'>
<class 'set'>
```

### Which one should I use?

| I need... | Use |
|---|---|
| Many items, in order, that may change | list `[]` |
| A small fixed group of values, like a date | tuple `()` |
| Unique items, or to compare groups | set `{}` (empty: `set()`) |
| To find values by a name | dictionary `{key: value}` |

## Common mistakes

### Trying to change a tuple

<!-- error -->
```python
size = (20, 30)
size.append(40)
```

```text
Traceback (most recent call last):
AttributeError: 'tuple' object has no attribute 'append'
```

Tuples have no `.append()` because they cannot change. If you need to add items, you wanted a list: `size = [20, 30]`.

### Unpacking the wrong number of values

<!-- error -->
```python
date = (14, "March", 2024)
day, month = date
```

```text
Traceback (most recent call last):
ValueError: too many values to unpack (expected 2)
```

The tuple has three values, but only two variables are waiting. Use three: `day, month, year = date`.

### Using a position in a set

<!-- error -->
```python
colors = {"red", "blue"}
print(colors[0])
```

```text
Traceback (most recent call last):
TypeError: 'set' object is not subscriptable
```

"Not subscriptable" means "you cannot use square brackets on it". Sets have no positions. If you need the items in order, use `sorted(colors)`, which returns a list.

### Expecting `{}` to be an empty set

<!-- error -->
```python
seen = {}
seen.add("tea")
```

```text
Traceback (most recent call last):
AttributeError: 'dict' object has no attribute 'add'
```

`{}` is an empty dictionary. Write `seen = set()`.

## Exercises

### Predict the output

#### Exercise 1: Tuple basics

<!-- no-verify -->
```python
recipe = ("Soup", 30, "easy")
name, minutes, level = recipe
print(name)
print(minutes * 2)
print(len(recipe))
```

<details>
<summary>Show answer</summary>

```python
recipe = ("Soup", 30, "easy")
name, minutes, level = recipe
print(name)
print(minutes * 2)
print(len(recipe))
```

Output:

```text
Soup
60
3
```

</details>

#### Exercise 2: How many unique?

<!-- no-verify -->
```python
answers = ["yes", "no", "yes", "yes", "maybe", "no"]
print(len(answers))
print(len(set(answers)))
```

<details>
<summary>Show answer</summary>

```python
answers = ["yes", "no", "yes", "yes", "maybe", "no"]
print(len(answers))
print(len(set(answers)))
```

Output:

```text
6
3
```

</details>

#### Exercise 3: Comparing groups

<!-- no-verify -->
```python
monday = {"Ana", "Bruno", "Carla"}
tuesday = {"Carla", "Davi"}
print(sorted(monday & tuesday))
print(sorted(monday | tuesday))
print(sorted(tuesday - monday))
```

<details>
<summary>Show answer</summary>

```python
monday = {"Ana", "Bruno", "Carla"}
tuesday = {"Carla", "Davi"}
print(sorted(monday & tuesday))
print(sorted(monday | tuesday))
print(sorted(tuesday - monday))
```

Output:

```text
['Carla']
['Ana', 'Bruno', 'Carla', 'Davi']
['Davi']
```

</details>

### Fix the bug

#### Exercise 4: The one-item tuple

This should print `<class 'tuple'>` but prints `<class 'str'>`. Fix it.

<!-- no-verify -->
```python
colors = ("green")
print(type(colors))
```

<details>
<summary>Show answer</summary>

```python
colors = ("green",)
print(type(colors))
```

Output:

```text
<class 'tuple'>
```

The comma is what makes a tuple.

</details>

#### Exercise 5: Collecting unique cities

This program should collect each city only once, but it crashes. Fix it.

<!-- no-verify -->
```python
cities = {}
for city in ["Porto", "Lisbon", "Porto"]:
    cities.add(city)
print(sorted(cities))
```

<details>
<summary>Show answer</summary>

```python
cities = set()
for city in ["Porto", "Lisbon", "Porto"]:
    cities.add(city)
print(sorted(cities))
```

Output:

```text
['Lisbon', 'Porto']
```

</details>

### Write it

#### Exercise 6: Unique words

Given the sentence below, print how many words it has and how many **different** words it has. Use `.split()` to turn the sentence into a list of words.

<!-- no-verify -->
```python
sentence = "the cat saw the dog and the dog saw the cat"
```

<details>
<summary>Show answer</summary>

```python
sentence = "the cat saw the dog and the dog saw the cat"
words = sentence.split()
print(len(words))
print(len(set(words)))
```

Output:

```text
11
5
```

</details>

#### Exercise 7: A function that returns two values

Write a function `split_name(full_name)` that returns the first name and the last name as a tuple. Use `.split()`. Then unpack the result into two variables and print them.

<details>
<summary>Hint</summary>

`"Ana Souza".split()` gives `["Ana", "Souza"]`. Return `parts[0], parts[-1]`.

</details>

<details>
<summary>Show answer</summary>

```python
def split_name(full_name):
    parts = full_name.split()
    return parts[0], parts[-1]

first, last = split_name("Ana Souza")
print(first)
print(last)
```

Output:

```text
Ana
Souza
```

</details>

#### Exercise 8: What is missing from the shopping?

You planned to buy the items in `plan`, and the items in `cart` are what you actually picked up. Print, in alphabetical order, what you forgot.

<!-- no-verify -->
```python
plan = {"milk", "eggs", "bread", "coffee"}
cart = {"eggs", "coffee", "chocolate"}
```

<details>
<summary>Show answer</summary>

```python
plan = {"milk", "eggs", "bread", "coffee"}
cart = {"eggs", "coffee", "chocolate"}
print(sorted(plan - cart))
```

Output:

```text
['bread', 'milk']
```

</details>

## Review

#### Review 1: Dictionaries (previous file)

What does this print?

<!-- no-verify -->
```python
ages = {"Ana": 30, "Bruno": 25}
ages["Ana"] = ages["Ana"] + 1
print(ages.get("Bruno", 0) + ages.get("Carla", 0))
print(ages["Ana"])
```

<details>
<summary>Show answer</summary>

```python
ages = {"Ana": 30, "Bruno": 25}
ages["Ana"] = ages["Ana"] + 1
print(ages.get("Bruno", 0) + ages.get("Carla", 0))
print(ages["Ana"])
```

Output:

```text
25
31
```

</details>

#### Review 2: Functions with `return` (module 03)

What is the difference between these two functions? What does the program print?

<!-- no-verify -->
```python
def double_print(n):
    print(n * 2)

def double_return(n):
    return n * 2

a = double_print(5)
b = double_return(5)
print(a)
print(b)
```

<details>
<summary>Show answer</summary>

```python
def double_print(n):
    print(n * 2)

def double_return(n):
    return n * 2

a = double_print(5)
b = double_return(5)
print(a)
print(b)
```

Output:

```text
10
None
10
```

`double_print` shows 10 on the screen but gives nothing back, so `a` is `None`. `double_return` shows nothing, but gives back 10, which is stored in `b`.

</details>

## Recap

- A tuple `(a, b)` is like a list that cannot change. Good for small fixed groups, like a date.
- Unpacking: `day, month = (14, "March")`. The number of variables must match.
- A one-item tuple needs a comma: `("tea",)`.
- A set `{a, b}` has no duplicates and no order. Use `set(my_list)` to remove duplicates and `sorted()` to print in order.
- `&` common items, `|` all items, `-` items only in the first. An empty set is `set()`, because `{}` is a dictionary.

**Next:** [JSON](json.md)
