# class Student:
#     def __init__(self, name, house, patronus):
#         name = name.strip()
#         house = house.strip()
#         patronus = patronus.strip().lower()

#         if not name:
#             raise ValueError("Missing name")

#         valid_houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
#         if house not in valid_houses:
#             raise ValueError("Invalid house")

#         self.name = name
#         self.house = house
#         self.patronus = patronus

#     def __str__(self):
#         return f"{self.name} from {self.house} has a {self.patronus} patronus."

#     def charm(self):
#         if self.patronus == "stag":
#             return "🐴"
#         if self.patronus == "otter":
#             return "🦦"
#         if self.patronus == "jack russell terrier":
#             return "🐶"
#         return "✨"


# def main():
#     student = get_student()
#     print("Expeto Patronum!")
#     print(student.charm())
#     print(f"{student.name} from {student.house} has a {student.patronus} patronus.")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ")
#     return Student(name, house, patronus)


# if __name__ == "__main__":
#     main()

class Student:
    def __init__(self, name, house):
        self.name = name.strip()
        self.house = house.strip()


    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        valid_houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        if house not in valid_houses:
            raise ValueError("Invalid house")
        self._house = house

    def __str__(self):
        return f"{self.name} from {self._house}."

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

def main():
    student = Student.get()
    print(student)


@classmethod
def get(cls):
    name = input("Name: ")
    house = input("House: ")
    return cls(name, house)


if __name__ == "__main__":
    main()
