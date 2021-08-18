T = int(input())
for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]   # 가로 방향
    h_arr = [[0]*9 for _ in range(9)]                           # 세로 방향
    for i in range(9):
        for j in range(9):
            h_arr[j][i] = arr[i][j]

    k = [0] * 9
    ans = 1
    for i in range(9):
        if ans == 0:
            break
        for n in range(1, 10):                # 1~9 숫자 중 가로, 세로 줄에 있으면, 리스트 k의 해당 자리에 1
            if n in arr[i] and n in h_arr[i]:
                k[n-1] = 1
            else:
                ans = 0
                break
    if ans:                                   # 가로, 세로 줄 충족 시 9칸 검사
        dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
        r = [1, 4, 7]
        chk = [0] * 9
        for p in r:
            for i in range(9):
                nx, ny = p+dx[i], p+dy[i]
                if arr[nx][ny] in range(1, 10): # 9칸 중 각각이 1~9를 하나씩 만족하는지
                    chk[arr[nx][ny]-1] = 1
            if 0 in chk:                        # 안 채워진 칸이 있으면 미충족
                ans = 0
                break
    print(f'#{t} {ans}')