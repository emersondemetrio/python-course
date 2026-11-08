# Teacher's guide: Module 11, AI
# Every example and exercise answer from this module's lessons, in order.
# Run it from this folder:  python guide.py
#
# Calls to the Anthropic API are only shown as comments (they need the
# library, a key and the internet). Everything else runs for real.

import json
import os
import sqlite3

print("=" * 50)
print("LESSON: what-is-an-llm.md")

print("\n--- Example: predicting the next word (a tiny model)")
# The point: a real LLM does this, at a gigantic scale, with pieces of text.
text = "the cat sat on the mat the cat ate the fish the cat sat on the sofa"
words = text.split()

next_words = {}
for i in range(len(words) - 1):
    current = words[i]
    following = words[i + 1]
    if current not in next_words:
        next_words[current] = {}
    next_words[current][following] = next_words[current].get(following, 0) + 1

print(next_words["the"])
print(next_words["cat"])


def most_likely_after(word):
    options = next_words[word]
    return max(options, key=options.get)


sentence = ["the"]
for _ in range(4):
    sentence.append(most_likely_after(sentence[-1]))
print(" ".join(sentence))

print("\n--- Example: estimating tokens")
# Rule of thumb: about 4 characters per token in English.


def estimate_tokens(text):
    return round(len(text) / 4)


prompt = "Suggest three easy dinner recipes using rice, eggs and spinach."
print(len(prompt), "characters")
print("About", estimate_tokens(prompt), "tokens")

print("\n--- Example: what a call costs")
price_input_per_million = 1.00  # dollars
price_output_per_million = 5.00  # dollars

input_tokens = 800
output_tokens = 300

cost = (input_tokens / 1_000_000) * price_input_per_million + (
    output_tokens / 1_000_000
) * price_output_per_million
print(f"One call: ${cost:.4f}")
print(f"1000 calls: ${cost * 1000:.2f}")

print("\n--- Mistake: asking the model to do math your program can do")
# prompt = "What is the total of 1847.35 + 922.10 + 3310.75?"
# Python does it exactly and for free:
print(round(1847.35 + 922.10 + 3310.75, 2))

print("\n--- Exercise 1: counting next words")
# Ask her to predict before running.
words = "I like tea I like coffee I love tea".split()

after_i = {}
for i in range(len(words) - 1):
    if words[i] == "I":
        nxt = words[i + 1]
        after_i[nxt] = after_i.get(nxt, 0) + 1

print(after_i)

print("\n--- Exercise 2: the wrong job for AI")
# Broken idea:
# prompt = "An order has 3 items at 12.50 each. Is the total above 30? Answer yes or no."
# answer = ask_llm(prompt)
quantity = 3
price = 12.50
total = quantity * price

if total > 30:
    print(f"Yes, the total is {total}")
else:
    print(f"No, the total is {total}")

print("\n--- Exercise 3: cost calculator")


def call_cost(input_tokens, output_tokens, input_price, output_price):
    return input_tokens / 1_000_000 * input_price + output_tokens / 1_000_000 * output_price


cost = call_cost(2000, 500, 1.00, 5.00)
print(f"${cost:.4f}")

print("\n--- Exercise 4: rules or AI?")
# Ask her to decide each one and give a reason before you show this.
answers = [
    ("Warn when a plant has not been watered for 7+ days", "Rules: fixed date comparison"),
    ("Write a friendly birthday message", "LLM: creative, varied text"),
    ("Calculate the total of a shopping list", "Rules: it is math"),
    ("Turn a messy note into a calendar event", "LLM: messy language into structure"),
    ("Sort books by publication year", "Rules: sorted() does it perfectly"),
]
for feature, answer in answers:
    print(f"{feature} -> {answer}")

print("\n--- Review 1: most common item (module 6)")


def most_common(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return max(counts, key=counts.get)


print(most_common(["tea", "coffee", "tea", "water", "tea"]))

print("\n--- Review 2: formatting money (module 1)")
total = 6.5
print(f"Total: ${total:.2f}")


print("\n" + "=" * 50)
print("LESSON: calling-an-llm.md")

print("\n--- Example: never put the key in your code")
# # NEVER do this
# client = anthropic.Anthropic(api_key="sk-ant-abc123...")

print("\n--- Example: setting an environment variable in the terminal")
# Windows PowerShell, only this window:
#   $env:ANTHROPIC_API_KEY = "sk-ant-your-key-here"
# Windows, permanent (open a NEW terminal after):
#   setx ANTHROPIC_API_KEY "sk-ant-your-key-here"
# macOS / Linux:
#   export ANTHROPIC_API_KEY="sk-ant-your-key-here"

print("\n--- Example: reading environment variables")
os.environ["COFFEE_SIZE"] = "large"  # here we set it in code, only to demonstrate

print(os.environ.get("COFFEE_SIZE"))
print(os.environ.get("TEA_SIZE"))
print(os.environ.get("TEA_SIZE", "medium"))

print("\n--- Example: stop early if the key is missing")
# import os
# import sys
#
# if not os.environ.get("ANTHROPIC_API_KEY"):
#     print("Missing ANTHROPIC_API_KEY. Set it in your terminal or in a .env file.")
#     sys.exit(1)

print("\n--- Example: a .env file")
# .env contents:
#   ANTHROPIC_API_KEY=sk-ant-your-key-here
# Install:  uv add python-dotenv
# In the code:
#   from dotenv import load_dotenv
#   load_dotenv()  # reads .env and sets the environment variables
# .gitignore must have:  .venv/  __pycache__/  .env
# .env.example (committed, fake value):
#   ANTHROPIC_API_KEY=put-your-key-here

print("\n--- Example: your first call (needs anthropic, a key and internet)")
# Install:  uv add anthropic
#
# import anthropic
# from dotenv import load_dotenv
#
# load_dotenv()
# client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment
#
# message = client.messages.create(
#     model="claude-haiku-5-5",
#     max_tokens=500,
#     messages=[
#         {
#             "role": "user",
#             "content": "Suggest three easy dinners with rice, eggs and spinach. One line each.",
#         }
#     ],
# )
#
# print(message.content[0].text)
#
# Run:  uv run first_call.py

print("\n--- Example: what came back")
# print(message.stop_reason)          # "end_turn" if it finished, "max_tokens" if it was cut
# print(message.usage.input_tokens)   # how many tokens you sent
# print(message.usage.output_tokens)  # how many tokens it wrote

print("\n--- Example: a system prompt")
# message = client.messages.create(
#     model="claude-haiku-5-5",
#     max_tokens=300,
#     system="You are a friendly cooking assistant. Answer in at most three short sentences. "
#            "Only suggest vegetarian dishes.",
#     messages=[{"role": "user", "content": "What can I make with potatoes?"}],
# )
# print(message.content[0].text)

print("\n--- Example: conversations, sending the history")
# The model does not remember: you send the whole conversation every time.
# history = [
#     {"role": "user", "content": "Suggest a name for a small coffee shop."},
#     {"role": "assistant", "content": "How about 'The Daily Grind'?"},
#     {"role": "user", "content": "Nice! Now a slogan for it."},
# ]
# message = client.messages.create(model="claude-haiku-5-5", max_tokens=200, messages=history)
# print(message.content[0].text)

print("\n--- Example: wrapping it in a function")
# import anthropic
# from dotenv import load_dotenv
#
# load_dotenv()
# client = anthropic.Anthropic(timeout=30.0)
#
# def ask(question, system="You are a helpful assistant. Be brief."):
#     try:
#         message = client.messages.create(
#             model="claude-haiku-5-5",
#             max_tokens=500,
#             system=system,
#             messages=[{"role": "user", "content": question}],
#         )
#         return message.content[0].text
#     except anthropic.AuthenticationError:
#         print("Your API key is missing or wrong.")
#     except anthropic.RateLimitError:
#         print("Too many requests. Wait a little and try again.")
#     except anthropic.APITimeoutError:
#         print("The model took too long to answer.")
#     except anthropic.APIConnectionError:
#         print("Could not reach the API. Are you online?")
#     except anthropic.APIStatusError as error:
#         print(f"The API returned an error: {error.status_code}")
#     return None
#
# answer = ask("Give me one tip to keep houseplants healthy.")
# if answer:
#     print(answer)

print("\n--- Mistake: AuthenticationError")
# anthropic.AuthenticationError: Error code: 401 - ... 'invalid x-api-key'
# Fix: check the key in .env, and that load_dotenv() runs before Anthropic().

print("\n--- Mistake: calling the model inside a big loop")
# for product in all_10000_products:
#     ask(f"Write a description for {product}")
# 10000 calls = 10000 times the cost. Test with 3 first.

print("\n--- Exercise 1: reading the environment")
# Ask her to predict before running.
os.environ["CITY"] = "Lisbon"
print(os.environ.get("CITY", "unknown"))
print(os.environ.get("PLANT_API_KEY", "missing"))

print("\n--- Exercise 2: three problems")
# Broken: key in the code, no max_tokens, prints the whole content list.
# client = anthropic.Anthropic(api_key="sk-ant-abc123secret")
# message = client.messages.create(
#     model="claude-haiku-5-5",
#     messages=[{"role": "user", "content": "Write a haiku about rain."}],
# )
# print(message.content)
#
# Fixed:
# load_dotenv()
# client = anthropic.Anthropic()
# message = client.messages.create(
#     model="claude-haiku-5-5",
#     max_tokens=200,
#     messages=[{"role": "user", "content": "Write a haiku about rain."}],
# )
# print(message.content[0].text)

print("\n--- Exercise 3: building the messages list")


def build_messages(history, new_question):
    messages = []
    for question, answer in history:
        messages.append({"role": "user", "content": question})
        messages.append({"role": "assistant", "content": answer})
    messages.append({"role": "user", "content": new_question})
    return messages


history = [("Name a calm color.", "Sage green.")]
for message in build_messages(history, "And an energetic one?"):
    print(message)

print("\n--- Exercise 4: your own assistant (needs anthropic and a key)")
# import os
# import sys
#
# import anthropic
# from dotenv import load_dotenv
#
# load_dotenv()
# if not os.environ.get("ANTHROPIC_API_KEY"):
#     print("Missing ANTHROPIC_API_KEY. Create a .env file with your key.")
#     sys.exit(1)
#
# client = anthropic.Anthropic(timeout=30.0)
#
# question = input("Ask me something: ")
# message = client.messages.create(
#     model="claude-haiku-5-5",
#     max_tokens=400,
#     system="You are a patient tutor. Explain things simply, in at most five sentences.",
#     messages=[{"role": "user", "content": question}],
# )
#
# print()
# print(message.content[0].text)
# print()
# print(f"Tokens: {message.usage.input_tokens} in, {message.usage.output_tokens} out")
#
# Run:  uv run assistant.py

print("\n--- Review 1: .gitignore check (module 5)")
print("Ignore: .env (secret key), .venv/ (recreate with uv sync), __pycache__/")
print("Commit: app.py, .env.example, pyproject.toml, uv.lock")

print("\n--- Review 2: a function that returns None on failure (modules 3 and 7)")


def to_number(text):
    try:
        return float(text)
    except ValueError:
        return None


print(to_number("3.5"))
print(to_number("three"))


print("\n" + "=" * 50)
print("LESSON: prompts.md")

print("\n--- Example: a weak prompt and a strong prompt")
weak = "Give me dinner ideas."
strong = (
    "Suggest 3 dinners for a family with two small kids, on a weekday.\n"
    "Ingredients we have: rice, eggs, spinach, tomatoes.\n"
    "Each must be ready in 30 minutes and contain no nuts.\n"
    "Answer as a numbered list, one line each: dish name, then the time in minutes."
)
print("Weak:", weak)
print("Strong:")
print(strong)

print("\n--- Example: building prompts with functions")


def build_dinner_prompt(ingredients, people, minutes):
    ingredient_list = ", ".join(ingredients)
    return (
        f"Suggest 3 dinners for {people} people.\n"
        f"Ingredients available: {ingredient_list}.\n"
        f"Each must be ready in at most {minutes} minutes.\n"
        "Answer as a numbered list, one line each: dish name, then the time in minutes."
    )


print(build_dinner_prompt(["rice", "eggs", "spinach"], 4, 30))
# Then, with the ask() function from the last lesson:
# prompt = build_dinner_prompt(["rice", "eggs", "spinach"], 4, 30)
# print(ask(prompt))

print("\n--- Example: examples inside the prompt")
few_shot = (
    "Write a short, friendly reminder for each task. Follow the style of the examples.\n\n"
    "Task: water the plants\n"
    "Reminder: Your green friends are thirsty! A little water today keeps them happy.\n\n"
    "Task: pay the electricity bill\n"
    "Reminder: Quick one: the electricity bill is waiting. Two minutes and it's done!\n\n"
    "Task: call the dentist\n"
    "Reminder:"
)
print(few_shot)

print("\n--- Example: asking for JSON")


def build_json_prompt(ingredients):
    return (
        "Suggest 2 dinners using these ingredients: " + ", ".join(ingredients) + ".\n"
        "Answer ONLY with JSON, no other text, in exactly this shape:\n"
        '[{"dish": "name", "minutes": 20}]'
    )


print(build_json_prompt(["rice", "eggs"]))
# A typical answer:
# [{"dish": "Egg fried rice", "minutes": 20}, {"dish": "Rice omelette", "minutes": 15}]

print("\n--- Example: reading the JSON safely")
FENCE = "`" * 3  # three backticks


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

print("\n--- Example: checking the shape of the data")


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

print("\n--- Worked example: loading plants from SQLite")
connection = sqlite3.connect(":memory:")
connection.execute(
    "CREATE TABLE plants (name TEXT, days_since_water INTEGER,"
    " water_every_days INTEGER, location TEXT)"
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

rows = connection.execute(
    "SELECT name, days_since_water, water_every_days, location FROM plants"
).fetchall()
plants = [
    {"name": r[0], "days_since_water": r[1], "water_every_days": r[2], "location": r[3]}
    for r in rows
]
print(len(plants), "plants loaded")
connection.close()

print("\n--- Worked example: rules first")


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

print("\n--- Worked example: building the prompt from the data")


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
        "Suggest 2 other useful things they could do this week. "
        "Do not repeat the watering advice.\n"
        "Answer ONLY with JSON, no other text, in this shape:\n"
        + json.dumps([{"plant": "name", "suggestion": "one short sentence"}])
    )


plants = [
    {"name": "Basil", "days_since_water": 3, "water_every_days": 2, "location": "kitchen window"},
    {"name": "Fern", "days_since_water": 6, "water_every_days": 4, "location": "bathroom"},
]
rules = ["Water the Basil (1 day(s) late).", "Water the Fern (2 day(s) late)."]
print(build_plant_prompt(plants, rules))

print("\n--- Worked example: putting it together (the AI part needs a key)")
# prompt = build_plant_prompt(plants, rule_suggestions(plants))
# answer = ask(prompt)
# Here we pretend the model answered, so the rest runs:
answer = (
    '[{"plant": "Basil", "suggestion": "Pinch off the top leaves to make it grow bushier."},'
    ' {"plant": "Fern", "suggestion": "Mist the leaves, since ferns love humidity."}]'
)

ai_suggestions = parse_json_answer(answer) if answer else None
if not ai_suggestions:
    ai_suggestions = []  # the app still works without AI

print("Do this today:")
for suggestion in rule_suggestions(plants):
    print(" -", suggestion)

print("Ideas for this week:")
for item in ai_suggestions:
    print(f" - {item['plant']}: {item['suggestion']}")

print("\n--- Mistake: trusting the JSON blindly")
# answer = "Here you go: [{\"dish\": \"Soup\"}]"
# dinners = json.loads(answer)
# json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
answer = 'Here you go: [{"dish": "Soup"}]'
print(parse_json_answer(answer))

print("\n--- Exercise 1: what the model will see")
# Ask her to predict before running. 120 // 20 is 6.


def build_prompt(book, pages_left):
    return (
        f"I am reading '{book}' and have {pages_left} pages left. "
        f"Suggest a reading plan for {pages_left // 20} days."
    )


print(build_prompt("Dune", 120))

print("\n--- Exercise 2: the crashing parser")
# Broken version crashes on the second call:
# def read_tags(answer):
#     return json.loads(answer)
# print(read_tags("Tags: cozy, quick"))
# json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)


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

print("\n--- Exercise 3: improve the prompt")
# Weak:  Tell me about some books.
better = (
    "Write a one-sentence summary for each of these books:\n"
    "- Dune\n"
    "- The Little Prince\n"
    "- Pride and Prejudice\n\n"
    "Answer ONLY with JSON, no other text, in exactly this shape:\n"
    '[{"title": "book title", "summary": "one sentence"}]'
)
print(better)

print("\n--- Exercise 4: build a prompt from data")


def build_shopping_prompt(items):
    soon = [item["name"] for item in items if item["days_left"] <= 2]
    return (
        "Suggest 2 simple recipes that use these ingredients before they spoil: "
        + ", ".join(soon)
        + ".\n"
        "Answer ONLY with JSON, no other text, in this shape:\n"
        + json.dumps([{"recipe": "name", "uses": ["ingredient"]}])
    )


fridge = [
    {"name": "milk", "days_left": 2},
    {"name": "cheese", "days_left": 10},
    {"name": "spinach", "days_left": 1},
]
print(build_shopping_prompt(fridge))

print("\n--- Exercise 5: rules and AI together")


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

print("\n--- Review 1: reading rows from SQLite (module 9)")
connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE books (title TEXT, pages INTEGER)")
connection.executemany(
    "INSERT INTO books VALUES (?, ?)",
    [("The Little Prince", 96), ("Dune", 412)],
)

for (title,) in connection.execute("SELECT title FROM books WHERE pages > ?", (300,)):
    print(title)
connection.close()

print("\n--- Review 2: a route that returns suggestions (module 10, needs Flask)")
# from flask import Flask, jsonify
#
# app = Flask(__name__)
#
# @app.route("/suggestions")
# def suggestions():
#     return jsonify(rule_suggestions(plants))
