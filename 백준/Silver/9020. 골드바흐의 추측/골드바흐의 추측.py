import math

def is_prime(n): 
    if n == 1: return False
    if n == 2: return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

count = int(input())

for i in range(count):
    num = int(input())
    
    up = num // 2
    down = num // 2
    
    while True:
        if is_prime(up) and is_prime(down):
            print(down, up)
            break
        else:
            up += 1
            down -= 1
            