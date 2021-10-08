T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    clerks = list(map(int, input().split()))

    mn = 10000 * N
    for i in range(1 << N):
        tower = [0] * N
        for j in range(N):
            if i & (1 << j):
                tower[j] = clerks[j]
        if sum(tower) >= B:
            if sum(tower) < mn:
                mn = sum(tower)  # 최소값 갱신
    ans = mn - B
    print(f'#{tc} {ans}')