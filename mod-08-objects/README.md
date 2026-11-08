# Module 08: Objects

So far, your programs keep data in variables, lists and dictionaries, and keep behavior in functions. That works, but as a program grows, the data and the functions that work on it drift apart. In this module you learn to keep them together, in **objects**.

Objects are how most real Python programs are organized. They are also how the final project represents a ceramic piece: one object that knows its name, its clay, its current stage, and how to move to the next stage.

## What you will learn

- What a class is, and what an object is
- How to give an object data (attributes) and behavior (methods)
- How to make an object print nicely
- How to protect an object from invalid changes with `raise`
- How to save an object as a dictionary (and JSON) and load it back
- When to use a class and when a simple dictionary is enough
- How one class can build on another (inheritance), and when not to do that

## Files, in order

1. [classes.md](classes.md): classes, objects, attributes, methods, a status that only moves forward
2. [inheritance.md](inheritance.md): subclasses, `super()`, overriding, `isinstance`

## You are ready for the next module when you can...

- [ ] Explain the difference between a class and an object with your own analogy
- [ ] Write a class with `__init__`, two attributes and one method, without looking
- [ ] Explain what `self` is in one sentence
- [ ] Make a method refuse an invalid change using `raise ValueError(...)`
- [ ] Convert an object to a dictionary and create an object from a dictionary
- [ ] Say when you would NOT use inheritance

**Start here:** [classes.md](classes.md)
