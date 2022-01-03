T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    # 십자
    for i in range(N):
        for j in range(N):
            cross = diag = arr[i][j]
            for p in range(1, M):
                # 왼, 위, 오, 아래
                di, dj = [0, -p, 0, p], [-p, 0, p, 0]
                dx, dy = [-p, -p, p, p], [-p, p, p, -p]
                for k in range(4):
                    ni, nj = i+di[k], j+dj[k]
                    nx, ny = i+dx[k], j+dy[k]
                    if 0<=ni<N and 0<=nj<N:
                        cross += arr[ni][nj]
                    if 0<=nx<N and 0<=ny<N:
                        diag += arr[nx][ny]
            if cross >= diag:
                if cross > mx:
                    mx = cross
            else:
                if diag > mx:
                    mx = diag
    print(f'#{t} {mx}')