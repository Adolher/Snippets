my_info = ("Jörg", 37, "Programmer")
print(my_info)
print(my_info[1])
name, age, occupation = my_info
print(name)
print(age)
print(occupation)
one_element_tuple = (4,)
print(one_element_tuple)

list_1 = [1, 2, 3, 4]
list_2 = [4, 3, 2, 1]
tup = zip(list_1, list_2)
print(tup)
list_3 = [list(entry) for entry in tup]
print(list_3)

my_info[1] = 27