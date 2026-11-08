# 15. Mood diary

A tiny diary: each time you run it, it asks how you feel, saves the answer in a file, and shows every entry so far, numbered.

**You will practice:** `input`, functions with parameters, `open` with `with`, modes `"a"` and `"r"`, `write` and `"\n"`, `read`, `enumerate`

**Difficulty:** ★★★

## The task

Create `diary.py`. Organize it in functions, like the program from class 3:

1. `save_mood(file_name, mood)`: opens the file in **append** mode and writes the mood on its own line.
2. `show_diary(file_name)`: opens the file in **read** mode, prints the title `YOUR DIARY` and then every line, numbered from 1.
3. After the functions, the main part of the program:
   - asks `How are you feeling today? ` with `input`
   - calls `save_mood` with the file name `diary.txt` and the answer
   - prints `Saved!` and an empty line
   - calls `show_diary`

Run the program three times, answering `tired`, then `happy`, then `calm`.

## What it should look like

The third run:

```console
PS C:\Users\you\Projects\extra> python diary.py
How are you feeling today? calm
Saved!

YOUR DIARY
1. tired
2. happy
3. calm
```

## Hints

<details>
<summary>Hint 1</summary>

The file name is just a string. The file is only opened inside the functions, with `with open(file_name, "a") as diary:`.

</details>

<details>
<summary>Hint 2</summary>

Without `"\n"`, every mood ends up glued on the same line: `tiredhappycalm`.

</details>

<details>
<summary>Hint 3</summary>

`read()` gives the whole file as one text. `.splitlines()` turns that text into a list, one item per line, which you can use with `enumerate`.

</details>

## Check yourself

- [ ] After three runs, `cat diary.txt` in the terminal shows three lines.
- [ ] Running again does not erase the old entries.
- [ ] The program opens the file only inside the functions.
- [ ] `print()` with nothing inside makes the empty line.

## Go further

- Save the mood together with a short note: ask two questions and write `calm - quiet morning`.
- What happens if you delete `diary.txt` and run the program? And if you change `"a"` to `"w"`? Try it, then put it back.
