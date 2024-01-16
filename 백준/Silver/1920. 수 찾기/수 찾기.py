import sys

A_num = int(input())

A = []
A = list(map(int, sys.stdin.readline().split()))

B_num = int(input())

B = []
B = list(map(int, sys.stdin.readline().split()))

A.sort()

def search(N): # N을 찾아서 있는 지 없는 지 return
    pl = 0
    pr = len(A) - 1
    pc = (len(A) - 1) // 2
    is_ = False
    
    while True:
        if pl > pr:
            break
        if N > A[pc]:
            pl = pc + 1
            pc = (pl + pr) // 2
        elif N < A[pc]:
            pr = pc - 1
            pc = (pl + pr) // 2
        elif N == A[pc]:
            is_ = True
            break
    return is_    
    

right = [0] * len(B)

for i in range(len(B)):
    if search(B[i]):
        right[i] = 1
        
for i in range(len(right)):
    print(right[i])