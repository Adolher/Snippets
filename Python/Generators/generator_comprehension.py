a_generator = (x + x for x in range(7))

print(a_generator)
for a in a_generator:
    print(a)