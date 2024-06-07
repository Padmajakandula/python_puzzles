def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
limit = 1000000
def generate_primes(limit):
    primes = []
    num = 2
    while num < limit:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes
def find_longest_prime_sum(limit):
    primes = generate_primes(limit)
    prime_set = set(primes)  
    max_length = 0
    max_prime_sum = 0
    for i in range(len(primes)):
        for j in range(i + max_length, len(primes)):
            prime_sum = sum(primes[i:j])
            if prime_sum >= limit:
                break
            if prime_sum in prime_set and (j - i) > max_length:
                max_length = j - i
                max_prime_sum = prime_sum

    return max_prime_sum
"""limit = 1000000"""
result = find_longest_prime_sum(limit)
print("The prime below one million is :", result)
