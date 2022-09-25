def func():
    print("In the function")

def func_with_return():
    return "The returned string"

def func_2(s):
    print(f"{s} in the function")







func()
func_2("I am")


print(func_with_return())


def f1(*args):
    print(args)

f1("Hello", 2, True)
f1(False)

def f2(times, *args):
    for x in range(times):
        print(args)

f2(3, 5, "a_string", 1.8)