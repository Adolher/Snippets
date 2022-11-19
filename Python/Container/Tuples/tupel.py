my_info = ("Joerg", 37, "Programmer")
print("tupel is ", my_info)
print("second element of tupel is: ", my_info[1])
name, age, occupation = my_info
print("after unpacking the tupel: ")
print("\tname =", name)
print("\tage =", age)
print("\toccupation =", occupation)
one_element_tuple = (4,)
print("one_element_tuple: ",one_element_tuple)

list_1 = [1, 2, 3, 4]
list_2 = [4, 3, 2, 1]
tup = zip(list_1, list_2)
print("after zipping two lists: ", tup)
list_3 = tuple(entry for entry in tup)
print("after casting: ", list_3)

try:
    my_info[1] = 27
except TypeError as e:
    print("a tuple is UNCHANGEABLE")
    print("ERROR message is: ", e)

d = dir(tuple)
print("Tuple methods are: ")
for entry in d:
    if not entry.startswith("__"):
        print("\t",entry)