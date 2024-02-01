import sys

N = int(input())
st = []
for _ in range(N):
    st.append(int(sys.stdin.readline().strip()))
    
result = [[int(1e9), int(1e9)] for _ in range(N+1)]

def solve():
    result[0] = [0, 0]
    result[1] = [result[0][0] + st[0], st[0]]
    for i in range(2, N+1):
        result[i][0] = result[i-1][1] + st[i-1]
        result[i][1] = max(result[i-2][0], result[i-2][1]) + st[i-1]

    return max(result[N][0], result[N][1])  
    
print(solve())
