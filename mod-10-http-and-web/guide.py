# ruff: noqa: UP015
# Teacher's guide: Module 10, HTTP and the web
# Every example and exercise answer from this module's lessons, in order.
# Run it from this folder:  python guide.py
#
# Code that needs Flask, requests, the network or the terminal is only shown
# as comments. Everything else runs for real.

import json
import os
import sqlite3
from urllib.parse import parse_qs, urlencode, urlparse

print("=" * 50)
print("LESSON: how-the-web-works.md")

print("\n--- Example: the parts of a URL")
# Point at each part on the board before running: scheme, host, port, path, query.
url = "https://api.example.com:443/books/42?format=short&lang=en"
parts = urlparse(url)

print(parts.scheme)
print(parts.hostname)
print(parts.port)
print(parts.path)
print(parse_qs(parts.query))

print("\n--- Example: what a status code means")
# Ask her: which group is "my fault" and which is "the server's fault"?


def explain(code):
    if 200 <= code < 300:
        return f"{code}: success"
    elif 400 <= code < 500:
        return f"{code}: the client made a mistake"
    elif 500 <= code < 600:
        return f"{code}: the server had a problem"
    return f"{code}: something else"


for code in [200, 201, 404, 500]:
    print(explain(code))

print("\n--- Example: headers are a dictionary")
headers = {"Accept": "application/json", "User-Agent": "my-first-client"}
print(headers)

print("\n--- Example: JSON text becomes a dictionary")
# true in JSON becomes True in Python.
body = '{"id": 42, "title": "The Little Prince", "available": true}'
book = json.loads(body)

print(book["title"])
print(book["available"])

print("\n--- Example: a dictionary becomes JSON text")
# None in Python becomes null in JSON.
order = {"dish": "soup", "quantity": 2, "notes": None}
print(json.dumps(order))

print("\n--- Mistake: forgetting that JSON is text")
# body = '{"title": "The Little Prince"}'
# print(body["title"])
# TypeError: string indices must be integers, not 'str'
body = '{"title": "The Little Prince"}'
book = json.loads(body)
print(book["title"])

print("\n--- Mistake: single quotes in JSON")
# json.loads("{'title': 'The Little Prince'}")
# json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: ...
print(json.loads('{"title": "The Little Prince"}'))

print("\n--- Exercise 1: parts of a URL")
# Ask her to predict before running.
parts = urlparse("https://shop.example.com/products/7?color=blue")
print(parts.hostname)
print(parts.path)
print(parts.query)

print("\n--- Exercise 2: JSON in, Python out")
# Ask her to predict before running: false -> False, null -> None.
text = '{"name": "Ana", "admin": false, "phone": null}'
user = json.loads(text)
print(user["admin"], user["phone"])

print("\n--- Exercise 3: the broken order")
# Broken version:
# order = '{"dish": "soup", "quantity": 1}'
# print(order["dish"])
# TypeError: string indices must be integers, not 'str'
order = '{"dish": "soup", "quantity": 1}'
data = json.loads(order)
print(data["dish"])

print("\n--- Exercise 4: which method?")


def method_for(action):
    methods = {
        "read": "GET",
        "create": "POST",
        "update": "PUT",
        "remove": "DELETE",
    }
    return methods.get(action, "unknown")


for action in ["read", "create", "update", "remove", "dance"]:
    print(action, "->", method_for(action))

print("\n--- Exercise 5: build a URL")


def book_url(book_id, lang):
    return f"https://api.example.com/books/{book_id}?lang={lang}"


print(book_url(42, "en"))
print(book_url(7, "pt"))

print("\n--- Review 1: counting with a dictionary (module 6)")
codes = [200, 200, 404, 200, 500, 404, 200]

counts = {}
for code in codes:
    counts[code] = counts.get(code, 0) + 1

print(counts)

print("\n--- Review 2: catching a bad JSON (module 7)")


def safe_load(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


print(safe_load('{"ok": true}'))
print(safe_load("not json"))


print("\n" + "=" * 50)
print("LESSON: calling-apis.md")

# Setup in the terminal (show, don't run here):
#   cd ~\Projects
#   uv init apis
#   cd apis
#   uv add requests

print("\n--- Example: your first request (needs requests and internet)")
# import requests
#
# response = requests.get("https://api.github.com/users/octocat", timeout=10)
#
# print(response.status_code)
# print(response.headers["Content-Type"])
#
# uv run first_request.py  ->  200
#                              application/json; charset=utf-8

print("\n--- Example: reading the JSON body (needs requests and internet)")
# import requests
#
# response = requests.get("https://api.github.com/users/octocat", timeout=10)
# user = response.json()
#
# print(user["login"])
# print(user["name"])
# print(f"Public repositories: {user['public_repos']}")
#
# Output: octocat / The Octocat / Public repositories: 8

print("\n--- Example: the same body, without the network")
# This is what .json() does for you: it turns the response text into a dictionary.
body = """
{
  "login": "octocat",
  "name": "The Octocat",
  "public_repos": 8,
  "followers": 4000
}
"""
user = json.loads(body)
print(f"{user['name']} (@{user['login']}) has {user['followers']} followers")

print("\n--- Example: sending options with params (needs requests and internet)")
# import requests
#
# response = requests.get(
#     "https://api.github.com/users/octocat/repos",
#     params={"sort": "updated", "per_page": 3},
#     timeout=10,
# )
#
# print(response.url)
# for repo in response.json():
#     print("-", repo["name"])

print("\n--- Example: what params builds")
params = {"sort": "updated", "per_page": 3}
print("https://api.github.com/users/octocat/repos?" + urlencode(params))

print("\n--- Example: checking if it worked (needs requests and internet)")
# import requests
#
# response = requests.get("https://api.github.com/users/this-user-does-not-exist-123", timeout=10)
#
# if response.status_code == 200:
#     print(response.json()["name"])
# elif response.status_code == 404:
#     print("User not found.")
# else:
#     print(f"Something went wrong: {response.status_code}")

print("\n--- Example: handling errors with raise_for_status (needs requests)")
# import requests
#
# def get_user(username):
#     try:
#         response = requests.get(f"https://api.github.com/users/{username}", timeout=10)
#         response.raise_for_status()
#         return response.json()
#     except requests.exceptions.HTTPError as error:
#         print(f"The server said no: {error}")
#     except requests.exceptions.Timeout:
#         print("The server took too long to answer.")
#     except requests.exceptions.ConnectionError:
#         print("Could not connect. Are you online?")
#     return None
#
# user = get_user("octocat")
# if user:
#     print(user["name"])

print("\n--- Example: sending data with POST (needs requests)")
# new_note = {"title": "Buy coffee", "done": False}
# response = requests.post("https://example.com/api/notes", json=new_note, timeout=10)
# print(response.status_code)  # 201 if it was created

print("\n--- Example: keys go in the headers (needs requests)")
# headers = {"Authorization": "Bearer YOUR-KEY-HERE"}
# response = requests.get("https://api.example.com/data", headers=headers, timeout=10)

print("\n--- Example: the standard-library option, urllib (needs internet)")
# import json
# from urllib.request import urlopen
#
# with urlopen("https://api.github.com/users/octocat", timeout=10) as response:
#     user = json.loads(response.read())
#
# print(user["name"])

print("\n--- Mistake: forgetting the parentheses on json")
# user = response.json
# print(user["name"])
# TypeError: 'method' object is not subscriptable
# Fix: user = response.json()

print("\n--- Mistake: running with the wrong Python")
# python first_request.py
# ModuleNotFoundError: No module named 'requests'
# Fix: uv run first_request.py

print("\n--- Exercise 1: reading nested data")
# Ask her to predict before running. [1] is the second day.
body = '{"city": "Lisbon", "forecast": [{"day": "Mon", "max": 21}, {"day": "Tue", "max": 24}]}'
data = json.loads(body)
print(data["forecast"][1]["day"], data["forecast"][1]["max"])

print("\n--- Exercise 2: the impatient program (needs requests)")
# Broken: no timeout and no status check.
# response = requests.get("https://api.github.com/users/octocat")
# print(response.json()["name"])
#
# Fixed:
# response = requests.get("https://api.github.com/users/octocat", timeout=10)
# if response.status_code == 200:
#     print(response.json()["name"])
# else:
#     print(f"Request failed with status {response.status_code}")

print("\n--- Exercise 3: forecast summary")
body = """
{"city": "Lisbon", "forecast": [
  {"day": "Mon", "min": 14, "max": 21},
  {"day": "Tue", "min": 15, "max": 24},
  {"day": "Wed", "min": 13, "max": 19}
]}
"""
data = json.loads(body)

hottest = data["forecast"][0]
for day in data["forecast"]:
    print(f"{day['day']}: {day['min']} to {day['max']} degrees")
    if day["max"] > hottest["max"]:
        hottest = day

print(f"Hottest day in {data['city']}: {hottest['day']}")

print("\n--- Exercise 4: your own client function (needs requests)")
# import requests
#
# def get_repo_count(username):
#     try:
#         response = requests.get(f"https://api.github.com/users/{username}", timeout=10)
#         response.raise_for_status()
#         return response.json()["public_repos"]
#     except requests.exceptions.RequestException:
#         return None
#
# print(get_repo_count("octocat"))                       # 8
# print(get_repo_count("this-user-does-not-exist-123"))  # None

print("\n--- Review 1: writing JSON to a file (modules 4 and 6)")
user = {"login": "octocat", "name": "The Octocat"}

with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file)

with open("user.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

print(loaded["name"])
os.remove("user.json")

print("\n--- Review 2: filtering a list of dictionaries (modules 2 and 6)")
repos = [
    {"name": "Hello-World", "stars": 2500},
    {"name": "test-repo", "stars": 3},
    {"name": "Spoon-Knife", "stars": 12000},
]

for repo in repos:
    if repo["stars"] > 100:
        print(repo["name"])


print("\n" + "=" * 50)
print("LESSON: building-an-api.md")

# Setup in the terminal (show, don't run here):
#   cd ~\Projects
#   uv init todo-api
#   cd todo-api
#   uv add flask
# Run the server:
#   uv run flask --app app run --debug
# Then open http://127.0.0.1:5000 in the browser.

print("\n--- Example: hello, server (app.py, needs Flask)")
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return "Hello from my first server!"

print("\n--- Example: returning JSON (needs Flask)")
# from flask import Flask, jsonify
#
# app = Flask(__name__)
#
# @app.route("/about")
# def about():
#     return jsonify({"name": "To-do API", "version": 1})
#
# Browser shows: {"name": "To-do API", "version": 1}

print("\n--- Example: URL parameters (needs Flask)")
# @app.route("/hello/<name>")
# def hello(name):
#     return jsonify({"message": f"Hello, {name}!"})
#
# @app.route("/square/<int:number>")
# def square(number):
#     return jsonify({"number": number, "square": number * number})

print("\n--- Example: query strings with request.args (needs Flask)")
# from flask import Flask, jsonify, request
#
# app = Flask(__name__)
#
# @app.route("/greet")
# def greet():
#     name = request.args.get("name", "stranger")
#     times = request.args.get("times", 1, type=int)
#     return jsonify({"message": " ".join([f"Hi, {name}!"] * times)})
#
# Try: http://127.0.0.1:5000/greet?name=Ana&times=2

print("\n--- Example: a tiny to-do API (needs Flask)")
# from flask import Flask, jsonify, request
#
# app = Flask(__name__)
#
# todos = [
#     {"id": 1, "title": "Buy coffee", "done": False},
#     {"id": 2, "title": "Water the plants", "done": True},
# ]
# next_id = 3
#
# def find_todo(todo_id):
#     for todo in todos:
#         if todo["id"] == todo_id:
#             return todo
#     return None
#
# @app.route("/todos", methods=["GET"])
# def list_todos():
#     return jsonify(todos)
#
# @app.route("/todos/<int:todo_id>", methods=["GET"])
# def get_todo(todo_id):
#     todo = find_todo(todo_id)
#     if todo is None:
#         return jsonify({"error": "To-do not found"}), 404
#     return jsonify(todo)
#
# @app.route("/todos", methods=["POST"])
# def create_todo():
#     global next_id
#     data = request.get_json(silent=True)
#     if not data or not data.get("title"):
#         return jsonify({"error": "The field 'title' is required"}), 400
#     todo = {"id": next_id, "title": data["title"], "done": False}
#     todos.append(todo)
#     next_id += 1
#     return jsonify(todo), 201
#
# @app.route("/todos/<int:todo_id>", methods=["DELETE"])
# def delete_todo(todo_id):
#     todo = find_todo(todo_id)
#     if todo is None:
#         return jsonify({"error": "To-do not found"}), 404
#     todos.remove(todo)
#     return jsonify({"deleted": todo_id})

print("\n--- Example: the API logic, without Flask")
# The parts that are just Python can run anywhere.
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

print("\n--- Example: testing your API from the terminal")
# Windows PowerShell:
#   Invoke-RestMethod http://localhost:5000/todos
#   Invoke-RestMethod -Method Post -Uri http://localhost:5000/todos
#       -ContentType "application/json" -Body '{"title": "Call the dentist"}'
#   Invoke-RestMethod -Method Delete -Uri http://localhost:5000/todos/1
# macOS / Linux:
#   curl http://localhost:5000/todos
#   curl -X POST http://localhost:5000/todos -H "Content-Type: application/json"
#       -d '{"title": "Call the dentist"}'
#   curl -X DELETE http://localhost:5000/todos/1

print("\n--- Example: testing your API from Python (needs requests and the server running)")
# import requests
#
# base = "http://localhost:5000"
# created = requests.post(f"{base}/todos", json={"title": "Read a chapter"}, timeout=5)
# print(created.status_code, created.json())
# print(requests.get(f"{base}/todos", timeout=5).json())

print("\n--- Example: a web page that talks to your API")
# Folder:
#   todo-api/
#   ├── app.py
#   └── templates/
#       └── index.html
#
# In app.py:
# from flask import Flask, jsonify, request, render_template
#
# @app.route("/")
# def home():
#     return render_template("index.html")
#
# In index.html, the JavaScript she already knows:
#   const response = await fetch("/todos");
#   const todos = await response.json();
# and to create:
#   await fetch("/todos", {
#     method: "POST",
#     headers: { "Content-Type": "application/json" },
#     body: JSON.stringify({ title: input.value }),
#   });
# Show the full index.html from the lesson on screen.

print("\n--- Mistake: forgetting to return (needs Flask)")
# @app.route("/about")
# def about():
#     jsonify({"name": "To-do API"})
#
# TypeError: The view function for 'about' did not return a valid response. ...
# Fix: return jsonify({"name": "To-do API"})

print("\n--- Exercise 1: which function runs?")
# Ask her to answer each one before you show this. (To-dos 1 and 2 exist.)
answers = [
    ("GET /todos/2", "get_todo(2), status 200"),
    ("GET /todos/42", "get_todo(42), status 404, find_todo returns None"),
    ('POST /todos {"title": ""}', "create_todo(), status 400, empty title counts as missing"),
    ("DELETE /todos/1", "delete_todo(1), status 200"),
    ("GET /todos/abc", "no function runs: <int:todo_id> rejects abc, Flask answers 404"),
]
for request_line, answer in answers:
    print(request_line, "->", answer)

print("\n--- Exercise 2: the route that never creates (needs Flask)")
# Broken: no methods=["POST"] and no return.
# @app.route("/notes")
# def create_note():
#     data = request.get_json(silent=True)
#     note = {"text": data["text"]}
#     notes.append(note)
#     jsonify(note), 201
#
# Fixed:
# @app.route("/notes", methods=["POST"])
# def create_note():
#     data = request.get_json(silent=True)
#     note = {"text": data["text"]}
#     notes.append(note)
#     return jsonify(note), 201

print("\n--- Exercise 3: mark as done (needs Flask)")
# @app.route("/todos/<int:todo_id>/done", methods=["PUT"])
# def mark_done(todo_id):
#     todo = find_todo(todo_id)
#     if todo is None:
#         return jsonify({"error": "To-do not found"}), 404
#     todo["done"] = True
#     return jsonify(todo)
#
# Test: Invoke-RestMethod -Method Put -Uri http://localhost:5000/todos/1/done

print("\n--- Exercise 4: filter with a query string")


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

# And the route that uses it (needs Flask):
# @app.route("/todos", methods=["GET"])
# def list_todos():
#     done = request.args.get("done")
#     return jsonify(filter_todos(todos, done))

print("\n--- Exercise 5: show done items on the page (JavaScript)")
# for (const todo of todos) {
#   const item = document.createElement("li");
#   item.textContent = todo.title + (todo.done ? " (done)" : "");
#
#   if (!todo.done) {
#     const button = document.createElement("button");
#     button.textContent = "Done";
#     button.addEventListener("click", async () => {
#       await fetch(`/todos/${todo.id}/done`, { method: "PUT" });
#       loadTodos();
#     });
#     item.appendChild(button);
#   }
#
#   list.appendChild(item);
# }

print("\n--- Review 1: saving to SQLite instead of memory (module 9)")


def add_todo(connection, title):
    cursor = connection.execute("INSERT INTO todos (title, done) VALUES (?, 0)", (title,))
    connection.commit()
    return cursor.lastrowid


connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE todos (id INTEGER PRIMARY KEY, title TEXT, done INTEGER)")

print(add_todo(connection, "Buy coffee"))
print(add_todo(connection, "Water the plants"))
print(connection.execute("SELECT id, title FROM todos").fetchall())
connection.close()

print("\n--- Review 2: a class for the to-do (module 8)")


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
