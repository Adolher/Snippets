l = [0, 1, 2, 3, 4]
try:
    l.remove(6)
except ValueError as e:
    print(e)