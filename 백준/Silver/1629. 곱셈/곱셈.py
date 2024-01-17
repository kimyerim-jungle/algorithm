import sys

nums = list(map(int, sys.stdin.readline().split()))

A = nums[0]
B = nums[1]
C = nums[2]
    
answer = 1

while B > 0:
    if B % 2:
        answer *= A
        answer %= C
        
    A *= A
    A %= C
    
    B //= 2
print(answer)
