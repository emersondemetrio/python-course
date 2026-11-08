# Module 07: Organizing code

Your programs are getting bigger. When everything lives in one long file, it gets hard to find things, hard to change one part without breaking another, and hard to know if it still works. This module is about the habits that professional programmers use to keep code under control: splitting it into files, handling errors on purpose, testing it automatically, and installing other people's code safely.

None of these topics adds a new "power" to your programs. They make your programs easier to grow, and that is what separates a script from a project.

## What you will learn

- How to split your code into several files (**modules**) and folders (**packages**), and import between them.
- How to handle errors on purpose with `try` and `except`, and how to signal errors with `raise`.
- How to create a project, install libraries and run your code with **uv**, and keep your code clean with **ruff**.
- How to write small programs that check your other programs (**tests**), and run them with `pytest`.

## Files, in order

1. [modules.md](modules.md)
2. [exceptions.md](exceptions.md)
3. [uv-and-ruff.md](uv-and-ruff.md)
4. [testing.md](testing.md)

`uv-and-ruff.md` comes before `testing.md` on purpose: `pytest` is a library, and uv is how you install it.

## You are ready for the next module when

- [ ] You can move a function to another file and import it with `from file import function`.
- [ ] You can explain what `if __name__ == "__main__":` is for.
- [ ] You can catch a specific error, like `ValueError`, without hiding all the others.
- [ ] You can use `raise` in your own function and explain why it is better than returning a fake value.
- [ ] You can write a test file with two or three tests and run it with `pytest`.
- [ ] You can create a project with `uv init`, add a library with `uv add`, run code with `uv run`, and check and format it with ruff.

**Next:** [Modules](modules.md)
