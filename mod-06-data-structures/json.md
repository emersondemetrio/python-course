# JSON

> **In one sentence:** JSON is a text format for saving and sending data, and it looks almost exactly like Python dictionaries and lists.

## Why it matters

In module 04 you saved text to files, one line at a time. That works for a simple list of names, but what about a list of contacts, each with a name, a phone and a city? You would have to invent your own format and write code to read it back. JSON (pronounced "jay-son") solves this. It is a standard format that every programming language understands. Websites send JSON, apps store JSON, and the APIs you will use in modules 10 and 11 talk in JSON. Learning it now means your data can survive after the program ends, with its shape intact.

## Analogy

Imagine you need to move house. Your furniture (your data) is arranged in a certain way in your rooms (your program). To move it, you pack everything into labeled boxes (JSON text). The boxes travel in the truck (a file, or the internet). At the new house, you unpack the boxes and the furniture is back in shape.

Turning data into JSON text is **packing**. Turning JSON text back into data is **unpacking**. Python's `json` module does both for you.

## The idea, step by step

### What JSON looks like

Here is a contact written in JSON:

<!-- no-verify -->
```json
{
    "name": "Ana",
    "phone": "555-0101",
    "favorite": true,
    "tags": ["work", "family"]
}
```

It looks like a Python dictionary, with a few small differences:

| JSON | Python |
|---|---|
| strings always use double quotes `"..."` | single or double quotes |
| `true` and `false` | `True` and `False` |
| `null` | `None` |
| an object `{}` | a dictionary |
| an array `[]` | a list |

### Packing: from Python to JSON text with `json.dumps()`

`json` is a module that comes with Python. You import it, like you imported `random`. The function `json.dumps()` (read it as "dump string") turns Python data into a JSON string.

```python
import json

contact = {"name": "Ana", "favorite": True, "nickname": None}
text = json.dumps(contact)
print(text)
print(type(text))
```

Output:

```text
{"name": "Ana", "favorite": true, "nickname": null}
<class 'str'>
```

Notice the result is a **string**. `True` became `true`, `None` became `null`, and the quotes became double quotes.

### Making it readable with `indent`

By default everything is on one line. Add `indent=4` to put each item on its own line, indented by 4 spaces:

```python
import json

contact = {"name": "Ana", "tags": ["work", "family"]}
print(json.dumps(contact, indent=4))
```

Output:

```text
{
    "name": "Ana",
    "tags": [
        "work",
        "family"
    ]
}
```

### Unpacking: from JSON text to Python with `json.loads()`

`json.loads()` ("load string") does the opposite: it reads JSON text and gives you real Python data.

```python
import json

text = '{"title": "Dune", "pages": 412, "read": false}'
book = json.loads(text)
print(book["title"])
print(book["pages"] + 1)
print(book["read"])
print(type(book))
```

Output:

```text
Dune
413
False
<class 'dict'>
```

The JSON text was just a string. After `json.loads()`, it is a dictionary, and `412` is a real number you can do math with.

### Saving to a file with `json.dump()`

To save directly into a file, use `json.dump()` (without the "s"). It receives the data and an open file. Remember from module 04: `"w"` means write, and it replaces whatever was in the file.

```python
import json

books = [
    {"title": "Dune", "pages": 412},
    {"title": "Emma", "pages": 474},
]

with open("books.json", "w", encoding="utf-8") as file:
    json.dump(books, file, indent=4)

print("Saved!")
```

Output:

```text
Saved!
```

If you open `books.json` in Cursor, you will see:

<!-- no-verify -->
```json
[
    {
        "title": "Dune",
        "pages": 412
    },
    {
        "title": "Emma",
        "pages": 474
    }
]
```

### Loading from a file with `json.load()`

`json.load()` (without the "s") reads an open file and gives you the data back:

```python
import json

with open("books.json", "w", encoding="utf-8") as file:
    json.dump([{"title": "Dune", "pages": 412}], file)

with open("books.json", "r", encoding="utf-8") as file:
    books = json.load(file)

for book in books:
    print(f"{book['title']}: {book['pages']} pages")
```

Output:

```text
Dune: 412 pages
```

(The first `with` block is only there so this example creates the file it reads. In a real program, the file would already exist from a previous run.)

An easy way to remember the four functions:

| | to/from a string | to/from a file |
|---|---|---|
| Python to JSON (pack) | `json.dumps(data)` | `json.dump(data, file)` |
| JSON to Python (unpack) | `json.loads(text)` | `json.load(file)` |

The **s** stands for **string**.

### Accents and special characters: `ensure_ascii=False`

By default, `json` replaces letters with accents by strange codes:

```python
import json

print(json.dumps({"city": "São Paulo"}))
print(json.dumps({"city": "São Paulo"}, ensure_ascii=False))
```

Output:

```text
{"city": "S\u00e3o Paulo"}
{"city": "São Paulo"}
```

Both versions are correct JSON, and both load back as `"São Paulo"`. But the second one is readable by humans. When you save files with `json.dump()`, use `ensure_ascii=False` together with `encoding="utf-8"` in `open()`.

### The load-or-start-empty pattern

Here is the pattern you will use in almost every program that saves data. The first time the program runs, the file does not exist yet, so we start with an empty list. After that, we load what was saved before.

```python
import json
import os

FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_contacts(contacts):
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4, ensure_ascii=False)

contacts = load_contacts()
print(f"Loaded {len(contacts)} contacts")

contacts.append({"name": "José", "phone": "555-0123"})
save_contacts(contacts)

print(f"Now there are {len(load_contacts())} contacts")
```

Output:

```text
Loaded 0 contacts
Now there are 1 contacts
```

`os.path.exists(FILE)` answers `True` or `False`: does this file exist? Run this program three times on your computer and the number keeps growing, because each run loads what the previous run saved. That is your data surviving after the program ends.

The name `FILE` is in capital letters as a convention: it tells other programmers "this value is a setting, it does not change while the program runs".

## Common mistakes

### Confusing `dump` with `dumps` (and `load` with `loads`)

<!-- error -->
```python
import json

text = '{"name": "Ana"}'
data = json.load(text)
```

```text
Traceback (most recent call last):
AttributeError: 'str' object has no attribute 'read'
```

`json.load()` expects an open **file** and tries to call `.read()` on it. You gave it a string. For a string, use `json.loads(text)`, with the **s**.

### Single quotes in JSON text

<!-- error -->
```python
import json

data = json.loads("{'name': 'Ana'}")
```

```text
Traceback (most recent call last):
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
```

JSON only accepts double quotes for strings. Python accepts both, which is why this one is easy to forget. Write the JSON with double quotes inside, and use single quotes for the Python string around it: `'{"name": "Ana"}'`.

### Loading a file that does not exist

<!-- error -->
```python
import json

with open("missing.json", "r", encoding="utf-8") as file:
    data = json.load(file)
```

```text
Traceback (most recent call last):
FileNotFoundError: [Errno 2] No such file or directory: 'missing.json'
```

The first time your program runs, the file has not been created yet. Use the load-or-start-empty pattern: check with `os.path.exists()` first and return an empty list if the file is not there.

### Saving something JSON does not understand

<!-- error -->
```python
import json

tags = {"python", "beginner"}
print(json.dumps(tags))
```

```text
Traceback (most recent call last):
TypeError: Object of type set is not JSON serializable
```

JSON knows objects (dicts), arrays (lists), strings, numbers, `true`/`false` and `null`. It does not know sets. Convert first: `json.dumps(sorted(tags))` saves it as a list.

## Exercises

### Predict the output

#### Exercise 1: Python to JSON

<!-- no-verify -->
```python
import json

plant = {"name": "Fern", "indoor": True, "sold": False, "price": None}
print(json.dumps(plant))
```

<details>
<summary>Show answer</summary>

```python
import json

plant = {"name": "Fern", "indoor": True, "sold": False, "price": None}
print(json.dumps(plant))
```

Output:

```text
{"name": "Fern", "indoor": true, "sold": false, "price": null}
```

</details>

#### Exercise 2: JSON to Python

<!-- no-verify -->
```python
import json

text = '{"temps": [21, 24, 19], "city": "Porto"}'
weather = json.loads(text)
print(weather["city"])
print(max(weather["temps"]))
print(len(weather))
```

<details>
<summary>Show answer</summary>

```python
import json

text = '{"temps": [21, 24, 19], "city": "Porto"}'
weather = json.loads(text)
print(weather["city"])
print(max(weather["temps"]))
print(len(weather))
```

Output:

```text
Porto
24
2
```

`len(weather)` is 2 because the dictionary has two keys: `"temps"` and `"city"`.

</details>

### Fix the bug

#### Exercise 3: The wrong function

This should turn the dictionary into a JSON string and print it, but it crashes. Fix it.

<!-- no-verify -->
```python
import json

order = {"drink": "latte", "size": "large"}
print(json.dump(order))
```

<details>
<summary>Hint</summary>

Do you want to write to a file or create a string?

</details>

<details>
<summary>Show answer</summary>

```python
import json

order = {"drink": "latte", "size": "large"}
print(json.dumps(order))
```

Output:

```text
{"drink": "latte", "size": "large"}
```

`json.dump()` writes to a file and needs a file as its second argument. `json.dumps()` returns a string.

</details>

#### Exercise 4: Unreadable accents

The file looks like `{"dish": "Feijoada com farofa", "country": "Brasil", "note": "Delicioso, n\u00e3o?"}`. Change the code so the accent is saved as a normal letter.

<!-- no-verify -->
```python
import json

dish = {"dish": "Feijoada com farofa", "country": "Brasil", "note": "Delicioso, não?"}
print(json.dumps(dish))
```

<details>
<summary>Show answer</summary>

```python
import json

dish = {"dish": "Feijoada com farofa", "country": "Brasil", "note": "Delicioso, não?"}
print(json.dumps(dish, ensure_ascii=False))
```

Output:

```text
{"dish": "Feijoada com farofa", "country": "Brasil", "note": "Delicioso, não?"}
```

</details>

### Write it

#### Exercise 5: Save and load a to-do list

Write a program that:

1. Creates a list of three tasks, where each task is a dictionary with `"title"` and `"done"` (True or False).
2. Saves the list to `todo.json` with `indent=4`.
3. Loads it back from the file into a new variable.
4. Prints each task as `[x] title` if done, or `[ ] title` if not.

<details>
<summary>Hint</summary>

For step 4, inside the loop: `if task["done"]: mark = "x"` and `else: mark = " "`.

</details>

<details>
<summary>Show answer</summary>

```python
import json

tasks = [
    {"title": "Water the plants", "done": True},
    {"title": "Pay the bills", "done": False},
    {"title": "Call the dentist", "done": False},
]

with open("todo.json", "w", encoding="utf-8") as file:
    json.dump(tasks, file, indent=4)

with open("todo.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

for task in loaded:
    if task["done"]:
        mark = "x"
    else:
        mark = " "
    print(f"[{mark}] {task['title']}")
```

Output:

```text
[x] Water the plants
[ ] Pay the bills
[ ] Call the dentist
```

</details>

#### Exercise 6: A growing guest book

Using the load-or-start-empty pattern, write a program that asks for a name with `input()`, adds it to a list saved in `guests.json`, and prints how many guests there are now. Run it a few times on your computer.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
import json
import os

FILE = "guests.json"

def load_guests():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_guests(guests):
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(guests, file, indent=4, ensure_ascii=False)

guests = load_guests()
name = input("Your name: ")
guests.append(name)
save_guests(guests)
print(f"Thank you, {name}! We have {len(guests)} guests.")
```

```console
PS C:\Users\you\Projects> python guests.py
Your name: Ana
Thank you, Ana! We have 1 guests.
PS C:\Users\you\Projects> python guests.py
Your name: Bruno
Thank you, Bruno! We have 2 guests.
```

</details>

## Review

#### Review 1: Records (dictionaries)

What does this print?

<!-- no-verify -->
```python
pets = [
    {"name": "Rex", "kind": "dog"},
    {"name": "Mia", "kind": "cat"},
    {"name": "Bob", "kind": "dog"},
]
dogs = 0
for pet in pets:
    if pet["kind"] == "dog":
        dogs = dogs + 1
print(dogs)
```

<details>
<summary>Show answer</summary>

```python
pets = [
    {"name": "Rex", "kind": "dog"},
    {"name": "Mia", "kind": "cat"},
    {"name": "Bob", "kind": "dog"},
]
dogs = 0
for pet in pets:
    if pet["kind"] == "dog":
        dogs = dogs + 1
print(dogs)
```

Output:

```text
2
```

</details>

#### Review 2: File modes (module 04)

What is the difference between opening a file with `"w"` and with `"a"`? Which one does `save_contacts()` in this lesson use, and why is that correct there?

<details>
<summary>Show answer</summary>

`"w"` (write) erases the file and writes it from the beginning. `"a"` (append) keeps what is there and adds to the end.

`save_contacts()` uses `"w"`, and that is correct: the list we are saving already contains the old contacts (we loaded them first) plus the new one. If we used `"a"`, the file would end up with two JSON lists glued together, which is not valid JSON.

</details>

## Recap

- JSON is text that looks like Python dicts and lists, with `true`, `false`, `null` and double quotes only.
- `json.dumps()` and `json.loads()` work with strings. `json.dump()` and `json.load()` work with files. The **s** is for **string**.
- Use `indent=4` to make it readable and `ensure_ascii=False` (with `encoding="utf-8"`) to keep accents.
- Load-or-start-empty: if the file does not exist yet, start with `[]`.
- JSON cannot store sets; turn them into lists first.

**Next:** [Comprehensions](comprehensions.md)
