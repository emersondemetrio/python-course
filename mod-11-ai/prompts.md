# Prompts

> **In one sentence:** A **prompt** is the text you send to the model, and the clearer and more complete it is (task, context, data, format), the more useful and predictable the answer.

## Why it matters

The same model can give a vague, useless answer or a precise, ready-to-use one. The difference is almost always the prompt. And when the answer goes into a **program** (not just a person reading it), you also need it in a format your code can read, like JSON.

This file also answers an important question: when should you **not** use AI at all?

## Analogy

Imagine asking a new assistant at work to "organize the event". You will get something, but probably not what you wanted. Now imagine you say: "Organize a dinner for 12 people next Friday at 8pm, budget 600, two guests are vegetarian, send me three restaurant options as a list with name, price per person and address." Same assistant, much better result.

The model is that new assistant: very capable, knows nothing about your situation, and does exactly what the words say.

## The idea, step by step

### The parts of a good prompt

A good prompt usually has:

1. **The task:** what you want, as a clear instruction. "Suggest three dinners", not "dinner ideas?".
2. **Context:** who it is for and why. "For a family with two small kids, on a weekday."
3. **The data:** the facts the model needs, which it cannot know. "We have: rice, eggs, spinach, tomatoes."
4. **Constraints:** limits. "Ready in 30 minutes. No nuts."
5. **The format:** exactly how the answer should look. "A numbered list, one line each, with the name and the time."

Compare:

```text
Weak:   Give me dinner ideas.

Strong: Suggest 3 dinners for a family with two small kids, on a weekday.
        Ingredients we have: rice, eggs, spinach, tomatoes.
        Each must be ready in 30 minutes and contain no nuts.
        Answer as a numbered list, one line each: dish name, then the time in minutes.
```

### Building prompts with functions

In a program, the data changes every time, but the structure of the prompt does not. So you write a **function that builds the prompt** from your data. This is the part you can test without spending anything:

```python
def build_dinner_prompt(ingredients, people, minutes):
    ingredient_list = ", ".join(ingredients)
    return (
        f"Suggest 3 dinners for {people} people.\n"
        f"Ingredients available: {ingredient_list}.\n"
        f"Each must be ready in at most {minutes} minutes.\n"
        "Answer as a numbered list, one line each: dish name, then the time in minutes."
    )

print(build_dinner_prompt(["rice", "eggs", "spinach"], 4, 30))
```

Output:

```text
Suggest 3 dinners for 4 people.
Ingredients available: rice, eggs, spinach.
Each must be ready in at most 30 minutes.
Answer as a numbered list, one line each: dish name, then the time in minutes.
```

Then you send it with the `ask()` function from the previous file:

<!-- no-verify -->
```python
prompt = build_dinner_prompt(["rice", "eggs", "spinach"], 4, 30)
print(ask(prompt))
```

### Examples inside the prompt

When the format or tone is hard to describe, **show** one or two examples. Models are very good at copying a pattern:

```text
Write a short, friendly reminder for each task. Follow the style of the examples.

Task: water the plants
Reminder: Your green friends are thirsty! A little water today keeps them happy.

Task: pay the electricity bill
Reminder: Quick one: the electricity bill is waiting. Two minutes and it's done!

Task: call the dentist
Reminder:
```

### Asking for JSON

A numbered list is fine for a person. For a program, you want **JSON**: then `json.loads` turns the answer into a list or dictionary (module 6), and your code can loop over it, save it in a database, or send it to a web page.

To get JSON reliably:

- Say clearly that you want **only** JSON, no extra text.
- Describe the exact shape, ideally with an example.

```python
def build_json_prompt(ingredients):
    return (
        "Suggest 2 dinners using these ingredients: " + ", ".join(ingredients) + ".\n"
        "Answer ONLY with JSON, no other text, in exactly this shape:\n"
        '[{"dish": "name", "minutes": 20}]'
    )

print(build_json_prompt(["rice", "eggs"]))
```

Output:

```text
Suggest 2 dinners using these ingredients: rice, eggs.
Answer ONLY with JSON, no other text, in exactly this shape:
[{"dish": "name", "minutes": 20}]
```

A typical answer would be:

```text
[{"dish": "Egg fried rice", "minutes": 20}, {"dish": "Rice omelette", "minutes": 15}]
```

### Reading the JSON safely

Even with clear instructions, the model sometimes adds things: a sentence before the JSON, or wraps it in Markdown code fences (three backticks and the word `json`). Sometimes the JSON is simply broken. Your program must not crash because of that.

So you write a careful parsing function: remove the fences if they exist, try `json.loads`, and return `None` if it fails (the same pattern as in module 7):

```python
import json

FENCE = "`" * 3  # three backticks, written this way so this page displays correctly


def parse_json_answer(text):
    text = text.strip()
    if text.startswith(FENCE):
        text = text.removeprefix(FENCE + "json").removeprefix(FENCE)
        text = text.removesuffix(FENCE).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


clean = '[{"dish": "Egg fried rice", "minutes": 20}]'
fenced = FENCE + 'json\n[{"dish": "Rice omelette", "minutes": 15}]\n' + FENCE
broken = "Sure! Here are some ideas: egg fried rice and omelette."

print(parse_json_answer(clean))
print(parse_json_answer(fenced))
print(parse_json_answer(broken))
```

Output:

```text
[{'dish': 'Egg fried rice', 'minutes': 20}]
[{'dish': 'Rice omelette', 'minutes': 15}]
None
```

After parsing, also check the **shape**: is it a list? Does each item have the keys you need? Never assume.

```python
def valid_dinners(data):
    if not isinstance(data, list):
        return []
    result = []
    for item in data:
        if isinstance(item, dict) and "dish" in item and "minutes" in item:
            result.append(item)
    return result

print(valid_dinners([{"dish": "Soup", "minutes": 25}, {"name": "oops"}]))
print(valid_dinners("not a list"))
```

Output:

```text
[{'dish': 'Soup', 'minutes': 25}]
[]
```

`isinstance(value, list)` checks the type of a value: it returns `True` if `value` is a list.

### Rules first, AI second

Before using a model for a feature, ask: **can a few `if`s do it?** If yes, use the `if`s. Rules are:

- **Exact:** the same input always gives the same output.
- **Free and instant:** no API call.
- **Easy to test** (module 7) and easy to explain.

The model shines where rules are hard to write: creative text, ideas, understanding messy language, combining many small facts into a suggestion.

A strong pattern is to use **both**: rules find the facts, the model turns them into friendly, creative advice.

### Worked example: what should I do next?

Let's build a small "next step" helper for houseplants, with the data in a SQLite database (module 9). Each plant has a name, how many days since it was last watered, and how often it needs water.

**Step 1: the data.** We use an in-memory database so the example runs anywhere:

```python
import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute(
    "CREATE TABLE plants (name TEXT, days_since_water INTEGER, water_every_days INTEGER, location TEXT)"
)
connection.executemany(
    "INSERT INTO plants VALUES (?, ?, ?, ?)",
    [
        ("Basil", 3, 2, "kitchen window"),
        ("Cactus", 10, 21, "living room"),
        ("Fern", 6, 4, "bathroom"),
        ("Snake plant", 5, 14, "bedroom"),
    ],
)

rows = connection.execute("SELECT name, days_since_water, water_every_days, location FROM plants").fetchall()
plants = [
    {"name": r[0], "days_since_water": r[1], "water_every_days": r[2], "location": r[3]}
    for r in rows
]
print(len(plants), "plants loaded")
```

Output:

```text
4 plants loaded
```

**Step 2: rules.** Which plants need water? This is a simple comparison, so no AI:

<!-- no-verify -->
```python
def needs_water(plant):
    return plant["days_since_water"] >= plant["water_every_days"]

def rule_suggestions(plants):
    suggestions = []
    for plant in plants:
        if needs_water(plant):
            late = plant["days_since_water"] - plant["water_every_days"]
            suggestions.append(f"Water the {plant['name']} ({late} day(s) late).")
    return suggestions

for suggestion in rule_suggestions(plants):
    print(suggestion)
```

Here is the whole thing together, verified:

```python
plants = [
    {"name": "Basil", "days_since_water": 3, "water_every_days": 2, "location": "kitchen window"},
    {"name": "Cactus", "days_since_water": 10, "water_every_days": 21, "location": "living room"},
    {"name": "Fern", "days_since_water": 6, "water_every_days": 4, "location": "bathroom"},
    {"name": "Snake plant", "days_since_water": 5, "water_every_days": 14, "location": "bedroom"},
]

def needs_water(plant):
    return plant["days_since_water"] >= plant["water_every_days"]

def rule_suggestions(plants):
    suggestions = []
    for plant in plants:
        if needs_water(plant):
            late = plant["days_since_water"] - plant["water_every_days"]
            suggestions.append(f"Water the {plant['name']} ({late} day(s) late).")
    return suggestions

for suggestion in rule_suggestions(plants):
    print(suggestion)
```

Output:

```text
Water the Basil (1 day(s) late).
Water the Fern (2 day(s) late).
```

These suggestions are always correct and cost nothing. Notice that the rules could not tell you, for example, that the fern might like more humidity, or a nice idea for the empty corner of the living room. That is where the model helps.

**Step 3: the prompt, built from the data.** We send the model the facts (including what the rules found) and ask for creative suggestions in JSON:

```python
import json

def build_plant_prompt(plants, rule_results):
    lines = []
    for plant in plants:
        lines.append(
            f"- {plant['name']}: in the {plant['location']}, "
            f"last watered {plant['days_since_water']} days ago, "
            f"needs water every {plant['water_every_days']} days"
        )
    plant_text = "\n".join(lines)
    already = "\n".join("- " + r for r in rule_results) or "- nothing"

    return (
        "You help a beginner take care of houseplants.\n\n"
        f"These are their plants:\n{plant_text}\n\n"
        f"Our app already told them:\n{already}\n\n"
        "Suggest 2 other useful things they could do this week. Do not repeat the watering advice.\n"
        "Answer ONLY with JSON, no other text, in this shape:\n"
        + json.dumps([{"plant": "name", "suggestion": "one short sentence"}])
    )

plants = [
    {"name": "Basil", "days_since_water": 3, "water_every_days": 2, "location": "kitchen window"},
    {"name": "Fern", "days_since_water": 6, "water_every_days": 4, "location": "bathroom"},
]
rules = ["Water the Basil (1 day(s) late).", "Water the Fern (2 day(s) late)."]
print(build_plant_prompt(plants, rules))
```

Output:

```text
You help a beginner take care of houseplants.

These are their plants:
- Basil: in the kitchen window, last watered 3 days ago, needs water every 2 days
- Fern: in the bathroom, last watered 6 days ago, needs water every 4 days

Our app already told them:
- Water the Basil (1 day(s) late).
- Water the Fern (2 day(s) late).

Suggest 2 other useful things they could do this week. Do not repeat the watering advice.
Answer ONLY with JSON, no other text, in this shape:
[{"plant": "name", "suggestion": "one short sentence"}]
```

Look at the prompt before sending it. If it would confuse a person, it will probably confuse the model.

**Step 4: call, parse, combine.**

<!-- no-verify -->
```python
prompt = build_plant_prompt(plants, rule_suggestions(plants))
answer = ask(prompt)

ai_suggestions = parse_json_answer(answer) if answer else None
if not ai_suggestions:
    ai_suggestions = []  # the app still works without AI

print("Do this today:")
for suggestion in rule_suggestions(plants):
    print(" -", suggestion)

print("Ideas for this week:")
for item in ai_suggestions:
    print(f" - {item['plant']}: {item['suggestion']}")
```

```console
PS C:\Users\you\Projects\ai> uv run plants.py
Do this today:
 - Water the Basil (1 day(s) late).
 - Water the Fern (2 day(s) late).
Ideas for this week:
 - Basil: Pinch off the top leaves to make it grow bushier.
 - Fern: Mist the leaves, since ferns love humidity.
```

Notice the design: the important, factual part (watering) comes from rules and **always works**. The AI part is a bonus: if the API is down, the key is missing or the JSON is broken, the program still shows the rule-based suggestions. This is how you will build the suggestions in the final project.

## Common mistakes

### Vague prompts

"Help me with my plants" gets a generic article about plants. Say what you want, give your data, and ask for a format.

### Trusting the JSON blindly

<!-- error -->
```python
import json

answer = "Here you go: [{\"dish\": \"Soup\"}]"
dinners = json.loads(answer)
```

```text
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

The model added a sentence before the JSON. Always parse with a function like `parse_json_answer` that returns `None` instead of crashing, and have a plan for when it does.

### Sending more data than needed

Sending your whole database in every prompt costs more, is slower, and may leak private information. Send only the fields the model needs for this task.

### Using AI where a rule works

If the answer can be calculated (dates, totals, thresholds, sorting), calculate it in Python. Use the model for what code cannot do well.

## Exercises

### Predict the output

#### Exercise 1: What the model will see

What does this print?

<!-- no-verify -->
```python
def build_prompt(book, pages_left):
    return f"I am reading '{book}' and have {pages_left} pages left. Suggest a reading plan for {pages_left // 20} days."

print(build_prompt("Dune", 120))
```

<details>
<summary>Show answer</summary>

```python
def build_prompt(book, pages_left):
    return f"I am reading '{book}' and have {pages_left} pages left. Suggest a reading plan for {pages_left // 20} days."

print(build_prompt("Dune", 120))
```

Output:

```text
I am reading 'Dune' and have 120 pages left. Suggest a reading plan for 6 days.
```

`120 // 20` is `6`. The math was done by Python before the prompt was sent, not by the model.

</details>

### Fix the bug

#### Exercise 2: The crashing parser

This program crashes whenever the model answers with anything other than perfect JSON. Make `read_tags` return an empty list instead of crashing.

<!-- no-verify -->
```python
import json

def read_tags(answer):
    return json.loads(answer)

print(read_tags('["cozy", "quick"]'))
print(read_tags("Tags: cozy, quick"))
```

<details>
<summary>Show answer</summary>

```python
import json

def read_tags(answer):
    try:
        data = json.loads(answer)
    except json.JSONDecodeError:
        return []
    if not isinstance(data, list):
        return []
    return data

print(read_tags('["cozy", "quick"]'))
print(read_tags("Tags: cozy, quick"))
```

Output:

```text
['cozy', 'quick']
[]
```

Catching the error handles broken text; checking `isinstance` handles valid JSON with the wrong shape (like a dictionary).

</details>

### Write it

#### Exercise 3: Improve the prompt

Rewrite this prompt so the answer is useful for a program. The program needs, for a list of 3 book titles, a list of objects with the title and a one-sentence summary.

```text
Tell me about some books.
```

<details>
<summary>Show answer</summary>

```text
Write a one-sentence summary for each of these books:
- Dune
- The Little Prince
- Pride and Prejudice

Answer ONLY with JSON, no other text, in exactly this shape:
[{"title": "book title", "summary": "one sentence"}]
```

It now has a clear task, the data (the titles), a constraint (one sentence) and an exact format.

</details>

#### Exercise 4: Build a prompt from data

Write a function `build_shopping_prompt(items)` that receives a list of dictionaries like `{"name": "milk", "days_left": 2}` and returns a prompt asking for 2 recipe ideas that use the items expiring soonest (2 days or less). Use the rules to pick the items **before** building the prompt. Ask for JSON with `recipe` and `uses`.

<details>
<summary>Hint</summary>

First make a list of names with `days_left <= 2`. Then join them with `", "` and put them in an f-string.

</details>

<details>
<summary>Show answer</summary>

```python
import json

def build_shopping_prompt(items):
    soon = [item["name"] for item in items if item["days_left"] <= 2]
    return (
        "Suggest 2 simple recipes that use these ingredients before they spoil: "
        + ", ".join(soon) + ".\n"
        "Answer ONLY with JSON, no other text, in this shape:\n"
        + json.dumps([{"recipe": "name", "uses": ["ingredient"]}])
    )

fridge = [
    {"name": "milk", "days_left": 2},
    {"name": "cheese", "days_left": 10},
    {"name": "spinach", "days_left": 1},
]
print(build_shopping_prompt(fridge))
```

Output:

```text
Suggest 2 simple recipes that use these ingredients before they spoil: milk, spinach.
Answer ONLY with JSON, no other text, in this shape:
[{"recipe": "name", "uses": ["ingredient"]}]
```

The rule (days left) decided **which** items matter; the model will only do the creative part.

</details>

#### Exercise 5: Rules and AI together

Write `next_steps(tasks, ai_answer)` where `tasks` is a list like `{"title": "Pay rent", "days_overdue": 3}` and `ai_answer` is the raw text the model returned (or `None`). It returns a list of strings: first one line per overdue task (rules), then the AI ideas if `ai_answer` is valid JSON (a list of strings), otherwise nothing extra. Test it with a valid answer and with `None`.

<details>
<summary>Show answer</summary>

```python
import json

def next_steps(tasks, ai_answer):
    steps = []
    for task in tasks:
        if task["days_overdue"] > 0:
            steps.append(f"Overdue: {task['title']} ({task['days_overdue']} days)")

    if ai_answer:
        try:
            ideas = json.loads(ai_answer)
        except json.JSONDecodeError:
            ideas = []
        if isinstance(ideas, list):
            for idea in ideas:
                steps.append(f"Idea: {idea}")
    return steps

tasks = [
    {"title": "Pay rent", "days_overdue": 3},
    {"title": "Read a chapter", "days_overdue": 0},
]
print(next_steps(tasks, '["Set up automatic rent payment"]'))
print(next_steps(tasks, None))
```

Output:

```text
['Overdue: Pay rent (3 days)', 'Idea: Set up automatic rent payment']
['Overdue: Pay rent (3 days)']
```

Even with no AI answer, the user still gets the most important information.

</details>

## Review

#### Review 1: Reading rows from SQLite (module 9)

Create an in-memory table `books (title TEXT, pages INTEGER)`, insert two books, and print the titles of books with more than 300 pages, using a `WHERE` clause.

<details>
<summary>Show answer</summary>

```python
import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE books (title TEXT, pages INTEGER)")
connection.executemany(
    "INSERT INTO books VALUES (?, ?)",
    [("The Little Prince", 96), ("Dune", 412)],
)

for (title,) in connection.execute("SELECT title FROM books WHERE pages > ?", (300,)):
    print(title)
```

Output:

```text
Dune
```

</details>

#### Review 2: A route that returns suggestions (module 10)

Write a Flask route `GET /suggestions` that returns, as JSON, the result of `rule_suggestions(plants)` from this file.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/suggestions")
def suggestions():
    return jsonify(rule_suggestions(plants))
```

With this, your web page can show the suggestions with `fetch("/suggestions")`. Database, API and AI: that is the full shape of the final project.

</details>

## Recap

- A good prompt has a task, context, the data, constraints and an exact format.
- Build prompts with functions from your data, and print them to check before sending.
- When a program needs the answer, ask for **only JSON** with an example shape, and parse it with a function that returns `None` instead of crashing.
- Use rules for facts and calculations, and the model for creative or language tasks. Combining both is often best.
- Design so the app still works when the AI part fails.

**Next:** [The final project](../mod-final-project/README.md)
