def dfs(x, y, c):
    global mn
    if x == y == N - 1:
        if c < mn:
            mn = c
        return
    else:
        if c >= mn:
            return
        else:
            dx, dy = [0, 1], [1, 0]  # 오, 아래
            for d in range(2):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    dfs(nx, ny, c + arr[nx][ny])


T = int(input())
for t in range(1, T + 1):
    N = int(input())  # 가로, 세로 칸 수
    arr = [list(map(int, input().split())) for _ in range(N)]

    mn = 10 * N * N
    dfs(0, 0, arr[0][0])
    print(f'#{t} {mn}')