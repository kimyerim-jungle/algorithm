import sys

num = int(input())
a = []
for i in range(num):
    a.append(int(sys.stdin.readline()))
    
a.sort()

for i in range(num):
    print(a[i])