T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    pz = [list(map(int, input().split())) for _ in range(N)]
    npz = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            npz[i][j] = pz[j][i]
    bk = []
    r_cnt = c_cnt = 0
    ans = 0
    for i in range(N):
        r_cnt = c_cnt = 0
        for j in range(N):
            if pz[i][j] == 1:
                r_cnt += 1
            else:
                if r_cnt == K:
                    ans += 1
                r_cnt = 0

            if npz[i][j] == 1:
                c_cnt += 1
            else:
                if c_cnt == K:
                    ans += 1
                c_cnt = 0
        if r_cnt == K:
            ans += 1
        if c_cnt == K:
            ans += 1

    print(f'#{t} {ans}')