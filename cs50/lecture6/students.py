# with open("students.csv") as file:
#     for line in file:
#         name, house, year = line.rstrip().split(",")
#         print(f"{name} is in {house} and is in year {year}.")

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house, year = line.rstrip().split(",")
#         students.append({"name": name, "house": house, "year": year})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']} and is in year {student['year']}.")

# import csv
# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}.")

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
