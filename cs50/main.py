def main():
    hello()

def hello(to = "world"):
    name = input("What is your name? ").strip().title()
    print("hello, " + name + "!")


main()
