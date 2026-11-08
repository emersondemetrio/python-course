# Module 06: Data structures

So far you have stored information in single variables and in lists. Lists are great for "a bunch of things in order", but real data usually has more shape. A recipe has a name, a time and a list of ingredients. A contact has a name, a phone and an email. In this module you learn the tools Python gives you to store data with shape, and how to save that data to a file in a format that other programs understand.

## What you will learn

- How to store information as **key and value** pairs (dictionaries).
- How to use **tuples** for small groups of values that do not change.
- How to use **sets** to remove duplicates and compare groups.
- How to save and load your data as **JSON**, the most common data format on the internet.
- How to build a new list from an old one in a single line (**comprehensions**).

## Files, in order

1. [dictionaries.md](dictionaries.md)
2. [tuples-and-sets.md](tuples-and-sets.md)
3. [json.md](json.md)
4. [comprehensions.md](comprehensions.md)

Take your time with dictionaries. They are the most important topic of this module, and you will use them in every module that follows.

## You are ready for the next module when

- [ ] You can create a dictionary, read a value, add a new key and change an existing one.
- [ ] You can explain the difference between `contacts["Ana"]` and `contacts.get("Ana")`.
- [ ] You can loop over a dictionary with `.items()` and print every key and value.
- [ ] You can count how many times each word appears in a list, using a dictionary.
- [ ] You can store a list of records (a list of dictionaries) and find one by name.
- [ ] You can save a list of dictionaries to a `.json` file and load it back.
- [ ] You can turn a `for` loop with `.append()` into a list comprehension, and back.

**Next:** [Dictionaries](dictionaries.md)
