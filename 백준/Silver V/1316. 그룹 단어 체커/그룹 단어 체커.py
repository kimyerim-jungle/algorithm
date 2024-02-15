import sys

N = int(input())
num = 0
for _ in range(N):
    string = []
    s = sys.stdin.readline().strip()
    string.append(s[0])
    n = s[0]
    b = 0
    for i in range(1, len(s)):
        if n == s[i]:
            continue
        else:
            if s[i] in string:
                b = 1
                break
            else:
                n = s[i]
                string.append(n)
    if b == 0:
        num += 1
            
print(num)