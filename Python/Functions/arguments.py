
# positional arguments
def positional_arguments(x, y, z):
    msg="{:<35}"
    print(msg.format("positional_arguments(1, -1, 3)"), end=" -> ")
    print(f"x = {x:<4}| y = {y:<4}| z = {z:<4}")

positional_arguments(1, -1, 3)


# keyword arguments
def keyword_arguments(x, y, z):
    msg="{:<35}"
    print(msg.format("keyword_arguments(z=6, x=3, y=37)"), end=" -> ")
    print(f"x = {x:<4}| y = {y:<4}| z = {z:<4}")

keyword_arguments(z=6, x=3, y=37)


# default arguments
def default_arguments(x, y, z=8):
    msg="{:<35}"
    print(msg.format("default_arguments(5, 7)"), end=" -> ")
    print(f"x = {x:<4}| y = {y:<4}| z = {z:<4}")

default_arguments(5, 7)


# positional argument packing
def argument_packing(*args):
    print("\n- - - positional argument packing - - -")
    print("Type of args: ", type(args))
    print("Value of args: ", args)
    print("argument_packing(\"Hi\", True, 6.6)", end=" -> ")
    for arg in args:
        print(arg, end=" ")
    print()

argument_packing("Hi", True, 6.6)


# keyword argument packing
def keyword_argument_packing(**kwargs):
    print("\n- - - keyword argument packing - - -")
    print("Type of kwargs: ", type(kwargs))
    print("Value of kwargs: ", kwargs)
    print("keyword_argument_packing(quark1=\"Hi\", quark2=True, quark3=6.6)", end=" -> ")
    for kwarg in kwargs:
        print(kwarg, end=" ")
    print()

keyword_argument_packing(quark1="Hi", quark2=True, quark3=6.6)


# mixing args, *args, kwargs and **kwargs
def print_animals(animal1, animal2, *args, animal4, **kwargs):
    print("\n- - - mixing args, *args, kwargs and **kwargs - - -")
    print("print_animals('Snake', 'Fish', 'Guinea Pig', 'Owl', animal4='Cat', animal5='Dog')")
    print("args -> ",animal1, animal2)
    print("*args -> ",args)
    print("kwarg -> ",animal4)
    print("**kwargs -> ",kwargs)

print_animals('Snake', 'Fish', 'Guinea Pig', 'Owl', animal4='Cat', animal5='Dog')


# unpacking operateor in function calls
print("\n- - - unpacking operateor in function calls - - -\n")
print("""my_num_list = [3, 6, 9]
def sum(num1, num2, num3):
  print(num1 + num2 + num3)
sum(*my_num_list)""")
my_num_list = [3, 6, 9]
def sum(num1, num2, num3):
  print(num1 + num2 + num3)
 
sum(*my_num_list)


print("""\nnumbers  = {'num1': 3, 'num2': 6, 'num3': 9}
def sum(num1, num2, num3):
  print(num1 + num2 + num3)
sum(**numbers)""")
numbers  = {'num1': 3, 'num2': 6, 'num3': 9}
 
def sum(num1, num2, num3):
  print(num1 + num2 + num3)
 
sum(**numbers)


print("""\nstart_and_stop = [3, 6]
range_values = range(*start_and_stop)
print(list(range_values))""")
start_and_stop = [3, 6]
 
range_values = range(*start_and_stop)
print(list(range_values))


print("""\na, *b, c = [3, 6, 9, 12, 15]
 print(b)""")
a, *b, c = [3, 6, 9, 12, 15]
print(b)


print("""\nmy_tuple = (3, 6, 9)
merged_tuple = (0, *my_tuple, 12)
print(merged_tuple)""")
my_tuple = (3, 6, 9)
merged_tuple = (0, *my_tuple, 12)
print(merged_tuple)


print("""\nnum_collection = [3, 6, 9]
def power_two(*nums): 
  for num in nums:
    print(num**2)
power_two(*num_collection)""")
num_collection = [3, 6, 9]
 
def power_two(*nums): 
  for num in nums:
    print(num**2)
 
power_two(*num_collection)