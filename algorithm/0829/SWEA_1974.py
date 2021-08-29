T = int(input())
for t in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    flag = False
    # 가로, 세로 행 검사
    for i in range(9):
        check_row = [0] * 10
        check_col = [0] * 10
        if flag:
            break
        for j in range(9):
            if check_row[sudoku[i][j]] or check_col[sudoku[j][i]]:
                ans = 0
                flag = True
                break
            check_row[sudoku[i][j]] = 1
            check_col[sudoku[j][i]] = 1
    # 네모칸 검사
    if not flag:
        surr = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in (1, 4, 7):
            for j in (1, 4, 7):
                check = [0]*10
                for k in range(9):
                    ci, cj = i+surr[k][0], j+surr[k][1]
                    if check[sudoku[ci][cj]]:
                        ans = 0
                        flag = True
                        break
                    check[sudoku[ci][cj]] = 1
    if not flag:
        ans = 1
    print(f'#{t} {ans}')

