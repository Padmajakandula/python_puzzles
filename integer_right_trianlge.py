def count_solutions(p):
    count = 0
    for a in range(1, p // 2):
        for b in range(a, p // 2):
            c = p - a - b
            if a * a + b * b == c * c:
                count += 1
    return count
max_solutions = 0
best_p = 0
for p in range(1, 1001):
    solutions = count_solutions(p)
    if solutions > max_solutions:
        max_solutions = solutions
        best_p = p
print("The value of p with the maximum number of solutions is:", best_p)
print("The maximum number of solutions is:", max_solutions)
