"""
pypy3로 돌림.

참고 사이트: https://hongcoding.tistory.com/118
- 해야할 일이 많을 땐 함수 단위로 나누기
- 여기서도 dfs 사용할 수 있음을 배우기
- return과 exit(0)의 차이 알아내기
"""
import sys
input = sys.stdin.readline

# 스도쿠 맵 받기
sudoku = [[] for _ in range(9)]
for n in range(9):
    sudoku[n] = list(map(int, input().split()))
# 0 위치 모은 거: blank
blank = []
for r in range(9):
    for c in range(9):
        if sudoku[r][c] == 0:
            blank.append((r, c))

def row(x, val):
    for i in range(9):
        if val == sudoku[x][i]:
            return False
    return True

def column(y, val):
    for j in range(9):
        if val == sudoku[j][y]:
            return False
    return True

def sqr(x, y, val):
    # 좌측 상단 칸
    row = x // 3 * 3
    col = y // 3 * 3
    for a in range(3):
        for b in range(3):
            if val == sudoku[row+a][col+b]:
                return False
    return True

def dfs(i):
    if i == len(blank):
        # 출력
        for p in range(9):
            # for q in range(9):
            #     print(sudoku[p][q], end=' ')
            # print()
            print(*sudoku[p])
        # return
        exit(0) # 이 부분을 왜 return으로 하면 틀릴까?
    for num in range(1, 10):
        x, y = blank[i][0], blank[i][1]
        if row(x, num) and column(y, num) and sqr(x, y, num):
            sudoku[x][y] = num
            dfs(i+1)
            sudoku[x][y] = 0

dfs(0)