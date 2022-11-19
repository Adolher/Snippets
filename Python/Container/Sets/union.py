set_1 = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
set_2 = frozenset({2, 4, 6, 8, 10, 12, 14, 16, 18, 20})

set_3 = set_1.union(set_2)
print(set_3)    # set_3 becomes Type of left operand

set_1 = frozenset({3, 6, 9, 12, 15, 18, 21, 24, 27, 30})
set_2 = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

set_3 = set_1 | set_2
print(set_3)    # set_3 becomes Type of left operand