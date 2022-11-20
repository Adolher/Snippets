from collections import deque

b = dir(deque)

for a in b:
    if not a.startswith("_"):
        s = f".{a}()"
        print(s)
