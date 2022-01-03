T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    mx = 0
    for i in range(N):
        for j in range(M):
            a = arr[i][j]
            total = a
            for p in range(1, a+1):
                di = [-p, 0, p, 0]
                dj = [0, p, 0, -p]
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < M:
                        total += arr[ni][nj]
            if total > mx:
                mx = total
    print(f'#{tc+1} {mx}')





