set_example_1 = {"item1", "item2", "item3", "item3"}
a_list = ["item1", "item1", "item2", "item3"]
set_example_2 = set(a_list)
print(set_example_1)
print(set_example_2)    # duplicates are removed
print(dir(set_example_1))

set_example_1.add("item4")
print(set_example_1)
set_example_2.update([5, 9, True])
print(set_example_2)

set_example_1.remove("item4")
print(set_example_1)
try:
    set_example_1.remove("item4")
except KeyError as e:
    print(KeyError)
set_example_1.discard("item1")
print(set_example_1)
set_example_1.discard("item1")
print(set_example_1)

print(9 in set_example_2)
