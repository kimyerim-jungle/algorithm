import sys

testcase = int(input())
for _ in range(testcase):
    string = sys.stdin.readline().split()

    a = ""

    length = int(string[0])
    string = string[1]
    for i in range(len(string)):
        for _ in range(length):
            a += string[i]
    print(a)