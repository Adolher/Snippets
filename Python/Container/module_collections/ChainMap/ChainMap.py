from collections import ChainMap
x = dir(dict)

b = dir(ChainMap)
for a in b:
    if not a.startswith("_"): # and a not in x:
        s = f".{a}()"
        if a in x:
            print("from dict -> ", end="")
        print(s)