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
    x = y = 0

    z_r, z_c = 0, 0
    while x < 3:
        visited = [0] * 9
        for i in range(3):
            row = 3*x + i
            for j in range(3):
                col = 3*y + j
                if sudoku[row][col] > 0:
                    visited[sudoku[row][col]-1] += 1
                else:
                    z_r = row
                    z_c = col
        if sum(visited) == 8:
            sudoku[z_r][z_c] = visited.index(0)+1
            zero_count -=1
        y += 1
        if y == 3:
            y = 0
            x += 1
    """
    행 012 열 012, 345, 678
    행 345 열 012, 345, 678
    행 678 열 012, 345, 678
    """

# 출력
for a in range(9):
    for b in range(9):
        print(sudoku[a][b], end=' ')
    print()
