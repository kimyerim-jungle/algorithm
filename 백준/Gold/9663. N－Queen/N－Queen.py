num = int(input())

def n_queen(n): # n개의 퀸
    q = [0] * n  # 열 리스트에 행 번호를 기록
    row_flag = [False] * n
    a_flag = [False] * (n + n-1)  # /// 방향
    b_flag = [False] * (n + n-1)  # \\\ 방향
    global count
    count = 0
    
    def set(r): # r 열에 퀸을 놓겠다
        global count
        
        for j in range(n): # 주어진 퀸의 개수 만큼 반복 , 행
            # 플래그가 모두 거짓이면 아무 퀸도 해당 행열에 없다
            # 이때 열[]에 퀸을 넣어줌 열[] = 행
            if (not row_flag[j] and
                not a_flag[r + j] and
                not b_flag[r - j + (n-1)]):
                q[r] = j
            # 그리고 마지막 퀸이면 count++
                if r == (n-1):
                    count += 1
            # 마지막이 아니면 플래그 참으로 바꾸고 재귀
                else:
                    row_flag[j] = a_flag[r+j] = b_flag[r-j+(n-1)] = True
                    set(r+1)   # 0열을 놨으면 1열을 놓겠다
                    row_flag[j] = a_flag[r+j] = b_flag[r-j+(n-1)] = False
               
    set(0)
    return count
        
print(n_queen(num))