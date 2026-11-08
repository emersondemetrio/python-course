# 12. Temperature converter

Write a function that converts Celsius to Fahrenheit and use it on a list of temperatures.

**You will practice:** `def`, `return`, arithmetic, `for`, f-strings

**Difficulty:** ★★☆

## The task

Create `converter.py`.

1. Define a function `celsius_to_fahrenheit` with one parameter, `celsius`. It **returns** the temperature in Fahrenheit. The formula is: multiply by 9, divide by 5, then add 32.
2. Create a list with the values `0, 25, 37, 100`.
3. With a `for` loop, convert each value and print one line per temperature.

## What it should look like

```text
0 C is 32.0 F
25 C is 77.0 F
37 C is 98.6 F
100 C is 212.0 F
```

## Hints

<details>
<summary>Hint 1</summary>

Write the formula exactly in the order given: `celsius * 9 / 5 + 32`. Python does `*` and `/` before `+`, just like in school math.

</details>

<details>
<summary>Hint 2</summary>

The results have `.0` because `/` always gives a `float`. That's expected.

</details>

<details>
<summary>Hint 3</summary>

Inside the loop: first call the function and store the result, then print.

</details>

## Check yourself

- [ ] The function uses `return`, not `print`.
- [ ] Water boils at 212 F and freezes at 32 F: your output agrees.
- [ ] You call the function in only one place (inside the loop).

## Go further

- Write the opposite function, `fahrenheit_to_celsius` (subtract 32, multiply by 5, divide by 9), and test it with 212.
- Use `round(value, 1)` to show only one decimal place.
