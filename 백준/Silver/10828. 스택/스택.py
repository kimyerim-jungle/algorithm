import sys

n = int(input())
stack = []

def push(s, num):
    s.append(num)
    
def pop(s):
    if len(s) == 0:
        print(-1)
    else:
        num = s[len(s)-1]
        del s[len(s)-1]
        
        print(num)

def size(s):
    print(len(s))

def empty(s):
    if len(s) > 0:
        print(0)
    else:
        print(1)

def top(s):
    if len(s) == 0:
        print(-1)
    else:
        print(s[len(s)-1])
    
    
for _ in range(n):
    do = []
    do.append(sys.stdin.readline().split())
    if do[0][0] == 'push':
        push(stack, int(do[0][1]))
    elif do[0][0] == 'pop':
        pop(stack)
    elif do[0][0] == 'top':
        top(stack)
    elif do[0][0] == 'empty':
        empty(stack)
    elif do[0][0] == 'size':
        size(stack)
    
        