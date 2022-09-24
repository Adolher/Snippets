def func():
    print("In the function")

def func_2(s):
    print(f"{s} in the function")

def a(x, y, z=9):
    print(f"x = {x}\ny = {y}\nz = {z}")

func()
func_2("I am")
a(1, -1)
a(1, -1, 3)