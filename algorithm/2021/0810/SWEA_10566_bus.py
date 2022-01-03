T = int(input())
for t in range(T):
    K, N, M = map(int, input().split())
    gas = list(map(int, input().split()))

    answer = 0
    start = N
    while start > gas[0]:
        for i in range(K, 0, -1):
            if (start - i) in gas:
                answer += 1
                break
            elif (start - i) == 0:
                break
        start = start - i
    for n in range(M-1):
        if gas[n + 1] - gas[n] > K or gas[0] > K:
            answer = 0
            break

    print('#{} {}'.format(t+1, answer))