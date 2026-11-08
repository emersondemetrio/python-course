# Comprehensions

> **In one sentence:** a comprehension builds a new list (or set, or dictionary) from another one in a single line, replacing a `for` loop with `.append()`.

## Why it matters

You have written this shape of code many times: create an empty list, loop over something, and `.append()` a result. It is so common that Python has a shorter way to write it. You will see comprehensions everywhere in other people's code, on Stack Overflow, in documentation and in code written by AI tools, so you need to be able to read them. Writing them is a bonus.

Important: a comprehension does **nothing new**. Anything a comprehension does, a `for` loop can do. It is only a shorter way to write a pattern you already know.

## Analogy

Imagine you ask a friend for help in the kitchen. The long way: "Take an empty bowl. Now pick up the first tomato. Cut it. Put it in the bowl. Now pick up the second tomato. Cut it. Put it in the bowl..."

The short way: "A bowl of every tomato, cut." Same result, one sentence. A comprehension is that one sentence.

## The idea, step by step

### From a loop to a comprehension

Here is the loop you already know. It makes a new list with every price doubled:

```python
prices = [10, 25, 4]
doubled = []
for price in prices:
    doubled.append(price * 2)
print(doubled)
```

Output:

```text
[20, 50, 8]
```

And here is the same thing as a list comprehension:

```python
prices = [10, 25, 4]
doubled = [price * 2 for price in prices]
print(doubled)
```

Output:

```text
[20, 50, 8]
```

Look at how the pieces move:

<!-- no-verify -->
```python
doubled = []                    # 1. the empty list...
for price in prices:            # 2. ...the loop...
    doubled.append(price * 2)   # 3. ...and what gets added

doubled = [price * 2 for price in prices]
#          ^ 3.       ^ 2.               the [] is 1.
```

Read a comprehension out loud from the middle: "**for** each price **in** prices, take **price times 2**, and put them all in a list."

### More examples

Any expression can go in front, as long as it uses the loop variable:

```python
names = ["ana", "bruno", "carla"]
print([name.upper() for name in names])
print([len(name) for name in names])
print([f"Hello, {name}!" for name in names])
```

Output:

```text
['ANA', 'BRUNO', 'CARLA']
[3, 5, 5]
['Hello, ana!', 'Hello, bruno!', 'Hello, carla!']
```

It also works with `range()`:

```python
squares = [n * n for n in range(1, 6)]
print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

### Filtering with `if`

You can add an `if` at the **end** to keep only some items. Here is the loop version:

```python
temps = [18, 25, 31, 22, 29]
hot = []
for t in temps:
    if t > 24:
        hot.append(t)
print(hot)
```

Output:

```text
[25, 31, 29]
```

And the comprehension:

```python
temps = [18, 25, 31, 22, 29]
hot = [t for t in temps if t > 24]
print(hot)
```

Output:

```text
[25, 31, 29]
```

Read it: "for each t in temps, **if** t is greater than 24, keep t."

You can transform and filter at the same time:

```python
products = [
    {"name": "Notebook", "price": 12.5},
    {"name": "Pencil", "price": 1.5},
    {"name": "Mug", "price": 9.0},
]
cheap_names = [p["name"] for p in products if p["price"] < 10]
print(cheap_names)
```

Output:

```text
['Pencil', 'Mug']
```

This is a very common real use: pull one field out of a list of records, keeping only some of them.

### Set and dictionary comprehensions (briefly)

The same idea works with curly braces. With single values, you get a **set** (no duplicates):

```python
words = ["Apple", "apple", "APPLE", "pear"]
unique = {w.lower() for w in words}
print(sorted(unique))
```

Output:

```text
['apple', 'pear']
```

With `key: value`, you get a **dictionary**:

```python
names = ["ana", "bruno", "carla"]
lengths = {name: len(name) for name in names}
print(lengths)
```

Output:

```text
{'ana': 3, 'bruno': 5, 'carla': 5}
```

A useful one: apply a change to every price in a menu.

```python
menu = {"espresso": 5.0, "latte": 8.0}
new_menu = {drink: price * 1.1 for drink, price in menu.items()}
print(new_menu)
```

Output:

```text
{'espresso': 5.5, 'latte': 8.8}
```

(If you see something like `8.800000000000001` in other examples, that is normal: computers store decimal numbers with tiny rounding errors. Use `round(price * 1.1, 2)` when it matters.)

### When NOT to use a comprehension

Comprehensions are great when they are short and easy to read. Use a normal `for` loop when:

- **The line gets long or confusing.** If you have to read it three times, write the loop.
- **You need more than one step per item**, like calculating something, checking it, and then printing.
- **You only want to do something, not build a list.** Printing is the classic example:

<!-- no-verify -->
```python
# Do not do this: it builds a useless list of None values just to print.
[print(name) for name in names]

# Do this:
for name in names:
    print(name)
```

A good rule: a comprehension should **build** something. If you are not going to use the new list, use a loop.

## Common mistakes

### Putting the `if` in the wrong place

<!-- error -->
```python
temps = [18, 25, 31]
hot = [if t > 24 t for t in temps]
```

```text
    hot = [if t > 24 t for t in temps]
           ^^
SyntaxError: invalid syntax
```

The filter `if` goes at the **end**: `[t for t in temps if t > 24]`.

### Using a variable that is not the loop variable

<!-- error -->
```python
prices = [10, 25, 4]
doubled = [p * 2 for price in prices]
```

```text
Traceback (most recent call last):
NameError: name 'p' is not defined
```

The loop variable is called `price`, but the front part uses `p`. They must be the same name: `[price * 2 for price in prices]`.

### Forgetting `.items()` in a dictionary comprehension

<!-- error -->
```python
menu = {"espresso": 5.0, "latte": 8.0}
cheap = {d: p for d, p in menu if p < 6}
```

```text
Traceback (most recent call last):
ValueError: too many values to unpack (expected 2)
```

Same mistake as in a normal loop: looping over a dictionary gives only keys. Use `menu.items()`.

## Exercises

### Predict the output

#### Exercise 1: Read the comprehension

<!-- no-verify -->
```python
numbers = [1, 2, 3, 4, 5, 6]
print([n * 10 for n in numbers])
print([n for n in numbers if n % 2 == 0])
print([n + 1 for n in numbers if n > 4])
```

<details>
<summary>Hint</summary>

`n % 2 == 0` is `True` when `n` is even (the remainder of dividing by 2 is zero).

</details>

<details>
<summary>Show answer</summary>

```python
numbers = [1, 2, 3, 4, 5, 6]
print([n * 10 for n in numbers])
print([n for n in numbers if n % 2 == 0])
print([n + 1 for n in numbers if n > 4])
```

Output:

```text
[10, 20, 30, 40, 50, 60]
[2, 4, 6]
[6, 7]
```

In the last one, the filter runs first (only 5 and 6 pass), then each one gets `+ 1`.

</details>

#### Exercise 2: Dictionary comprehension

<!-- no-verify -->
```python
stock = {"apples": 0, "pears": 4, "plums": 0, "figs": 2}
available = {fruit: amount for fruit, amount in stock.items() if amount > 0}
print(available)
```

<details>
<summary>Show answer</summary>

```python
stock = {"apples": 0, "pears": 4, "plums": 0, "figs": 2}
available = {fruit: amount for fruit, amount in stock.items() if amount > 0}
print(available)
```

Output:

```text
{'pears': 4, 'figs': 2}
```

</details>

### Fix the bug

#### Exercise 3: Wrong order

This should give `['BREAD', 'MILK']` (only items with 5 letters or fewer, in capitals), but it is a syntax error. Fix it.

<!-- no-verify -->
```python
items = ["bread", "chocolate", "milk"]
short = [for item in items item.upper() if len(item) <= 5]
print(short)
```

<details>
<summary>Show answer</summary>

```python
items = ["bread", "chocolate", "milk"]
short = [item.upper() for item in items if len(item) <= 5]
print(short)
```

Output:

```text
['BREAD', 'MILK']
```

The order is always: what to keep, then `for`, then the optional `if`.

</details>

### Write it

#### Exercise 4: Loop to comprehension

Rewrite this loop as a list comprehension. The output must be the same.

<!-- no-verify -->
```python
cities = ["lisbon", "porto", "faro"]
titles = []
for city in cities:
    titles.append(city.title())
print(titles)
```

<details>
<summary>Show answer</summary>

```python
cities = ["lisbon", "porto", "faro"]
titles = [city.title() for city in cities]
print(titles)
```

Output:

```text
['Lisbon', 'Porto', 'Faro']
```

</details>

#### Exercise 5: Comprehension to loop

Now the opposite: rewrite this comprehension as a normal `for` loop with `.append()`.

<!-- no-verify -->
```python
words = ["sun", "moonlight", "sky", "rainbow"]
long_words = [w for w in words if len(w) > 3]
print(long_words)
```

<details>
<summary>Show answer</summary>

```python
words = ["sun", "moonlight", "sky", "rainbow"]
long_words = []
for w in words:
    if len(w) > 3:
        long_words.append(w)
print(long_words)
```

Output:

```text
['moonlight', 'rainbow']
```

Being able to go both ways is the real skill. If a comprehension ever confuses you, rewrite it as a loop.

</details>

#### Exercise 6: Titles of unread books

Using one list comprehension, create a list with only the titles of the books that were not read yet.

<!-- no-verify -->
```python
books = [
    {"title": "Dune", "read": True},
    {"title": "Emma", "read": False},
    {"title": "Ubik", "read": False},
]
```

<details>
<summary>Hint</summary>

`not book["read"]` is `True` when the book was not read.

</details>

<details>
<summary>Show answer</summary>

```python
books = [
    {"title": "Dune", "read": True},
    {"title": "Emma", "read": False},
    {"title": "Ubik", "read": False},
]
to_read = [book["title"] for book in books if not book["read"]]
print(to_read)
```

Output:

```text
['Emma', 'Ubik']
```

</details>

## Review

#### Review 1: JSON (previous file)

Which function would you use in each case: `json.dump`, `json.dumps`, `json.load` or `json.loads`?

1. Read a `.json` file into a list.
2. Turn a dictionary into a string to print it.
3. Save a list into a `.json` file.
4. Turn the text `'{"a": 1}'` into a dictionary.

<details>
<summary>Show answer</summary>

1. `json.load(file)`
2. `json.dumps(data)`
3. `json.dump(data, file)`
4. `json.loads(text)`

The **s** is for **string**. No **s** means a file.

</details>

#### Review 2: Sets (tuples and sets)

What does this print?

<!-- no-verify -->
```python
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(sorted(a & b))
print(sorted(a - b))
print(len(a | b))
```

<details>
<summary>Show answer</summary>

```python
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(sorted(a & b))
print(sorted(a - b))
print(len(a | b))
```

Output:

```text
[3, 4]
[1, 2]
5
```

</details>

## Recap

- `[expression for item in items]` builds a new list. It is a short version of a `for` loop with `.append()`.
- Add a filter at the end: `[x for x in items if condition]`.
- Curly braces give a set `{x for x in items}` or a dictionary `{k: v for k, v in d.items()}`.
- Read it from the middle: "for each item in items, keep this".
- If it is long, confusing, or only prints things, use a normal loop.

**Next:** [Module 07: Organizing code](../module-07-organizing-code/README.md)
