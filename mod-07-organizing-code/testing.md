# Testing

> **In one sentence:** a test is a small piece of code that runs your code and checks that the result is what you expected, so the computer can tell you when something breaks.

## Why it matters

How do you know your program works? Until now, you ran it, typed some inputs and looked at the screen. That works once. But every time you change something, you would have to check everything again by hand, and you will forget something. Tests do this checking for you, in a second, as many times as you want. They also give you courage: you can improve your code, run the tests, and know right away if you broke anything. In the final project of this course, tests will protect the parts you build early while you add new ones.

## Analogy

Think of a baker who wrote down a cake recipe. Before selling the cake, she checks: is it sweet? Is it fully baked inside? Did it rise? She has a short checklist and goes through it every time she changes the recipe, even a little.

A test file is that checklist, written in Python. Each test is one item: "with 2 cups of flour, the conversion should give 240 grams". `pytest` is the assistant who goes through the whole checklist and tells you which items passed and which failed.

## The idea, step by step

### `assert`: the smallest possible test

`assert` is a Python keyword that means "I am sure this is true". If it is true, nothing happens. If it is false, Python raises an `AssertionError`.

```python
def with_tax(price):
    return round(price * 1.10, 2)

assert with_tax(10) == 11.0
assert with_tax(0) == 0
print("All checks passed")
```

Output:

```text
All checks passed
```

Now imagine someone changes `1.10` to `1.01` by mistake:

<!-- error -->
```python
def with_tax(price):
    return round(price * 1.01, 2)

assert with_tax(10) == 11.0
print("All checks passed")
```

```text
Traceback (most recent call last):
AssertionError
```

The program stopped right at the broken check. The mistake was caught by the computer, not by a customer.

You can add a message after a comma to explain what went wrong:

<!-- error -->
```python
total = 10 + 10
assert total == 30, f"expected 30, got {total}"
```

```text
Traceback (most recent call last):
AssertionError: expected 30, got 20
```

### Why not just `print`?

With `print`, **you** have to look at the output and decide if it is right. With `assert`, the expected answer is written in the code, and the **computer** decides. You only need to look when something fails. That is the whole point of a test.

### pytest: a tool to run many tests

Writing `assert` lines at the bottom of your file works, but it gets messy. `pytest` is a library that organizes this. It is the most popular testing tool in Python.

`pytest` does not come with Python. It is a tool for you, the developer, so you add it to your uv project with `--dev` (you learned this in [uv-and-ruff.md](uv-and-ruff.md)). In the terminal, inside your project folder:

```powershell
uv add --dev pytest
```

### Writing tests for pytest

Imagine a uv project, created with `uv init shop` as in the previous lesson, with this code (the files `uv init` made, like `pyproject.toml`, are left out of the picture):

<!-- no-verify -->
```text
shop/
├── prices.py
└── test_prices.py
```

<!-- no-verify -->
```python
# prices.py
def with_tax(price):
    return round(price * 1.10, 2)

def apply_discount(price, percent):
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return price - price * percent / 100
```

The tests go in a separate file. pytest finds tests by their **names**, so follow these rules exactly:

- The test **file** name starts with `test_`: `test_prices.py`.
- Each test **function** name starts with `test_`: `def test_discount_of_half():`.
- Inside each test, use `assert`.

<!-- no-verify -->
```python
# test_prices.py
from prices import with_tax, apply_discount

def test_with_tax_adds_ten_percent():
    assert with_tax(10) == 11.0

def test_discount_of_half():
    assert apply_discount(80, 50) == 40

def test_discount_of_zero_changes_nothing():
    assert apply_discount(80, 0) == 80
```

Give tests long, descriptive names. When one fails, the name tells you what broke without reading the code.

### Running the tests

In the terminal, inside the `shop` folder, type `uv run pytest`:

```console
PS C:\Users\you\Projects\shop> uv run pytest
============================= test session starts ==============================
collected 3 items

test_prices.py ...                                                       [100%]

============================== 3 passed in 0.02s ===============================
```

Each dot `.` is a test that passed. pytest found the file and the three functions by itself, because their names start with `test_`.

Add `-v` (verbose) to see each test by name:

```console
PS C:\Users\you\Projects\shop> uv run pytest -v
test_prices.py::test_with_tax_adds_ten_percent PASSED                    [ 33%]
test_prices.py::test_discount_of_half PASSED                             [ 66%]
test_prices.py::test_discount_of_zero_changes_nothing PASSED             [100%]

============================== 3 passed in 0.02s ===============================
```

### When a test fails

Now break `with_tax` on purpose (change `1.10` to `1.01`) and run again:

```console
PS C:\Users\you\Projects\shop> uv run pytest
collected 3 items

test_prices.py F..                                                       [100%]

=================================== FAILURES ===================================
________________________ test_with_tax_adds_ten_percent ________________________

    def test_with_tax_adds_ten_percent():
>       assert with_tax(10) == 11.0
E       assert 10.1 == 11.0
E        +  where 10.1 = with_tax(10)

test_prices.py:4: AssertionError
=========================== short test summary info ============================
FAILED test_prices.py::test_with_tax_adds_ten_percent - assert 10.1 == 11.0
========================= 1 failed, 2 passed in 0.02s ==========================
```

How to read it:

- `F..`: the first test **F**ailed, the other two passed.
- The `>` arrow points to the line that failed.
- `assert 10.1 == 11.0`: pytest shows the **real** values. `with_tax(10)` returned `10.1`, but you expected `11.0`.
- The last line is the summary: 1 failed, 2 passed.

Now you know exactly where to look. Fix the code, run again, see green.

### Testing that an error happens: `pytest.raises`

Sometimes the correct behavior **is** an exception. `apply_discount(80, 150)` should raise `ValueError`, because a 150% discount makes no sense. To test that, use `pytest.raises` with `with`:

<!-- no-verify -->
```python
# test_prices.py
import pytest
from prices import apply_discount

def test_discount_above_100_is_an_error():
    with pytest.raises(ValueError):
        apply_discount(80, 150)
```

Read it as: "inside this block, I expect a `ValueError`". If the error happens, the test passes. If the function returns normally, the test fails, because you expected an error and none came.

### Many cases at once: `parametrize` (briefly)

When you want to check the same function with many inputs, you do not need to write one test per input. `pytest.mark.parametrize` runs one test several times with different values:

<!-- no-verify -->
```python
import pytest
from prices import apply_discount

@pytest.mark.parametrize("price, percent, expected", [
    (100, 10, 90),
    (100, 50, 50),
    (80, 25, 60),
    (80, 0, 80),
])
def test_apply_discount(price, percent, expected):
    assert apply_discount(price, percent) == expected
```

The line starting with `@` is called a **decorator**. You do not need to understand decorators yet. Just read it as: "run this test four times, once for each row, filling `price`, `percent` and `expected` from the row". pytest will report 4 tests.

### What to test

A good starting checklist for each function:

1. A **normal** case: `apply_discount(80, 50) == 40`.
2. An **edge** case, at the limits: `apply_discount(80, 0)`, `apply_discount(80, 100)`, an empty list, an empty string.
3. A **wrong** input that should raise an error: `apply_discount(80, 150)`.

Test what the function **does** (the result), not how it does it. That way you can rewrite the inside of the function, and the tests still tell you if the result is right.

## Common mistakes

### The test file or function does not start with `test_`

```console
PS C:\Users\you\Projects\shop> uv run pytest
collected 0 items

============================ no tests ran in 0.01s =============================
```

"collected 0 items" means pytest did not find any test. Check the names: the file must be `test_something.py` and every function must be `def test_something():`. A file called `prices_test.py` works too, but `tests_prices.py` or `check_prices.py` does not.

### Comparing with `=` instead of `==`

<!-- error -->
```python
assert 1 + 1 = 2
```

```text
    assert 1 + 1 = 2
                 ^
SyntaxError: invalid syntax
```

`=` stores a value, `==` compares. In tests you always compare: `assert 1 + 1 == 2`.

### Calling the function outside `pytest.raises`

<!-- no-verify -->
```python
def test_discount_above_100_is_an_error():
    result = apply_discount(80, 150)
    with pytest.raises(ValueError):
        print(result)
```

The `ValueError` is raised on the first line, **before** reaching `with pytest.raises`, so the test crashes instead of passing. The call that should fail must be **inside** the `with` block.

### `pytest` is not recognized

```console
PS C:\Users\you\Projects\shop> pytest
pytest : The term 'pytest' is not recognized as the name of a cmdlet, function, script file, or operable program.
```

pytest is installed inside the project's `.venv`, and the terminal on its own does not look there. **Fix:** always start it with `uv run pytest`, which runs it inside the project. If uv then says it cannot find `pytest`, add it first with `uv add --dev pytest`.

## Exercises

### Predict the output

#### Exercise 1: Which asserts pass?

Which of these lines raise an `AssertionError`?

<!-- no-verify -->
```python
assert 2 * 3 == 6
assert "tea".upper() == "Tea"
assert len([1, 2, 3]) == 3
assert 10 / 4 == 2
```

<details>
<summary>Show answer</summary>

Line 2 and line 4 fail.

- `"tea".upper()` is `"TEA"`, not `"Tea"`.
- `10 / 4` is `2.5`, not `2`.

In a real run, Python stops at the **first** failing assert (line 2) and never checks line 4. That is why pytest, which runs each test function separately, is more useful: it reports all failures at once.

</details>

#### Exercise 2: Read the report

You run pytest and see this. How many tests ran? Which one failed, and what did the function really return?

```console
test_temps.py .F.                                                        [100%]
...
FAILED test_temps.py::test_freezing_point - assert 0.0 == 32
========================= 1 failed, 2 passed in 0.01s ==========================
```

<details>
<summary>Show answer</summary>

Three tests ran (`.F.`): the second one failed. It is `test_freezing_point`. The function returned `0.0`, but the test expected `32`. Maybe the conversion function forgot to add 32, or the test called the wrong function.

</details>

### Fix the bug

#### Exercise 3: Invisible tests

pytest says "collected 0 items" for this file, called `checks.py`. Fix the names (two problems).

<!-- no-verify -->
```python
# checks.py
from prices import with_tax

def tax_of_ten():
    assert with_tax(10) == 11.0
```

<details>
<summary>Show answer</summary>

Rename the file to `test_prices.py` and the function to start with `test_`:

<!-- no-verify -->
```python
# test_prices.py
from prices import with_tax

def test_tax_of_ten():
    assert with_tax(10) == 11.0
```

</details>

### Write it

#### Exercise 4: Tests with plain `assert`

Here is a function. Write three `assert` lines for it: one normal case, one with an empty string, and one with uppercase letters. Then print `"ok"`.

<!-- no-verify -->
```python
def count_vowels(text):
    total = 0
    for letter in text.lower():
        if letter in "aeiou":
            total = total + 1
    return total
```

<details>
<summary>Show answer</summary>

```python
def count_vowels(text):
    total = 0
    for letter in text.lower():
        if letter in "aeiou":
            total = total + 1
    return total

assert count_vowels("banana") == 3
assert count_vowels("") == 0
assert count_vowels("APPLE") == 2
print("ok")
```

Output:

```text
ok
```

</details>

#### Exercise 5: Your first pytest file

Create a folder `temps` with:

1. `convert.py` with `celsius_to_fahrenheit(c)` (formula: `c * 9 / 5 + 32`).
2. `test_convert.py` with three tests: water freezes (0 gives 32), water boils (100 gives 212), and body temperature (37 gives 98.6, use `round(..., 1)`).

Run `uv run pytest -v`.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# convert.py
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32
```

<!-- no-verify -->
```python
# test_convert.py
from convert import celsius_to_fahrenheit

def test_water_freezes():
    assert celsius_to_fahrenheit(0) == 32

def test_water_boils():
    assert celsius_to_fahrenheit(100) == 212

def test_body_temperature():
    assert round(celsius_to_fahrenheit(37), 1) == 98.6
```

```console
PS C:\Users\you\Projects\temps> uv run pytest -v
test_convert.py::test_water_freezes PASSED                               [ 33%]
test_convert.py::test_water_boils PASSED                                 [ 66%]
test_convert.py::test_body_temperature PASSED                            [100%]

============================== 3 passed in 0.01s ===============================
```

Why `round` in the last test? `37 * 9 / 5 + 32` gives `98.60000000000001` because of the tiny rounding errors computers make with decimals. Comparing decimal numbers exactly is risky; round them first.

</details>

#### Exercise 6: Testing an error

Using the `divide` function from the exceptions lesson (the version that raises `ValueError` when `b` is 0), write a test that checks that dividing by zero raises `ValueError`.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# test_divide.py
import pytest
from calc import divide

def test_divide_normal():
    assert divide(10, 4) == 2.5

def test_divide_by_zero_is_an_error():
    with pytest.raises(ValueError):
        divide(5, 0)
```

(Assuming `divide` lives in a file called `calc.py`.)

</details>

## Review

#### Review 1: Exceptions (this module)

What does this print?

<!-- no-verify -->
```python
def check_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return "ok"

for age in [30, -2]:
    try:
        print(check_age(age))
    except ValueError as error:
        print(f"error: {error}")
```

<details>
<summary>Show answer</summary>

```python
def check_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return "ok"

for age in [30, -2]:
    try:
        print(check_age(age))
    except ValueError as error:
        print(f"error: {error}")
```

Output:

```text
ok
error: age cannot be negative
```

</details>

#### Review 2: Functions with `return` (module 03)

Why is it much easier to test a function that **returns** its result than a function that only **prints** it?

<details>
<summary>Show answer</summary>

A test needs to get the result in its hands to compare it: `assert with_tax(10) == 11.0`. A function that only prints sends the result to the screen and gives back `None`, so the test has nothing to compare. This is one more reason to separate calculating (`return`) from showing (`print`).

</details>

## Recap

- `assert condition` does nothing if the condition is true and raises `AssertionError` if it is false.
- pytest finds tests by name: files `test_*.py`, functions `def test_*():`. Run with `uv run pytest` (`-v` for details).
- `.` passed, `F` failed. A failure shows the line and the real values.
- `with pytest.raises(ValueError):` tests that an error happens.
- Test a normal case, an edge case and a wrong input. Test results, not the insides.

**Next:** [Module 08: Objects](../mod-08-objects/README.md)
