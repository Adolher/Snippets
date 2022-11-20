from collections import *
import collections

b = dir(collections)
for a in b:
    if not a.startswith("_"):
        print(a, type(eval(a)))
        s = f"dir({a})"
        x = eval(s)
        print("\t", end="")
        for y in x:
            if not y.startswith("_"):
                print(f"{y}", end=", ")
        print(end="\n\n")