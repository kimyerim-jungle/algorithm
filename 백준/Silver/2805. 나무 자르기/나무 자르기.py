import sys

N, M = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))

def search(min, max):
    
    while True:
        tall = 0
        count = (min + max) // 2
        for tree in trees:
            if tree - count > 0:
                tall += tree - count
                
        if tall == M or min > max: 
            return count
        elif tall > M :
            min =  count + 1
        elif tall < M:
            max = count - 1
            
    return count


print(search(0, max(trees)))        
     