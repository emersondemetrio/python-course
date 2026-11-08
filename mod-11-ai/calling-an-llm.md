# Calling an LLM

> **In one sentence:** To use an LLM from Python, you install the provider's library, give it your secret API key through an environment variable, send a list of messages, and read the text that comes back.

## Why it matters

Chat apps are great for people. But when your **program** needs the model (to write a suggestion, summarize a note, turn text into data), it has to call the model's API directly. This file shows you how, and how to do it safely so your secret key never ends up on GitHub.

## Analogy

The API key is like the key card to an office building that charges you for every visit. If you leave the card on a public bench (or in a public repository), anyone can use it, and you get the bill. So you keep it in your pocket (an environment variable) and only show it at the door (the API call).

The call itself is like sending a letter to a very fast writer: you write who they should be ("you are a helpful cooking assistant"), what you need, and how long the answer can be. A few seconds later, a letter comes back.

## The idea, step by step

### Getting an API key

You need an account with an AI provider. In this course we use **Anthropic** (the company that makes Claude). Create an account in the Anthropic Console, add a small amount of credit, set a monthly spending limit, and create an **API key**. It looks like `sk-ant-...` followed by a long string.

Copy it once and keep it somewhere safe, like a password manager. Treat it exactly like a password.

### Never put the key in your code

This is the most important rule of the file:

<!-- no-verify -->
```python
# NEVER do this
client = anthropic.Anthropic(api_key="sk-ant-abc123...")
```

If this file goes to GitHub (and in this course everything goes to GitHub), your key is public. Bots scan GitHub for keys all day long. Within minutes, someone else could be spending your money.

### Environment variables

An **environment variable** is a named value that lives in your terminal session, outside your code. Your program can read it, but it is not saved in your files.

Set one in the terminal:

```powershell
# Windows (PowerShell): only for this terminal window
$env:ANTHROPIC_API_KEY = "sk-ant-your-key-here"

# Windows: permanent (open a NEW terminal after running it)
setx ANTHROPIC_API_KEY "sk-ant-your-key-here"
```

```bash
# macOS / Linux: only for this terminal window
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
```

Read it in Python with `os.environ`, which works like a dictionary:

```python
import os

os.environ["COFFEE_SIZE"] = "large"  # here we set it in code, only to demonstrate

print(os.environ.get("COFFEE_SIZE"))
print(os.environ.get("TEA_SIZE"))
print(os.environ.get("TEA_SIZE", "medium"))
```

Output:

```text
large
None
medium
```

Like `dict.get`, `os.environ.get` returns `None` (or your default) when the variable does not exist.

A good habit is to check for the key at the start of your program and stop with a clear message if it is missing:

<!-- no-verify -->
```python
import os
import sys

if not os.environ.get("ANTHROPIC_API_KEY"):
    print("Missing ANTHROPIC_API_KEY. Set it in your terminal or in a .env file.")
    sys.exit(1)
```

### A .env file

Typing the key in every new terminal gets boring. A common solution is a file called `.env` in your project folder:

```text
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

The package `python-dotenv` reads this file and puts its values into the environment:

```powershell
python -m pip install python-dotenv
```

<!-- no-verify -->
```python
from dotenv import load_dotenv

load_dotenv()  # reads .env and sets the environment variables
```

And now the second most important rule: **add `.env` to your `.gitignore`** (module 5) **before** your next commit:

```text
.venv/
__pycache__/
.env
```

Check with `git status`: the `.env` file must **not** appear in the list. A nice extra: commit a file called `.env.example` with the variable names but fake values, so others know what to fill in:

```text
ANTHROPIC_API_KEY=put-your-key-here
```

### Installing the SDK

An **SDK** (Software Development Kit) is a library made by the provider to make calling their API easy. You could use `requests` (module 10), but the SDK handles the details for you.

```powershell
python -m pip install anthropic
```

### Your first call

Create `first_call.py`:

<!-- no-verify -->
```python
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment

message = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=500,
    messages=[
        {"role": "user", "content": "Suggest three easy dinners with rice, eggs and spinach. One line each."}
    ],
)

print(message.content[0].text)
```

```console
(.venv) PS C:\Users\you\Projects\ai> python first_call.py
1. Spinach fried rice: stir-fry cooked rice with spinach, garlic and scrambled eggs.
2. Baked eggs on spinach rice: spread rice in a dish, add spinach, crack eggs on top and bake.
3. Rice bowl: warm rice topped with sauteed spinach and a soft-boiled egg.
```

Your answer will be different: the model writes a new text every time.

Piece by piece:

- `anthropic.Anthropic()` creates a **client**, the object that talks to the API. It finds your key in `ANTHROPIC_API_KEY` by itself.
- `model` chooses which model answers. Smaller models (like Haiku) are faster and cheaper; bigger ones are better at hard tasks. Check the provider's documentation for the current list of model names.
- `max_tokens` is the maximum length of the **answer**. If the model reaches it, the answer is cut in the middle. It also limits how much one call can cost.
- `messages` is a **list of dictionaries**. Each one has a `role` (`"user"` for you, `"assistant"` for the model) and `content` (the text).
- The answer comes back as an object. The text is in `message.content[0].text`. (`content` is a list because answers can have several parts; for simple text there is one.)

### What came back

The response has more than just the text. Two useful things:

<!-- no-verify -->
```python
print(message.stop_reason)          # "end_turn" if it finished, "max_tokens" if it was cut
print(message.usage.input_tokens)   # how many tokens you sent
print(message.usage.output_tokens)  # how many tokens it wrote
```

`usage` tells you exactly what you will pay for. Printing it while you learn is a good way to develop a feeling for cost.

### A system prompt

The `system` parameter sets the model's role and rules for the whole conversation. Think of it as instructions to the assistant before the customer walks in:

<!-- no-verify -->
```python
message = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=300,
    system="You are a friendly cooking assistant. Answer in at most three short sentences. Only suggest vegetarian dishes.",
    messages=[{"role": "user", "content": "What can I make with potatoes?"}],
)
print(message.content[0].text)
```

The user message changes every call; the system prompt usually stays the same.

### Conversations: sending the history

The model does not remember previous calls (see the previous file). To have a conversation, you send the earlier messages again, alternating `user` and `assistant`:

<!-- no-verify -->
```python
history = [
    {"role": "user", "content": "Suggest a name for a small coffee shop."},
    {"role": "assistant", "content": "How about 'The Daily Grind'?"},
    {"role": "user", "content": "Nice! Now a slogan for it."},
]

message = client.messages.create(model="claude-haiku-5-5", max_tokens=200, messages=history)
print(message.content[0].text)
```

The longer the history, the more input tokens each call costs.

### Wrapping it in a function

In a real program, you don't want API details spread everywhere. Put the call in one function, with error handling (module 7) and a timeout (module 10):

<!-- no-verify -->
```python
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(timeout=30.0)


def ask(question, system="You are a helpful assistant. Be brief."):
    try:
        message = client.messages.create(
            model="claude-haiku-5-5",
            max_tokens=500,
            system=system,
            messages=[{"role": "user", "content": question}],
        )
        return message.content[0].text
    except anthropic.AuthenticationError:
        print("Your API key is missing or wrong.")
    except anthropic.RateLimitError:
        print("Too many requests. Wait a little and try again.")
    except anthropic.APITimeoutError:
        print("The model took too long to answer.")
    except anthropic.APIConnectionError:
        print("Could not reach the API. Are you online?")
    except anthropic.APIStatusError as error:
        print(f"The API returned an error: {error.status_code}")
    return None


answer = ask("Give me one tip to keep houseplants healthy.")
if answer:
    print(answer)
```

Now the rest of your program only calls `ask(...)` and checks whether it got `None`. If you ever change providers, you only change this one function.

### Other providers

OpenAI, Google and others work in a very similar way: install their SDK, set their key in an environment variable, send a list of messages with roles, read the text from the response. The names of the functions and fields change a little, but everything you learned here carries over.

## Common mistakes

### The key ended up on GitHub

If you ever commit a key, even for a minute, consider it stolen. Go to the provider's console, **delete that key** and create a new one. Deleting the file from the repository is not enough, because it stays in the Git history.

### AuthenticationError

```text
anthropic.AuthenticationError: Error code: 401 - {'type': 'error', 'error': {'type': 'authentication_error', 'message': 'invalid x-api-key'}}
```

The key is missing, has a typo, or was deleted. Check `os.environ.get("ANTHROPIC_API_KEY")`, check that `load_dotenv()` is called **before** `anthropic.Anthropic()`, and check that the terminal where you set the variable is the same one where you run the program.

### The answer stops in the middle

If `message.stop_reason` is `"max_tokens"`, the answer hit your limit. Increase `max_tokens` or ask for a shorter answer in the prompt.

### Calling the model inside a big loop

<!-- no-verify -->
```python
for product in all_10000_products:
    ask(f"Write a description for {product}")
```

This is 10,000 paid calls. Test with 2 or 3 items first, look at `usage`, multiply, and only then decide.

## Exercises

### Predict the output

#### Exercise 1: Reading the environment

What does this print? (Assume `PLANT_API_KEY` was never set.)

<!-- no-verify -->
```python
import os

os.environ["CITY"] = "Lisbon"
print(os.environ.get("CITY", "unknown"))
print(os.environ.get("PLANT_API_KEY", "missing"))
```

<details>
<summary>Show answer</summary>

```python
import os

os.environ["CITY"] = "Lisbon"
print(os.environ.get("CITY", "unknown"))
print(os.environ.get("PLANT_API_KEY", "missing"))
```

Output:

```text
Lisbon
missing
```

</details>

### Fix the bug

#### Exercise 2: Three problems

This program works on the author's computer, but it has three problems. Find them.

<!-- no-verify -->
```python
import anthropic

client = anthropic.Anthropic(api_key="sk-ant-abc123secret")

message = client.messages.create(
    model="claude-haiku-5-5",
    messages=[{"role": "user", "content": "Write a haiku about rain."}],
)
print(message.content)
```

<details>
<summary>Hint</summary>

One is about safety, one is a required parameter, and one is about what gets printed.

</details>

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
import anthropic
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=200,
    messages=[{"role": "user", "content": "Write a haiku about rain."}],
)
print(message.content[0].text)
```

1. The key was written in the code. It now comes from the environment (and that old key must be deleted in the console).
2. `max_tokens` is required.
3. `message.content` is a list of blocks; the text is in `message.content[0].text`.

</details>

### Write it

#### Exercise 3: Building the messages list

Without calling any API, write a function `build_messages(history, new_question)` that receives a list of `(question, answer)` tuples and a new question, and returns the `messages` list in the format the API expects. Test it with one previous exchange.

<details>
<summary>Show answer</summary>

```python
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
```

Output:

```text
{'role': 'user', 'content': 'Name a calm color.'}
{'role': 'assistant', 'content': 'Sage green.'}
{'role': 'user', 'content': 'And an energetic one?'}
```

Building the data with a function you can test, and only then sending it, is a habit that saves money and time.

</details>

#### Exercise 4: Your own assistant

Write a small program `assistant.py` that:

1. Loads the key from `.env` and stops with a clear message if it is missing.
2. Asks the user for a question with `input()`.
3. Calls the model with a system prompt of your choice.
4. Prints the answer and how many tokens were used.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
import os
import sys

import anthropic
from dotenv import load_dotenv

load_dotenv()
if not os.environ.get("ANTHROPIC_API_KEY"):
    print("Missing ANTHROPIC_API_KEY. Create a .env file with your key.")
    sys.exit(1)

client = anthropic.Anthropic(timeout=30.0)

question = input("Ask me something: ")
message = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=400,
    system="You are a patient tutor. Explain things simply, in at most five sentences.",
    messages=[{"role": "user", "content": question}],
)

print()
print(message.content[0].text)
print()
print(f"Tokens: {message.usage.input_tokens} in, {message.usage.output_tokens} out")
```

```console
(.venv) PS C:\Users\you\Projects\ai> python assistant.py
Ask me something: What is a variable in Python?

A variable is a name that points to a value, like a label on a box...

Tokens: 41 in, 87 out
```

</details>

## Review

#### Review 1: .gitignore check (module 5)

Which of these files should be listed in `.gitignore` in an AI project, and why? `app.py`, `.env`, `.env.example`, `.venv/`, `requirements.txt`, `__pycache__/`

<details>
<summary>Show answer</summary>

Ignore `.env` (it has your secret key), `.venv/` (it is big and anyone can recreate it with `pip install -r requirements.txt`) and `__pycache__/` (files Python creates automatically).

Commit `app.py`, `.env.example` (it only has fake values and shows which variables are needed) and `requirements.txt`.

</details>

#### Review 2: A function that returns None on failure (modules 3 and 7)

Write `to_number(text)` that returns the text converted to `float`, or `None` if it cannot be converted.

<details>
<summary>Show answer</summary>

```python
def to_number(text):
    try:
        return float(text)
    except ValueError:
        return None

print(to_number("3.5"))
print(to_number("three"))
```

Output:

```text
3.5
None
```

This is the same pattern as the `ask()` function: try, catch the errors you expect, return `None` when it fails.

</details>

## Recap

- Keep your API key in an environment variable or a `.env` file, and put `.env` in `.gitignore`. Never write it in your code.
- `client = anthropic.Anthropic()` reads the key from `ANTHROPIC_API_KEY`.
- `client.messages.create(model=..., max_tokens=..., messages=[...])` sends the call; the text is in `message.content[0].text`.
- Use `system=` for the model's role and rules, and send previous messages if you need a conversation.
- Wrap the call in one function with `try`/`except` and a timeout; check `message.usage` to understand cost.

**Next:** [Prompts](prompts.md)
