text = "This is an example"
print(f"original text: {text}")
spaced = "   This is an spaced example   "
print(f"spaced text: {spaced}")
to_format = "I am {}"
print(f"text for formatting: {to_format}")

def title(text):
    return text.title()
def upper(text):
    return text.upper()
def lower(text):
    return text.lower()
def split(text, v):
    return text.split(v)
def join(list, v):
    return v.join(list)
def strip(text):
    return text.strip()
def replace(text, o, n):
    return text.replace(o, n)
def find(text, v):
    return text.find(v)
def format(text, v):
    return text.format(v)

o = {"title": [title(text), ],
    "upper": [upper(text),],
    "lower": [lower(text),],
    "split": [split(text, " "), split(text, "a")],
    "join": [join(split(text, " "),",")],
    "strip": [strip(spaced),],
    "replace": [replace(text, "an", "no")],
    "find": [find(text, "a")],
    "format": [format(to_format, "proud")],
    }

d = dir(str)
print("String methods are: ")
count = 0
for i in range(len(d)):
    if not d[i].startswith("__"):
        count += 1
        if d[i] in o:
            x = o.get(d[i])
            for y in x:
                print(f"\n{count:>2} -> {d[i]:>18}", end=" ")
                print(f"-> |{y}|", end="")
        else:
            print(f"\n{count:>2} -> {d[i]:>18}", end=" ")
        
