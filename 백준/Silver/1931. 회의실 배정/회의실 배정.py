import sys

def solve():
    num = int(input())
    M = []
    for _ in range(num):
        s, e = map(int, sys.stdin.readline().split())
        M.append((s, e))
        
    M.sort(reverse=True)
          
    count = 0
    start = 2**31   
    for m in M:  # m [start] [end]
        if m[1] <= start:
            count += 1
            start = m[0]
        
    return count
     
print(solve())