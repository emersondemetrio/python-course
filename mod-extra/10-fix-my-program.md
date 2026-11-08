# 10. Fix my program

This program has four bugs. Python will show you one error at a time. Fix them one by one until it runs.

**You will practice:** reading error messages, `:` and indentation, `str()`, names, list positions

**Difficulty:** ★★☆

## The task

1. Create `fix_me.py` and copy the program below exactly as it is.
2. Run it. Read the error message: which line, and what kind of error?
3. Fix **only that** error, save, and run again.
4. Repeat until the program runs. You will meet these four errors, in this order:
   - `SyntaxError: expected ':'`
   - `TypeError: can only concatenate str (not "int") to str`
   - `NameError: name 'Show_first' is not defined. Did you mean: 'show_first'?`
   - `IndexError: list index out of range`
5. Above each line you fixed, write a comment explaining the bug in your own words.

<!-- no-verify -->
```python
# This program prints a small shopping list.
items = ["rice", "beans", "coffee"]
total_items = len(items)

print("You have " + total_items + " items")

for item in items
    print(item)

def show_first(list_of_items):
    print("First: " + list_of_items[0])

Show_first(items)

print(f"Last: {items[3]}")
```

## What it should look like

When all four bugs are fixed:

```text
You have 3 items
rice
beans
coffee
First: rice
Last: coffee
```

## Hints

<details>
<summary>Hint 1</summary>

Read the error from the bottom up. The last line says **what** went wrong; a line above it says **where** (the line number).

</details>

<details>
<summary>Hint 2</summary>

A `SyntaxError` stops Python before anything runs, which is why it shows up first even though it is not on the first line.

</details>

<details>
<summary>Hint 3</summary>

Python is case sensitive, and a list of 3 items has positions 0, 1 and 2.

</details>

## Check yourself

- [ ] You fixed one bug at a time, running after each fix.
- [ ] Each fixed line has a comment explaining the bug.
- [ ] For the last bug, you can name two different ways to get the last item.

## Go further

- Break the program again on purpose in a new way (remove a quote, delete an indentation) and read the new error.
- Write down in your notes the four error types and what each one usually means.
