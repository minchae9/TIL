"""
dfs
"""

def dfs(x, y):
    global cnt
    cnt += 1
    arr[x][y] = 0   # 방문 표시
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0<=nx<N and 0<=ny<N and arr[nx][ny]:
            dfs(nx, ny)
    return cnt

N = int(input())    # 한 변 길이
arr = [list(map(int, list(input()))) for _ in range(N)]
total = 0
ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            total += 1
            cnt = 0
            val = dfs(i, j)
            ans.append(val)
ans.sort()
print(total)
for a in ans:
    print(a)