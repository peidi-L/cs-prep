# Python Coding Practice

Use this document as a coding workout. For each exercise, create a `.py` file in this folder, write your solution, run it, and then test it with a few different inputs.

## Warmup

### 1. Greeting Program

Ask the user for their name and print:

```text
Hello, NAME! Welcome to Python practice.
```

Bonus: also ask for their favorite programming language.

### 2. Age Calculator

Ask the user for their birth year and calculate their age.

Example:

```text
Enter your birth year: 2005
You are about 21 years old.
```

### 3. Even or Odd

Ask the user for a number. Print whether the number is even or odd.

## Conditionals

### 4. Simple Grade Checker

Ask for a score from `0` to `100`, then print a grade:

- `90` or above: `A`
- `80` to `89`: `B`
- `70` to `79`: `C`
- `60` to `69`: `D`
- Below `60`: `F`

Bonus: handle invalid scores like `-5` or `120`.

### 5. Password Strength

Ask the user to enter a password.

Print:

- `Too short` if it has fewer than 8 characters
- `Good length` if it has 8 or more characters
- `Strong password` if it has 12 or more characters

## Loops

### 6. Countdown

Ask the user for a starting number and count down to `1`.

Example:

```text
5
4
3
2
1
Blast off!
```

### 7. Sum of Numbers

Ask the user for a positive number `n`.

Use a loop to calculate:

```text
1 + 2 + 3 + ... + n
```

Example:

```text
Enter n: 5
The sum is 15.
```

## Lists

### 8. Favorite Foods

Create an empty list. Ask the user to enter three favorite foods, then print the list.

Bonus: print each food on its own line.

### 9. Largest Number

Given this list:

```python
numbers = [12, 45, 7, 89, 23, 56]
```

Write code that finds and prints the largest number without using `max()`.

## Functions

### 10. Temperature Converter

Write a function called `celsius_to_fahrenheit(celsius)` that converts Celsius to Fahrenheit.

Formula:

```text
fahrenheit = celsius * 9 / 5 + 32
```

Test it with:

```python
print(celsius_to_fahrenheit(0))    # 32
print(celsius_to_fahrenheit(100))  # 212
```

### 11. Word Counter

Write a function called `count_words(sentence)` that returns how many words are in a sentence.

Example:

```python
count_words("Python is fun")  # 3
```

## Mini Projects

### 12. Number Guessing Game

Create a program where:

1. The computer stores a secret number.
2. The user guesses the number.
3. The program says `Too high`, `Too low`, or `Correct`.
4. The game repeats until the user guesses correctly.

Bonus: use `random.randint()` to choose the secret number.

### 13. To-Do List

Create a simple command-line to-do list.

The user should be able to:

- Add a task
- View all tasks
- Remove a task
- Quit the program

## Reflection

After each exercise, write short answers:

- What was easy?
- What was confusing?
- What did you learn?
- What would you try differently next time?

