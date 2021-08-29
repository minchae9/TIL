def search(i, j, N):
    q = []  # 큐생성
    visited = [[0] * N for _ in range(N)]  # visited 생성
    q.append((i, j))  # 시작점 인큐
    while q:
        a, b = q.pop(0)  # pop
        if (a, b) == (ei, ej):  # 도착점에 닿으면, return
            return visited[a][b] - 1
        di, dj = [0, -1, 0, 1], [-1, 0, 1, 0]  # 탐색 (왼, 위, 오, 아래)
        for k in range(4):
            ni, nj = a + di[k], b + dj[k]
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[a][b] + 1
    return 0


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    # 출발점, 도착점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j
            elif maze[i][j] == 3:
                ei, ej = i, j

    print(f'#{t} {search(si, sj, N)}')