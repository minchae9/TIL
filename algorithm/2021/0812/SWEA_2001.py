T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    mx = 0
    for j in range(N-M+1):
        for i in range(N-M+1):
            flies = 0
            for k in range(M):
                for p in range(M):
                    flies += A[i+k][j+p]
            if flies > mx:
                mx = flies
    print(f'#{tc+1} {mx}')