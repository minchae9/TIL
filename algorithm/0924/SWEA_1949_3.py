"""
현재 위치를 인자로 들고 다니는 버전 (설명 들은 내용)
"""
def dfs2(x, y, h, s, k):
    global visited, mx
    if s > mx:
        mx = s
    visited[x][y] = 1

    for p in range(4):
        nx, ny = x+dx[p], y+dy[p]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
            continue

        if h > site[nx][ny]:    # 안 파도 됨
            dfs2(nx, ny, site[nx][ny], s+1, k)
        elif k and h > site[nx][ny] - K:    # 팔 수 있음
            dfs2(nx, ny, site[x][y]-1, s+1, 0)

    visited[x][y] = 0






T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())    # N 지도 길이 K 최대 공사 깊이
    site = [list(map(int, input().split())) for _ in range(N)]
    # 가장 높은 봉우리 찾기
    peak = []
    mx_height = 21
    while not peak:
        mx_height -= 1
        for i in range(N):
            for j in range(N):
                if site[i][j] == mx_height:
                    peak.append((i, j))
    # 탐색
    visited = [[0]*N for _ in range(N)]
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]   # 위, 오, 아래, 왼
    mx = 1
    for a in range(len(peak)):
        x, y = peak[a][0], peak[a][1]
        dfs2(x, y, mx_height, 1, 1)
    print(f'#{t} {mx}')