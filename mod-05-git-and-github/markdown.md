# Markdown

> **In one sentence:** Markdown is a way of writing plain text with a few simple symbols (like `#` and `*`) that turn into nicely formatted titles, lists, links and code when displayed.

## Why it matters

Every GitHub project has a `README.md`, and the `.md` means Markdown. This course is written in Markdown. Many note apps, chat tools and documentation sites use it too. It is also the perfect format for your own study notes: you write fast in plain text, and it still looks organized.

## Analogy

Think of the marks a teacher makes on a draft: underline this, make this a title, put these in a list. Markdown is the same idea. You write the text with small marks, and the screen (GitHub, your editor's preview) applies them for you. The file itself stays readable even without formatting.

## The idea, step by step

Create a file called `practice.md` in a practice folder and open it in your editor. In Cursor (and VS Code), press `Ctrl+Shift+V` to open the **preview**, or right-click the file tab and choose "Open Preview". Keep the preview open side by side while you try each example.

### Headings

Start a line with `#` and a space. More `#` means a smaller heading:

```markdown
# Main title
## Section
### Subsection
```

Use one `#` title at the top of a file, then `##` for sections. Do not skip the space: `#Title` is not a heading in most places.

### Paragraphs and line breaks

Text written on consecutive lines becomes **one** paragraph. To start a new paragraph, leave an **empty line**:

```markdown
This is the first paragraph.
This line joins the first paragraph.

This is a second paragraph.
```

### Emphasis

```markdown
*italic* or _italic_
**bold**
`code inside a sentence`
~~crossed out~~
```

Use backticks (`` ` ``) for anything that is code, a command, or a file name: "run `git status`", "open `notes.py`".

### Lists

Bulleted lists use `-` (or `*`). Numbered lists use `1.`, `2.`, and so on. Indent with spaces to make a sub-list:

```markdown
- milk
- eggs
  - 6 for the cake
  - 6 for breakfast
- bread

1. Open the terminal
2. Go to the project folder
3. Run the program
```

A **task list** (checkboxes) works on GitHub:

```markdown
- [x] Install Python
- [ ] Finish module 05
```

### Links and images

```markdown
[Python website](https://www.python.org)
[Next lesson](github.md)
![A ceramic bowl](images/bowl.png)
```

- A link is `[text shown](address)`. The address can be a website or another file in the same repository.
- An image is the same, with a `!` in front. The text in brackets describes the image for people who cannot see it.

### Code blocks

For several lines of code, put three backticks on a line before and after. Write the language name right after the opening backticks to get colors:

````markdown
```python
name = "Ana"
print(f"Hello, {name}!")
```

```powershell
python notes.py
```
````

Without the language name it still works, but without colors.

### Tables

```markdown
| Command      | What it does              |
|--------------|---------------------------|
| `git status` | Shows the situation       |
| `git add .`  | Puts changes in the box   |
```

The first line is the header, the second line (with dashes) separates it, and each following line is a row. The columns do not need to be perfectly aligned in the text; they will look aligned on screen.

### Hidden sections with `<details>`

This course hides exercise answers so you can try first. That is done with two HTML tags that GitHub understands inside Markdown:

````markdown
<details>
<summary>Show answer</summary>

The answer goes here. It can have **bold**, lists and code:

```python
print("hello")
```

</details>
````

- `<summary>` is the text you click.
- **Leave an empty line** after `</summary>` and before `</details>`. Without them, the Markdown inside is shown as raw symbols on GitHub.

This is also great for your own notes: write a question, and hide the answer below it to quiz yourself later.

### Previewing and committing

Write, check the preview, save. Markdown files are committed and pushed like any other file. On GitHub, any `.md` file is shown formatted when you click it, and the `README.md` is shown on the repository's front page.

## Common mistakes

### No space after `#`

```markdown
#Notes
```

Shows as plain text `#Notes`. **Fix:** `# Notes`.

### Lists glued to a paragraph

```markdown
My shopping list:
- milk
- eggs
```

Some renderers show this fine, others join it into the paragraph. **Fix:** leave an empty line before the list.

### Code block never closed

If you forget the closing three backticks, **everything** after it becomes code. **Fix:** every opening ```` ``` ```` needs a closing ```` ``` ```` on its own line.

### `<details>` without empty lines

````markdown
<details><summary>Show answer</summary>**bold** and `code` here</details>
````

On GitHub, you will see the raw `**` and backticks. **Fix:** add an empty line after `</summary>` and before `</details>`.

## Exercises

Write each answer in your `practice.md` and check it in the preview.

### Predict the output

#### Exercise 1: What will it look like?

Describe how this is displayed:

```markdown
## Tasks

Buy **coffee** and `run notes.py`.

1. Wash
2. Dry
```

<details>
<summary>Show answer</summary>

A section heading "Tasks". Then a paragraph where "coffee" is bold and "run notes.py" is shown in a code font. Then a numbered list with "Wash" and "Dry".

</details>

### Fix the bug

#### Exercise 2: Three problems

This text has three formatting problems. Find and fix them.

````markdown
#My Recipes
Ingredients:
- flour
- sugar
```python
print("bake")
````

<details>
<summary>Show answer</summary>

````markdown
# My Recipes

Ingredients:

- flour
- sugar

```python
print("bake")
```
````

1. Missing space after `#`.
2. Missing empty line before the list (and after the title).
3. The code block was never closed.

</details>

### Write it

#### Exercise 3: Your module notes

Create `notes/python.md` (or add to it, if you already have one) with:

- a `#` title
- a `##` section for each module you have studied
- in each section, a bullet list of 3 things you learned
- at least one code block with a small Python example

<details>
<summary>Show answer</summary>

````markdown
# My Python notes

## Module 04: Files

- `with open(name, "a", encoding="utf-8") as file:` opens a file and closes it by itself
- `"w"` erases, `"a"` adds to the end
- `file.read().splitlines()` gives a list of lines

```python
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("buy coffee\n")
```

## Module 05: Git and GitHub

- `git add .` then `git commit -m "message"`
- `git push` sends commits to GitHub
- `git status` when in doubt
````

</details>

#### Exercise 4: A Git cheat sheet table

Write a table with two columns, "Command" and "What it does", with at least five Git commands from this module.

<details>
<summary>Show answer</summary>

```markdown
| Command                  | What it does                           |
|--------------------------|----------------------------------------|
| `git init`               | Starts a repository in this folder     |
| `git status`             | Shows what changed and what is staged  |
| `git add .`              | Stages all changes                     |
| `git commit -m "msg"`    | Saves a commit with a message          |
| `git log --oneline`      | Lists commits, one per line            |
| `git push`               | Sends commits to GitHub                |
```

</details>

#### Exercise 5: A self-quiz with `<details>`

Write a question about files with the answer hidden inside a `<details>` block. Push it to GitHub and check that the answer opens when you click.

<details>
<summary>Show answer</summary>

````markdown
**Question:** Which mode adds to a file without erasing it?

<details>
<summary>Answer</summary>

Mode `"a"` (append).

</details>
````

</details>

## Review

#### Review 1: commit messages (git-basics.md)

You just added a "How to run" section to your README. Write a good commit message for it.

<details>
<summary>Show answer</summary>

Something like `Add how to run section to README`. It starts with a verb and says what the commit does.

</details>

#### Review 2: strings (module 01)

What does this print?

```python
title = "notes"
print("# " + title.upper())
print(f"Total: {len(title)} letters")
```

<details>
<summary>Show answer</summary>

Output:

```text
# NOTES
Total: 5 letters
```

`.upper()` returns the text in capitals, and `len` counts the characters.

</details>

## Recap

- `#`, `##`, `###` make headings; leave an empty line between paragraphs and before lists.
- `**bold**`, `*italic*`, `` `code` ``; `[text](link)` and `![description](image.png)`.
- Code blocks use three backticks with the language name, and must be closed.
- Tables use `|` and a dashed line under the header.
- `<details>` and `<summary>` hide content; leave empty lines inside them so Markdown still works.

**Next:** [Module 06: Data structures](../mod-06-data-structures/README.md)
