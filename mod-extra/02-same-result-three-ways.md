# 02. Same result, three ways

Print the same sentence using three different techniques, then play with `sep`.

**You will practice:** concatenation with `+`, `str()`, f-strings, `print` with commas, `sep`

**Difficulty:** ★☆☆

## The task

Create `three_ways.py` with two variables:

- `plant` with the text `"basil"`
- `days` with the number `3`

Then:

1. Print `Water the basil every 3 days` using **concatenation** (`+`).
2. Print the same sentence using an **f-string**.
3. Print the same sentence using **commas** inside `print` (several values).
4. Print the three plants `basil`, `mint` and `rosemary` in one `print`, separated by ` | `.
5. Print the same three plants in one `print`, each on its own line, using `sep` again.

## What it should look like

```text
Water the basil every 3 days
Water the basil every 3 days
Water the basil every 3 days
basil | mint | rosemary
basil
mint
rosemary
```

## Hints

<details>
<summary>Hint 1</summary>

With `+`, you need spaces inside the quotes, and `days` must become text with `str(days)`. With commas, `print` adds the spaces for you.

</details>

<details>
<summary>Hint 2</summary>

An f-string starts with `f` before the quotes, and variables go inside curly braces: `f"... {plant} ..."`.

</details>

<details>
<summary>Hint 3</summary>

`sep` decides what goes between the values: `print("a", "b", sep="-")` prints `a-b`. A new line is written `"\n"`.

</details>

## Check yourself

- [ ] The first three lines are identical.
- [ ] Only the `+` version needed `str()`.
- [ ] You used `sep` twice, with two different values.
- [ ] You can say which of the three ways you find easiest to read, and why.

## Go further

- Add a variable `minutes = 5` and print `Water the basil every 3 days for 5 minutes` in all three ways.
- What happens with `print("basil", "mint", sep="")`? Try it and write the answer in a comment.
