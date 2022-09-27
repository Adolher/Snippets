# All functions are first-class-objects
#
# First-class-objects can be
#
# 1. ...stored as a variable

def up_func(text):
    return text.upper()

up = up_func
print(up("hello"))

def down_func(text):
    return text.lower()

down = down_func
print(down("HELLO"))

# 2. ...passed as arguments to a function

def a_nother_func(func, text):
    up = func(text)
    return up

print(a_nother_func(up_func,"a func as arg"))

a_list = ["word", "wOrd", "WORD"]
new_list = map(lambda text: up(text), a_list)
print(list(new_list))

# 3. ...returned by a fuction

def up_or_down(text):
    if text.isupper():
        return down
    else:
        return up

x_func = up_or_down("hello")
print(x_func("is it up or down"))



# 4. ...stored in data structures (e.g. lists, dictionaries, etc.)

a_list = [up, down]
text = "hElLo"

for i in a_list:
    print(i(text))