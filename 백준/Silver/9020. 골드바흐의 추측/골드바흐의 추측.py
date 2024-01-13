import math

def is_prime(n): # 2말고는 홀수만 삽입
    if n == 1: return False
    if n == 2: return True
    if n == 3: return True
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

count = int(input())
counter = 0

for i in range(count):
    num = int(input())
    prime = 2
    prime_set = []
    
    while True:
        if prime > (num // 2):
            break
        
        if is_prime(prime):
            if is_prime(num - prime):
                prime_set.append([prime, num - prime])
        if prime == 2:
            prime += 1
        else:
            prime += 2
    
    sub_min = prime_set[0][1] - prime_set[0][0] # 두 소수의 차이값
    min_index = 0
    for i in range(len(prime_set)):
        sub_set = abs(prime_set[i][0] - prime_set[i][1])
        if sub_min > sub_set:
            sub_min = sub_set
            min_index = i
    
    print(f"{prime_set[min_index][0]} {prime_set[min_index][1]}")