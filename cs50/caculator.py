#x = int(input("Enter a number: "))
#y = int(input("Enter another number: "))
#3z = x + y
#3print(f"The two numbers are {x} and {y}, and their sum is {z}.")

#x = float(input("Enter a number: "))
#y = float(input("Enter another number: "))
#z = round(x + y)
#print(f"The two numbers are {x} and {y}, and their sum is {z:,}.")

def main():
    x = float(input("Enter a number: "))
    print(f"The square of {x} is {square(x)}.")

def square(n):
    return n * n

main()
