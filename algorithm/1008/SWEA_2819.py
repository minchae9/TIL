def dfs(x, y, s):
    if len(s) == 7:
        nums.add(s)
        return
    else:
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 위, 오, 아래, 왼
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<=nx<4 and 0<=ny<4:
                dfs(nx, ny, s+arr[nx][ny])

T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    nums = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])
    print(f'#{tc} {len(nums)}')