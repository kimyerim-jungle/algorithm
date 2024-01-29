import sys

string = sys.stdin.readline()
num = []
n = ''
add = 0
for i in range(len(string)):
    if string[i] == '+':
        add += int(n)
        n=''
    elif string[i] == '-':
        num.append(add + int(n))
        n=''
        add = 0
    else:
        n += string[i]
    
    if i == len(string)-1:
        add += int(n)
        num.append(add)

result = num[0]
def dp(result):
    for i in range(1, len(num)):
        result = result - num[i]   
    return result
            
result = dp(result)
print(result)