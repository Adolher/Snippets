class Human:
    def __init__(self, name):
        self.name = name


class Adault(Human):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def say(self):
        print(f"I am {self.name} and i am {self.age} years old")


class Parent(Adault):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.number_of_childs = 3
    def say(self):
        super().say()
        print("and i am proud to be a parent of {} kids!".format(self.number_of_childs))

a_mom = Parent("Theresa", 37)
a_mom.say()