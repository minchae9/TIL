def bfs(i, j, N):
    q = []# 큐 생성
    visited = [[0]*16 for _ in range(16)]# visited 생성
    q.append((i, j))# 시작점 enqueue
    visited[i][j] = 1# (시작점 visited 표시)
    while q:
        a, b = q.pop(0) # pop
        if maze[a][b] == 3:
            return 1    # 처리
        for di, dj in [(0, -1), (-1, 0), (0, 1), (1, 0)]:  # 왼, 위, 오, 아래
            ni, nj = a+di, b+dj
            if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))  # 인접 노드 enqueue
                visited[ni][nj] = 1 # 인접 노드 visited 표시
    return 0


# def dfs(i, j, N):
#     if maze[i][j] == 3:
#         return 1
#     else:
#         for di, dj in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
#             ni, nj = i+di, j+dj
#             if maze[ni][nj] != 1 and visited[ni][nj] == 0:
#                 visited[ni][nj] += 1
#                 if dfs(ni, nj, N):
#                     return 1
#         return 0

for _ in range(10):
    t = int(input())
    maze = [list(map(int, list(input()))) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    # ans = dfs(1, 1, 16)
    ans = bfs(1, 1, 16)
    print(f'#{t} {ans}')