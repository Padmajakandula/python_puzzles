import math
def factorial(n):
    factorial_result = math.factorial(n)
    factorial_str = str(factorial_result)
    digit_sum = sum(int(digit) for digit in factorial_str)
    return digit_sum
result = factorial(100)
print(result)
