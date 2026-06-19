# print("Hello, World!")
# name = input("What is your name? ")
# print(f"Nice to meet you, {name}!")

# age = input("How old are you? ")
# future_age = int(age) + 5
# print(f"In 5 years, you will be {future_age} years old.")

# favourite_colour = input("What is your favourite colour? ")
# print(f"{name}, your favourite colour is {favourite_colour}.")

# num1 = int(input("Enter your first number: "))
# num2 = int(input("Enter your second number: "))
# print(f"{num1} + {num2} = {num1 + num2}")

# number = int(input("Please enter a number: "))
# if number % 2 == 0:
#     print(f"{number} is an even number.")
# else:
#     print(f"{number} is an odd number.")

# number = int(input("Please enter a number: "))
# if number > 0:
#     print(f"{number} is a positive number.")
# elif number < 0:
#     print(f"{number} is a negative number.")
# else:
#     print(f"{number} is zero.")

# from datetime import datetime

# current_year = datetime.now().year
# birth_year = int(input("What year were you born? "))

# age = current_year - birth_year

# print(f"You are about {age} years old.")


# num_1 = int(input("Please enter a number: "))
# num_2 = int(input("Please enter another number: "))

# print(f"{num_1} + {num_2} = {num_1 + num_2}")
# print(f"{num_1} - {num_2} = {num_1 - num_2}")
# print(f"{num_1} * {num_2} = {num_1 * num_2}")
# print(f"{num_1} / {num_2} = {num_1 / num_2}")

# number = int(input("Please enter a number: "))
# if number % 3 == 0:
#     print(f"{number} is divisible by 3.")
# else:
#     print(f"{number} is not divisible by 3.")
    
# number = int(input("Please enter a number: "))
# if number % 3 == 0 and number % 5 == 0:
#     print(f"{number} is divisible by both 3 and 5.")
# else:
#     print(f"{number} is not divisible by both 3 and 5.")

# trial = input("Please enter a password: ")
# if trial == "python123":
#     print("Access granted.")
# else:
#     print("Access denied.")

# num1 = int(input("Please enter your first number: "))
# num2 = int(input("Please enter your second number: "))
# num3 = int(input("Please enter your third number: "))

# if num1 >= num2 and num1 >= num3:
#     largest = num1
# elif num2 >= num1 and num2 >= num3:
#     largest = num2
# else:
#     largest = num3  

# print(f"The largest number is: {largest}")

number = int(input("Please enter a number: "))
if number > 0 and number % 2 == 0:
    print(f"{number} is positive and even.")
elif number > 0 and number % 2 != 0:
    print(f"{number} is positive and odd.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")
