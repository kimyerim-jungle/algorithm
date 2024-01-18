import sys

num = int(input())
list = []
for _ in range(num):
    list.append(sys.stdin.readline().strip())

count = []
def recur(n, x, y):     # 크기 n, 시작 index
    k = list[x][y]
    
    if n == 1:
        count.append(k)
        #print('return ', k)
        return
    elif n > 1:
        for i in range(x, n+x):
            for j in range(y, n+y):
                #print(f'i:{i} j:{j}// x={x} y={y} // n = {n}')
                if k == list[i][j]:
                    continue
                
                if x+(n//2) < num or y+(n//2) < num:
                    count.append("(")
                    recur(n//2, x, y)
                    recur(n//2, x, y+(n//2))
                    recur(n//2, x+(n//2), y)
                    recur(n//2, x+(n//2), y+(n//2))
                    count.append(")")
                    return
                
    count.append(k)
        
        
    
recur(num, 0, 0)

for i in range(len(count)):
    print(count[i], end="")