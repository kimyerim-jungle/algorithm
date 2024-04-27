import sys, math
from collections import deque

S = int(input())

queue = deque()
list = set()

queue.append((1, 0, 0))
while queue:
    n, clip, time = queue.popleft()
    #print(f"n={n}  clip={clip}  time={time}")
    
    if n == S:
        print(time)
        break
    
    for i in range(1, 4):
        a, b = n, clip
        if i == 1: # 1번 연산
            b = n
        elif i == 2: # 2번 연산
            a = n + clip
        elif i == 3: # 3번 연산
            if n-1 <= 0:
                continue
            a = n-1
        if (a, b, time+1) in list:
            continue
        queue.append((a, b, time+1)) 
        list.add((a, b, time+1))  
