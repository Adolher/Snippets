import itertools

even = {2, 4, 6, 8, 10}
odd = [3, 5, 7, 9]

numbers = itertools.chain(even, odd)

for n in numbers:
    print(n)