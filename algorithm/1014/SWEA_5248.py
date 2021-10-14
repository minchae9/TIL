T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    check = [n for n in range(N+1)]
    wants = list(map(int, input().split()))
    for i in range(M):
        a, b = wants[2*i], wants[2*i+1]
        if a > b:
            a, b = b, a

        for j in range(1, N+1):
            if check[j] == check[b]:
                check[j] = check[a]

    res = set(check)
    print(f'#{tc} {len(res)-1}')