num = 10001
i = 2
count = 0
prime = 0
p = []
while count < num:
    for x in range (2,i+1):
        if len(p) ==2:
            break
        elif i%x == 0:
            p.append(x)

    if len(p)==1:
        prime = i
        count += 1
    p = []
    i+=1       
print(prime)
    
    
