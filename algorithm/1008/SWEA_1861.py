def dfs(x, y, c):
    global mx, ans
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 위, 오, 아래, 왼
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == arr[x][y] + 1:
            dfs(nx, ny, c+1)
    else:
        if c > mx:
            mx = c
            ans = start
        elif c == mx:
            if start < ans:
                ans = start
        return



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    ans = 10 ** 3
    for i in range(N):
        for j in range(N):
            if N**2 - arr[i][j] + 1 < mx:
                continue
            start = arr[i][j]
            dfs(i, j, 1)
    print(f'#{tc} {ans} {mx}')