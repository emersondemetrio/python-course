# 03. Terminal treasure hunt

Build a small set of folders and files using only the terminal, then find your way around them.

**You will practice:** `pwd`, `ls`, `cd`, `cd ..`, `mkdir`, `echo`, `cat`, `Tab`, `history`, `clear` / `Ctrl+L`

**Difficulty:** ★☆☆

## The task

No Python today: everything happens in the terminal (PowerShell on Windows). Do not use the mouse or the editor.

1. Go to your `Projects` folder. Check where you are with `pwd`.
2. Create a folder `extra` (if you don't have it yet) and go into it.
3. Inside `extra`, create a folder called `hunt` and go into it.
4. Inside `hunt`, create two folders: `kitchen` and `garden`. Check with `ls` that both are there.
5. Go into `garden` and create a file with a clue:
   `echo "The key is under the blue pot" > clue.txt`
6. Go back up one level, then go into `kitchen` and create another file:
   `echo "Look in the garden" > note.txt`
7. Go back to `hunt`. Without entering any folder, show the content of both files with `cat`.
8. Use `Tab` to complete folder names at least twice.
9. Run `history` and look at everything you did. Then clear the screen.

## What it should look like

When you run `pwd` inside `hunt`, the path ends like this (yours starts with your own user folder):

```text
...\Projects\extra\hunt
```

From the `hunt` folder, the two `cat` commands show:

```text
The key is under the blue pot
Look in the garden
```

## Hints

<details>
<summary>Hint 1</summary>

`mkdir name` creates a folder. `cd name` goes into it. `cd ..` goes up one level.

</details>

<details>
<summary>Hint 2</summary>

`cat` accepts a path, not only a file name: from `hunt`, a file inside `garden` is `garden/clue.txt`.

</details>

<details>
<summary>Hint 3</summary>

Lost? Run `pwd` to see where you are and `ls` to see what is around you. That is always the first step.

</details>

## Check yourself

- [ ] You never used the mouse.
- [ ] `ls` inside `hunt` shows `garden` and `kitchen`.
- [ ] Both `cat` commands worked from the `hunt` folder.
- [ ] You can explain the difference between `cd garden` and `cd ..`.

## Go further

- Create a third folder `attic` with a file `treasure.txt`, and change `note.txt` so the clues lead to it. (Using `>` again on the same file replaces its content.)
- Open the whole `hunt` folder in the editor with `cursor .` and check that everything is where you expect.
