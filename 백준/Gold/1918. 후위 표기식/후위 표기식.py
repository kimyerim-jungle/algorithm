import sys
from collections import deque

stack = []
string = sys.stdin.readline().strip()
answer = deque()
gh = False


for i in string:
    if i == '+' or i == '-':
        if len(stack) > 0:
            if stack[-1] == '+' or stack[-1] == '-':
                print(stack.pop(), end='')
                stack.append(i)
            else:
                while stack:
                    if stack[-1] == '(':
                        break
                    print(stack.pop(), end='')
                stack.append(i)
        else:
            stack.append(i)
    elif i == '/' or i == '*':
        if len(stack) > 0:
            if stack[-1] == '+' or stack[-1] == '-':
                stack.append(i) 
            else:
                while stack:
                    if stack[-1] == '+' or stack[-1] == '-' or stack[-1] == '(':
                        break
                    s = stack.pop()
                    print(s, end='')
                stack.append(i)
        else:
            stack.append(i)
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack:
            if stack[-1] == '(':
                stack.pop()
                break
            print(stack.pop(), end='')
    else:    
        print(i, end='')


while stack:
    i = stack.pop()
    print(i, end='')
