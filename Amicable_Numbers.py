def sum_of_divisors(n):
    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i            
    return sum_divisors
sum_amicable = 0
for a in range(1, 10000):
    b = sum_of_divisors(a)
    if a != b and sum_of_divisors(b) == a:
        sum_amicable += a
print(sum_amicable)
