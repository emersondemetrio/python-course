# How the web works

> **In one sentence:** On the web, a **client** (like your browser) sends a **request** to a **server**, and the server sends back a **response**.

## Why it matters

Every website you visit, every app on your phone and every "log in with Google" button works with this same back-and-forth. Once you understand it, you can make your Python programs fetch data from other services and, later, build services of your own.

## Analogy

Think of a restaurant. You are the **client**: you sit at the table and ask for things. The kitchen is the **server**: it receives orders, prepares them and sends them back. The waiter carries the order to the kitchen (the **request**) and brings the plate back to you (the **response**).

The menu has rules: you order by the dish name, you can ask for changes ("no onions, please"), and sometimes the kitchen says "sorry, we are out of that". The web works the same way. There are rules for how to ask (HTTP), how to name what you want (the URL), and standard ways to say "here it is" or "we don't have that".

## The idea, step by step

### Client and server

- A **client** is a program that asks for something. Your browser is a client. A Python program that downloads data is also a client.
- A **server** is a program that waits for requests and answers them. It usually runs on a computer somewhere else, but it can also run on your own computer.

The same computer can be both. In the next files, your Python program will be a client first, and then you will build a server.

### The URL: the address of what you want

A **URL** (Uniform Resource Locator) is the full address of something on the web. Let's take one apart:

```text
https://api.example.com:443/books/42?format=short&lang=en
```

| Part | In the example | What it means |
|---|---|---|
| Scheme | `https` | The rules (protocol) used to talk. `https` is HTTP with encryption. |
| Host | `api.example.com` | Which computer to talk to. |
| Port | `443` | Which "door" on that computer. Usually hidden, because `https` uses 443 and `http` uses 80 by default. |
| Path | `/books/42` | Which thing you want on that server. |
| Query string | `?format=short&lang=en` | Extra options, as `name=value` pairs joined by `&`. |

Python can take a URL apart for you with `urllib.parse`, from the standard library:

```python
from urllib.parse import urlparse, parse_qs

url = "https://api.example.com:443/books/42?format=short&lang=en"
parts = urlparse(url)

print(parts.scheme)
print(parts.hostname)
print(parts.port)
print(parts.path)
print(parse_qs(parts.query))
```

Output:

```text
https
api.example.com
443
/books/42
{'format': ['short'], 'lang': ['en']}
```

`parse_qs` returns a list for each name because the same name can appear more than once in a query string.

### HTTP: the language of requests and responses

**HTTP** (HyperText Transfer Protocol) is the set of rules clients and servers use to talk. A request is just text. When your browser opens a page, it sends something like this:

```text
GET /books/42 HTTP/1.1
Host: api.example.com
Accept: application/json
```

And the server answers with something like this:

```text
HTTP/1.1 200 OK
Content-Type: application/json

{"id": 42, "title": "The Little Prince"}
```

Every request has a **method**, a **path**, some **headers** and sometimes a **body**. Every response has a **status code**, some **headers** and usually a **body**.

### Methods: what you want to do

The method is the verb of the request. These four are the most common:

| Method | Meaning | Restaurant version |
|---|---|---|
| `GET` | Read something. | "Can I see the menu?" |
| `POST` | Create something new. | "I'd like to order a soup." |
| `PUT` | Replace or update something. | "Please change my soup to a salad." |
| `DELETE` | Remove something. | "Please cancel my dessert." |

When you type a URL in the browser and press Enter, the browser always sends a `GET`.

### Status codes: how did it go?

The status code is a three-digit number at the start of every response. The first digit tells you the family:

- `2xx`: success.
- `4xx`: the **client** made a mistake (asked for something that does not exist, sent bad data).
- `5xx`: the **server** had a problem.

The ones you will see most:

| Code | Name | Meaning |
|---|---|---|
| `200` | OK | Everything worked, here is your answer. |
| `201` | Created | The new thing you sent (with `POST`) was created. |
| `400` | Bad Request | Your request was wrong, for example missing data. |
| `404` | Not Found | The thing you asked for does not exist. |
| `500` | Internal Server Error | The server crashed while handling your request. |

Here is a small function that turns a code into a sentence, using what you learned about `if`:

```python
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
```

Output:

```text
200: success
201: success
404: the client made a mistake
500: the server had a problem
```

### Headers: extra information

**Headers** are `Name: value` lines that travel with requests and responses. They are like notes stuck to the order. Some common ones:

- `Content-Type: application/json` says "the body is JSON".
- `Accept: application/json` says "please answer me in JSON".
- `Authorization: Bearer abc123` carries a key or token that proves who you are.

In Python, headers are usually written as a dictionary:

<!-- no-verify -->
```python
headers = {"Accept": "application/json", "User-Agent": "my-first-client"}
```

### JSON: the common language

Clients and servers can be written in different languages (Python, JavaScript, Java...). To understand each other, they usually send data as **JSON**, the text format you learned in module 6. It looks almost exactly like Python dictionaries and lists.

```python
import json

body = '{"id": 42, "title": "The Little Prince", "available": true}'
book = json.loads(body)

print(book["title"])
print(book["available"])
```

Output:

```text
The Little Prince
True
```

Notice that JSON writes `true` in lowercase and Python writes `True`. `json.loads` translates for you. Going the other way, `json.dumps` turns a Python dictionary into JSON text:

```python
import json

order = {"dish": "soup", "quantity": 2, "notes": None}
print(json.dumps(order))
```

Output:

```text
{"dish": "soup", "quantity": 2, "notes": null}
```

### localhost and ports

When you build a server in this module, it will run on **your own computer**. Your computer calls itself `localhost` (or the number `127.0.0.1`).

A computer can run many servers at once. Each one listens on a different **port**, a number like `5000` or `8000`. So `http://localhost:5000/` means "talk to the server on my own computer that listens at door 5000".

### Seeing requests in the browser

Your browser can show you every request a page makes. Try it now:

1. Open any website in Chrome or Edge.
2. Press `F12` (or right-click the page and choose **Inspect**).
3. Click the **Network** tab.
4. Reload the page with `F5`.

Each line is one request. Click one and look at the **Headers** tab: you will see the URL, the method, the status code and the headers. The **Response** (or **Preview**) tab shows what came back. This tool will be your best friend when something does not work.

## Common mistakes

### Confusing the client and the server

When something goes wrong, first ask: "who is making the request, and who is answering?" A `404` means the server could not find what the client asked for. Usually the fix is in the URL the client used, not in the server.

### Forgetting that JSON is text

What travels over the network is **text**. You must turn it into a dictionary before using it like one:

<!-- error -->
```python
body = '{"title": "The Little Prince"}'
print(body["title"])
```

```text
TypeError: string indices must be integers, not 'str'
```

`body` is a string, not a dictionary. Use `json.loads` first:

```python
import json

body = '{"title": "The Little Prince"}'
book = json.loads(body)
print(book["title"])
```

Output:

```text
The Little Prince
```

### Using single quotes in JSON

JSON only accepts **double quotes**. Python is happy with single quotes, but JSON is not:

<!-- error -->
```python
import json

json.loads("{'title': 'The Little Prince'}")
```

```text
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
```

Write JSON with double quotes, or build a Python dictionary and let `json.dumps` write the JSON for you.

## Exercises

### Predict the output

#### Exercise 1: Parts of a URL

What does this print?

<!-- no-verify -->
```python
from urllib.parse import urlparse

parts = urlparse("https://shop.example.com/products/7?color=blue")
print(parts.hostname)
print(parts.path)
print(parts.query)
```

<details>
<summary>Show answer</summary>

```python
from urllib.parse import urlparse

parts = urlparse("https://shop.example.com/products/7?color=blue")
print(parts.hostname)
print(parts.path)
print(parts.query)
```

Output:

```text
shop.example.com
/products/7
color=blue
```

The host is the computer, the path is the thing on that computer, and the query is everything after the `?`, without the `?`.

</details>

#### Exercise 2: JSON in, Python out

What does this print?

<!-- no-verify -->
```python
import json

text = '{"name": "Ana", "admin": false, "phone": null}'
user = json.loads(text)
print(user["admin"], user["phone"])
```

<details>
<summary>Show answer</summary>

```python
import json

text = '{"name": "Ana", "admin": false, "phone": null}'
user = json.loads(text)
print(user["admin"], user["phone"])
```

Output:

```text
False None
```

JSON `false` becomes Python `False`, and JSON `null` becomes Python `None`.

</details>

### Fix the bug

#### Exercise 3: The broken order

This code should print `soup`, but it crashes. Fix it.

<!-- no-verify -->
```python
order = '{"dish": "soup", "quantity": 1}'
print(order["dish"])
```

<details>
<summary>Hint</summary>

What type is `order`? Is it a dictionary or a string?

</details>

<details>
<summary>Show answer</summary>

```python
import json

order = '{"dish": "soup", "quantity": 1}'
data = json.loads(order)
print(data["dish"])
```

Output:

```text
soup
```

`order` is JSON text. `json.loads` turns it into a dictionary.

</details>

### Write it

#### Exercise 4: Which method?

Write a function `method_for(action)` that receives one of the words `"read"`, `"create"`, `"update"` or `"remove"` and returns the matching HTTP method. For any other word, return `"unknown"`. Test it with the four words and with `"dance"`.

<details>
<summary>Show answer</summary>

```python
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
```

Output:

```text
read -> GET
create -> POST
update -> PUT
remove -> DELETE
dance -> unknown
```

A dictionary is perfect here: each action points to one method, and `.get` gives a default when the key is missing.

</details>

#### Exercise 5: Build a URL

Write a function `book_url(book_id, lang)` that returns a URL like `https://api.example.com/books/42?lang=en`. Use an f-string.

<details>
<summary>Show answer</summary>

```python
def book_url(book_id, lang):
    return f"https://api.example.com/books/{book_id}?lang={lang}"

print(book_url(42, "en"))
print(book_url(7, "pt"))
```

Output:

```text
https://api.example.com/books/42?lang=en
https://api.example.com/books/7?lang=pt
```

</details>

## Review

#### Review 1: Counting with a dictionary (module 6)

Here is a list of status codes a server returned today. Count how many times each code appears and print the result.

<!-- no-verify -->
```python
codes = [200, 200, 404, 200, 500, 404, 200]
```

<details>
<summary>Show answer</summary>

```python
codes = [200, 200, 404, 200, 500, 404, 200]

counts = {}
for code in codes:
    counts[code] = counts.get(code, 0) + 1

print(counts)
```

Output:

```text
{200: 4, 404: 2, 500: 1}
```

</details>

#### Review 2: Catching a bad JSON (module 7)

Write a function `safe_load(text)` that returns the dictionary from a JSON text, or `None` if the text is not valid JSON. Use `try` and `except json.JSONDecodeError`.

<details>
<summary>Show answer</summary>

```python
import json

def safe_load(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None

print(safe_load('{"ok": true}'))
print(safe_load("not json"))
```

Output:

```text
{'ok': True}
None
```

</details>

## Recap

- A **client** sends a **request**; a **server** sends back a **response**.
- A URL has a scheme, a host, an optional port, a path and an optional query string.
- The method says what you want to do: `GET` reads, `POST` creates, `PUT` updates, `DELETE` removes.
- Status codes: `2xx` success, `4xx` client mistake, `5xx` server problem.
- Data usually travels as JSON text: `json.loads` reads it, `json.dumps` writes it.

**Next:** [Calling APIs](calling-apis.md)
