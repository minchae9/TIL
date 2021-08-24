def findroute(i, j, N):
    if i == ei and j == ej:
        return 1
    else:   # 왼, 위, 오, 아래 순
        maze[i][j] = 1
        for di, dj in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                if maze[ni][nj] == 0:
                    if findroute(ni, nj, N):
                        return 1
                elif maze[ni][nj] == 3:
                    return 1
        return 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    maze = list(list(int(c) for c in input()) for _ in range(N))
    # 출발점, 도착점
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j
            elif maze[i][j] == 3:
                ei, ej = i, j
    # 경로 판정
    ans = findroute(si, sj, N)
    print(f'#{t} {ans}')