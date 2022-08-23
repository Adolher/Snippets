list = ["Index 0", "Index 1", "Index 2", "Index 3", "Index 4"]

for x in list:
  print(x)

for i in range(4):
  print(i)

zero_list = [[0 for y in range(6)] for x in range(4)]
for x in range(len(zero_list)):
    for y in range(len(zero_list[x])):
        print(zero_list[x][y], end=" ")
    print()
print(zero_list)


list = [ 1, 2, 3, 4, 5, 6]
print(list)

scaled_list = [ x*2 for x in list]
print(scaled_list)

scaled_odd = [ x*2 for x in list if x%2==0]
print(scaled_odd)

scaled_diff = [ x*2 if x%2==0 else x*7 for x in list]
print(scaled_diff)
