# 09. Party invitations

Write a personalized invitation for every guest on a list, then change the list.

**You will practice:** lists, `for`, f-strings, `append`, `len`, positions `[0]` and `[-1]`

**Difficulty:** ★★☆

## The task

Create `invitations.py`.

1. Create a list `guests` with `Ana`, `Rui`, `Lia` and `Bia`.
2. With a `for` loop, print one invitation per guest (see below).
3. After the loop, add `Caio` to the list.
4. Print how many guests there are now.
5. Print the first and the last guest of the list.

## What it should look like

```text
Dear Ana, you are invited to my birthday on Saturday at 8 pm!
Dear Rui, you are invited to my birthday on Saturday at 8 pm!
Dear Lia, you are invited to my birthday on Saturday at 8 pm!
Dear Bia, you are invited to my birthday on Saturday at 8 pm!
Now there are 5 guests.
The first guest is Ana and the last is Caio.
```

## Hints

<details>
<summary>Hint 1</summary>

The invitation text is the same for everyone; only the name changes. One `print` inside the loop is enough.

</details>

<details>
<summary>Hint 2</summary>

`guests.append("Caio")` adds to the end of the list.

</details>

<details>
<summary>Hint 3</summary>

Position `0` is the first item. Position `-1` is always the last, no matter how long the list is.

</details>

## Check yourself

- [ ] Caio did not get an invitation (he was added after the loop). Can you explain why?
- [ ] You used `[-1]` instead of counting the position of the last guest.
- [ ] The number 5 comes from `len`.

## Go further

- Move the `append` to **before** the loop. What changes?
- Turn the invitation into a function `invite(name)` and call it inside the loop.
