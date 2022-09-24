def in_range(num, lower, upper):
    return True if num >= lower and num <= upper else False

def same_name(your_name, my_name):
    return True if your_name == my_name else False

def always_false(num):
    if num > 0 and num < 0:
        return True
    else:
        return False

def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif rating < 9:
        return "This one was fun."
    else:
        return "Outstanding!"

def max_num(num1, num2, num3):
    m = num1
    l = [num1, num2, num3]
    for n in l:
        if n > m:
            m = n
    return "It's a tie!" if l.count(m) > 1 else m


print(in_range(10, 10, 10))
print(in_range(5, 10, 20))
print(same_name("Colby", "Colby"))
print(same_name("Tina", "Amber"))
print(always_false(0))
print(always_false(-1))
print(always_false(1))
print(movie_review(9))
print(movie_review(4))
print(movie_review(6))
print(max_num(-10, 0, 10))
print(max_num(-10, 5, -30))
print(max_num(-5, -10, -10))
print(max_num(2, 3, 3))
