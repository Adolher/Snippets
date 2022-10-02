class Animal:
    def __init__(self, name, sound="Grrr"):
        self.name = name
        self.sound = sound
    def eat(self):
        print("{} is eating food".format(self.name))
    def make_noise(self):
        print("{} makes {}".format(self.name, self.sound))

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Bark")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

my_cat = Cat("Maya")
my_cat.eat()
my_cat.make_noise()
your_dog = Dog("Rudi")
your_dog.eat()
your_dog.make_noise()