import itertools

list = ["white", "red", "blue"]

result = itertools.combinations(list, 2)

for r1 in result:
    print(r1)
print()
result2 = itertools.combinations_with_replacement(list, 2)
for r in result2:
    print(r)