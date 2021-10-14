def check(x, y):
    global visited
    q = []
    q.append((x, y))
    visited[x][y] = 0
    while q:
        x, y = q.pop(0)
        for (dx, dy) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] > arr[x][y]:
                    k = visited[x][y] + 1 + (arr[nx][ny] - arr[x][y])
                else:
                    k = visited[x][y] + 1

                if visited[nx][ny] > k:
                    visited[nx][ny] = k
                    q.append((nx, ny))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 가로세로 길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[1000000] * N for _ in range(N)]
    mn = 1000000
    check(0, 0)
    print(f'#{tc} {visited[-1][-1]}')