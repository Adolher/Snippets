def large_power(base, exponent):
    return True if (base ** exponent) > 5000 else False

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    return True if (food_bill + electricity_bill + internet_bill + rent) > budget else False

def twice_as_large(num1, num2):
    return True if num1 > num2 * 2 else False

def divisible_by_ten(num):
    return True if num % 10 == 0 else False

def not_sum_to_ten(num1, num2):
    return True if num1+num2 != 10 else False

print(large_power(2, 13))
print(large_power(2, 12))
print(over_budget(100, 20, 30, 10, 40))
print(over_budget(80, 20, 30, 10, 30))
print(twice_as_large(10, 5))
print(twice_as_large(11, 5))
print(divisible_by_ten(20))
print(divisible_by_ten(25))
print(not_sum_to_ten(9, -1))
print(not_sum_to_ten(9, 1))
print(not_sum_to_ten(5,5))
