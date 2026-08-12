"""Beginner Python exercises.

These replace the old scratch files with runnable functions you can test,
reuse, and rewrite from memory.
"""


def greeting(name: str) -> str:
    return f"Nice to meet you, {name}!"


def age_in_five_years(age: int) -> int:
    return age + 5


def add_numbers(first: int, second: int) -> int:
    return first + second


def is_even(number: int) -> bool:
    return number % 2 == 0


def sign_of_number(number: int) -> str:
    if number > 0:
        return "positive"
    if number < 0:
        return "negative"
    return "zero"


def divisible_by_three_and_five(number: int) -> bool:
    return number % 3 == 0 and number % 5 == 0


def check_password(password: str) -> bool:
    return password == "python123"


def largest_of_three(first: int, second: int, third: int) -> int:
    return max(first, second, third)


def classify_number(number: int) -> str:
    if number == 0:
        return "zero"

    parity = "even" if is_even(number) else "odd"
    sign = "positive" if number > 0 else "negative"
    return f"{sign} and {parity}"


def demo() -> None:
    print(greeting("Peidi"))
    print(f"In 5 years: {age_in_five_years(21)}")
    print(f"3 + 4 = {add_numbers(3, 4)}")
    print(f"10 is even: {is_even(10)}")
    print(f"-2 is {sign_of_number(-2)}")
    print(f"15 divisible by 3 and 5: {divisible_by_three_and_five(15)}")
    print(f"Password accepted: {check_password('python123')}")
    print(f"Largest: {largest_of_three(7, 3, 9)}")
    print(f"8 is {classify_number(8)}")


if __name__ == "__main__":
    demo()
