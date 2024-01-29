import sys

string_A = sys.stdin.readline().strip()
string_B = sys.stdin.readline().strip()
la = len(string_A)
lb = len(string_B)
dp = [[0 for _ in range(lb+1)] for _ in range(la+1)]

for i in range(1, la+1):
    for j in range(1, lb+1):
        if string_A[i-1] == string_B[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        elif string_A[i-1] != string_B[j-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
print(dp[la][lb])