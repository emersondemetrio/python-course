# 07. A function that returns a value

Write a function that calculates something and gives the result back, then use that result in sentences.

**You will practice:** `def`, parameters, `return`, using a returned value, f-strings

**Difficulty:** ★★☆

## The task

Create `prices.py`.

1. Define a function `total_price` with two parameters, `price` and `quantity`. It must **return** (not print) the price multiplied by the quantity.
2. Call it to calculate the cost of 3 cups at 12 each. Store the result in a variable `cups`.
3. Call it again for 2 plates at 25 each. Store the result in `plates`.
4. Print the three sentences below. The last number is the sum of the two results.

The function itself must not contain any `print`.

## What it should look like

```text
3 cups cost R$ 36
2 plates cost R$ 50
Everything costs R$ 86
```

## Hints

<details>
<summary>Hint 1</summary>

`return` hands the value back to whoever called the function. Catch it in a variable: `result = my_function(...)`.

</details>

<details>
<summary>Hint 2</summary>

If you see `None` in your output, the function is missing a `return`.

</details>

<details>
<summary>Hint 3</summary>

Since `cups` and `plates` are numbers, you can add them directly inside the f-string.

</details>

## Check yourself

- [ ] There is no `print` inside `total_price`.
- [ ] `36`, `50` and `86` were calculated by Python.
- [ ] You can explain why `print` inside the function would not let you add the two results.

## Go further

- Write a function `with_discount(value)` that returns the value minus 10. Use it on the final total.
- Call one function inside the other: `with_discount(total_price(12, 3))`. What does it give?
