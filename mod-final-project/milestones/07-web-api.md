# Milestone 7: A web API

## Goal

Give Atanor a web interface. Python becomes a **server** with an API (the part that answers requests with data), and a page made with HTML, CSS and JavaScript shows the pieces and lets you add new ones.

## Requires

Module 10: how the web works (client, server, HTTP methods, status codes, JSON), calling APIs, and building an API with Flask.

## What you will build

| Method | Address | What it does |
|---|---|---|
| `GET` | `/pieces` | Returns all pieces as JSON |
| `POST` | `/pieces` | Creates a piece from the JSON sent |
| `GET` | `/pieces/<id>` | Returns one piece |
| `POST` | `/pieces/<id>/advance` | Moves a piece to its next stage |
| `GET` | `/` | Serves the web page |

The flow of a click:

```text
You click "Add" → JavaScript (fetch) → HTTP POST /pieces → Flask → storage.py → atanor.db
                                                                              ↓
The page updates ← JavaScript reads the JSON ← HTTP response ← Flask ←────────┘
```

Everything runs on your own computer. The browser and the server talk through `http://127.0.0.1:5000`, an address that means "this machine".

## Steps

### Step 1: Install Flask

With the virtual environment active, install Flask and add it to `requirements.txt`.

<details>
<summary>Show answer</summary>

```powershell
.venv\Scripts\Activate.ps1
python -m pip install flask
```

`requirements.txt`:

```text
flask
pytest
```

</details>

### Step 2: Validate what arrives

Before touching Flask, write a pure function `validate_new_piece(data)` that receives a dictionary (what the browser sends) and returns a list of error messages. An empty list means the data is valid.

Rules: `name`, `clay` and `technique` are required and cannot be empty. `temperature`, if present, must be a whole number between 0 and 1400.

<details>
<summary>Show answer</summary>

```python
def validate_new_piece(data):
    errors = []
    for field in ["name", "clay", "technique"]:
        if not str(data.get(field, "")).strip():
            errors.append(f"{field} is required")
    temperature = data.get("temperature", 0)
    if not isinstance(temperature, int) or not 0 <= temperature <= 1400:
        errors.append("temperature must be a whole number between 0 and 1400")
    return errors


print(validate_new_piece({"name": "Bowl", "clay": "stoneware", "technique": "wheel", "temperature": 1240}))
print(validate_new_piece({"name": " ", "clay": "stoneware", "temperature": 5000}))
```

Output:

```text
[]
['name is required', 'technique is required', 'temperature must be a whole number between 0 and 1400']
```

The server must **never** trust what the browser sends. Anyone can send any request, even without your page. Keeping this check in a separate function makes it easy to test without a server.

</details>

### Step 3: The first route

Create `app.py` at the project root with a single route, `GET /pieces`, that returns all pieces as JSON. Open `http://127.0.0.1:5000/pieces` in the browser.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# app.py
from flask import Flask, jsonify

from atanor.storage import all_pieces, connect

app = Flask(__name__)


@app.get("/pieces")
def list_pieces():
    conn = connect()
    return jsonify([piece.to_dict() for piece in all_pieces(conn)])


if __name__ == "__main__":
    app.run(debug=True)
```

```powershell
python app.py
```

The browser shows your pieces as JSON. That is what an API returns: data, not a page.

- `@app.get("/pieces")` connects the address `/pieces`, with the method GET, to the function below it.
- We open the connection **inside** the function. Flask can answer requests on different threads, and a SQLite connection must stay on the thread that created it.
- `debug=True` reloads the server when you save a file and shows detailed errors. Never use it on a server open to the internet.

</details>

### Step 4: The other routes

Add `POST /pieces`, `GET /pieces/<id>` and `POST /pieces/<id>/advance`. Return proper status codes:

- `201` when a piece is created
- `400` when the data is invalid or the piece is already finished
- `404` when the piece does not exist

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# app.py
from datetime import date

from flask import Flask, jsonify, request

from atanor.piece import Piece, StageError
from atanor.storage import all_pieces, connect, get_piece, insert_piece, update_stage
from atanor.validation import validate_new_piece

app = Flask(__name__, static_folder="static", static_url_path="")


@app.get("/")
def home():
    return app.send_static_file("index.html")


@app.get("/pieces")
def list_pieces():
    return jsonify([piece.to_dict() for piece in all_pieces(connect())])


@app.post("/pieces")
def create_piece():
    data = request.get_json(silent=True) or {}
    errors = validate_new_piece(data)
    if errors:
        return jsonify(errors=errors), 400
    piece = Piece(
        data["name"].strip(), data["clay"].strip(), data["technique"].strip(),
        data.get("glaze", ""), data.get("temperature", 0), data.get("notes", ""),
        date.today().isoformat(),
    )
    insert_piece(connect(), piece)
    return jsonify(piece.to_dict()), 201


@app.get("/pieces/<int:piece_id>")
def show_piece(piece_id):
    piece = get_piece(connect(), piece_id)
    if piece is None:
        return jsonify(error="piece not found"), 404
    return jsonify(piece.to_dict())


@app.post("/pieces/<int:piece_id>/advance")
def advance_piece(piece_id):
    conn = connect()
    piece = get_piece(conn, piece_id)
    if piece is None:
        return jsonify(error="piece not found"), 404
    try:
        piece.advance(date.today().isoformat())
    except StageError as error:
        return jsonify(error=str(error)), 400
    update_stage(conn, piece)
    return jsonify(piece.to_dict())


if __name__ == "__main__":
    app.run(debug=True)
```

Put `validate_new_piece` in `atanor/validation.py`.

- `<int:piece_id>` captures the number in the address and passes it to the function. `/pieces/abc` gives a 404 automatically.
- `request.get_json(silent=True)` reads the JSON sent. `silent=True` returns `None` instead of crashing if the body is not valid JSON, and `or {}` turns that into an empty dictionary.
- `return jsonify(...), 201` returns the data **and** the status code.

</details>

### Step 5: Try the API from the terminal

Before writing the page, test the API with requests sent from Python, in a second terminal while the server is running.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# try_api.py
import json
from urllib.request import Request, urlopen

BASE = "http://127.0.0.1:5000"

body = json.dumps({"name": "Rice bowl", "clay": "stoneware", "technique": "wheel"}).encode()
request = Request(f"{BASE}/pieces", data=body, headers={"Content-Type": "application/json"}, method="POST")
with urlopen(request) as response:
    print(response.status, json.load(response))

with urlopen(f"{BASE}/pieces") as response:
    for piece in json.load(response):
        print(piece["id"], piece["name"], piece["stage"])
```

```console
PS C:\Users\you\Projects\atanor> python try_api.py
201 {'clay': 'stoneware', 'created': '2026-11-08', 'id': 3, 'name': 'Rice bowl', 'stage': 'modeled', ...}
1 Blue bowl bisque_fired
2 Small vase drying
3 Rice bowl modeled
```

`urllib` comes with Python. In module 10 you may have used the `requests` library, which is shorter. Both work.

</details>

### Step 6: The page

Create `static/index.html`, `static/style.css` and `static/app.js`. The page has a form (name, clay, technique) and a list of pieces, each with an "Advance" button. Use `fetch` to call the API.

<details>
<summary>Show answer</summary>

`static/index.html`:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Atanor</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>Atanor</h1>

  <form id="new-piece">
    <input name="name" placeholder="Name" required>
    <input name="clay" placeholder="Clay" required>
    <input name="technique" placeholder="Technique" required>
    <button type="submit">Add</button>
  </form>
  <p id="message"></p>

  <ul id="pieces"></ul>

  <script src="app.js"></script>
</body>
</html>
```

`static/style.css`:

```css
body { font-family: system-ui, sans-serif; max-width: 640px; margin: 2rem auto; padding: 0 1rem; }
form { display: flex; flex-wrap: wrap; gap: 0.5rem; }
input { flex: 1 1 8rem; padding: 0.4rem; }
#pieces { list-style: none; padding: 0; }
#pieces li { display: flex; justify-content: space-between; align-items: center;
             padding: 0.6rem 0; border-bottom: 1px solid #ddd; }
.stage { color: #666; font-size: 0.9rem; }
#message { color: #b00; }
```

`static/app.js`:

```javascript
const list = document.querySelector("#pieces");
const form = document.querySelector("#new-piece");
const message = document.querySelector("#message");

async function loadPieces() {
  const response = await fetch("/pieces");
  const pieces = await response.json();
  list.innerHTML = "";
  for (const piece of pieces) {
    const item = document.createElement("li");
    item.innerHTML = `<span>${piece.name} <span class="stage">(${piece.stage})</span></span>`;
    if (piece.stage !== "glaze_fired") {
      const button = document.createElement("button");
      button.textContent = "Advance";
      button.addEventListener("click", () => advance(piece.id));
      item.appendChild(button);
    }
    list.appendChild(item);
  }
}

async function advance(id) {
  const response = await fetch(`/pieces/${id}/advance`, { method: "POST" });
  if (!response.ok) {
    message.textContent = (await response.json()).error;
  }
  loadPieces();
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const data = Object.fromEntries(new FormData(form));
  const response = await fetch("/pieces", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (response.ok) {
    form.reset();
    message.textContent = "";
    loadPieces();
  } else {
    message.textContent = (await response.json()).errors.join(", ");
  }
});

loadPieces();
```

- `event.preventDefault()` stops the browser from sending the form the old way (reloading the page). We send it ourselves with `fetch`.
- `Object.fromEntries(new FormData(form))` turns the form into an object like `{name: "...", clay: "...", technique: "..."}`, using the `name` of each input.
- `await` waits for the server to answer before the next line runs.

</details>

### Step 7: Test the API without a browser

Flask has a **test client** that sends fake requests directly to your app. Write tests for creating a piece and for a missing piece.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
# tests/test_api.py
import pytest

import app as atanor_app


@pytest.fixture
def client(tmp_path, monkeypatch):
    db = tmp_path / "test.db"
    real_connect = atanor_app.connect
    monkeypatch.setattr(atanor_app, "connect", lambda: real_connect(db))
    return atanor_app.app.test_client()


def test_create_and_list(client):
    response = client.post("/pieces", json={"name": "Bowl", "clay": "stoneware", "technique": "wheel"})
    assert response.status_code == 201
    names = [piece["name"] for piece in client.get("/pieces").get_json()]
    assert names == ["Bowl"]


def test_invalid_piece(client):
    response = client.post("/pieces", json={"name": ""})
    assert response.status_code == 400


def test_missing_piece(client):
    assert client.get("/pieces/999").status_code == 404
```

`monkeypatch.setattr` temporarily replaces `connect` inside `app.py`, so the tests use a temporary database file instead of your real `atanor.db`. After the test, everything goes back to normal.

</details>

## Checkpoint

```console
PS C:\Users\you\Projects\atanor> python app.py
 * Running on http://127.0.0.1:5000
```

Open `http://127.0.0.1:5000` in the browser:

1. Add a piece: it appears in the list as `modeled`.
2. Click "Advance" a few times: the stage changes, and the button disappears at `glaze_fired`.
3. Stop the server (`Ctrl+C`), start it again, reload the page: the pieces are still there.
4. `python -m pytest` passes.

## Commit

```powershell
git add .
git commit -m "Add Flask API and web page"
git push
```

## Stretch goals

#### Stretch 1: Show the pieces grouped by stage

In `app.js`, show one section per stage, in the lifecycle order. Write the grouping logic first in Python, to be sure of the idea.

<details>
<summary>Show answer</summary>

```python
STAGES = ["modeled", "drying", "bisque_fired", "glazed", "glaze_fired"]
pieces = [
    {"name": "Bowl", "stage": "drying"},
    {"name": "Vase", "stage": "modeled"},
    {"name": "Mug", "stage": "drying"},
]

groups = {stage: [] for stage in STAGES}
for piece in pieces:
    groups[piece["stage"]].append(piece["name"])

for stage, names in groups.items():
    if names:
        print(f"{stage}: {', '.join(names)}")
```

Output:

```text
modeled: Vase
drying: Bowl, Mug
```

The same idea in JavaScript: create an object with one empty array per stage, push each piece into its stage, then draw one `<h2>` and one `<ul>` per non-empty stage.

</details>

#### Stretch 2: Escape the names

If someone names a piece `<b>Bowl</b>`, the page shows it in bold, because `innerHTML` interprets HTML. Fix `loadPieces` so names are always shown as plain text.

<details>
<summary>Show answer</summary>

```javascript
const name = document.createElement("span");
name.textContent = `${piece.name} `;
const stage = document.createElement("span");
stage.className = "stage";
stage.textContent = `(${piece.stage})`;
name.appendChild(stage);
item.appendChild(name);
```

`textContent` never interprets HTML. Here it is just bold text, but the same hole lets someone inject a `<script>` into your page (an attack called **XSS**).

</details>

**Next:** [Milestone 8: Suggestions](08-suggestions.md)
