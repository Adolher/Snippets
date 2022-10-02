class AClass():
    def __init__(self, name) -> None:
        self.name = name
        self.__priv_var = None

    def get_priv_var(self):
        return self.__priv_var

    def set_priv_var(self, new_var):
        if isinstance(new_var, int):
            self.__priv_var = new_var
        else:
            raise TypeError

    def delete_priv_var(self):
        del self.__priv_var
