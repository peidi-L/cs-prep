# def main():
#     print_column(3)

# def print_column(height):
#     print("#\n" * height, end="")

# main()

# def main():
#     print_row(4)

# def print_row(width):
#     print("?" * width)

def main():
    print_square(3)

def print_square(size):
    #for each row in the square
    for i in range(size):
        print_row(size)

    print()

def print_row(width):
    print("#" * width)

main()
