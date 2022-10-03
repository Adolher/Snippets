my_list = [0, 1, 2, 3]
my_iter_list = iter(my_list)
print(dir(my_iter_list))
print(my_iter_list.__next__())
print(my_iter_list.__next__())
print(my_iter_list.__next__())
print(my_iter_list.__next__())
print(my_iter_list.__next__())