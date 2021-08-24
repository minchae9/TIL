def f(i, N, s): # P[i]의 값을 결정
    global minV
    if i == N:  # 순열 만들기 완료
        if minV > s:
            minV = s
        return
    else:
        if s >= minV:
            return
        else:
            for j in range(i, N): # P[i] <-> P[j] 자리교환
                P[i], P[j] = P[j], P[i]
                f(i+1, N, s+arr[i][P[i]])
                P[i], P[j] = P[j], P[i]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = 90
    P = list(k for k in range(N))
    f(0, N, 0)
    print(f'#{t} {minV}')
