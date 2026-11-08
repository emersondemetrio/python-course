# Strings: working with text

> **In one sentence:** a string (`str`) is a piece of text in quotes, and you can join strings with `+` or fill values into them with f-strings.

## Why it matters

Almost every program talks to a person: it shows a message, a total, a list, a greeting. All of that is text. Knowing how to build text from variables is one of the skills you will use every single day.

## Analogy

Think of a **form letter** with blanks: "Dear ____, your order of ____ cups will arrive on ____." The letter is the same for everyone; only the blanks change.

- **Concatenation** (`+`) is like cutting pieces of paper and taping them together. It works, but every piece must already be paper (text). You cannot tape a coin to it.
- An **f-string** is the form letter itself: you write the whole sentence and mark the blanks with `{}`. Python fills them in for you, whatever is inside.

## The idea, step by step

### Quotes

A string is text between quotes. Single and double quotes work the same way:

```python
print("Hello")
print('Hello')
```

Output:

```text
Hello
Hello
```

Pick one style and be consistent. Double quotes are handy when the text has an apostrophe: `"It's late"`.

### New lines with `\n`

`\n` inside a string means "start a new line here". It is written with two characters, but it counts as one invisible character.

```python
print("First line\nSecond line")
```

Output:

```text
First line
Second line
```

### Joining strings with `+` (concatenation)

```python
first = "Maria"
last = "Silva"
print(first + " " + last)
```

Output:

```text
Maria Silva
```

`+` does not add spaces for you. The `" "` in the middle is a string with just one space.

### `+` only joins text with text

If you try to join a string with a number, Python stops:

<!-- error -->
```python
cups = 2
print("Cups: " + cups)
```

```text
TypeError: can only concatenate str (not "int") to str
```

Python refuses to guess whether you wanted to add numbers or join text. You have to convert the number to text first with `str()`:

```python
cups = 2
print("Cups: " + str(cups))
```

Output:

```text
Cups: 2
```

### f-strings: filling in the blanks

Put an `f` right before the opening quote, and write any value or variable inside `{}`:

```python
name = "Maria"
cups = 2
print(f"{name} ordered {cups} cups.")
```

Output:

```text
Maria ordered 2 cups.
```

This is called **interpolation**. Notice that you did **not** need `str(cups)`: the f-string converts the value to text for you. That is why f-strings are usually the easier choice.

### Calculations and function calls inside `{}`

The `{}` can hold any expression, not only a variable. Python calculates it first and then puts the result in the text.

```python
price = 4.5
cups = 2
print(f"Total: {price * cups}")
print(f"One plus one is {1 + 1}")
print(f"The word 'coffee' has {len('coffee')} letters")
```

Output:

```text
Total: 9.0
One plus one is 2
The word 'coffee' has 6 letters
```

### What happens without the `f`

If you forget the `f`, the braces are just characters:

```python
name = "Maria"
print("Hello, {name}")
print(f"Hello, {name}")
```

Output:

```text
Hello, {name}
Hello, Maria
```

### `print` with several values, `sep` and `end`

`print` can receive several values separated by commas. It puts a space between them automatically:

```python
print("Total:", 9, "reais")
```

Output:

```text
Total: 9 reais
```

The space comes from a setting called `sep` (separator). You can change it:

```python
print("apple", "banana", "pear", sep=", ")
print("apple", "banana", "pear", sep="\n")
```

Output:

```text
apple, banana, pear
apple
banana
pear
```

`print` also adds a new line at the **end** of everything it prints. You can change that with `end`:

```python
print("Loading", end="...")
print("done")
```

Output:

```text
Loading...done
```

### How long is a string?

`len()` counts the characters, including spaces:

```python
print(len("tea"))
print(len("green tea"))
```

Output:

```text
3
9
```

### Going through each character

A string is a sequence of characters, so a `for` loop can visit them one by one:

```python
for letter in "tea":
    print(letter)
```

Output:

```text
t
e
a
```

You will study loops in depth in module 02.

## Common mistakes

### Joining text and a number with `+`

<!-- error -->
```python
age = 30
print("I am " + age + " years old")
```

```text
TypeError: can only concatenate str (not "int") to str
```

**Fix 1:** convert with `str()`: `print("I am " + str(age) + " years old")`.
**Fix 2 (usually nicer):** use an f-string: `print(f"I am {age} years old")`.

### Forgetting the `f`

```python
city = "Porto"
print("I live in {city}")
```

```text
I live in {city}
```

No error, just the wrong text. **Fix:** `print(f"I live in {city}")`.

### Quotes that do not match

<!-- error -->
```python
print("Hello')
```

```text
SyntaxError: unterminated string literal (detected at line 1)
```

The string opened with `"` but tried to close with `'`. Python keeps looking for the closing `"` until the end of the line. **Fix:** open and close with the same kind of quote.

### Missing spaces when joining

```python
first = "Ana"
last = "Costa"
print(first + last)
```

```text
AnaCosta
```

**Fix:** add the space yourself: `first + " " + last`, or use `f"{first} {last}"`.

## Exercises

### Predict the output

#### Exercise 1: With and without f

```python
food = "soup"
print("I like {food}")
print(f"I like {food}")
```

<details>
<summary>Show answer</summary>

```text
I like {food}
I like soup
```

Only the string with `f` in front fills in the blank.

</details>

#### Exercise 2: Joining text

```python
a = "5"
b = "5"
print(a + b)
print(f"{a}{b}")
```

<details>
<summary>Show answer</summary>

```text
55
55
```

Both are text, so `+` joins them. The f-string puts one right after the other, so the result is the same.

</details>

#### Exercise 3: Separators

```python
print("a", "b", "c")
print("a", "b", "c", sep="-")
print("a", "b", "c", sep="")
```

<details>
<summary>Show answer</summary>

```text
a b c
a-b-c
abc
```

`sep` is what goes **between** the values. An empty `sep` means nothing in between.

</details>

#### Exercise 4: Math inside braces

```python
apples = 3
print(f"{apples} apples")
print(f"{apples * 2} apples")
print(f"{apples} * 2 apples")
```

<details>
<summary>Show answer</summary>

```text
3 apples
6 apples
3 * 2 apples
```

Only what is **inside** `{}` is calculated. In the third line, `* 2` is outside the braces, so it is just text.

</details>

### Fix the bug

#### Exercise 5: The broken receipt

This should print `Total: 18 reais` but crashes. Fix it in two different ways: once with `str()` and once with an f-string.

<!-- no-verify -->
```python
total = 18
print("Total: " + total + " reais")
```

<details>
<summary>Show answer</summary>

```python
total = 18
print("Total: " + str(total) + " reais")
print(f"Total: {total} reais")
```

```text
Total: 18 reais
Total: 18 reais
```

</details>

#### Exercise 6: Glued words

This prints `Goodmorning,Ana` instead of `Good morning, Ana`. Fix it.

<!-- no-verify -->
```python
greeting = "Good"
time = "morning,"
name = "Ana"
print(greeting + time + name)
```

<details>
<summary>Show answer</summary>

```python
greeting = "Good"
time = "morning,"
name = "Ana"
print(greeting + " " + time + " " + name)
```

```text
Good morning, Ana
```

Or with an f-string: `print(f"{greeting} {time} {name}")`.

</details>

### Write it

#### Exercise 7: Coffee order

Create the variables `customer = "Lucas"`, `drink = "latte"` and `price = 9.5`. Print, using one f-string:

```text
Lucas ordered a latte for 9.5 reais.
```

<details>
<summary>Show answer</summary>

```python
customer = "Lucas"
drink = "latte"
price = 9.5
print(f"{customer} ordered a {drink} for {price} reais.")
```

```text
Lucas ordered a latte for 9.5 reais.
```

</details>

#### Exercise 8: Three lines, one print

Using a single `print` and `\n`, print:

```text
Milk
Eggs
Bread
```

<details>
<summary>Show answer</summary>

```python
print("Milk\nEggs\nBread")
```

```text
Milk
Eggs
Bread
```

Another way: `print("Milk", "Eggs", "Bread", sep="\n")`.

</details>

#### Exercise 9: Word length

Create `word = "pineapple"` and print the sentence below, using `len()` inside an f-string:

```text
pineapple has 9 letters
```

<details>
<summary>Show answer</summary>

```python
word = "pineapple"
print(f"{word} has {len(word)} letters")
```

```text
pineapple has 9 letters
```

</details>

## Review

These revisit [data-types.md](data-types.md).

#### Review 1: Which type?

What does this print?

```python
value = "12"
print(type(value))
value = 12
print(type(value))
```

<details>
<summary>Show answer</summary>

```text
<class 'str'>
<class 'int'>
```

The same name first holds text, then a number. The type belongs to the value, not to the name.

</details>

#### Review 2: Total price

Create `price = 3` and `quantity = 4`, calculate the total, and print `Total: 12` using an f-string.

<details>
<summary>Show answer</summary>

```python
price = 3
quantity = 4
total = price * quantity
print(f"Total: {total}")
```

```text
Total: 12
```

</details>

## Recap

- A string is text in quotes. `\n` makes a new line.
- `+` joins strings, but only strings: use `str()` to convert numbers.
- f-strings (`f"... {value} ..."`) fill values into text and convert them for you.
- Anything inside `{}` is calculated first: variables, math, even `len(...)`.
- `print` puts `sep` between values (a space by default) and `end` after them (a new line by default).

**Next:** [built-in.md](built-in.md)
