import sys

a = []
sum = 0

for i in range(9):
    a.append(int(sys.stdin.readline()))
    sum += a[i]

sub = sum - 100 # 오버되는 키
list = []

for i in range(9):
    x = a[i]
    if x > sub:
        continue
    
    for j in range(i + 1, 9):
        y = a[j]
        
        if sub - x == y:
            list.append([x, y])
        else:
            continue
        
a.remove(list[0][0])
a.remove(list[0][1])  
a.sort()

for i in range(7):
    print(a[i])