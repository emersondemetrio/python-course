# 14. Letter counter

Count characters, a specific letter and words in a sentence, using a loop over a string.

**You will practice:** looping over a string, `if`, counters, `len`, f-strings

**Difficulty:** ★★★

## The task

Create `counter.py`.

1. Create a variable `sentence` with the text `the cat sat on the mat`.
2. Create a variable `letter` with the text `a`.
3. Print how many characters the sentence has (spaces count too).
4. Go through the sentence one character at a time and count how many times `letter` appears. Print the result.
5. Count the words. There is no special tool for it yet: think about what separates the words in the sentence.

## What it should look like

```text
The sentence has 22 characters.
The letter 'a' appears 3 times.
It has 6 words.
```

## Hints

<details>
<summary>Hint 1</summary>

A `for` loop works on text too: `for char in sentence:` gives one character per turn.

</details>

<details>
<summary>Hint 2</summary>

Single quotes can go inside double quotes with no problem: `f"The letter '{letter}' ..."`.

</details>

<details>
<summary>Hint 3</summary>

Count the spaces. How many words are there for each space? Try with a short sentence on paper, like `hello world`.

</details>

## Check yourself

- [ ] The number of characters comes from `len`, not from counting by hand.
- [ ] Changing `letter` to `t` gives a different count without changing anything else.
- [ ] Your word count works for another sentence too (try one of your own).

## Go further

- Turn the letter counting into a function `count_letter(text, letter)` that returns the number.
- Count `T` in `The cat` and then `t`. Are they the same? Why not?
