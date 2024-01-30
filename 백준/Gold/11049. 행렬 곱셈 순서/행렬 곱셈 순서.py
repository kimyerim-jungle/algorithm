import sys

def solve():
    INF = 2**31
    N = int(input())
    list = []
    dp = [[INF for _ in range(N)] for _ in range(N)]  # (바뀐 열 수, 곱의 결과)
    for _ in range(N):
        r, c = map(int, sys.stdin.readline().split())
        list.append((r, c))
       
    for i in range(N):
        dp[i][i] = 0
        
    # c로 끝나면 C로 시작하는 행렬을 찾고
    # 곱한 값 dp에 저장
    # A로 시작하는 행렬곱의 최소를 저장 AB보다 AC가 작으면 갱신
    
    for i in range(N): # x 앞 행렬  행렬의 앞 뒤 순서가 바뀌진 않음 ABC 입력 -> BA 곱은 XX
        for j in range(N-i):
            if j == j+i: continue
            a = j
            b = j+i
            for k in range(a, b): # x 뒤 행렬  m,k
                if dp[a][b] > dp[a][k] + dp[k+1][b] + list[a][0]*list[k][1]*list[b][1]:
                    dp[a][b] = dp[a][k] + dp[k+1][b] + list[a][0]*list[k][1]*list[b][1]
    return dp[0][N-1]

print(solve())

