# PEP8 https://peps.python.org/pep-0008/#programming-recommendations
# Always use a def statement instead of an assignment statement that binds a lambda expression directly to an identifier

add = lambda x, y: x + y
print(add(5,7))

max = lambda x, y: x if x > y else y
print(max(5,7))