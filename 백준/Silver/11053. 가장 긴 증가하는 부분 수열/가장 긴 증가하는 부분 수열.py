import sys

def solve():
    num = int(input())
    seq = list(map(int, sys.stdin.readline().split()))
    
    lcs = [1 for _ in range(num)]

    for i in range(1, num):
        for j in range(i):
            if seq[i] > seq[j]:
                if lcs[i] < lcs[j] + 1:
                    lcs[i] = lcs[j] + 1

    return max(lcs)
print(solve())
