from abc import ABC, abstractmethod
from organs import *
from tail_secondary import *
from mixins import *


class BaseClass(ABC):

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def num_legs(self):
        pass


class Characteristics(BaseClass):  # single inheritance
    def __init__(self, *args):  # variable number of arguments
        expected_args = 3
        if len(args) != expected_args:
            raise ValueError(f"Expected {expected_args} arguments, but got {len(args)}.")

        colors, num_legs, tail_length = args
        self.color = colors
        self.organs = {
            "Heart": Heart(),
            "Brain": Brain(),
        }
        self.tail = Tail(tail_length)  # aggregate


    def __repr__(self):
        pass

    def __str__(self):
        pass


class Animal(Characteristics, SoundMixin):  # multiple inheritance
    def __init__(self, name, colors, num_legs, tail):
        self.name = name
        super().__init__(colors, num_legs, tail)

    def __repr__(self):  # overriding
        return f"{self.organs.get( "Brain" )}"

    def __str__(self):  # overriding
        return (
            f"{self.tail}\n"
            f"His name is {self.name},"
            f"He has a {self.color} color,"
            f"He has {self.num_legs} legs."
            f"{self.organs.get('Heart')}"
        )


class Cat(Animal):  # Multilevel inheritance
    def __init__(self, name, colors, num_legs, tail):
        self.name = name
        super().__init__(name, colors, num_legs, tail)
        self.__legs = num_legs  # private

    @property
    def num_legs(self):  # encapsulation get
        return self.__legs

    @num_legs.setter  # encapsulation set validation
    def num_legs(self, values):
        name_of_creator, new_num_of_legs = values
        list1 = ["nika", "beka", "giorgi", "nini", "marie", "nino"]
        if name_of_creator in list1:
            self.__legs = new_num_of_legs
        else:
            raise f"Choose correct name of Creator"
    def get_name(self):
        print(f"my name is {self.name}")
    def make_sound(self, sound):
        return f" The  {self.name} Sound is '{sound}"

firstname = str(input("Enter the name of the animal "))
color = str(input(f"Enter the color of {firstname} "))
number_legs = int(input(f"Enter the number of legs for {firstname} "))
tail_secondary = int(input(f"Enter the length of tail for {firstname}"))
tob = Cat(firstname, color, number_legs, tail_secondary,)
tob.wings = Wings()  # Runtime
print(tob.wings.get_wings(4))
print(tob.make_sound("MIAU"))
change_legs = input(f' {tob.__str__()} \n Do you want to change the number of legs for {firstname}, Yes or No ')

# Error-flow

try:
    if change_legs not in ["Yes", "No"]:
        raise ValueError("Please enter 'Yes' or 'No' correctly")

    elif change_legs == "Yes":
        creator_name = input("Please enter the name of creators from Group III: ")
        new_num_of_legs_secondary = int(input("Please enter the number of legs: "))
        tob.num_legs = (creator_name, new_num_of_legs_secondary)
        print(tob.__str__())

    else:
        print("No changes made.")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"An error occurred Because you entered wrong name of Creator: {e}")