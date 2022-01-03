T = int(input())
for t in range(1, T+1):
    N = int(input())
    pc = list(map(int, input().split()))

    # 최대값
    mx = 0
    for n in range(N):
        if pc[n] > mx:
            mx = pc[n]
            mx_idx = n

    bl = 0
    item = []

    k = 0
    while k <= N-1:
        if k < mx_idx:
            bl -= pc[k]
            item.append(pc[k])
            k += 1
        elif k == mx_idx:
            bl += mx*len(item)
            item = []

            mx = 0
            for p in range(k+1, N):
                if pc[p] > mx:
                    mx = pc[p]
                    mx_idx = p
            k += 1

    print(f'#{t} {bl}')