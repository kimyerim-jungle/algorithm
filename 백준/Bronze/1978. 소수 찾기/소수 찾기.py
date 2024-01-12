import sys
import math

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

num = int(input())
p = list(map(int, sys.stdin.readline().split()))
count = 0

for i in range(num):
    if is_prime(p[i]):
        count += 1
        
print(count)