my_list = [0, 1, 2, 3]

my_iter_list = iter(my_list)

print(dir(my_iter_list))

for i in range(5):
    try:
        print(my_iter_list.__next__())
    except StopIteration as e:
        print(e)
        print(StopIteration)