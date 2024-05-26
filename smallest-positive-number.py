def isdivisible1to20(num):
    for i in range(1,21):
        if num%i!=0:
            return False
    return True 
num=1
while True:
    if isdivisible1to20(num):
        break
    num+=1
print(num)    
