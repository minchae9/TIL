T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [0, 1, 0, -1]                  # 델타 따로
    dj = [1, 0, -1, 0]
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):          # 4개니까
                dx, dy = i + di[k], j + dj[k]
                if 0 <= dx < N and 0 <= dy < N:    # 범위 벗어나지 않을 때만
                    ans += abs(arr[i][j] - arr[dx][dy])
    print(f'#{t+1} {ans}')
