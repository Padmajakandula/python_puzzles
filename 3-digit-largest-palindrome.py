largest_palindrome = 0
largest_3_digit_num=999
for i in range(largest_3_digit_num, 99, -1):
    for j in range(i, 99, -1):
        product = i * j
        if str(product) == str(product)[::-1]:
            if product > largest_palindrome:
                largest_palindrome = product
print(largest_palindrome)
