"""
설명 들었음.
"""
from collections import deque

def bfs(areas):
    ans = 0
    q = deque()
    visited = [[-1] * M for _ in range(N)]
    for a in range(len(areas)): # 물 위치 넣기
        x, y = areas[a]
        q.append(areas[a])
        visited[x][y] = 0
    while q:
        k, h = q.popleft()
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 위, 오, 아래, 왼
        for j in range(4):
            nx, ny = k+dx[j], h+dy[j]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] < 0 and arr[nx][ny] == 'L':
                visited[nx][ny] = visited[k][h] + 1
                q.append((nx, ny))
    for v in visited:
        ans += sum(v)
    return ans


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    lst = []
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 'W':
                lst.append((r, c))
    ans = bfs(lst)
    print(f'#{t} {ans}')