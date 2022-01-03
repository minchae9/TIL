def dfs(x, y, s, k):    # x,y 시작 좌표 s 등산로 길이 k 공사가능여부
    global visited, mx
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 위, 오, 아래, 왼
    for j in range(4):
        nx, ny = x+dx[j], y+dy[j]
        if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
            if site[nx][ny] < site[x][y]:   # 안 파도 됨
                visited[nx][ny] += 1
                dfs(nx, ny, s+1, k)
                visited[nx][ny] -= 1
            elif k == 1 and site[nx][ny] - K < site[x][y]:   # 팔 수 있음
                k = 0
                original = site[nx][ny]
                site[nx][ny] = site[x][y] - 1
                visited[nx][ny] += 1
                dfs(nx, ny, s+1, k)
                visited[nx][ny] -= 1
                site[nx][ny] = original
                k = 1
    else:
        if s > mx:
            mx = s
        return


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
    mx = 1
    for a in range(len(peak)):
        x, y = peak[a][0], peak[a][1]
        visited[x][y] = 1
        dfs(x, y, 1, 1)
        visited[x][y] = 0
    print(f'#{t} {mx}')