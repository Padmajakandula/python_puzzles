min_a = 2
max_a = 100
min_b = 2
max_b = 100
def count_distinct_powers(min_a, max_a, min_b, max_b):
    distinct_terms = set()
    for a in range(min_a, max_a + 1):
        for b in range(min_b, max_b + 1):
            distinct_terms.add(a ** b)
    return len(distinct_terms)
distinct_term_count = count_distinct_powers(min_a, max_a, min_b, max_b)
print("Number of distinct terms :", distinct_term_count)
