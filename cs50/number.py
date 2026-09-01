def main():
    x = get_int()
    print(f"You entered: {x}")


def get_int():
    while True:
        try:
            x = int(input("Enter an integer: "))
            return x
        except ValueError:
            pass

main()

