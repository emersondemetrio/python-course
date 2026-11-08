# Inheritance

> **In one sentence:** inheritance lets a new class start with everything another class already has, and then add or change only what is different.

## Why it matters

Sometimes you have two kinds of things that are almost the same. A store sells products, and some products are food (they have an expiration date) while others are not. Without inheritance, you would copy the whole `Product` class into a `Food` class and keep both copies in sync forever. With inheritance, `Food` reuses `Product` and only adds the expiration date. You will also see inheritance all the time in libraries: many tools ask you to "create a class that inherits from ours".

## Analogy

Think of a **basic recipe and its variations**. You have a recipe for plain bread. A cheese bread is "plain bread, plus cheese". Nobody rewrites the whole bread recipe on the cheese bread card: the card says "follow the plain bread recipe, then add 100 g of cheese before baking".

In Python, plain bread is the **parent class** (also called *base class* or *superclass*). Cheese bread is the **child class** (also called *subclass*). The child **inherits** everything from the parent and then adds or changes some steps.

A quick test to know if inheritance fits: say the sentence "a **child** is a **parent**". "Cheese bread is a bread": yes. "Food is a product": yes. "A car is an engine": no (a car **has** an engine), so no inheritance there.

## The idea, step by step

### A parent class

Let's start with a simple product:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        return f"{self.name}: ${self.price}"

pen = Product("pen", 1.5)
print(pen.describe())
```

Output:

```text
pen: $1.5
```

### A child class

To create a class that inherits, put the parent's name in parentheses after the new class name:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        return f"{self.name}: ${self.price}"

class Food(Product):
    pass

bread = Food("bread", 3.0)
print(bread.describe())
```

Output:

```text
bread: $3.0
```

`class Food(Product):` reads as "Food is a kind of Product". The body is just `pass` (which means "nothing here"), yet `Food` already has `__init__`, `name`, `price` and `describe()`: it inherited all of them.

### Adding something new with `super().__init__`

Food needs an extra attribute: the expiration date. The child gets its own `__init__`, and inside it, asks the parent to do its part first:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        return f"{self.name}: ${self.price}"

class Food(Product):
    def __init__(self, name, price, expires):
        super().__init__(name, price)
        self.expires = expires

milk = Food("milk", 1.2, "2026-12-01")
print(milk.name, milk.price, milk.expires)
```

Output:

```text
milk 1.2 2026-12-01
```

`super()` means "the parent class". So `super().__init__(name, price)` runs the parent's `__init__`, which stores `name` and `price`. Then the child stores what is new. This is the "follow the plain bread recipe, then add cheese" step.

### Changing a behavior: overriding

If the child writes a method with the same name as the parent's, the child's version wins. This is called **overriding**.

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        return f"{self.name}: ${self.price}"

class Food(Product):
    def __init__(self, name, price, expires):
        super().__init__(name, price)
        self.expires = expires

    def describe(self):
        return f"{self.name}: ${self.price} (expires {self.expires})"

items = [Product("pen", 1.5), Food("milk", 1.2, "2026-12-01")]
for item in items:
    print(item.describe())
```

Output:

```text
pen: $1.5
milk: $1.2 (expires 2026-12-01)
```

Look at the loop: it calls `describe()` on every item without caring which class it is. Each object answers in its own way. This is one of the most useful ideas in programming with objects.

### Reusing the parent inside an override

The `Food` version of `describe` repeats the parent's text. You can reuse it with `super()` again:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        return f"{self.name}: ${self.price}"

class Food(Product):
    def __init__(self, name, price, expires):
        super().__init__(name, price)
        self.expires = expires

    def describe(self):
        basic = super().describe()
        return f"{basic} (expires {self.expires})"

print(Food("milk", 1.2, "2026-12-01").describe())
```

Output:

```text
milk: $1.2 (expires 2026-12-01)
```

Now if you change how the parent describes products, food changes too.

### Checking the kind of object: `isinstance`

`isinstance(object, Class)` answers `True` or `False`: "is this object a kind of this class?". A child object also counts as its parent:

```python
class Product:
    pass

class Food(Product):
    pass

pen = Product()
milk = Food()
print(isinstance(milk, Food))
print(isinstance(milk, Product))
print(isinstance(pen, Food))
```

Output:

```text
True
True
False
```

Milk is food, and food is a product, so milk is also a product. A pen is a product, but not food.

You will use `isinstance` mostly when catching errors (all exceptions are classes that inherit from `Exception`) and occasionally when a list mixes different kinds of objects. If you find yourself writing many `if isinstance(...)` checks, it usually means you should override a method instead.

### When NOT to use inheritance

Inheritance is powerful, and beginners tend to use it too much. Prefer simple solutions:

- **If only a value is different, use an attribute, not a subclass.** A small and a large coffee are not different classes; they are one `Order` class with a `size` attribute.
- **If it is "has a", not "is a", store an object inside another.** An order has a customer; it is not a customer. Write `self.customer = customer`.
- **Keep it shallow.** One level (parent and child) is usually enough. Long chains (`A` → `B` → `C` → `D`) are hard to read, because to understand `D` you have to read all four classes.

A good rule: start without inheritance. Add it only when you notice two classes that are copies of each other with a small difference.

## Common mistakes

### Forgetting to call `super().__init__`

<!-- error -->
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Food(Product):
    def __init__(self, name, price, expires):
        self.expires = expires

milk = Food("milk", 1.2, "2026-12-01")
print(milk.name)
```

```text
AttributeError: 'Food' object has no attribute 'name'
```

When the child has its own `__init__`, the parent's `__init__` does NOT run by itself. Nobody stored `name` and `price`. Fix: add `super().__init__(name, price)` as the first line of the child's `__init__`.

### Passing `self` to `super().__init__`

<!-- error -->
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Food(Product):
    def __init__(self, name, price, expires):
        super().__init__(self, name, price)
        self.expires = expires

milk = Food("milk", 1.2, "2026-12-01")
```

```text
TypeError: Product.__init__() takes 3 positional arguments but 4 were given
```

`super()` already knows which object it is working on, so `self` is passed automatically. Writing it again sends one argument too many. Fix: `super().__init__(name, price)`.

### Using inheritance for "has a"

<!-- no-verify -->
```python
class Customer:
    def __init__(self, name):
        self.name = name

class Order(Customer):   # an order is NOT a customer
    def __init__(self, name, item):
        super().__init__(name)
        self.item = item
```

This runs, but the design is wrong, and it will confuse you later (does an order have a phone number? an order history?). An order **has** a customer. Store it as an attribute instead:

```python
class Customer:
    def __init__(self, name):
        self.name = name

class Order:
    def __init__(self, customer, item):
        self.customer = customer
        self.item = item

ana = Customer("Ana")
order = Order(ana, "latte")
print(order.customer.name, order.item)
```

```text
Ana latte
```

## Exercises

### Predict the output

#### Exercise 1: Who answers?

```python
class Animal:
    def sound(self):
        return "..."

class Dog(Animal):
    def sound(self):
        return "Woof"

class Fish(Animal):
    pass

for pet in [Dog(), Fish()]:
    print(pet.sound())
```

<details>
<summary>Show answer</summary>

```text
Woof
...
```

`Dog` overrides `sound`. `Fish` does not, so it uses the parent's version.

</details>

#### Exercise 2: isinstance

```python
class Vehicle:
    pass

class Bike(Vehicle):
    pass

bike = Bike()
car = Vehicle()
print(isinstance(bike, Vehicle), isinstance(car, Bike))
```

<details>
<summary>Show answer</summary>

```text
True False
```

Every bike is a vehicle, but not every vehicle is a bike.

</details>

### Fix the bug

#### Exercise 3: The missing title

This should print `Podcast: Coffee Talk, 45 min`. Find and fix the bug.

<!-- error -->
```python
class Media:
    def __init__(self, title):
        self.title = title

class Podcast(Media):
    def __init__(self, title, minutes):
        self.minutes = minutes

    def describe(self):
        return f"Podcast: {self.title}, {self.minutes} min"

episode = Podcast("Coffee Talk", 45)
print(episode.describe())
```

```text
AttributeError: 'Podcast' object has no attribute 'title'
```

<details>
<summary>Show answer</summary>

```python
class Media:
    def __init__(self, title):
        self.title = title

class Podcast(Media):
    def __init__(self, title, minutes):
        super().__init__(title)
        self.minutes = minutes

    def describe(self):
        return f"Podcast: {self.title}, {self.minutes} min"

episode = Podcast("Coffee Talk", 45)
print(episode.describe())
```

```text
Podcast: Coffee Talk, 45 min
```

The child's `__init__` must call the parent's with `super().__init__(title)`.

</details>

### Write it

#### Exercise 4: Employees and managers

Write a class `Employee` with `name` and `salary`, and a method `yearly()` that returns `salary * 12`. Then write `Manager(Employee)` that also receives a `bonus` and overrides `yearly()` to return the parent's yearly value plus the bonus. Print the yearly value of an employee with salary 3000 and of a manager with salary 5000 and bonus 10000.

<details>
<summary>Hint</summary>

Inside `Manager.yearly`, use `super().yearly()` to get the normal yearly value.

</details>

<details>
<summary>Show answer</summary>

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def yearly(self):
        return self.salary * 12

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def yearly(self):
        return super().yearly() + self.bonus

print(Employee("Bia", 3000).yearly())
print(Manager("Caio", 5000, 10000).yearly())
```

```text
36000
70000
```

</details>

#### Exercise 5: Inherit or not?

For each pair, decide: should the second be a subclass of the first, an attribute of it, or neither? Write your answer as a sentence.

1. `Book` and `Ebook`
2. `Car` and `Wheel`
3. `Coffee` and `LargeCoffee`

<details>
<summary>Show answer</summary>

1. **Subclass.** An ebook is a book, with extra things like file size.
2. **Attribute.** A car has wheels; a wheel is not a car. Use `self.wheels = [...]`.
3. **Neither.** A large coffee is the same thing with a different value. Use one `Coffee` class with a `size` attribute.

</details>

## Review

#### Review 1: Classes (previous file)

What does this print?

```python
class Lamp:
    def __init__(self):
        self.on = False

    def toggle(self):
        self.on = not self.on

lamp = Lamp()
lamp.toggle()
lamp.toggle()
lamp.toggle()
print(lamp.on)
```

<details>
<summary>Show answer</summary>

```text
True
```

Each `toggle()` flips the value: False → True → False → True.

</details>

#### Review 2: Modules (module 07)

You have a file `shop.py` with a class `Product` in it. Write the line that imports the class into another file in the same folder.

<details>
<summary>Show answer</summary>

<!-- no-verify -->
```python
from shop import Product
```

`shop` is the file name without `.py`; `Product` is the name inside it.

</details>

## Recap

- `class Child(Parent):` creates a class that inherits everything from `Parent`.
- In the child's `__init__`, call `super().__init__(...)` first so the parent can store its part.
- Writing a method with the same name in the child **overrides** the parent's version; `super().method()` reuses it.
- `isinstance(obj, Class)` checks the kind of an object; a child object counts as its parent too.
- Use inheritance only for "is a". For "has a", store an object as an attribute. When in doubt, keep it simple.

**Next:** [Module 09: Databases](../mod-09-databases/README.md)
