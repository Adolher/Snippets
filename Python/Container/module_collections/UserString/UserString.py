from collections import UserString
str_name = 'python powered patterned products'
str_word = 'patterned '


class SubtractString(UserString):
  def __sub__(self, subtrahend):
    if isinstance(subtrahend, SubtractString):
        if subtrahend.data in self.data:
            return self.data.replace(subtrahend.data,"")
    elif isinstance(subtrahend, str):
        if subtrahend in self.data:
            return self.data.replace(subtrahend,"")

a = SubtractString(str_name)
b = SubtractString(str_word)
d = "powered "
c = a - b
print(f"{c} = {a} - {b}")

c = a - d
print(f"{c} = {a} - {d}")