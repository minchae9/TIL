T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    ppl = list(map(int, input().split()))
    # 손님 정렬
    for i in range(len(ppl)-1, 0, -1):
        for j in range(i):
            if ppl[j] > ppl[j+1]:
                ppl[j], ppl[j+1] = ppl[j+1], ppl[j]
    taken = 0
    # 붕어빵 개수
    for person in ppl:
        time = person // M
        cake = person // M * K
        if (cake - taken) >= 1:
            taken += 1
        else:
            ans = 'Impossible'
            break
    else:
        ans = 'Possible'
    print(f'#{t} {ans}')