class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print("{} is eating food".format(self.name))

class Dog(Animal):
    def bark(self):
        print("Bark")

class Cat(Animal):
    def meow(self):
        print("Meow")

my_cat = Cat("Maya")
my_cat.eat()
my_cat.meow()
your_dog = Dog("Rudi")
your_dog.eat()
your_dog.bark()