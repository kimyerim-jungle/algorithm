num = int(input())

# 기둥은 3개

print((2**num)-1)

def print_mov(x, fr, to):
    if x > 1:
        print_mov(x - 1, fr, 6 - fr - to)
    
    print(fr, to)
    
    if x > 1:
        print_mov(x - 1, 6 - fr - to, to)

if num <= 20:  
    print_mov(num, 1, 3)