class Tail:
    def __init__(self, length):
        self.length = length
        self.list = ["Tiger", "Cat"]

    def __str__(self):
        self.choose_animal()
        if self.length < 20:
            return f" This Cat has {self.length} meters long tail"
        return f"This Tiger has {self.length} meters long tail"

    def choose_animal(self):
        if self.length > 20:
            print(f"This animal is {self.list[0]}")
        else:
            print(f"This animal is {self.list[1]}")


class Wings:
    @staticmethod
    def get_wings(num_wings):
        if num_wings == 2:
            return "It is Bird"
        elif num_wings > 4:
            return "It is Dinosaur"