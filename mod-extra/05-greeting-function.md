# 05. Greeting function

Write a function once and call it many times with different names.

**You will practice:** `def`, parameters, calling a function, f-strings

**Difficulty:** ★☆☆

## The task

Create `greetings.py`.

1. Define a function `greet` with one parameter, `name`. It prints `Good morning, <name>! Have a nice day.`
2. **Call** it three times, with `"Ana"`, `"Rui"` and `"Lia"`.
3. Define a second function `greet_time` with **two** parameters: `name` and `time_of_day`. It prints `Good <time_of_day>, <name>!`
4. Call it twice: Ana in the afternoon, Rui in the evening.

## What it should look like

```text
Good morning, Ana! Have a nice day.
Good morning, Rui! Have a nice day.
Good morning, Lia! Have a nice day.
Good afternoon, Ana!
Good evening, Rui!
```

## Hints

<details>
<summary>Hint 1</summary>

Defining is not calling. The `def` block only teaches Python the function. Nothing is printed until you write `greet("Ana")` on a line of its own, outside the function (no indentation).

</details>

<details>
<summary>Hint 2</summary>

`name` is the **parameter** (the empty slot in the definition). `"Ana"` is the **argument** (the value you put in the slot when you call).

</details>

<details>
<summary>Hint 3</summary>

With two parameters, the order of the arguments matters: the first value goes to the first parameter.

</details>

## Check yourself

- [ ] Each function has only one `print` inside, but you see several lines.
- [ ] The calls are not indented.
- [ ] You can point at a parameter and at an argument in your code.
- [ ] Swap the arguments in one call: `greet_time("evening", "Rui")`. What happens? Undo it.

## Go further

- Make a list of five names and call `greet` for each one using a `for` loop.
- Write a function `goodbye(name)` and call it after each greeting.
