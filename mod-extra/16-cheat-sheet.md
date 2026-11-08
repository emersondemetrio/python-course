# 16. Your own cheat sheet

Write, in Markdown and in your own words, a cheat sheet of everything you have learned so far.

**You will practice:** Markdown (headings, lists, code blocks), explaining concepts in your own words

**Difficulty:** ★★☆

## The task

In your `notes` folder, create `cheat-sheet.md`. Without copying from the course, write:

1. A `#` title for the whole page.
2. A `##` section **Terminal** with a list of the commands you know, each with a short explanation, and one example inside a code block.
3. A `##` section **Python basics** with:
   - `###` Variables and types (`int`, `float`, `str`)
   - `###` Joining text (`+` with `str()`, f-strings, `print` with commas and `sep`)
   - `###` Lists and `for` (with `enumerate`)
   - `###` Functions (definition vs call, parameter vs argument, `return` vs `print`)
   - `###` Files (`open`, `with`, `"r"`, `"a"`, `read()`, `write`)
4. In each `###` section: one or two sentences in your own words and one short example in a ```` ```python ```` code block.
5. A last section **Errors I have met**, listing the error types you have seen and what caused them.
6. Open the Markdown preview in the editor and check that everything looks right.

## What it should look like

The structure of the page (the content is yours):

```text
# My Python cheat sheet
## Terminal
## Python basics
### Variables and types
### Joining text
### Lists and for
### Functions
### Files
## Errors I have met
```

## Hints

<details>
<summary>Hint 1</summary>

A code block starts and ends with three backticks. Write the language right after the first three: `python` or `bash`.

</details>

<details>
<summary>Hint 2</summary>

If you can't explain something in one sentence, that's a sign to review it. Mark it with a `TODO` and ask in the next class.

</details>

<details>
<summary>Hint 3</summary>

Run each example before pasting it, so your cheat sheet only has code that works.

</details>

## Check yourself

- [ ] The preview shows headings in three different sizes.
- [ ] Every example in the cheat sheet runs.
- [ ] Nothing was copied: everything is in your own words.
- [ ] There is at least one `TODO` with a doubt to take to class (it's fine to have doubts!).

## Go further

- Add a table to the cheat sheet comparing `"r"`, `"a"` and `"w"`.
- Commit the cheat sheet to your GitHub repository.
