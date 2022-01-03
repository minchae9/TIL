T = int(input())
for tc in range(T):
    N, n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    mx = 0
    for i in range(N-n+1):
        for j in range(N-m+1):
            total = 0
            for a in range(n):
                for b in range(m):
                    total += A[i+a][j+b]
            if total > mx:
                mx = total
    print(f'#{tc+1} {mx}')