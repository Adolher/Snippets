
def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print("Professor", end=" ")
        print_name_function(*args, **kwargs)
    return wrapper

@title_decorator
def print_name(name, location):
    print(name +  "works at " + location)

print_name("Wagner", "Home")