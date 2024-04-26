import sys, math
from collections import deque

p = [1 for _ in range(10000)]

def prime():
    for i in range(1000, 10000):
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                p[i] = 0
                break
    
def bfs(x, y):
    visited = [0 for _ in range(10000)]
    queue = deque()
    queue.append((x, 0))
    
    while queue:
        q, count = queue.popleft()
        if q == y:
            return count
        
        visited[q] = 1
        string = list(str(q))
        for i in range(4):
            tmp = string.copy()
            for j in range(10):
                tmp[i] = str(j)
                isprime = int("".join(tmp))
                if isprime > 1000 and p[isprime] == 1 and visited[isprime] == 0:
                    visited[q] = 1
                    queue.append((isprime, count+1))
    
T = int(input())
prime()

count = []
for i in range(T):
    x, y = map(int, sys.stdin.readline().split())
    a = bfs(x, y)
    print(a if a != None else "Impossible")
    