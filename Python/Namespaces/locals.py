l = locals().copy()
for k in l:
    print(f"{k}: {l[k]}")
print("\n")

def a_func(val1, val2):
    val3 = "a_value"
    l = locals().copy()
    for k in l:
        print(f"{k}: {l[k]}")
    print("\n")

a_func(8, "h")

l = locals().copy()
for k in l:
    print(f"{k}: {l[k]}")
print("\n")