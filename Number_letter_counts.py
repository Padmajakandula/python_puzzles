def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if 1 <= n < 10:
        return ones[n]  
    elif 10 < n < 20:
        return teens[n - 10]  
    elif 10 <= n < 100:
        return tens[n // 10] + ones[n % 10]  
    elif 100 <= n < 1000:
        if n % 100 == 0:
            return ones[n // 100] + "hundred"  
        else:
            return ones[n // 100] + "hundredand" + number_to_words(n % 100)  
    elif n == 1000:
        return "onethousand"
def count_letters_in_words(limit):
    total_letters = 0
    for i in range(1, limit + 1):
        word = number_to_words(i)
        total_letters += len(word)
    return total_letters
total_letters = count_letters_in_words(1000)
print(total_letters)


    
