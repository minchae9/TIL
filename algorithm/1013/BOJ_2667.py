"""
bfs
"""
def bfs(sx, sy):
    global ans
    q = []
    q.append((sx, sy))
    arr[sx][sy] = 0
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 위, 오, 아래, 왼
    cnt = 1
    while q:
        tx, ty = q.pop(0)
        for d in range(4):
            nx, ny = tx + dx[d], ty + dy[d]
            if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = 0
                cnt += 1
    ans.append(cnt)
    return

N = int(input())    # 한 변 길이
arr = [list(map(int, list(input()))) for _ in range(N)]
total = 0
ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            total += 1
            bfs(i, j)
ans.sort()
print(total)
for a in ans:
    print(a)