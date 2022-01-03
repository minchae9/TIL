T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    mx = 0
    for i in range(N):
        for j in range(N):
            total = 0
            for k in range(N):
                total += arr[i][k]
                total += arr[k][j]
            total -= arr[i][j]
            if total > mx:
                mx = total
    print(f'#{tc+1} {mx}')
