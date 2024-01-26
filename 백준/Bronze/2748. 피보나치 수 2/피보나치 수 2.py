num = int(input())

save = [0 for _ in range(num+1)]
save[0] = 0
save[1] = 1

def fibo(x):
    
    for i in range(2, x+1):
        save[i] = save[i-1] + save[i-2]
    
    return save[x]
    
print(fibo(num))