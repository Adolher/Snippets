class AClass():
    def __init__(self) -> None:
        self.name = "public_Name"
        self._name = "protected Name"   # just a convention
        self.__name = "private Name"

    def get_private_name(self):
        return self.__name

a = AClass()

print(a.name)
print(a._name)

# print(a.__name)
# AttributeError: 'AClass' object has no attribute '__name'.

print(a.get_private_name())