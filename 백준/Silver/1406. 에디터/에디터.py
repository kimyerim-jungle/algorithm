import sys
from collections import deque

string = deque(list(sys.stdin.readline().strip())) # left
right = deque()
N = int(sys.stdin.readline())
cur = len(string)

for i in range(N):
    set = list(sys.stdin.readline().split())
    
    if set[0] == 'P':
        string.append(set[1])
        cur += 1
    elif set[0] == 'L':
        cur -= 1
        if cur < 0: 
            cur = 0
            continue
        right.appendleft(string.pop())
    elif set[0] == 'D':
        cur += 1
        if cur > len(string)+len(right): 
            cur = len(string)+len(right)
            continue
        string.append(right.popleft())
    elif set[0] == 'B':
        if cur == 0:
            continue
        del string[cur-1]
        cur -= 1
        
sys.stdout.write(''.join(string) + ''.join(right))
