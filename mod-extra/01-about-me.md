# 01. About me

Store a few facts about yourself in variables and print them as sentences.

**You will practice:** variables, reassignment, `print`, concatenation with `+`, `str()`, comments

**Difficulty:** ★☆☆

## The task

1. In your `Projects/extra` folder, create a file called `about_me.py`.
2. At the top, write a comment saying what the program does.
3. Create four variables:
   - `name` with the text `"Ana"`
   - `city` with the text `"Porto Alegre"`
   - `drink` with the text `"coffee"`
   - `year` with the number `2026` (a number, not text: no quotes)
4. Print four sentences, joining text and variables with `+`.
5. Change the value of `drink` to `"tea"` (reassign it), then print one more sentence.
6. Save (`Ctrl+S`) and run it from the terminal with `python about_me.py`.

When it works, change the values to your own name, city and drink.

## What it should look like

```text
My name is Ana
I live in Porto Alegre
My favorite drink is coffee
This year is 2026
Actually, today I want tea
```

## Hints

<details>
<summary>Hint 1</summary>

Text goes between quotes, numbers do not: `city = "Porto Alegre"` but `year = 2026`.

</details>

<details>
<summary>Hint 2</summary>

`+` only joins text with text. If you see `TypeError: can only concatenate str (not "int") to str`, turn the number into text first with `str(year)`.

</details>

<details>
<summary>Hint 3</summary>

Python runs from top to bottom. The last sentence must come **after** the line where you change `drink`.

</details>

## Check yourself

- [ ] The file has a comment at the top.
- [ ] `year` is a number, not text.
- [ ] The output matches, line by line.
- [ ] You can explain why the last line shows `tea` and the third line shows `coffee`.

## Go further

- Add a variable `age` and print `Next year I will be ...`, calculating the number with `+ 1`.
- Write `Name = "Rui"` (capital N) and print `name`. Which value shows up? Why?
