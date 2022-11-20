from collections import Counter
x = dir(dict)

b = dir(Counter)
for a in b:
    if not a.startswith("_"):
        s = f".{a}()"
        if a in x:
            print("from dict -> ", end="")
        print(s)
