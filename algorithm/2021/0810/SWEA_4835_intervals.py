T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    mini = M * 10000
    maxi = 0
    for k in range(N-M+1):
        block = arr[k:k+M]
        sum_block = 0
        for b in block:
            sum_block += b
        if sum_block > maxi:
            maxi = sum_block
        if sum_block < mini:
            mini = sum_block
    answer = maxi - mini
    print('#{} {}'.format(t+1, answer))