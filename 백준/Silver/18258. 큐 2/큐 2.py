import sys

num = int(input())

global capacity
capacity = 2000000

queue = [None] * capacity

global no
no = 0
global f
f = 0
global rear
rear = 0

def push(q, n):
    global capacity
    global no
    global rear
    
    q[rear] = n
    rear += 1
    no += 1
    if rear == capacity:
        rear = 0
    
def pop(q):
    global capacity
    global no
    global f
    
    if no > 0:
        print(q[f])
        f += 1
        no -= 1
        if f == capacity:
            f = 0
    else:
        print(-1)

def size():
    global no
    print(no)
    
def empty():
    global no
    if no == 0:
        print(1)
    else:
        print(0)
    
def front(q):
    global no
    global f
    if no > 0:
        print(q[f])
    else:
        print(-1)
        
def back(q):
    global no
    global rear
    if no > 0:
        print(q[rear - 1])
    else:
        print(-1)
    

for _ in range(num):
    do = sys.stdin.readline().split()
    if do[0] == 'push':
        push(queue, int(do[1]))
    elif do[0] == 'pop':
        pop(queue)
    elif do[0] == 'size':
        size()
    elif do[0] == 'empty':
        empty()
    elif do[0] == 'front':
        front(queue)
    elif do[0] == 'back':
        back(queue)
        