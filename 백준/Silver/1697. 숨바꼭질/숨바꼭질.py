import sys
from collections import deque

X, K = map(int, sys.stdin.readline().split())

result = []
visited = [-1 for _ in range(100001)]
queue = deque()
queue.append((X, 0))

while queue:
    pos, time = map(int, queue.popleft())
    if pos == K:
        print(time)
        break
    if visited[pos] != -1:
        continue
        
    visited[pos] = 1
    if pos - 1 >= 0 and visited[pos - 1] == -1:
        queue.append((pos-1, time+1))
    if pos + 1 <= 100000 and visited[pos + 1] == -1:
        queue.append((pos+1, time+1))
    if pos * 2 <= 100000 and visited[pos * 2] == -1:
        queue.append((pos*2, time+1))
