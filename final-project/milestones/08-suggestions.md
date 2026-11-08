# Milestone 8: Suggestions

## Goal

Make Atanor tell you what to do next. First with **rules** you write yourself, then with an **AI model** (an LLM) that reads your history and proposes creative ideas.

## Requires

Module 11: what an LLM is, calling an LLM API, writing prompts, keeping API keys safe.

## What you will build

- `atanor/suggestions.py` with rule-based suggestions, fully tested.
- An AI suggestion that sends a summary of your pieces to Claude and returns ideas.
- A `GET /suggestions` route and a "What should I do next?" section on the page.

Rules and AI do different jobs:

| | Rules | AI |
|---|---|---|
| Example | "Blue bowl has been drying for 8 days. It is ready for the bisque firing." | "You have only used celadon on stoneware. Try it on porcelain for a lighter tone." |
| Always gives the same answer | Yes | No |
| Can be tested exactly | Yes | No |
| Costs money per use | No | Yes, a little |
| Can be wrong | Only if your rule is wrong | Yes, sometimes with confidence |

Good apps use rules for what must be **reliable** and AI for what benefits from **creativity**.

## Steps

### Step 1: The waiting times

In `atanor/suggestions.py`, create a dictionary with how many days a piece usually stays in each stage before moving on. These numbers are a starting point. Change them to match your studio.

```python
READY_AFTER_DAYS = {
    "modeled": 1,       # leather-hard, ready to trim and start drying
    "drying": 7,        # bone dry, ready for the bisque firing
    "bisque_fired": 2,  # cooled down, ready to glaze
    "glazed": 1,        # glaze dry, ready for the final firing
}
```

`glaze_fired` is not in the dictionary: a finished piece needs nothing.

### Step 2: One suggestion for one piece

Write `suggest(piece, today)` that returns a sentence if the piece has waited long enough, or `None` if not. `piece` is a dictionary with `name`, `stage` and `history`. `today` is a date as text.

<details>
<summary>Hint</summary>

The number of days in the current stage is `(date.fromisoformat(today) - date.fromisoformat(piece["history"][piece["stage"]])).days`. You may have written this in milestone 5 as `days_in_stage`.

</details>

<details>
<summary>Show answer</summary>

```python
from datetime import date

READY_AFTER_DAYS = {"modeled": 1, "drying": 7, "bisque_fired": 2, "glazed": 1}

NEXT_ACTION = {
    "modeled": "trim it and start drying",
    "drying": "the bisque firing",
    "bisque_fired": "glazing",
    "glazed": "the glaze firing",
}


def days_in_stage(piece, today):
    started = date.fromisoformat(piece["history"][piece["stage"]])
    return (date.fromisoformat(today) - started).days


def suggest(piece, today):
    stage = piece["stage"]
    if stage not in READY_AFTER_DAYS:
        return None
    days = days_in_stage(piece, today)
    if days < READY_AFTER_DAYS[stage]:
        return None
    return f"{piece['name']} has been {stage} for {days} days. It is ready for {NEXT_ACTION[stage]}."


bowl = {"name": "Blue bowl", "stage": "drying", "history": {"modeled": "2026-11-01", "drying": "2026-11-02"}}
print(suggest(bowl, "2026-11-10"))
print(suggest(bowl, "2026-11-05"))
```

Output:

```text
Blue bowl has been drying for 8 days. It is ready for the bisque firing.
None
```

"has been bisque_fired for 3 days" reads a bit odd. Stretch goal 1 fixes that with friendly names.

</details>

### Step 3: Suggestions for all pieces

Write `suggest_all(pieces, today)` that returns the list of suggestions, oldest wait first, and nothing for pieces that are not ready.

<details>
<summary>Show answer</summary>

```python
from datetime import date

READY_AFTER_DAYS = {"modeled": 1, "drying": 7, "bisque_fired": 2, "glazed": 1}
NEXT_ACTION = {"modeled": "trim it and start drying", "drying": "the bisque firing",
               "bisque_fired": "glazing", "glazed": "the glaze firing"}


def days_in_stage(piece, today):
    return (date.fromisoformat(today) - date.fromisoformat(piece["history"][piece["stage"]])).days


def suggest(piece, today):
    stage = piece["stage"]
    if stage not in READY_AFTER_DAYS:
        return None
    days = days_in_stage(piece, today)
    if days < READY_AFTER_DAYS[stage]:
        return None
    return f"{piece['name']} has been {stage} for {days} days. It is ready for {NEXT_ACTION[stage]}."


def suggest_all(pieces, today):
    waiting = sorted(pieces, key=lambda piece: days_in_stage(piece, today), reverse=True)
    suggestions = [suggest(piece, today) for piece in waiting]
    return [text for text in suggestions if text is not None]


pieces = [
    {"name": "Blue bowl", "stage": "drying", "history": {"drying": "2026-11-02"}},
    {"name": "Mug", "stage": "glazed", "history": {"glazed": "2026-10-30"}},
    {"name": "Vase", "stage": "drying", "history": {"drying": "2026-11-08"}},
    {"name": "Plate", "stage": "glaze_fired", "history": {"glaze_fired": "2026-10-01"}},
]
for text in suggest_all(pieces, "2026-11-10"):
    print("-", text)
```

Output:

```text
- Mug has been glazed for 11 days. It is ready for the glaze firing.
- Blue bowl has been drying for 8 days. It is ready for the bisque firing.
```

The Vase has been drying for only 2 days, and the Plate is finished, so neither appears.

`sorted(..., key=..., reverse=True)` sorts by the number the `key` function returns, biggest first. The `lambda` is a tiny function written in one line.

</details>

### Step 4: Test the rules

Write `tests/test_suggestions.py`. Because `today` is a parameter, every test uses a fixed date and always gets the same result.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# tests/test_suggestions.py
from atanor.suggestions import suggest, suggest_all


def piece(stage, since):
    return {"name": "Bowl", "stage": stage, "history": {stage: since}}


def test_drying_long_enough():
    assert "bisque firing" in suggest(piece("drying", "2026-11-01"), "2026-11-08")


def test_drying_too_soon():
    assert suggest(piece("drying", "2026-11-05"), "2026-11-08") is None


def test_finished_piece_has_no_suggestion():
    assert suggest(piece("glaze_fired", "2026-01-01"), "2026-11-08") is None


def test_suggest_all_skips_pieces_not_ready():
    pieces = [piece("drying", "2026-11-07"), piece("glazed", "2026-11-01")]
    assert len(suggest_all(pieces, "2026-11-08")) == 1
```

In the app, call these functions with your `Piece` objects converted with `piece.to_dict()`, and `date.today().isoformat()` as `today`.

</details>

### Step 5: Get an API key and keep it secret

1. Create an account at **console.anthropic.com**, add a small amount of credit and create an API key.
2. **Never** write the key in your code. Your repository is public: anyone could copy it and spend your credit.
3. Save it in an environment variable called `ANTHROPIC_API_KEY`.
4. Install the SDK (the official Python library to talk to the API).

<details>
<summary>Show answer</summary>

```powershell
python -m pip install anthropic
$env:ANTHROPIC_API_KEY = "sk-ant-..."
```

On macOS or Linux: `export ANTHROPIC_API_KEY="sk-ant-..."`.

This variable lasts only while this terminal is open. To keep it, create a file `.env` with `ANTHROPIC_API_KEY=sk-ant-...`, add `.env` to your `.gitignore` **before** anything else, and load it with the `python-dotenv` library.

Add `anthropic` to `requirements.txt`.

</details>

### Step 6: Summarize your studio for the AI

The model knows nothing about your pieces. You have to tell it, in text. Write `studio_summary(pieces)` that turns the list into a short, clear description. Keep it compact: you pay per amount of text sent.

<details>
<summary>Show answer</summary>

```python
def studio_summary(pieces):
    lines = []
    for piece in pieces:
        glaze = piece["glaze"] or "no glaze yet"
        lines.append(f"- {piece['name']}: {piece['clay']}, {piece['technique']}, {glaze}, stage {piece['stage']}")
    return "\n".join(lines)


pieces = [
    {"name": "Blue bowl", "clay": "stoneware", "technique": "wheel", "glaze": "celadon", "stage": "glaze_fired"},
    {"name": "Small vase", "clay": "porcelain", "technique": "hand-built", "glaze": "", "stage": "drying"},
]
print(studio_summary(pieces))
```

Output:

```text
- Blue bowl: stoneware, wheel, celadon, stage glaze_fired
- Small vase: porcelain, hand-built, no glaze yet, stage drying
```

This function is pure Python, so you can test it like any other. The part you cannot test exactly is what the model will answer.

</details>

### Step 7: Ask the model

Write `ai_suggestions(pieces)` that sends the summary to Claude with a clear instruction and returns the text of the answer.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# atanor/suggestions.py (continued)
import anthropic

SYSTEM_PROMPT = (
    "You are an experienced ceramics teacher helping a hobby potter. "
    "Based on their pieces, suggest 3 short, concrete ideas for what to try next: "
    "new glaze and clay combinations, techniques they have not used, or improvements. "
    "Each idea in one sentence. Do not repeat information they already know."
)


def ai_suggestions(pieces):
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment
    message = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=400,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": f"My pieces:\n{studio_summary(pieces)}"}],
    )
    return message.content[0].text
```

- `system` sets the role and the rules for the model. `messages` is the conversation, here a single message from you.
- `max_tokens` limits the size of the answer, and therefore the cost. A token is a piece of a word, roughly 3 or 4 letters.
- We use Haiku, the smallest and cheapest model, because this task is simple. A few dozen calls cost less than a coffee.

Try it in the terminal:

```console
PS C:\Users\you\Projects\atanor> python -c "from atanor.storage import connect, all_pieces; from atanor.suggestions import ai_suggestions; print(ai_suggestions([p.to_dict() for p in all_pieces(connect())]))"
1. Try celadon on your porcelain vase: on a white body it turns a lighter, clearer green.
2. You have only thrown on the wheel with stoneware; a hand-built stoneware piece would show you how the clay behaves without the wheel.
3. ...
```

Your answer will be different, and different every time. That is normal for an LLM.

</details>

### Step 8: Handle failures

The API can fail: no internet, invalid key, no credit, too many requests. The app must keep working, showing only the rule-based suggestions. Wrap the call so it never crashes the app.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
def safe_ai_suggestions(pieces):
    if not pieces:
        return "Add some pieces first, then I can suggest ideas."
    try:
        return ai_suggestions(pieces)
    except anthropic.APIError as error:
        return f"AI suggestions are unavailable right now ({error.__class__.__name__})."
```

`anthropic.APIError` is the parent of all errors the SDK raises for API problems, so one `except` covers them all. A missing key raises an error when the client is created, before any request, so also check that `ANTHROPIC_API_KEY` is set when the server starts and print a clear warning if it is not.

</details>

### Step 9: The route and the page

Add `GET /suggestions` to `app.py`, returning `{"rules": [...], "ai": "..."}`. AI suggestions are slow and cost money, so only ask for them when the user clicks a button: use `GET /suggestions?ai=1`.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# app.py (new route)
from atanor.suggestions import safe_ai_suggestions, suggest_all


@app.get("/suggestions")
def suggestions():
    pieces = [piece.to_dict() for piece in all_pieces(connect())]
    result = {"rules": suggest_all(pieces, date.today().isoformat())}
    if request.args.get("ai") == "1":
        result["ai"] = safe_ai_suggestions(pieces)
    return jsonify(result)
```

In `index.html`, add:

```html
<section>
  <h2>What should I do next?</h2>
  <ul id="rules"></ul>
  <button id="ask-ai">Ask for creative ideas</button>
  <p id="ai"></p>
</section>
```

In `app.js`:

```javascript
async function loadSuggestions(withAi = false) {
  const response = await fetch(withAi ? "/suggestions?ai=1" : "/suggestions");
  const data = await response.json();
  const rules = document.querySelector("#rules");
  rules.innerHTML = "";
  for (const text of data.rules) {
    const item = document.createElement("li");
    item.textContent = text;
    rules.appendChild(item);
  }
  if (data.rules.length === 0) {
    rules.innerHTML = "<li>Nothing to do right now.</li>";
  }
  if (withAi) {
    document.querySelector("#ai").textContent = data.ai;
  }
}

document.querySelector("#ask-ai").addEventListener("click", async (event) => {
  event.target.disabled = true;
  document.querySelector("#ai").textContent = "Thinking...";
  await loadSuggestions(true);
  event.target.disabled = false;
});

loadSuggestions();
```

Also call `loadSuggestions()` at the end of `advance()` and after adding a piece, so the list stays up to date.

</details>

## Checkpoint

1. `python -m pytest` passes, including the suggestion tests.
2. Open the page: the "What should I do next?" section lists pieces that are ready, based on the dates.
3. Click "Ask for creative ideas": after a few seconds, three ideas appear.
4. Close the terminal, open a new one **without** setting the key, start the server and click the button again: the page shows the "unavailable" message and everything else still works.

## Commit

```powershell
git status
git add .
git commit -m "Suggest next steps with rules and with Claude"
git push
```

Before pushing, read `git status` carefully: `.env` must **not** be in the list. If you ever commit a key by accident, delete it on console.anthropic.com immediately and create a new one. Removing it from the code is not enough, because it stays in the Git history.

Congratulations. Update your README: Atanor is finished. 🎉

## Stretch goals

#### Stretch 1: Friendly stage names

Show `drying` as "drying", `bisque_fired` as "waiting after the bisque firing", and so on, in the suggestions.

<details>
<summary>Show answer</summary>

```python
FRIENDLY = {
    "modeled": "freshly modeled",
    "drying": "drying",
    "bisque_fired": "out of the bisque firing",
    "glazed": "glazed",
}

print(f"Small vase has been {FRIENDLY['bisque_fired']} for 3 days.")
```

Output:

```text
Small vase has been out of the bisque firing for 3 days.
```

Use `FRIENDLY[stage]` instead of `stage` inside `suggest`.

</details>

#### Stretch 2: Let the AI know the rules

Send the rule-based suggestions to the model too, and ask it not to repeat them. Why does this make the answer better?

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
content = (
    f"My pieces:\n{studio_summary(pieces)}\n\n"
    f"Already planned:\n" + "\n".join(f"- {text}" for text in suggest_all(pieces, today)) +
    "\n\nSuggest ideas beyond what is already planned."
)
```

The model only knows what you send it. If it does not know the bowl is already going to the kiln, it may waste one of its three ideas telling you that. More relevant context gives more useful answers: this is the core of writing good prompts.

</details>

#### Stretch 3: A desktop window

Atanor runs in the browser, but you can wrap it in its own desktop window with **pywebview**, without changing the HTML, CSS or JavaScript.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# desktop.py
import threading

import webview

from app import app


def run_server():
    app.run(port=5000)


threading.Thread(target=run_server, daemon=True).start()
webview.create_window("Atanor", "http://127.0.0.1:5000", width=900, height=700)
webview.start()
```

```powershell
python -m pip install pywebview
python desktop.py
```

The Flask server runs in the background (a **thread**), and pywebview opens a native window pointing at it. `daemon=True` makes the server stop when you close the window. To turn it into a real `.exe` you can double-click, look up **PyInstaller**.

</details>

**Back to:** [Final project overview](../README.md)
