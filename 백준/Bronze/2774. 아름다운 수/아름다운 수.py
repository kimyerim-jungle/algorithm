N = int(input())

def beauti(n):
    num = []
    
    while n >= 10 :
        x = n % 10
        n = int(n / 10)
        if x not in num :
            num.append(x)
            
    if n not in num :
        num.append(n)  
        
    return len(num)       
    
for i in range(N):
    a = int(input())
    print(beauti(a))