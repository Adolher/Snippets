o = {}

d = dir(dict)
print("Dictionary methods are: ")
count = 0
for i in range(len(d)):
    if not d[i].startswith("__"):
        count += 1
        if d[i] in o:
            x = o.get(d[i])
            for y in x:
                print(f"\n{count} -> {d[i]}", end=" ")
                print(f"-> |{y}|", end="")
        else:
            print(f"\n{count} -> {d[i]}", end=" ")