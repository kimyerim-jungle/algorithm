import sys

num = int(input())

paper = []
for i in range(num):
    paper.append(list(map(int, sys.stdin.readline().split())))

def cutting(x, y, n):
    global w
    global b
    w = 0
    b = 0
    
    def cut(x, y, n):
        global w
        global b
        
        list_x = [x, x, x+n//2, x+n//2]
        list_y = [y, y+n//2, y, y+n//2]
        
        pre = -1
        #print(f'x = {x} y = {y} n = {n}')
        
        if n == 1:
            if paper[x][y] == 1:
                b += 1
                return
            else:
                w += 1
                return
        if n // 2 == 0:
            #print(f'======= return = {x, y} : {paper[x][y]}')
            return paper[x][y]
        else:
            pre = paper[x][y]
            for i in range(x, n + x):
                if i >= num: break
                k = 0 
                for j in range(y, n + y):
                    k = j
                    if j >= num: break
                    if pre == paper[i][j]:
                        continue
                    elif pre != paper[i][j]:
                        break
                
                #print(f'pre = {pre} i = {i} j = {k} n = {n}')
                if pre != paper[i][k]:
                    break
                if i == n + x - 1: # 마지막까지 돌았는데 같은 색
                    if pre == 0 :
                        w += 1
                    elif pre == 1:
                        b += 1
                    #print(f'===pre=== w = {w} b = {b} n = {n}')
                    return
                    
            for i in range(4):
                if list_x[i] >= num or list_x[i] < 0 or list_y[i] >= num or list_y[i] < 0:
                    continue
                cut(list_x[i], list_y[i], n//2)
            
            #print(f'======= w = {w} b = {b} n = {n}')
            
            
    cut(x, y, n)              
    
cutting(0, 0, num)

print(w)
print(b)