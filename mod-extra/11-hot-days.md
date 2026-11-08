# 11. Hot days

Go through a week of temperatures and count the hot days.

**You will practice:** lists of numbers, `for`, `if`, comparisons, a counter variable

**Difficulty:** ★★☆

## The task

Create `hot_days.py`.

1. Create a list `temperatures` with these values: `22, 31, 27, 35, 19, 30, 24`.
2. Create a counter variable `hot_days` that starts at `0`.
3. Go through the list with a `for` loop. A day is hot when it is **30 degrees or more**. For each hot day:
   - print `<temperature> degrees: hot day!`
   - add 1 to the counter
4. After the loop, print the total of hot days.

## What it should look like

```text
31 degrees: hot day!
35 degrees: hot day!
30 degrees: hot day!
Hot days this week: 3
```

## Hints

<details>
<summary>Hint 1</summary>

"30 or more" is `>=` in Python. Is 30 hot? Check that your output includes it.

</details>

<details>
<summary>Hint 2</summary>

A counter grows by reassigning it to itself plus one: `counter = counter + 1`.

</details>

<details>
<summary>Hint 3</summary>

Watch the indentation: the `if` is inside the `for`, and the two lines for hot days are inside the `if`. The final `print` is outside everything.

</details>

## Check yourself

- [ ] The counter starts at 0 **before** the loop.
- [ ] 30 is counted as hot.
- [ ] The total is printed only once.
- [ ] Change one temperature in the list and check that the total updates by itself.

## Go further

- Also count the cold days (below 20) with a second counter.
- Print `Cool day` for the days that are not hot, using `else`.
