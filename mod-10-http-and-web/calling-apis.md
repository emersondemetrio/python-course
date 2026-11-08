# Calling APIs

> **In one sentence:** An **API** is a door that a program opens for other programs, and with the `requests` library your Python code can knock on that door and get data back.

## Why it matters

Weather forecasts, exchange rates, maps, music catalogs, AI models: most of the useful data in the world is offered through APIs. If your program can call an API, it can use all of that without you copying anything by hand.

## Analogy

A website is a restaurant dining room, made for people: nice plates, decoration, music. An **API** is the takeaway window at the back, made for other programs: no decoration, just the food in a box. You say exactly what you want in a standard way, and you get a standard box back (usually JSON).

## The idea, step by step

### What is an API?

**API** stands for Application Programming Interface. For us, a **web API** is a server that answers requests with data (usually JSON) instead of web pages. Each URL the API offers is called an **endpoint**.

For example, GitHub has a public API. The endpoint `https://api.github.com/users/octocat` returns information about the user `octocat`. Open it in your browser now: you will see JSON instead of a pretty page.

### Installing requests

Python has a tool for HTTP in the standard library (`urllib`), but almost everybody uses a friendlier library called `requests`. Install it inside your virtual environment (module 7):

```powershell
# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install requests
```

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
python -m pip install requests
```

### Your first request

<!-- no-verify -->
```python
import requests

response = requests.get("https://api.github.com/users/octocat", timeout=10)

print(response.status_code)
print(response.headers["Content-Type"])
```

```console
PS C:\Users\you\Projects\apis> python first_request.py
200
application/json; charset=utf-8
```

- `requests.get(url)` sends a `GET` request and waits for the answer.
- The result is a **response object**. It has the status code, the headers and the body.
- `timeout=10` means "give up if the server does not answer in 10 seconds". Always use a timeout: without it, your program could wait forever.

### Reading the JSON body

`response.json()` reads the body and turns it into Python dictionaries and lists, like `json.loads` did in the previous file:

<!-- no-verify -->
```python
import requests

response = requests.get("https://api.github.com/users/octocat", timeout=10)
user = response.json()

print(user["login"])
print(user["name"])
print(f"Public repositories: {user['public_repos']}")
```

```console
PS C:\Users\you\Projects\apis> python read_user.py
octocat
The Octocat
Public repositories: 8
```

The numbers may be different when you run it, because the data on GitHub changes. That is normal: an API gives you **live** data.

Once you have the dictionary, everything you learned in module 6 applies. Here is the same idea with the JSON pasted into the code, so you can practice without internet:

```python
import json

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
```

Output:

```text
The Octocat (@octocat) has 4000 followers
```

### Sending options with params

Many APIs accept options in the query string. You could write them in the URL by hand, but `requests` can build the query string for you from a dictionary:

<!-- no-verify -->
```python
import requests

response = requests.get(
    "https://api.github.com/users/octocat/repos",
    params={"sort": "updated", "per_page": 3},
    timeout=10,
)

print(response.url)
for repo in response.json():
    print("-", repo["name"])
```

```console
PS C:\Users\you\Projects\apis> python repos.py
https://api.github.com/users/octocat/repos?sort=updated&per_page=3
- Hello-World
- Spoon-Knife
- octocat.github.io
```

`response.url` shows the final URL that `requests` built. Notice the `?sort=updated&per_page=3` part.

If you are curious how that is built, the standard library can do the same:

```python
from urllib.parse import urlencode

params = {"sort": "updated", "per_page": 3}
print("https://api.github.com/users/octocat/repos?" + urlencode(params))
```

Output:

```text
https://api.github.com/users/octocat/repos?sort=updated&per_page=3
```

### Checking if it worked

Not every request succeeds. Always check the status code before using the body:

<!-- no-verify -->
```python
import requests

response = requests.get("https://api.github.com/users/this-user-does-not-exist-123", timeout=10)

if response.status_code == 200:
    print(response.json()["name"])
elif response.status_code == 404:
    print("User not found.")
else:
    print(f"Something went wrong: {response.status_code}")
```

```console
PS C:\Users\you\Projects\apis> python check.py
User not found.
```

There is also a shortcut: `response.raise_for_status()` raises an error if the status code is `4xx` or `5xx`, and does nothing if it is `2xx`. Combine it with `try`/`except` from module 7:

<!-- no-verify -->
```python
import requests

def get_user(username):
    try:
        response = requests.get(f"https://api.github.com/users/{username}", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as error:
        print(f"The server said no: {error}")
    except requests.exceptions.Timeout:
        print("The server took too long to answer.")
    except requests.exceptions.ConnectionError:
        print("Could not connect. Are you online?")
    return None

user = get_user("octocat")
if user:
    print(user["name"])
```

This is the pattern to use in real programs: a function that either returns the data or returns `None` and explains what happened.

### Sending data with POST

To create something, you send a `POST` with a JSON body. `requests` turns your dictionary into JSON if you use `json=`:

<!-- no-verify -->
```python
import requests

new_note = {"title": "Buy coffee", "done": False}
response = requests.post("https://example.com/api/notes", json=new_note, timeout=10)

print(response.status_code)  # 201 if it was created
```

You will build an API that receives exactly this kind of request in the next file.

### Keys and limits

Some APIs are open (like the GitHub user endpoint). Most ask you for an **API key**, a secret code that identifies you. It usually goes in a header:

<!-- no-verify -->
```python
headers = {"Authorization": "Bearer YOUR-KEY-HERE"}
response = requests.get("https://api.example.com/data", headers=headers, timeout=10)
```

Never write a real key directly in your code or commit it to Git. Module 11 shows how to keep keys safe with environment variables.

APIs also have **rate limits**: a maximum number of requests per hour. GitHub allows 60 per hour without a key. If you go over, you get status `403` or `429`. Do not call an API inside a loop that runs thousands of times.

### The standard-library option: urllib

If you cannot install packages, Python's own `urllib.request` can also make requests. It is more verbose, which is why most people prefer `requests`:

<!-- no-verify -->
```python
import json
from urllib.request import urlopen

with urlopen("https://api.github.com/users/octocat", timeout=10) as response:
    user = json.loads(response.read())

print(user["name"])
```

## Common mistakes

### Forgetting the parentheses on json

<!-- no-verify -->
```python
user = response.json
print(user["name"])
```

```text
TypeError: 'method' object is not subscriptable
```

`response.json` (without parentheses) is the method itself, not its result. You saw this same mistake with `read` and `read()` when working with files. Call it: `response.json()`.

### Using the body before checking the status

If the request failed, the body may be an error message instead of the data you expect, and you get a confusing `KeyError` later. Check `response.status_code` or call `response.raise_for_status()` first.

### No timeout

`requests.get(url)` without `timeout=` can hang forever if the server never answers. Always pass a timeout, like `timeout=10`.

### Running the file with the wrong Python

```text
ModuleNotFoundError: No module named 'requests'
```

This means `requests` is not installed in the Python you are using. Activate your virtual environment (you should see `(.venv)` at the start of the terminal line) and install it with `python -m pip install requests`.

## Exercises

### Predict the output

#### Exercise 1: Reading nested data

An API returned this JSON. What does the code print?

<!-- no-verify -->
```python
import json

body = '{"city": "Lisbon", "forecast": [{"day": "Mon", "max": 21}, {"day": "Tue", "max": 24}]}'
data = json.loads(body)
print(data["forecast"][1]["day"], data["forecast"][1]["max"])
```

<details>
<summary>Show answer</summary>

```python
import json

body = '{"city": "Lisbon", "forecast": [{"day": "Mon", "max": 21}, {"day": "Tue", "max": 24}]}'
data = json.loads(body)
print(data["forecast"][1]["day"], data["forecast"][1]["max"])
```

Output:

```text
Tue 24
```

`data["forecast"]` is a list. Index `1` is the second item, a dictionary with `"day"` and `"max"`.

</details>

### Fix the bug

#### Exercise 2: The impatient program

This program sometimes freezes forever and sometimes crashes with a confusing `KeyError`. Fix both problems.

<!-- no-verify -->
```python
import requests

response = requests.get("https://api.github.com/users/octocat")
print(response.json()["name"])
```

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
import requests

response = requests.get("https://api.github.com/users/octocat", timeout=10)
if response.status_code == 200:
    print(response.json()["name"])
else:
    print(f"Request failed with status {response.status_code}")
```

`timeout=10` stops the freezing, and checking the status code avoids using an error body as if it were the data.

</details>

### Write it

#### Exercise 3: Forecast summary

Here is a JSON body like a weather API would return. Write a program that prints one line per day, like `Mon: 14 to 21 degrees`, and then the hottest day.

<!-- no-verify -->
```python
body = """
{"city": "Lisbon", "forecast": [
  {"day": "Mon", "min": 14, "max": 21},
  {"day": "Tue", "min": 15, "max": 24},
  {"day": "Wed", "min": 13, "max": 19}
]}
"""
```

<details>
<summary>Hint</summary>

Use `json.loads`, then a `for` loop over `data["forecast"]`. To find the hottest day, keep track of the biggest `max` while you loop.

</details>

<details>
<summary>Show answer</summary>

```python
import json

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
```

Output:

```text
Mon: 14 to 21 degrees
Tue: 15 to 24 degrees
Wed: 13 to 19 degrees
Hottest day in Lisbon: Tue
```

</details>

#### Exercise 4: Your own client function

Write a function `get_repo_count(username)` that calls `https://api.github.com/users/<username>`, and returns the number in `public_repos`, or `None` if anything goes wrong. Use a timeout and `try`/`except`. Test it with `octocat` and with a name that does not exist.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
import requests

def get_repo_count(username):
    try:
        response = requests.get(f"https://api.github.com/users/{username}", timeout=10)
        response.raise_for_status()
        return response.json()["public_repos"]
    except requests.exceptions.RequestException:
        return None

print(get_repo_count("octocat"))
print(get_repo_count("this-user-does-not-exist-123"))
```

```console
PS C:\Users\you\Projects\apis> python repo_count.py
8
None
```

`requests.exceptions.RequestException` is the parent of all the `requests` errors, so catching it covers timeouts, connection problems and bad status codes at once.

</details>

## Review

#### Review 1: Writing JSON to a file (modules 4 and 6)

Save this dictionary to a file called `user.json`, then read it back and print the name.

<!-- no-verify -->
```python
user = {"login": "octocat", "name": "The Octocat"}
```

<details>
<summary>Show answer</summary>

```python
import json

user = {"login": "octocat", "name": "The Octocat"}

with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file)

with open("user.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

print(loaded["name"])
```

Output:

```text
The Octocat
```

This is a simple **cache**: save what the API returned so you don't need to ask again.

</details>

#### Review 2: Filtering a list of dictionaries (modules 2 and 6)

Print only the names of the repositories that have more than 100 stars.

<!-- no-verify -->
```python
repos = [
    {"name": "Hello-World", "stars": 2500},
    {"name": "test-repo", "stars": 3},
    {"name": "Spoon-Knife", "stars": 12000},
]
```

<details>
<summary>Show answer</summary>

```python
repos = [
    {"name": "Hello-World", "stars": 2500},
    {"name": "test-repo", "stars": 3},
    {"name": "Spoon-Knife", "stars": 12000},
]

for repo in repos:
    if repo["stars"] > 100:
        print(repo["name"])
```

Output:

```text
Hello-World
Spoon-Knife
```

</details>

## Recap

- An **API** is a server that answers with data (usually JSON) instead of pages. Each URL it offers is an **endpoint**.
- `requests.get(url, params=..., timeout=10)` sends a request; `response.status_code` and `response.json()` read the answer.
- Always use a `timeout` and check the status (or call `raise_for_status()`) before using the body.
- `requests.post(url, json=data)` sends data to create something.
- Never put real API keys in your code.

**Next:** [Building an API](building-an-api.md)
