
def output(x):
    if not str(x).startswith("#"):
        msg = "Type: {:<25} Example: {}"
        print(msg.format(str(type(x)), x))
    else:
        msg = "\n- - - {} - - -"
        print(msg.format(x.replace("#","")))

# Text Type
output("#Text Type")
output("Hello")

# Numeric Types
output("#Numeric Types")
output(5)
output(5.2)
output(5+8j)
# Sequence Types
output("#Sequence Types")
l = [6, "Hello", True]
output(l)

t = ("Hello", False, 5.9)
output(t)

output(range(10))

# Mapping Type
output("#Mapping Type")
d = {"a": 1, "b": 2}
output(d)

# Set Types
output("#Set Types")
s = {1,2,3,4}
output(s)

fs = frozenset(s)
output(fs)

# Boolean Type
output("#Boolean Type")
output(True)

# Binary Types
output("#Binary Types")
output(b"15.9")
output(bytearray(15))
output(memoryview(bytes(5)))

# None Type'
output("#None Type")
output(None)






