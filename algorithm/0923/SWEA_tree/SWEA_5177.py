T = int(input())
for t in range(1, T+1):
    N = int(input())
    tree = [0]
    node = list(map(int, input().split()))
    for n in range(N):
        v = node[n]
        tree.append(v)
        # 원소 삽입 시, 조건에 맞도록 조정
        k = n + 1
        while k > 0:
            if tree[k] < tree[k//2]:
                tree[k], tree[k//2] = tree[k//2], tree[k]
            k = k // 2

    ans = 0
    while N > 0:
        N = N // 2
        ans += tree[N]

    print(f'#{t} {ans}')