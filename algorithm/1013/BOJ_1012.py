def bfs(i, j):
    global cnt
    q = [(i, j)]
    arr[i][j] = 0   # 방문표시
    while q:
        tx, ty = q.pop(0)
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = tx+dx, ty+dy
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = 0

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split()) # M 가로 N 세로 K 배추 심어진 개수
    arr = [[0] * M for _ in range(N)]
    cnt = 0
    # 배추 심어진 위치를 1로 표시
    for _ in range(K):
        y, x = map(int, input().split())
        arr[x][y] = 1
    # bfs로 탐색하며 구역 개수 구하기
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                cnt += 1
                bfs(i, j)
    print(cnt)