num=int(input("enter the number"))
for i in range(1,num+1):
    if num%i==0:
        flag=0
        for j in range(2,i):
            if i%j==0:
                flag=1
                break
        if flag==0:
            print("the prime factors are",i)
