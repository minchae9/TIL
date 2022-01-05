# 스도쿠 판 입력하며, 0 개수 몇 개인지
sudoku = [[0]*9 for _ in range(9)]
zero_count = 0
for n in range(9):
    sudoku[n] = list(map(int, input().split()))
    for i in sudoku[n]:
        if i == 0:
            zero_count += 1
# 0 개수 모두 사라질 때까지
while zero_count > 0:
    # 가로
    for r in range(9):
        if sum(sudoku[r]) < 45:
            if sudoku[r].count(0) == 1:
                for num in range(1, 10):
                    if num not in sudoku[r]:
                        sudoku[r][sudoku[r].index(0)] = num
                        zero_count -= 1
                        break
    # 세로
    for c in range(9):
        check = [0] * 9
        for i in range(9):
            if sudoku[i][c] > 0:
                check[sudoku[i][c]-1] += 1
        if sum(check) == 8:
            val = check.index(0) + 1
            for m in range(9):
                if sudoku[m][c] == 0:
                    sudoku[m][c] = val
                    zero_count -= 1
                    break
    # 3x3 정사각형
    """
    8 1 2
    7 ^ 3
    6 5 4
    """
    dx, dy = [0, -1, -1, 0, 1, 1, 1, 0, -1], [0, 0, 1, 1, 1, 0, -1, -1, -1] # 위에서부터 시계방향
    for i in range(1, 9, 3):
        for j in range(1, 9, 3):
            check = [0] * 9
            z_x = z_y = 0
            for d in range(9):
                nx, ny = i+dx[d], j+dy[d]
                if sudoku[nx][ny] > 0:
                    check[sudoku[nx][ny]-1] += 1
                else:
                    z_x, z_y = nx, ny
            if sum(check) == 8:
                sudoku[z_x][z_y] = check.index(0) + 1
                zero_count -= 1

# 출력
for a in range(9):
    for b in range(9):
        print(sudoku[a][b], end=' ')
    print()
