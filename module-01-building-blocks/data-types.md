# Data types and variables

> **In one sentence:** a variable is a name that points to a value, and every value has a type that decides what you can do with it.

## Why it matters

Almost every line of a program either creates a value, gives it a name, or uses it. If you know what a name holds and what type it is, you can predict what your code will do. Most beginner bugs come from a name holding something different from what you expected.

## Analogy

Think of a **label sticker** on a jar in your kitchen. The jar holds something (sugar, rice, coffee). The sticker is just a name so you can find it later. You can peel the sticker off and put it on a different jar: the name stays the same, but now it points to something else.

The **type** is what kind of thing is in the jar. You can stir sugar into coffee, but you cannot pour rice into the coffee machine. In the same way, Python lets you add two numbers, but complains if you try to add a number to a piece of text.

## The idea, step by step

### Creating a variable

You create a variable with the `=` sign. This is called **assignment**. Read it from right to left: "take the value on the right and give it the name on the left".

```python
cups = 3
print(cups)
```

Output:

```text
3
```

The `=` in Python does **not** mean "is equal to" like in math. It means "store this value under this name". (Comparing values uses `==`, which you will see in module 02.)

### Using variables in calculations

Once a value has a name, you can use the name anywhere you would use the value.

```python
price = 12
quantity = 3
total = price * quantity
print(total)
```

Output:

```text
36
```

Python first calculates `price * quantity`, which is `36`, and then stores that result under the name `total`.

### Reassignment: the latest value wins

You can give a name a new value at any time. Python runs your file **from top to bottom**, one line after the other, and a name always holds the **most recent** value it received.

```python
a = 2
a = 0
b = 5
c = a + b
print(c)
```

Output:

```text
5
```

When Python reaches `c = a + b`, `a` is already `0`, so `c` is `0 + 5`.

A variable can even use its own old value to calculate a new one:

```python
steps = 10
steps = steps + 5
print(steps)
```

Output:

```text
15
```

Read the second line from the right: "take the current `steps` (10), add 5, and store the result back in `steps`".

### Names: rules and good habits

- Names can contain letters, digits and `_`, but cannot start with a digit: `total2` is fine, `2total` is not.
- No spaces: use `_` instead, as in `first_name`.
- **Upper and lower case matter.** `Name` and `name` are two different variables.

```python
name = "Ana"
Name = "Bia"
print(name)
print(Name)
```

Output:

```text
Ana
Bia
```

A good name says what the value means: `price` is better than `p`, and `total_cups` is better than `x`.

### The basic types

| Type | What it is | Examples |
|---|---|---|
| `int` | whole number (integer) | `10`, `0`, `-3` |
| `float` | number with a decimal point | `3.14`, `0.5`, `10.0` |
| `str` | text (string), always in quotes | `"hello"`, `'10'`, `""` |
| `bool` | true or false (boolean) | `True`, `False` |

You can ask Python for the type of any value with `type()`:

```python
print(type(10))
print(type(10.0))
print(type("10"))
print(type(True))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

Look closely: `10`, `10.0` and `"10"` look similar to a human, but for Python they are three different types. The quotes are what make `"10"` a piece of text.

`True` and `False` are written with a capital first letter and without quotes.

### Arithmetic

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | add | `7 + 2` | `9` |
| `-` | subtract | `7 - 2` | `5` |
| `*` | multiply | `7 * 2` | `14` |
| `/` | divide | `7 / 2` | `3.5` |

```python
print(7 + 2)
print(7 * 2)
print(7 / 2)
print(6 / 2)
```

Output:

```text
9
14
3.5
3.0
```

Notice that `/` always gives a `float`, even when the division is exact: `6 / 2` is `3.0`, not `3`.

### Type hints do not force a type

Sometimes you will see a variable written like this:

```python
a: int = 10
print(a)
```

Output:

```text
10
```

The `: int` part is a **type hint**: a note for people (and for your editor) saying "this should be a whole number". Python itself does **not** enforce it. This still runs:

```python
a: int = 10
a = "ten"
print(a)
```

Output:

```text
ten
```

Type hints are useful as documentation, but they are not a lock.

### Converting between types

You can turn a value into another type with `int()`, `float()` and `str()`:

```python
print(int("42") + 1)
print(float("2.5") * 2)
print(str(7) + "7")
```

Output:

```text
43
5.0
77
```

- `int("42")` turns the text `"42"` into the number `42`, so adding 1 gives `43`.
- `str(7)` turns the number `7` into the text `"7"`, so `+` joins the texts and gives `"77"`.

`int()` on a float cuts off the decimal part (it does not round):

```python
print(int(3.9))
```

Output:

```text
3
```

## Common mistakes

### Using a variable before creating it

Python reads from top to bottom. If you use a name before giving it a value, it does not know what you mean.

<!-- error -->
```python
print(total)
total = 10
```

```text
NameError: name 'total' is not defined
```

**Fix:** create the variable first, then use it.

```python
total = 10
print(total)
```

```text
10
```

### Wrong upper or lower case

<!-- error -->
```python
city = "Lisbon"
print(City)
```

```text
NameError: name 'City' is not defined. Did you mean: 'city'?
```

`City` and `city` are different names. Python even suggests the one you probably meant. **Fix:** use exactly the same spelling: `print(city)`.

### Turning text that is not a number into a number

<!-- error -->
```python
age = int("thirty")
```

```text
ValueError: invalid literal for int() with base 10: 'thirty'
```

`int()` only works on text that looks like a whole number, such as `"30"`. A **ValueError** means "right type, wrong content".

### Forgetting that quotes make text

```python
a = "5"
b = "3"
print(a + b)
```

```text
53
```

This does not crash, which makes it sneaky. Both values are text, so `+` glues them together instead of adding. **Fix:** remove the quotes (`a = 5`), or convert with `int(a) + int(b)`.

## Exercises

### Predict the output

Read the code, write down what it prints, and only then open the answer.

#### Exercise 1: Last one wins

```python
coffee = 1
coffee = 2
coffee = 3
print(coffee)
```

<details>
<summary>Show answer</summary>

```text
3
```

Each line replaces the previous value. When `print` runs, `coffee` holds `3`.

</details>

#### Exercise 2: Order matters

```python
x = 4
y = x + 1
x = 10
print(y)
```

<details>
<summary>Show answer</summary>

```text
5
```

`y` was calculated when `x` was still `4`, so `y` is `5`. Changing `x` later does **not** go back and change `y`.

</details>

#### Exercise 3: What type is it?

```python
print(type(3))
print(type("3"))
print(type(3.0))
print(type(False))
```

<details>
<summary>Show answer</summary>

```text
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
```

The quotes make `"3"` a `str`. The decimal point makes `3.0` a `float`.

</details>

#### Exercise 4: Division

```python
print(10 / 2)
print(10 / 4)
```

<details>
<summary>Show answer</summary>

```text
5.0
2.5
```

`/` always produces a `float`, so even `10 / 2` shows `5.0`.

</details>

### Fix the bug

#### Exercise 5: The missing variable

This program should print `25`, but it crashes. Fix it.

<!-- no-verify -->
```python
width = 5
area = width * height
height = 5
print(area)
```

<details>
<summary>Hint</summary>

Python runs line by line from the top. Which line uses `height`, and when is `height` created?

</details>

<details>
<summary>Show answer</summary>

```python
width = 5
height = 5
area = width * height
print(area)
```

```text
25
```

`height` must exist before the line that uses it.

</details>

#### Exercise 6: Text that should be a number

This should print `15`, but it prints `105`. Fix it.

<!-- no-verify -->
```python
bags = "10"
extra = "5"
print(bags + extra)
```

<details>
<summary>Show answer</summary>

```python
bags = 10
extra = 5
print(bags + extra)
```

```text
15
```

With quotes, both values were text and `+` joined them. Without quotes they are numbers and `+` adds them. Another valid fix: `print(int(bags) + int(extra))`.

</details>

### Write it

#### Exercise 7: Pizza for everyone

Create a variable `slices_per_pizza` with `8` and a variable `pizzas` with `3`. Calculate the total number of slices in a variable `total_slices` and print it.

<details>
<summary>Show answer</summary>

```python
slices_per_pizza = 8
pizzas = 3
total_slices = slices_per_pizza * pizzas
print(total_slices)
```

```text
24
```

</details>

#### Exercise 8: Saving money

You have `100` saved. Every month you add `25`. Using **one variable** called `savings`, add 25 three times (one line per month) and print the final value.

<details>
<summary>Hint</summary>

Use the pattern `savings = savings + 25`.

</details>

<details>
<summary>Show answer</summary>

```python
savings = 100
savings = savings + 25
savings = savings + 25
savings = savings + 25
print(savings)
```

```text
175
```

</details>

#### Exercise 9: From text to number

The variable `typed = "1990"` holds a year as text. Convert it to a number, calculate how old someone born that year is in 2026, and print the result.

<details>
<summary>Show answer</summary>

```python
typed = "1990"
year = int(typed)
age = 2026 - year
print(age)
```

```text
36
```

</details>

## Recap

- `=` stores a value under a name. Read it from right to left.
- Python runs top to bottom, and a name always holds its most recent value.
- Names are case sensitive: `total` and `Total` are different.
- The four basic types are `int`, `float`, `str` and `bool`. Use `type()` to check.
- Convert with `int()`, `float()` and `str()`. Quotes always mean text.

**Next:** [strings.md](strings.md)
