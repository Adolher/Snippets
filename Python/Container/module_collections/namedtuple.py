from collections import namedtuple

Volume = namedtuple("Volume", ["width", "high", "deph"])

b = Volume(7,4,3)

for a in dir(b):
    if not a.startswith("_"):
        print(f"{a}",f"b.{a}","=", eval(f"b.{a}"))
        