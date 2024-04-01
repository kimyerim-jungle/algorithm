import sys
from collections import deque

G = int(input())
P = int(input())
plane = [0 for _ in range(P+1)]
dk = [-1 for _ in range(G+1)]
p = [-1 for _ in range(G+1)]

for i in range(1, P+1):
    x = int(sys.stdin.readline().strip())
    plane[i] = x

succ = 0  
for i in range(1, P+1):
    s = False
    if p[plane[i]] == -1:
        dk[plane[i]] = plane[i]-1
        succ += 1 
        s = True
        p[plane[i]] = i
    else:
        for j in range(dk[plane[i]], 0, -1):
            if p[j] == -1:
                dk[plane[i]] = j-1
                dk[j] = j-1
                succ += 1 
                s = True
                p[j] = i
                break 
    if not s: 
        break
    if succ == P:
        break
        
print(succ)   
