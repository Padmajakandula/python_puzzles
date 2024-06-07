def find_first_fibonacci_with_1000_digits():
    a = 1
    b = 1
    index = 2    
    while True:
        temp = b  
        b = a + b 
        a = temp  
        index += 1
        if len(str(b)) >= 1000:
            return index
first_term_index = find_first_fibonacci_with_1000_digits()
print("The first term in the Fibonacci sequence to contain 1000 digits is:", first_term_index)
