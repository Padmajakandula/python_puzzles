sum_total = 1000
a=0
b=0
c=0
for a in range(1, sum_total // 4):
    for b in range(a + 1, sum_total // 2):
        c = sum_total - a - b
        if a * a + b * b == c * c:
            print(f"The Pythagorean triplet is: a={a}, b={b}, c={c}")
            print(f"The product abc is: {a * b * c}")
