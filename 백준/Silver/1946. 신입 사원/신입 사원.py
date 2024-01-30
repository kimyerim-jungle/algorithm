import sys

def solve():
    result = []
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        total = []
        for _ in range(N):
            a, b = map(int, sys.stdin.readline().split())
            total.append((a, b))
           
        total.sort()
        
        count = 1
        small = total[0][1]
        for t in total:
            if t[1] < small:
                count += 1
                small = t[1]
            
        result.append(count)
    return result

result = solve()
for i in result:
    print(i)