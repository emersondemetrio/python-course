# Final project: Atanor

> **In one sentence:** Atanor is a ceramics studio manager that you build piece by piece while you take this course: it records your ceramic pieces, follows each one through its life from wet clay to finished glaze, and suggests what to do next.

The name comes from the *athanor*, the furnace that old alchemists kept burning for days. A kiln is the modern version.

## Why this project

Learning a language with small exercises is good, but things only stick when you use them to build something you care about. Atanor grows with you:

- After module 4 it is a tiny script that writes lines to a text file.
- After module 11 it is a real application with a database, a web page and AI suggestions.

Every milestone uses **only** what you have learned so far. You will rewrite parts of it more than once. That is normal: professional programmers rewrite code all the time when they learn a better way.

## What the finished system does

- **Catalog pieces.** Each piece has a name, clay, technique, glaze, firing temperature, notes and the date it was created.
- **Track the lifecycle.** Every piece goes through the same stages, always in this order:

  ```text
  modeled → drying → bisque_fired → glazed → glaze_fired
  ```

  | Stage | What it means |
  |---|---|
  | `modeled` | The piece was just shaped from wet clay. |
  | `drying` | It is drying slowly at room temperature. |
  | `bisque_fired` | It went through the first firing (the "bisque"). It is hard now, but still porous. |
  | `glazed` | Glaze was applied. It is waiting for the second firing. |
  | `glaze_fired` | The final firing is done. The piece is finished. |

- **Suggest what to do next.** First with simple rules ("this piece has been drying for 8 days, it is ready for the bisque firing"), then with an AI model that reads your history and proposes ideas.

## Milestones

Do them in order. Each one says which modules you need first.

| # | Milestone | Requires | What you build |
|---|---|---|---|
| 1 | [A text file](milestones/01-text-file.md) | Modules 0 to 4 | `atanor.py` asks for a piece and saves it as a line in `pieces.txt` |
| 2 | [A repository](milestones/02-repository.md) | Module 5 | The project goes to Git and to your GitHub |
| 3 | [JSON records](milestones/03-json-records.md) | Module 6 | Each piece becomes a dictionary saved in `pieces.json`, with a stage |
| 4 | [Modules and tests](milestones/04-modules-and-tests.md) | Module 7 | The code is split into a package, with errors handled and tests |
| 5 | [The Piece class](milestones/05-piece-class.md) | Module 8 | A `Piece` object that knows its stage history |
| 6 | [SQLite](milestones/06-sqlite.md) | Module 9 | Data moves from JSON into a real database |
| 7 | [A web API](milestones/07-web-api.md) | Module 10 | A Flask API and a web page made with HTML, CSS and JavaScript |
| 8 | [Suggestions](milestones/08-suggestions.md) | Module 11 | Rule-based suggestions, then AI suggestions |

## The finished app, folder by folder

This is where you will be at the end. Do not create it now: it grows one milestone at a time.

```text
atanor/
├── README.md              # what the app is and how to run it
├── pyproject.toml         # project info and libraries (flask, anthropic; pytest and ruff for development)
├── uv.lock                # exact library versions, written by uv
├── .gitignore             # files Git must ignore (database, virtual environment...)
├── main.py                # the terminal menu (milestone 4)
├── app.py                 # the web server (milestone 7)
├── atanor/                # the package with the real logic
│   ├── __init__.py
│   ├── piece.py           # the Piece class (milestone 5)
│   ├── storage.py         # saving and loading (JSON, then SQLite)
│   └── suggestions.py     # rules and AI (milestone 8)
├── static/
│   ├── index.html         # the page you open in the browser
│   ├── style.css
│   └── app.js
└── tests/
    ├── test_piece.py
    └── test_suggestions.py
```

## How to work

1. **One milestone at a time.** Read the whole guide before writing code.
2. **Try each step before opening the answer.** The answers are hidden on purpose. Being stuck for 10 minutes is part of learning. Being stuck for an hour is a sign to ask for help.
3. **Run your program after every step.** Small steps make errors easy to find.
4. **From milestone 2 on, everything lives in your own GitHub repository.** At the end of each milestone, make a commit. Your commit history becomes a diary of everything you learned.
5. **Stretch goals are optional.** Do them if you have energy. Skip them if not.

**Start here:** [Milestone 1: A text file](milestones/01-text-file.md)
