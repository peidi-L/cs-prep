# names = []

# for _ in range(3):
#     name = input("What's your name? ")
#     names.append(name)

# for name in names:
#     print(f"hello, {name}")

# name = input("What's your name? ")

# file = open("names.txt", "a")
# file.write(name + "\n")
# file.close()

# with open("names.txt", "r") as file:
#     for line in file:
#         print(f"hello, {line.rstrip()}")

# names = []

# with open("names.txt", "r") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names, reverse=True):
#     print(f"hello, {name}")

with open("names.txt", "r") as file:
    for line in sorted(file):
        print(f"hello, {line.rstrip()}")

