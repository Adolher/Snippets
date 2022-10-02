class School:
    def __init__(self, name, level, numbers_of_students) -> None:
        self.name = name
        self.level = level
        self.__numbers_of_students = numbers_of_students

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level
    def set_level(self, level):
        levels = ["primary", "middle", "high"]
        if level in levels:
            self.level = level
        else:
            TypeError

    def get_numbers_of_students(self):
        return self.__numbers_of_students
    def  set_numbers_of_students(self, number):
        if isinstance(number, int):
            self.__numbers_of_students = number
        else:
            raise TypeError

    def __repr__(self) -> str:
        msg = f"A {self.get_level()} school named {self.get_name()} with {self.get_numbers_of_students()} students"
        return msg


class PrimarySchool(School):
    def __init__(self, name, numbers_of_students, pickup_policy) -> None:
        super().__init__(name, "primary", numbers_of_students)
        self.pickup_policy = pickup_policy

    def get_pickup_policy(self):
        return self.pickup_policy

    def __repr__(self) -> str:
        msg = super().__repr__() + "\n" + self.get_pickup_policy()
        return msg

class MiddleSchool(School):
    def __init__(self, name, numbers_of_students) -> None:
        super().__init__(name, "middle", numbers_of_students)


class HighSchool(School):
    def __init__(self, name, numbers_of_students, sports_teams) -> None:
        super().__init__(name, "high", numbers_of_students)
        self.sports_teams = sports_teams

    def get_sports_teams(self):
        return self.sports_teams

    def __repr__(self) -> str:
        teams_str = ""
        for team in self.sports_teams:
            if team == self.sports_teams[-1]:
                teams_str += team + "."
            elif team == self.sports_teams[-2]:
                teams_str += team + " and "
            else:
                teams_str += team + ", "
        msg = super().__repr__() + "\nOur sprorts teams are: " + teams_str
        return msg

h = HighSchool("Hugo", 359, ["Basketball", "Judo", "Volleyball"])

print(h)