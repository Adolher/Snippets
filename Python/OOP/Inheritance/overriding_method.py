class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print("{} is eating food".format(self.name))
    def make_noise(self):
        print("A noise")

class Dog(Animal):
    def make_noise(self):
        print("Bark")

class Cat(Animal):
    def make_noise(self):
        print("Meow")

my_cat = Cat("Maya")
my_cat.eat()
my_cat.make_noise()
your_dog = Dog("Rudi")
your_dog.eat()
your_dog.make_noise()