import sys

def solve():
    list = []
    N, K = map(int, sys.stdin.readline().split())

    for _ in range(N):
        w, v = map(int, sys.stdin.readline().split())
        list.append((v, w))
        
    list.sort()
    result = [0 for _ in range(K+1)]
    for n in list:
        for i in range(K, 0, -1):
            # 해당 무게의 기존 가치 랑 뉴 가치 중 큰 거
            if n[1] <= i:
                if result[i] < result[i-n[1]] + n[0]:
                    result[i] = result[i-n[1]] + n[0]
    
    print(result[K])              
    
solve()