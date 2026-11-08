# 08. Numbered to-do list

Print a to-do list numbered from 1, the way people write lists on paper.

**You will practice:** lists, `for`, `enumerate` with `start=1`, `len`, f-strings

**Difficulty:** ★★☆

## The task

Create `todo.py`.

1. Create a list `tasks` with four items: `buy bread`, `water the plants`, `call mom`, `study Python`.
2. Print the title `TO DO TODAY`.
3. Use a `for` loop with `enumerate` to print each task with its number, **starting at 1**.
4. At the end, print how many tasks there are, using `len`.

## What it should look like

```text
TO DO TODAY
1. buy bread
2. water the plants
3. call mom
4. study Python
Total: 4 tasks
```

## Hints

<details>
<summary>Hint 1</summary>

`enumerate` gives two things on each turn: the position and the item. So the `for` needs two variable names: `for number, task in ...`.

</details>

<details>
<summary>Hint 2</summary>

By default, counting starts at 0. `enumerate(tasks, start=1)` starts at 1.

</details>

<details>
<summary>Hint 3</summary>

The last `print` must not be indented, or it will run once per task.

</details>

## Check yourself

- [ ] The numbers start at 1.
- [ ] Adding a fifth task to the list updates both the list and the total, without changing anything else.
- [ ] `Total` appears only once.

## Go further

- Add a task with `tasks.append(...)` after creating the list, and run again.
- Print only the first and the last task, using positions `[0]` and `[-1]`.
