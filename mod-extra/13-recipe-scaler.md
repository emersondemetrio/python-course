# 13. Recipe scaler

A cake recipe serves 4 people. Write a function that recalculates each ingredient for a different number of people.

**You will practice:** `def` with two parameters, `return`, arithmetic, f-strings, reusing a function

**Difficulty:** ★★★

## The task

The original recipe (for 4 people) uses: 200 g of flour, 100 g of sugar, 2 eggs and 250 ml of milk.

Create `recipe.py`.

1. Define a function `scale(amount, people)` that returns the amount needed for `people` people. Think about the math: the recipe is for 4.
2. Create a variable `people` with the value `6`.
3. Print the title and one line per ingredient, calling `scale` for each one.
4. Change `people` to `2` and run again: every amount must change by itself.

## What it should look like

With `people = 6`:

```text
Cake for 6 people:
- 300.0g flour
- 150.0g sugar
- 3.0 eggs
- 375.0ml milk
```

## Hints

<details>
<summary>Hint 1</summary>

First find the amount for **one** person (divide by 4), then multiply by the number of people.

</details>

<details>
<summary>Hint 2</summary>

You can call a function inside an f-string: `f"- {scale(200, people)}g flour"`.

</details>

<details>
<summary>Hint 3</summary>

Test the function before printing the recipe: `scale(200, 4)` must give back `200.0`. If not, the formula is wrong.

</details>

## Check yourself

- [ ] For 4 people, every amount stays the same as the original.
- [ ] For 6 people, the output matches.
- [ ] To change the number of people, you change **one** line only.

## Go further

- Put the ingredient names in one list and the amounts in another, and print the recipe with a `for` loop and `enumerate`.
- What happens with `people = 3`? How many eggs would you buy in real life?
