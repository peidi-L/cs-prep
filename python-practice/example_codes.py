from __future__ import annotations

"""
Example Python Codes: Beginner to Master.

This is an offline study file. Read it from top to bottom when you want a
guided tour, or jump to a section when you want a quick reminder.

Run this file with:
    python example_codes.py

Most examples are wrapped in functions so you can read, edit, and run one
section at a time without the whole file becoming messy.

How to study with this file:
    1. Read the explanation above a function.
    2. Predict what the code will print or return.
    3. Run the file.
    4. Change a value and run it again.
    5. Try writing a tiny version from memory.

Important symbols you will see:
    =      stores a value in a variable
    ==     checks whether two values are equal
    !=     checks whether two values are different
    <=     less than or equal to
    >=     greater than or equal to
    []     list, index, or type hint
    {}     dictionary, set, or formatted string placeholder
    ()     function call or grouping
    :      starts an indented block
    #      starts a comment

Offline practice ideas:
    Beginner:
        - Change the names, numbers, and lists.
        - Write your own conditionals for weather, grades, or passwords.
        - Make a list of favorite foods and print each one.

    Intermediate:
        - Rewrite fizz_buzz without looking.
        - Make a function that counts vowels in a word.
        - Read this file and count how many times "return" appears.

    Object-oriented:
        - Add a transfer() method to BankAccount.
        - Make a Student dataclass with name, subject, and grade.
        - Add another Animal subclass.

    Advanced:
        - Write a generator that yields even numbers.
        - Make a decorator that measures how long a function takes.
        - Try calculating fibonacci(30), then remove lru_cache and compare.

    Master:
        - Explain binary search out loud without using code.
        - Draw recursive_permutations(["A", "B", "C"]) on paper.
        - Write tests before changing a function.
"""

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Iterable


# ---------------------------------------------------------------------------
# Beginner examples
# ---------------------------------------------------------------------------


def hello_world() -> None:
    """The smallest useful Python program.

    print() writes text to the screen.

    The -> None part is a type hint. It means this function does not return a
    useful value; it only does an action.
    """
    print("Hello, world!")


def variables_and_types() -> None:
    """Variables are names that store values.

    Python guesses the type from the value:
        "Ada" is a str, short for string
        36 is an int, short for integer
        1.65 is a float, short for floating-point number
        True is a bool, short for boolean
    """
    name = "Ada"
    age = 36
    height = 1.65
    is_programmer = True

    print(name)
    print(age)
    print(height)
    print(is_programmer)


def strings() -> None:
    """Strings are text values.

    You can join strings, change their case, measure their length, and pull out
    individual characters. Python indexes start at 0, so full_name[0] means the
    first character.
    """
    first_name = "Grace"
    last_name = "Hopper"
    full_name = f"{first_name} {last_name}"

    print(full_name.upper())
    print(full_name.lower())
    print(f"First letter: {full_name[0]}")
    print(f"Name length: {len(full_name)}")


def math_operations() -> None:
    """Python can do normal arithmetic.

    Operators:
        +   addition
        -   subtraction
        *   multiplication
        /   division, gives a float
        //  floor division, drops the decimal part
        %   modulo, gives the remainder
        **  exponent, meaning "to the power of"
    """
    a = 10
    b = 3

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a // b)
    print(a % b)
    print(a**b)


def conditionals(score: int) -> str:
    """Conditionals let your program choose between paths.

    if checks the first condition.
    elif means "else if" and checks another condition.
    else catches everything that did not match.

    This function returns a letter grade instead of printing it. Returning is
    useful because another part of the program can use the result.
    """
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def loops() -> None:
    """Loops repeat code.

    A for loop is best when you know what you are looping over.
    range(1, 6) creates the numbers 1, 2, 3, 4, 5.

    A while loop repeats as long as its condition is True. Be careful: if the
    condition never becomes False, the loop runs forever.
    """
    for number in range(1, 6):
        print(number)

    countdown = 3
    while countdown > 0:
        print(f"{countdown}...")
        countdown -= 1

    print("Go!")


def lists() -> None:
    """Lists store ordered collections.

    Lists are mutable, meaning you can change them after creating them.
    append() adds to the end.
    remove() deletes the first matching item.
    """
    fruits = ["apple", "banana", "cherry"]
    fruits.append("orange")
    fruits.remove("banana")

    for fruit in fruits:
        print(fruit)


def dictionaries() -> None:
    """Dictionaries store key-value pairs.

    Use a dictionary when each value has a label. Here, "name", "age", and
    "course" are keys. The values are the information connected to those keys.
    """
    student = {
        "name": "Maya",
        "age": 20,
        "course": "Computer Science",
    }

    print(student["name"])
    student["grade"] = "A"

    for key, value in student.items():
        print(f"{key}: {value}")


# ---------------------------------------------------------------------------
# Intermediate examples
# ---------------------------------------------------------------------------


def fizz_buzz(limit: int) -> list[str]:
    """Classic practice problem for loops and conditionals.

    The modulo operator (%) checks remainders:
        number % 3 == 0 means "number divides evenly by 3"

    The order matters. Numbers divisible by both 3 and 5 must be checked before
    checking only 3 or only 5.
    """
    result = []

    for number in range(1, limit + 1):
        if number % 3 == 0 and number % 5 == 0:
            result.append("FizzBuzz")
        elif number % 3 == 0:
            result.append("Fizz")
        elif number % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(number))

    return result


def list_comprehensions() -> None:
    """A list comprehension builds a list in one compact line.

    Long version:
        squares = []
        for number in numbers:
            squares.append(number ** 2)

    Short version:
        squares = [number ** 2 for number in numbers]
    """
    numbers = [1, 2, 3, 4, 5]
    squares = [number**2 for number in numbers]
    even_squares = [number**2 for number in numbers if number % 2 == 0]

    print(squares)
    print(even_squares)


def functions_with_defaults(name: str, greeting: str = "Hello") -> str:
    """Functions can have default argument values.

    If the caller does not provide greeting, Python uses "Hello".
    This makes functions easier to reuse.
    """
    return f"{greeting}, {name}!"


def args_and_kwargs(*args: int, **kwargs: str) -> None:
    """*args and **kwargs collect flexible arguments.

    *args collects extra positional arguments into a tuple.
    **kwargs collects extra named arguments into a dictionary.

    This is common in library code, decorators, and wrapper functions.
    """
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")


def error_handling(text: str) -> int | None:
    """try/except handles errors without crashing the whole program.

    int("42") works, but int("hello") raises ValueError.
    The except block lets us respond calmly when bad input appears.
    """
    try:
        return int(text)
    except ValueError:
        print(f"Cannot convert {text!r} to an integer.")
        return None


def file_reading_example() -> None:
    """Files are usually handled with pathlib.Path.

    __file__ means "the current Python file".
    read_text() opens, reads, and closes the file for us.
    """
    path = Path(__file__)
    text = path.read_text()
    print(f"This file has {len(text.splitlines())} lines.")


def set_examples() -> None:
    """Sets store unique values and are great for comparisons.

    Set operators:
        |   union, all items from both sets
        &   intersection, items found in both sets
        -   difference, items in the left set but not the right set
    """
    python_students = {"Alex", "Jordan", "Sam"}
    java_students = {"Jordan", "Taylor", "Riley"}

    print(python_students | java_students)
    print(python_students & java_students)
    print(python_students - java_students)


def tuple_unpacking() -> None:
    """Tuples are ordered collections that are usually not changed.

    Unpacking lets you assign several variables at once:
        x, y = point

    This is common with coordinates, database rows, and function returns.
    """
    point = (4, 7)
    x, y = point
    print(f"x={x}, y={y}")


# ---------------------------------------------------------------------------
# Object-oriented programming
# ---------------------------------------------------------------------------


class BankAccount:
    """A class is a blueprint for objects.

    This class creates bank account objects. Each account has its own owner and
    balance. The methods are functions that belong to the object.

    self means "this specific object". If you make two BankAccount objects,
    each one has a different self.
    """

    def __init__(self, owner: str, balance: float = 0) -> None:
        """__init__ runs automatically when a new object is created."""
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Add money to this account.

        Raising ValueError is a clean way to say "the caller gave me an
        impossible value".
        """
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Remove money from this account if enough money exists."""
        if amount > self.balance:
            raise ValueError("Not enough money.")
        self.balance -= amount

    def __str__(self) -> str:
        """__str__ controls what print(account) displays."""
        return f"{self.owner}: ${self.balance:.2f}"


@dataclass
class Book:
    """dataclass saves you from writing boring setup code.

    Python automatically creates an __init__ method for title, author, and
    pages. Dataclasses are useful for objects that mostly store data.
    """

    title: str
    author: str
    pages: int

    def summary(self) -> str:
        return f"{self.title} by {self.author}, {self.pages} pages"


class Animal:
    """Parent class used to show inheritance."""

    def speak(self) -> str:
        return "Some sound"


class Dog(Animal):
    """Dog inherits from Animal but replaces speak()."""

    def speak(self) -> str:
        return "Woof!"


class Cat(Animal):
    """Cat also inherits from Animal and gives its own speak()."""

    def speak(self) -> str:
        return "Meow!"


def polymorphism_example(animals: list[Animal]) -> None:
    """Polymorphism means different objects share the same interface.

    Dog, Cat, and Animal all have speak(), so the loop can call speak() without
    caring which exact type it has.
    """
    for animal in animals:
        print(animal.speak())


# ---------------------------------------------------------------------------
# Advanced examples
# ---------------------------------------------------------------------------


def generator_example(limit: int) -> Iterable[int]:
    """Generators produce values one at a time.

    yield is like return, but the function can continue later. This saves memory
    when you have lots of values because Python does not build the whole list at
    once.
    """
    for number in range(limit):
        yield number * number


def lambda_and_sorting() -> None:
    """lambda creates a small anonymous function.

    sort(key=...) tells Python what value to sort by. Here, each person is a
    dictionary, and the lambda pulls out the "age" value.
    """
    people = [
        {"name": "Zoe", "age": 22},
        {"name": "Amir", "age": 19},
        {"name": "Lina", "age": 25},
    ]

    people.sort(key=lambda person: person["age"])
    print(people)


def decorator(func):
    """A decorator wraps one function with another function.

    Decorators are useful when many functions need the same extra behavior,
    like logging, timing, authentication, or caching.

    This decorator prints before and after the wrapped function runs.
    """

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result

    return wrapper


@decorator
def decorated_greeting(name: str) -> str:
    """This function is automatically passed through decorator()."""
    return f"Hi, {name}!"


@lru_cache(maxsize=None)
def fibonacci(number: int) -> int:
    """Recursive Fibonacci with caching.

    Recursion means a function calls itself.

    Without caching, fibonacci(40) repeats huge amounts of work. lru_cache
    remembers answers it has already calculated, which makes the function much
    faster.
    """
    if number < 2:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


def context_manager_example() -> None:
    """A context manager handles setup and cleanup.

    The with statement closes the file automatically, even if something goes
    wrong while writing. This pattern appears in files, database connections,
    locks, and network resources.
    """
    path = Path("temporary_example.txt")

    with path.open("w") as file:
        file.write("Python closes this file automatically.\n")

    print(path.read_text().strip())
    path.unlink()


def command_router_example(command: str) -> str:
    """Route a command string to the correct response.

    This is a simple version of command handling. Larger programs might use a
    dictionary of functions, classes, or a command framework instead.
    """
    command = command.lower()

    if command == "start":
        return "Starting program..."
    if command == "stop":
        return "Stopping program..."
    if command == "help":
        return "Available commands: start, stop, help"
    return "Unknown command."


# ---------------------------------------------------------------------------
# Master-level patterns
# ---------------------------------------------------------------------------


def binary_search(numbers: list[int], target: int) -> int:
    """Search a sorted list efficiently.

    Binary search only works when the list is sorted. It repeatedly cuts the
    search area in half, which is much faster than checking every item.

    It returns the index of the target, or -1 if the target is missing.
    """
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle
        if numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def recursive_permutations(items: list[str]) -> list[list[str]]:
    """Return every possible ordering of the input items.

    This demonstrates recursive thinking:
        1. Pick one item to go first.
        2. Find all permutations of the remaining items.
        3. Attach the chosen first item to each smaller permutation.

    Recursion always needs a base case. Here, a list with 0 or 1 items already
    has only one possible ordering.
    """
    if len(items) <= 1:
        return [items]

    result = []

    for index, item in enumerate(items):
        remaining = items[:index] + items[index + 1 :]

        for permutation in recursive_permutations(remaining):
            result.append([item] + permutation)

    return result


def clean_data(rows: list[dict[str, str]]) -> list[dict[str, str | int]]:
    """Turn messy input data into cleaner data.

    Real programs often receive data as strings, with extra spaces or strange
    casing. This function:
        strip() removes outside spaces
        title() makes names look consistent
        int() converts text age into a number
        if age >= 18 filters out minors
    """
    cleaned = []

    for row in rows:
        name = row["name"].strip().title()
        age = int(row["age"])

        if age >= 18:
            cleaned.append({"name": name, "age": age})

    return cleaned


def simple_unit_test() -> None:
    """Tiny tests using assert.

    assert means "this must be true". If it is false, Python raises an
    AssertionError. Real projects often use pytest or unittest, but assert is
    perfect for small practice files.
    """
    assert conditionals(95) == "A"
    assert conditionals(72) == "C"
    assert binary_search([1, 3, 5, 7], 5) == 2
    assert binary_search([1, 3, 5, 7], 6) == -1
    print("All simple tests passed.")


def main() -> None:
    """Run a sample of the examples.

    The examples above are definitions. They do not do much until something
    calls them. main() is a common place to call functions in the order you want
    to demonstrate them.
    """
    hello_world()
    print(conditionals(88))
    print(fizz_buzz(15))
    print(functions_with_defaults("Python learner"))

    account = BankAccount("Nina", 100)
    account.deposit(50)
    account.withdraw(25)
    print(account)

    book = Book("Automate the Boring Stuff with Python", "Al Sweigart", 592)
    print(book.summary())

    polymorphism_example([Dog(), Cat(), Animal()])
    print(list(generator_example(5)))
    print(decorated_greeting("Coder"))
    print(fibonacci(10))
    print(command_router_example("help"))
    print(binary_search([2, 4, 6, 8, 10], 8))
    print(recursive_permutations(["A", "B", "C"]))

    rows = [
        {"name": "  ada ", "age": "36"},
        {"name": "max", "age": "17"},
        {"name": " grace", "age": "85"},
    ]
    print(clean_data(rows))

    simple_unit_test()


if __name__ == "__main__":
    main()
