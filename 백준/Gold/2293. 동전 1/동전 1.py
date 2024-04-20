import sys

N, K = map(int, input().split())
coin = []
for _ in range(N):
    coin.append(int(sys.stdin.readline()))
    
dp = [0 for _ in range(K+1)]
dp[0] = 1
for i in coin:
    for j in range(i, K+1):
        dp[j] = dp[j-i] + dp[j]
    

print(dp[K])
