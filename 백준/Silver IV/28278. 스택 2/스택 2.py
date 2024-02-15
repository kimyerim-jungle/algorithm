import sys

N = int(input())
stack = []
num = []

for i in range(N):
    num = list(map(int, (sys.stdin.readline().split())))

    if num[0]==1:
        stack.append(num[1])
        
    elif num[0]==2:
        if len(stack) == 0 : print(-1)
        else :
            print(stack.pop())
    elif num[0]==3:
        print(len(stack))
    elif num[0]==4:
        if len(stack) > 0 : print(0)
        else : print(1)
    elif num[0]==5:
        if len(stack) == 0 : print(-1)
        else :
            print(stack[-1])