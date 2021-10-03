def bfs(r, c, cnt):
    global visited
    q = []
    q.append((r, c))
    visited[row][col] = 1
    while q:
        tx, ty = q.pop(0)
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 위, 오, 아래, 왼
        for i in range(4):
            nx, ny = tx+dx[i], ty+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0 and arr[nx][ny] == 1:
                visited[nx][ny] = visited[tx][ty] + 1
                q.append((nx, ny))
                cnt += 1    # cnt 변수로 사각형 크기 측정
    return cnt


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
squares = 0 # 사각형 개수
mx = 0
for row in range(n):
    for col in range(m):
        if visited[row][col] == 0 and arr[row][col]:
            squares += 1
            ans = bfs(row, col, 1)
            if ans > mx:    # 사각형 최대 크기 구함
                mx = ans
print(squares)
print(mx)