import sys

num = int(input())

str_list = []
for i in range(num):
    str_list.append(sys.stdin.readline().strip())

# 중복제거를 위해 set() 자료형 변환
list_set = set(str_list)
str_list = list(i for i in list_set)
str_list.sort()

sort_list = []
for i in range(1, 51):
    for j in range(len(str_list)):
        if len(str_list[j]) == i:
            sort_list.append(str_list[j])

# 정렬 후 문자열 순으로 정렬
for i in range(len(sort_list)):
    print(sort_list[i])