# 04. Shopping receipt

Print a small store receipt with prices, a total and the change.

**You will practice:** `float`, arithmetic, f-strings, variables

**Difficulty:** ★☆☆

## The task

Create `receipt.py`.

1. Create three variables with prices: bread costs `8.5`, milk costs `4.75`, coffee costs `22.0`.
2. Create a variable `total` that adds the three prices. Let Python do the math: don't type `35.25` yourself.
3. Print the receipt below using f-strings.
4. The customer paid with `50.0`. Print the change, calculated by Python.

## What it should look like

```text
RECEIPT
Bread:  R$ 8.5
Milk:   R$ 4.75
Coffee: R$ 22.0
Total:  R$ 35.25
Paid with R$ 50.0, change: R$ 14.75
```

## Hints

<details>
<summary>Hint 1</summary>

Numbers with a decimal point are `float`. In Python the decimal separator is a dot: `4.75`, never `4,75`.

</details>

<details>
<summary>Hint 2</summary>

You can do math directly inside the curly braces of an f-string: `f"{a - b}"`.

</details>

<details>
<summary>Hint 3</summary>

The spaces after `Bread:`, `Milk:` and `Coffee:` are just text inside the quotes, there to line up the prices.

</details>

## Check yourself

- [ ] `35.25` and `14.75` were calculated by Python, not typed.
- [ ] The prices line up in a column.
- [ ] Changing the price of milk changes the total and the change automatically.

## Go further

- Add a fourth item to the receipt.
- Add a line `Items: 3` where the 3 is a variable you created, not typed in the text.
