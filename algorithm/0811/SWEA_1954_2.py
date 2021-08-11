T = int(input())
for t in range(T):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    cnt = 1
    i, j = 0, -1
    k = 0

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    while cnt <= N*N:
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            arr[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj
        else:
            k = (k+1)%4
    print(f'#{t+1}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()