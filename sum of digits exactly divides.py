list = []
for num in range(1, 200):
    sum= 0
    for digit in str(num):
        sum+= int(digit)
    if sum!= 0 and num % sum == 0:
        list.append(num)
print(list)
