# Python Course

A beginner-friendly Python course that goes from "I have never opened a terminal" to "I built a complete app with a database, a web API and AI suggestions".

No computing background needed. If you can use a browser and you are curious, you can do this.

## Who this is for

- People who have **never programmed before**, or tried and got lost.
- People who know a little HTML and CSS and want to learn a "real" programming language.
- Adults learning at their own pace, with or without a teacher.

Everything is explained from zero. Every new word is defined the first time it appears.

## How to use this course

1. **Read the modules in order.** Each one builds on the previous ones.
2. **Type the examples yourself.** Do not copy and paste. Typing is how your fingers and your brain learn the shapes of the code.
3. **Try every exercise before opening the answer.** Getting it wrong is part of learning. The answer is hidden on purpose.
4. **Take notes in your own words.** At the end of each file there is a **Recap**. Copy it into your notes and rewrite it the way you would explain it to a friend.
5. **Do the Review exercises.** They bring back topics from earlier files. Remembering something after a few days is what makes it stick.
6. **Go slowly.** One file per study session is a good pace. Coming back tomorrow is better than rushing today.

## Modules

| Module | Topics | Final project milestone |
|---|---|---|
| [00 · The workbench](mod-00-workbench/) | Terminal, what Python is, organizing your work | |
| [01 · Building blocks](mod-01-building-blocks/) | Data types, variables, strings, built-in functions | |
| [02 · Decisions and loops](mod-02-decisions-and-loops/) | Conditionals, lists, `for` loops | |
| [03 · Functions](mod-03-functions/) | Defining and calling functions, scope, reading errors | |
| [04 · Files](mod-04-files/) | Reading and writing files | **Milestone 1:** save pieces to a text file |
| [05 · Git and GitHub](mod-05-git-and-github/) | Version control, GitHub, Markdown | **Milestone 2:** the project becomes a repository |
| [06 · Data structures](mod-06-data-structures/) | Dictionaries, tuples, sets, JSON, comprehensions | **Milestone 3:** each piece is a dictionary saved as JSON |
| [07 · Organizing code](mod-07-organizing-code/) | Modules, exceptions, uv and ruff, testing | **Milestone 4:** the project split into modules, with tests |
| [08 · Objects](mod-08-objects/) | Classes and inheritance | **Milestone 5:** a `Piece` class with its lifecycle |
| [09 · Databases](mod-09-databases/) | SQL basics, SQLite | **Milestone 6:** data moves from JSON to SQLite |
| [10 · HTTP and the web](mod-10-http-and-web/) | How the web works, calling APIs, building an API with Flask | **Milestone 7:** a web API and an HTML/CSS/JS interface |
| [11 · AI](mod-11-ai/) | What an LLM is, calling an LLM, writing prompts | **Milestone 8:** suggestions, first by rules, then with an LLM |
| [Final project](mod-final-project/) | Everything together | The finished ceramics studio manager |

Each module folder has a `README.md` with its goals, the files to read in order, and a checklist that tells you when you are ready to move on.

## How the files are organized

Every topic file follows the same structure, so you always know where to look:

1. **In one sentence:** the idea, short.
2. **Why it matters:** why you should care.
3. **Analogy:** a picture from everyday life.
4. **The idea, step by step:** the explanation, with small examples and their output.
5. **Common mistakes:** errors beginners make, the real message Python shows, and the fix.
6. **Exercises:** three kinds, easiest first:
   - **Predict the output:** read code without running it and write down what it prints.
   - **Fix the bug:** the code is broken. Find the problem and fix it.
   - **Write it:** write the code yourself, from zero.
7. **Review:** exercises about topics from earlier files.
8. **Recap:** a few bullets to copy into your notes.

## How the hidden answers work

Answers are hidden inside a box you can open by clicking it, like this:

<details>
<summary>Show answer</summary>

Surprise! This is where the answer would be.

Try the exercise first, then click to compare. If your answer is different but works, that is fine. There is usually more than one correct way to write code.

</details>

Some exercises also have a **Hint** box. Open the hint first if you are stuck, and only then the answer.

## What you need

- **Python 3** (version 3.12 or newer). Download it from [python.org](https://www.python.org/downloads/) (on Windows, check the box **"Add python.exe to PATH"** during installation), or install it with uv (`uv python install`).
- **A code editor:** [Cursor](https://www.cursor.com/) or [VS Code](https://code.visualstudio.com/), both free, with the **Python** and **Ruff** extensions.
- **A terminal:** PowerShell on Windows, Terminal on macOS or Linux. It is already on your computer.
- **[uv](https://docs.astral.sh/uv/)**, from module 07 on: one tool that creates projects, installs libraries and runs your code. Module 07 shows how to install it. We use uv instead of pip throughout the course.

Module 00 walks you through the first three.

## The final project

Throughout the course you will build a **ceramics studio manager**: an app to catalog ceramic pieces and follow each one through its lifecycle:

```text
modeled → drying → bisque firing → glazed → glaze firing
```

It starts in module 04 as a tiny script that saves pieces to a text file. Every module after that adds something new, until it becomes:

- a **SQLite database** that stores every piece,
- an **HTTP API** written with Flask,
- a **web interface** in HTML, CSS and JavaScript,
- **suggestions** for what to do next, first with simple rules ("this piece has been drying for 8 days, it is ready for the bisque firing"), then with an **LLM** (a large language model, the kind of AI behind chat assistants).

See the [final project](mod-final-project/) folder for the full plan.

## For contributors

Every Python example that shows an output is checked automatically: [`tools/verify.py`](tools/verify.py) runs each example and compares what it prints with the output written in the lesson. Before committing changes, run these from the repository root:

```bash
uv run tools/verify.py
uv run ruff check
uv run ruff format --check
```

## License

This course is free to use, share and adapt under the [MIT License](LICENSE).
