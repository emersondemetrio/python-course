# Building an API

> **In one sentence:** With the **Flask** library, a few lines of Python turn your functions into a web server that browsers, JavaScript and other programs can call.

## Why it matters

In the previous file your program was the client. Now it becomes the **server**. This is how real apps are built: a Python server keeps the data and the rules, and a web page (HTML, CSS and JavaScript) shows it nicely and talks to the server. You already know both halves; this file connects them.

## Analogy

Building an API is like opening your own small restaurant. You write the **menu** (the routes: which URLs exist and what each one does), you hire a **cook** for each dish (a Python function per route), and you decide what to answer when someone orders something that is not on the menu (`404`) or orders it wrong (`400`).

Flask is the building and the waiters: it receives the orders, finds the right cook, and carries the answer back. You only write the recipes.

## The idea, step by step

### Setting up the project

Create a new folder for this file's examples, a virtual environment, and install Flask:

```powershell
# Windows (PowerShell)
cd ~\Projects
mkdir todo-api
cd todo-api
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install flask
```

```bash
# macOS / Linux
cd ~/Projects
mkdir todo-api
cd todo-api
python3 -m venv .venv
source .venv/bin/activate
python -m pip install flask
```

### Hello, server

Create a file called `app.py`:

<!-- no-verify -->
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from my first server!"
```

Line by line:

- `Flask(__name__)` creates your app. `__name__` tells Flask where your file is (you met `__name__` in module 7).
- `@app.route("/")` is a **decorator**: it says "when someone requests the path `/`, call the function below". You don't need to know how decorators work inside to use them.
- `home()` is a normal function. Whatever it returns is sent back as the response body.

Run it from the terminal, in the project folder:

```powershell
flask --app app run --debug
```

```console
(.venv) PS C:\Users\you\Projects\todo-api> flask --app app run --debug
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Open `http://localhost:5000/` in the browser. You should see your message. In the terminal, a new line appears for each request, with the method, the path and the status code:

```console
127.0.0.1 - - [08/Nov/2026 15:30:12] "GET / HTTP/1.1" 200 -
```

- `--app app` tells Flask your app is in `app.py`.
- `--debug` restarts the server every time you save the file and shows helpful error pages. Use it while learning, never on a real public server.
- The server keeps running until you press `Ctrl+C`. While it runs, that terminal is busy: open a second terminal if you need to type other commands.

### Returning JSON

A web page returns HTML. An API returns JSON. Flask's `jsonify` turns a dictionary or list into a JSON response, with the right `Content-Type` header:

<!-- no-verify -->
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/about")
def about():
    return jsonify({"name": "To-do API", "version": 1})
```

Open `http://localhost:5000/about` and you will see:

```text
{"name": "To-do API", "version": 1}
```

Tip: in recent versions of Flask, returning a dictionary directly also works. Using `jsonify` makes it obvious that the answer is JSON.

### URL parameters

Often the path contains a value, like the ID in `/todos/3`. Write it in the route between `< >`, and Flask passes it to your function as a parameter:

<!-- no-verify -->
```python
@app.route("/hello/<name>")
def hello(name):
    return jsonify({"message": f"Hello, {name}!"})

@app.route("/square/<int:number>")
def square(number):
    return jsonify({"number": number, "square": number * number})
```

- `http://localhost:5000/hello/Ana` returns `{"message": "Hello, Ana!"}`.
- `http://localhost:5000/square/7` returns `{"number": 7, "square": 49}`.
- `<int:number>` tells Flask to convert the value to an `int`. If someone visits `/square/abc`, Flask answers `404` by itself, because `abc` is not a number.

### Query strings with request.args

Options after the `?` are in `request.args`, which works like a dictionary:

<!-- no-verify -->
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/greet")
def greet():
    name = request.args.get("name", "stranger")
    times = request.args.get("times", 1, type=int)
    return jsonify({"message": " ".join([f"Hi, {name}!"] * times)})
```

- `/greet` returns `{"message": "Hi, stranger!"}`.
- `/greet?name=Ana&times=2` returns `{"message": "Hi, Ana! Hi, Ana!"}`.

`.get` with a default works just like `dict.get`. `type=int` converts the text to a number.

### A tiny to-do API

Now let's build something real: an API to manage a to-do list. For now the data lives in a Python list in memory (in module 9 you learned how to keep it in a database; you will connect the two in the final project).

The plan, our "menu":

| Method | Path | What it does | Success code |
|---|---|---|---|
| `GET` | `/todos` | List all to-dos | `200` |
| `GET` | `/todos/<id>` | Get one to-do | `200` |
| `POST` | `/todos` | Create a to-do | `201` |
| `DELETE` | `/todos/<id>` | Delete a to-do | `200` |

Replace everything in `app.py` with:

<!-- no-verify -->
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {"id": 1, "title": "Buy coffee", "done": False},
    {"id": 2, "title": "Water the plants", "done": True},
]
next_id = 3


def find_todo(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return None


@app.route("/todos", methods=["GET"])
def list_todos():
    return jsonify(todos)


@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = find_todo(todo_id)
    if todo is None:
        return jsonify({"error": "To-do not found"}), 404
    return jsonify(todo)


@app.route("/todos", methods=["POST"])
def create_todo():
    global next_id
    data = request.get_json(silent=True)
    if not data or not data.get("title"):
        return jsonify({"error": "The field 'title' is required"}), 400

    todo = {"id": next_id, "title": data["title"], "done": False}
    todos.append(todo)
    next_id += 1
    return jsonify(todo), 201


@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = find_todo(todo_id)
    if todo is None:
        return jsonify({"error": "To-do not found"}), 404
    todos.remove(todo)
    return jsonify({"deleted": todo_id})
```

New things here:

- `methods=["POST"]` says which HTTP method a route accepts. Two routes can share the path `/todos` if they use different methods.
- `return jsonify(...), 404` returns a **tuple**: the body and the status code. Without the number, Flask uses `200`.
- `request.get_json(silent=True)` reads the JSON body of the request as a dictionary. `silent=True` makes it return `None` instead of crashing when the body is not valid JSON, so we can answer `400` ourselves.
- `global next_id` lets the function change the variable `next_id` that lives outside it. Normally you avoid `global`, but it keeps this first example short. In the final project, the database will create the IDs for you.

The rules of the API (finding, validating, creating) are plain Python that you already know. Here is the same logic without Flask, so you can see it run:

```python
todos = [
    {"id": 1, "title": "Buy coffee", "done": False},
    {"id": 2, "title": "Water the plants", "done": True},
]

def find_todo(todo_id):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return None

def validate(data):
    if not data or not data.get("title"):
        return "The field 'title' is required", 400
    return "ok", 201

print(find_todo(2))
print(find_todo(99))
print(validate({"title": "Call mom"}))
print(validate({}))
```

Output:

```text
{'id': 2, 'title': 'Water the plants', 'done': True}
None
('ok', 201)
("The field 'title' is required", 400)
```

### Testing your API

**GET requests** can be tested right in the browser: open `http://localhost:5000/todos` and `http://localhost:5000/todos/1`.

**POST and DELETE** need a tool. Open a **second terminal** (the first one is running the server).

On Windows PowerShell, use `Invoke-RestMethod`:

```powershell
# list
Invoke-RestMethod http://localhost:5000/todos

# create
Invoke-RestMethod -Method Post -Uri http://localhost:5000/todos -ContentType "application/json" -Body '{"title": "Call the dentist"}'

# delete
Invoke-RestMethod -Method Delete -Uri http://localhost:5000/todos/1
```

On macOS / Linux (and also in recent Windows, as `curl.exe`), use `curl`:

```bash
# list
curl http://localhost:5000/todos

# create
curl -X POST http://localhost:5000/todos -H "Content-Type: application/json" -d '{"title": "Call the dentist"}'

# delete
curl -X DELETE http://localhost:5000/todos/1
```

You can also test from Python with `requests`, which you learned in the previous file:

<!-- no-verify -->
```python
import requests

base = "http://localhost:5000"
created = requests.post(f"{base}/todos", json={"title": "Read a chapter"}, timeout=5)
print(created.status_code, created.json())
print(requests.get(f"{base}/todos", timeout=5).json())
```

```console
(.venv) PS C:\Users\you\Projects\todo-api> python try_api.py
201 {'done': False, 'id': 3, 'title': 'Read a chapter'}
[{'done': False, 'id': 1, 'title': 'Buy coffee'}, {'done': True, 'id': 2, 'title': 'Water the plants'}, {'done': False, 'id': 3, 'title': 'Read a chapter'}]
```

Notice two things: Flask sorts the keys alphabetically in its JSON, and when you restart the server, the new to-dos disappear. They only lived in memory. That is exactly the problem a database solves.

### A web page that talks to your API

Now the part where your HTML and JavaScript come in. Flask serves HTML files from a folder called `templates`. Create this structure:

```text
todo-api/
├── app.py
└── templates/
    └── index.html
```

Add this route to `app.py` (and import `render_template` at the top):

<!-- no-verify -->
```python
from flask import Flask, jsonify, request, render_template

@app.route("/")
def home():
    return render_template("index.html")
```

And create `templates/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My to-dos</title>
</head>
<body>
  <h1>My to-dos</h1>

  <form id="new-todo">
    <input id="title" placeholder="What do you need to do?" required>
    <button type="submit">Add</button>
  </form>

  <ul id="list"></ul>

  <script>
    async function loadTodos() {
      const response = await fetch("/todos");
      const todos = await response.json();

      const list = document.querySelector("#list");
      list.innerHTML = "";
      for (const todo of todos) {
        const item = document.createElement("li");
        item.textContent = todo.title + (todo.done ? " (done)" : "");
        list.appendChild(item);
      }
    }

    document.querySelector("#new-todo").addEventListener("submit", async (event) => {
      event.preventDefault();
      const input = document.querySelector("#title");

      await fetch("/todos", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title: input.value }),
      });

      input.value = "";
      loadTodos();
    });

    loadTodos();
  </script>
</body>
</html>
```

Open `http://localhost:5000/` and add a few to-dos. Then open DevTools (`F12`), go to the **Network** tab and add another one: you will see the `POST /todos` request with status `201`, followed by a `GET /todos`.

How the pieces fit:

1. The browser asks the server for `/`. Flask answers with `index.html`.
2. The page's JavaScript calls `fetch("/todos")`. Flask runs `list_todos()` and answers with JSON.
3. The JavaScript turns the JSON into `<li>` items. The server never builds HTML for the list: it only sends data.
4. When you submit the form, JavaScript sends a `POST` with a JSON body. Flask runs `create_todo()`.

`fetch` in JavaScript plays the same role as `requests` in Python: both are clients.

### A word about CORS

In the example above, the page and the API come from the same address (`localhost:5000`), so everything just works. If you open an HTML file from a **different** address (for example, by double-clicking it, or from another port) and it calls your API, the browser blocks the request with a **CORS** error in the console. CORS (Cross-Origin Resource Sharing) is a browser safety rule: a page may only call other addresses if those addresses allow it.

The simplest way to avoid it while learning: serve your pages from Flask itself, as we did. If you really need to allow another address, the package `flask-cors` does it.

## Common mistakes

### "Address already in use"

```text
Address already in use
Port 5000 is in use by another program.
```

Another server (maybe your own, in another terminal) is already using port 5000. Stop it with `Ctrl+C`, or run on another port: `flask --app app run --debug --port 5001`.

### 405 Method Not Allowed

You sent a `POST` to a route that only accepts `GET` (the default). Add the method to the route: `@app.route("/todos", methods=["POST"])`.

### Forgetting to return

<!-- no-verify -->
```python
@app.route("/about")
def about():
    jsonify({"name": "To-do API"})
```

```text
TypeError: The view function for 'about' did not return a valid response. The function either returned None or ended without a return statement.
```

Every route function must `return` something. Here, `jsonify(...)` creates the response but nobody returns it. Add `return`.

### The page shows old data or doesn't change

Check that you saved the file (`Ctrl+S`) and that the server is running with `--debug`. For HTML changes, reload the page with `Ctrl+F5` to skip the browser's cache.

### Sending JSON without the Content-Type header

If `fetch` or `curl` sends a body without `Content-Type: application/json`, `request.get_json(silent=True)` returns `None` and your API answers `400`. Always send that header with JSON bodies.

## Exercises

### Predict the output

#### Exercise 1: Which function runs?

Given the to-do API above, which function runs for each request, and what status code comes back? (Assume to-dos 1 and 2 exist.)

1. `GET /todos/2`
2. `GET /todos/42`
3. `POST /todos` with body `{"title": ""}`
4. `DELETE /todos/1`
5. `GET /todos/abc`

<details>
<summary>Show answer</summary>

1. `get_todo(2)`, status `200`.
2. `get_todo(42)`, status `404`, because `find_todo` returns `None`.
3. `create_todo()`, status `400`, because an empty title counts as missing (`not ""` is `True`).
4. `delete_todo(1)`, status `200`.
5. No function runs. `<int:todo_id>` does not accept `abc`, so Flask answers `404` by itself.

</details>

### Fix the bug

#### Exercise 2: The route that never creates

This route returns `405 Method Not Allowed` when the page sends a `POST`. Find the two problems.

<!-- no-verify -->
```python
@app.route("/notes")
def create_note():
    data = request.get_json(silent=True)
    note = {"text": data["text"]}
    notes.append(note)
    jsonify(note), 201
```

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
@app.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json(silent=True)
    note = {"text": data["text"]}
    notes.append(note)
    return jsonify(note), 201
```

1. The route only accepted `GET` (the default). It needs `methods=["POST"]`.
2. The last line was missing `return`.

Bonus: it would still crash if the body has no `"text"`. Add a check and answer `400`, like in `create_todo`.

</details>

### Write it

#### Exercise 3: Mark as done

Add a route `PUT /todos/<id>/done` to the to-do API that sets `done` to `True` and returns the updated to-do. If the to-do does not exist, return `404`. Test it with `Invoke-RestMethod -Method Put` or `curl -X PUT`.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
@app.route("/todos/<int:todo_id>/done", methods=["PUT"])
def mark_done(todo_id):
    todo = find_todo(todo_id)
    if todo is None:
        return jsonify({"error": "To-do not found"}), 404
    todo["done"] = True
    return jsonify(todo)
```

```powershell
Invoke-RestMethod -Method Put -Uri http://localhost:5000/todos/1/done
```

Because `todo` is the same dictionary that lives inside the `todos` list, changing it changes the list.

</details>

#### Exercise 4: Filter with a query string

Change `list_todos` so that `/todos?done=true` returns only finished to-dos, `/todos?done=false` only unfinished ones, and `/todos` all of them. First write the filtering as a normal function and test it without Flask.

<details>
<summary>Hint</summary>

`request.args.get("done")` returns the text `"true"`, `"false"` or `None`. Compare text, not booleans.

</details>

<details>
<summary>Show answer</summary>

The filtering logic, tested without Flask:

```python
def filter_todos(todos, done):
    if done is None:
        return todos
    wanted = done == "true"
    return [todo for todo in todos if todo["done"] == wanted]

todos = [
    {"id": 1, "title": "Buy coffee", "done": False},
    {"id": 2, "title": "Water the plants", "done": True},
]
print(filter_todos(todos, None))
print(filter_todos(todos, "true"))
print(filter_todos(todos, "false"))
```

Output:

```text
[{'id': 1, 'title': 'Buy coffee', 'done': False}, {'id': 2, 'title': 'Water the plants', 'done': True}]
[{'id': 2, 'title': 'Water the plants', 'done': True}]
[{'id': 1, 'title': 'Buy coffee', 'done': False}]
```

And the route that uses it:

<!-- no-verify -->
```python
@app.route("/todos", methods=["GET"])
def list_todos():
    done = request.args.get("done")
    return jsonify(filter_todos(todos, done))
```

Keeping the logic in a separate function makes it easy to test (module 7) and keeps the route short.

</details>

#### Exercise 5: Show done items on the page

Change the JavaScript in `index.html` so that each to-do has a "Done" button that calls your new `PUT /todos/<id>/done` route and then reloads the list.

<details>
<summary>Show answer</summary>

Replace the `for` loop inside `loadTodos` with:

```javascript
for (const todo of todos) {
  const item = document.createElement("li");
  item.textContent = todo.title + (todo.done ? " (done)" : "");

  if (!todo.done) {
    const button = document.createElement("button");
    button.textContent = "Done";
    button.addEventListener("click", async () => {
      await fetch(`/todos/${todo.id}/done`, { method: "PUT" });
      loadTodos();
    });
    item.appendChild(button);
  }

  list.appendChild(item);
}
```

</details>

## Review

#### Review 1: Saving to SQLite instead of memory (module 9)

Write a function `add_todo(connection, title)` that inserts a to-do into a SQLite table `todos (id INTEGER PRIMARY KEY, title TEXT, done INTEGER)` and returns the new ID. Test it with an in-memory database.

<details>
<summary>Show answer</summary>

```python
import sqlite3

def add_todo(connection, title):
    cursor = connection.execute(
        "INSERT INTO todos (title, done) VALUES (?, 0)", (title,)
    )
    connection.commit()
    return cursor.lastrowid

connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE todos (id INTEGER PRIMARY KEY, title TEXT, done INTEGER)")

print(add_todo(connection, "Buy coffee"))
print(add_todo(connection, "Water the plants"))
print(connection.execute("SELECT id, title FROM todos").fetchall())
```

Output:

```text
1
2
[(1, 'Buy coffee'), (2, 'Water the plants')]
```

Replace the `todos` list in your API with calls like this and your to-dos survive a restart. You will do exactly that in the final project.

</details>

#### Review 2: A class for the to-do (module 8)

Write a class `Todo` with `title` and `done` (starting as `False`), a method `finish()` and a method `to_dict()` that returns a dictionary ready for `jsonify`.

<details>
<summary>Show answer</summary>

```python
class Todo:
    def __init__(self, title):
        self.title = title
        self.done = False

    def finish(self):
        self.done = True

    def to_dict(self):
        return {"title": self.title, "done": self.done}

task = Todo("Buy coffee")
task.finish()
print(task.to_dict())
```

Output:

```text
{'title': 'Buy coffee', 'done': True}
```

`jsonify` cannot send an object directly, but it can send the dictionary that `to_dict()` returns.

</details>

## Recap

- Flask turns functions into routes: `@app.route("/path", methods=["GET"])` above a function that returns the response.
- Run it with `flask --app app run --debug` and open `http://localhost:5000`.
- Return JSON with `jsonify(...)`; return a different status code with `return jsonify(...), 404`.
- Read values from the path with `<int:id>`, from the query string with `request.args`, and from a JSON body with `request.get_json()`.
- A web page served by Flask can call your API with `fetch()`: the server sends data, the page's JavaScript shows it.

**Next:** [Module 11: AI](../module-11-ai/README.md)
