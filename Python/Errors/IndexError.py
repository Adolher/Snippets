l = [0, 1, 2, 3, 4]

try:
    print(l[7])
except IndexError as e:
    print(e)