# 셰이커 정렬 알고리즘
num = int(input())

a = []
for i in range(num):
    a.append(int(input()))

left = 0
right = len(a) - 1
last = right

while left < right:
    for i in range(right, left, -1):
        if a[i] < a[i - 1]:
            a[i - 1], a[i] = a[i], a[i - 1]
            last = i
    left = last
    
    for i in range(left, right):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            last = i
    right = last
    
for i in range(len(a)):
    print(a[i])