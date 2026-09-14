
import random


class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(f"{name} has been sorted into {random.choice(cls.houses)}!")


Hat.sort("Harry")
 