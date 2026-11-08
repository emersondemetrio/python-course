# Module 03: Functions

In the last module your programs learned to decide and to repeat. Now they learn to **organize**. A function is a piece of code with a name, which you write once and use as many times as you want.

Functions are also how programmers think. Instead of one long list of instructions, a program becomes a set of small, named steps: `read_file`, `calculate_total`, `show_menu`. Each one does one job.

This module also teaches you to **read errors**. Every programmer, at every level, sees errors all day. The difference is that experienced programmers read them calmly, because error messages tell you exactly where to look.

## What you will learn

- How to define a function and how to call it (and why these are different things)
- The difference between a **parameter** and an **argument**
- The difference between `return` and `print`, the most important idea of this module
- Where variables "live" (scope), and why functions should receive and return values
- How to organize a program with a `main()` function
- How to read a traceback and find the line that caused the problem
- How to use the debugger in Cursor to watch your code run step by step

## Files, in order

| # | File | What it covers | Time |
|---|---|---|---|
| 1 | [functions.md](functions.md) | `def`, calling, parameters and arguments, default values, `return` vs `print`, `None` | 90 to 120 min |
| 2 | [scope.md](scope.md) | Local and global variables, passing values in and out, `main()` | 60 min |
| 3 | [reading-errors.md](reading-errors.md) | Tracebacks, the most common errors, print debugging, the debugger | 60 to 90 min |

## How to study this module

1. In `functions.md`, do not rush the section **return vs print**. Read it, run it, and explain it out loud (to yourself, a friend, or a plant). If you can explain it, you understood it.
2. When an exercise crashes, **read the error before you look at the code**. Practicing that habit is half of this module.
3. As always: type the examples, try exercises before opening the answers, copy the Recap into your notes.

## You are ready for the next module when you can...

- [ ] Explain the difference between defining a function and calling it
- [ ] Point to the parameter and the argument in `greet("Ana")` and its `def`
- [ ] Explain, in your own words, the difference between `return` and `print`
- [ ] Explain why a function without `return` gives back `None`
- [ ] Write a function that receives two values and returns a result, without looking at an example
- [ ] Organize a small program with a `main()` function that calls the others
- [ ] Read a traceback and say on which line the problem is and what kind of problem it is
- [ ] Put a breakpoint in Cursor and step through a function

**Next:** [functions.md](functions.md)
