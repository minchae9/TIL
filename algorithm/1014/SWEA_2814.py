def dfs(start, cnt):
    global mx
    visited[start] = 1
    for d in range(1, N+1):
        if arr[start][d] == 1 and visited[d] == 0:
            dfs(d, cnt+1)
            visited[d] = 0
    if cnt > mx:
        mx = cnt
    return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    mx = 0
    for _ in range(M):
        x, y = map(int, input().split())
        arr[x][y] = 1
        arr[y][x] = 1
    for i in range(1, N+1):
        visited = [0] * (N + 1)
        res = dfs(i, 1)
    print(f'#{tc} {mx}')