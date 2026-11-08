# 06. Read the code first

Explain a program line by line in comments, predict what it prints, and only then run it.

**You will practice:** reading code, comments, lists, `for`, functions, `return`, calling vs referencing

**Difficulty:** ★★☆

## The task

1. Create `read_the_code.py` and copy the program below into it. **Do not run it yet.**
2. Above **every** line, write a comment in your own words saying what that line does.
3. At the bottom, write a comment with your prediction: exactly what will appear in the terminal, line by line.
4. Save and run it. Compare with your prediction.
5. For every line you got wrong, add a comment explaining what actually happened.

<!-- no-verify -->
```python
prices = [10, 25, 5]
total = 0
for price in prices:
    total = total + price
message = f"Total: {total}"
print(message)

def double(number):
    return number * 2

print(double(total))
print(double)
```

## What it should look like

Your file ends up with a comment above each line, like this (for a different line of code):

```text
# Creates a variable called city and stores the text "Lisbon" in it
city = "Lisbon"
```

And at the bottom, your prediction:

```text
# My prediction:
# line 1: ...
# line 2: ...
# line 3: ...
```

The real output appears when you run it. That is the moment to compare.

## Hints

<details>
<summary>Hint 1</summary>

For the `for` loop, play computer: write on paper the value of `total` after each turn of the loop.

</details>

<details>
<summary>Hint 2</summary>

Nothing inside `def` runs when Python reads it. It only runs when the function is called.

</details>

<details>
<summary>Hint 3</summary>

Look closely at the last line: `double` has no parentheses. Remember what happened in class with `read` without `()`.

</details>

## Check yourself

- [ ] Every line has a comment written **before** running.
- [ ] You wrote a prediction for each line of output.
- [ ] You explained in a comment the difference between `double(total)` and `double`.

## Go further

- Add `20` to the list and predict the new output before running.
- Change `return number * 2` to `print(number * 2)`. Predict, run, and explain what changed in the output.
