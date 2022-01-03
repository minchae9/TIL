T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 위, 오, 아래, 왼
    visited = [0] * (N**2 + 1)

    for i in range(N):
        for j in range(N):
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0<=nx<N and 0<=ny<N and arr[nx][ny] == arr[i][j] + 1:
                    visited[arr[i][j]] = 1

    start = 0
    mx = 0
    dist = 0
    for r in range(1, len(visited)):
        dist += 1
        if visited[r] == 0:
            if mx < dist:
                start = r - dist + 1
                mx = dist
            dist = 0
    print(f'#{tc} {start} {mx}')