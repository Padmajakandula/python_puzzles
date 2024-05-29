upper_limit = 2000000
sum = 0
for num in range(2, upper_limit):
    is_prime = True
    if num > 2 and num % 2 == 0:  
        is_prime = False
    else:
        for i in range(3, int(num**0.5) + 1, 2):  
            if num % i == 0:
                is_prime = False
                break
    
    if is_prime:
        sum_of_primes += num  
print(f"The sum of  primes below two million is: {sum}")
