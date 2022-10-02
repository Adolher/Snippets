class AClass():
    def __init__(self, name) -> None:
        self.name = name
        self.__priv_var = None

    def __repr__(self) -> str:
        return f"{self.name} is {self.priv_var}"

    @property
    def priv_var(self):
        """Docstring for the 'priv_var' property"""
        return self.__priv_var

    @priv_var.setter
    def priv_var(self, new_var):
        if isinstance(new_var, int):
            self.__priv_var = new_var
    
    @priv_var.deleter
    def priv_var(self):
        del self.__priv_var

a = AClass("Horst")
print(a)
a.priv_var = 5.3    # do not set because 5.3 is no int
print(a)
a.priv_var = 9      # set __priv_var = 9
print(a)
print(a.priv_var)   # get __priv_var
del a.priv_var      # delete __priv_var
print(a)

