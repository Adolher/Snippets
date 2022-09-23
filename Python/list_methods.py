my_list = []
print(my_list)
my_list.append("first entry")
print(my_list)
my_list.append("second entry")
print(my_list)
my_list.insert(2, {"entry", 7.9})
print(my_list)
my_list.remove("first entry")
print(my_list)

my_second_list = [False, 6]
my_final_list = my_list + ["a_word", (8.76, "tall")] + my_second_list
print(my_final_list)
i_forgot = "my_name"
my_final_list += [i_forgot]
print(my_final_list)
print(my_final_list.count("a_word"))
popped_entry = my_final_list.pop()
print(popped_entry, end="\t")
print(my_final_list)
popped_entry = my_final_list.pop(2)
print(popped_entry, end="\t")
print(my_final_list)
range_list = range(8)
print(range_list)
print(list(range_list))
range_list = range(8,24)
print(range_list)
print(list(range_list))
range_list = range(5,50,7)
print(range_list)
print(len(range_list))
print(list(range_list))
print(len(my_final_list))
sliced_list = list(range_list)[3:]
print(sliced_list)
sliced_list = list(range_list)[1:5]
print(sliced_list)
word = "Feuerwehrautoreifen"
letter_list = list(word)
print(letter_list)
sorted_letters = sorted(letter_list)
print(sorted_letters)
print(letter_list.count("e"))
letter_list.sort()
print(letter_list)
letter_list.sort(reverse=True)
print(letter_list)
