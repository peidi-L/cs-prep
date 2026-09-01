# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin"
# }

# print(students[0])  # Hermione
# print(students[1])  # Harry
# print(students[2])  # Ron
# print(students[3])  # Draco
# print(students["Hermione"])  # Gryffindor
# print(students["Harry"])  # Gryffindor
# print(students["Ron"])  # Gryffindor
# print(students["Draco"])  # Slytherin

# for student in students:
#     print(student, students[student], sep=", ")

# for i in range(len(students)):
#     print(i+1, students[i])

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": "Serpent"}
]
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
