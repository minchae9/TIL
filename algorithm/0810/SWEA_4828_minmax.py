T = int(input())
for i in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    maxi = 0
    mini = 1000000
    for n in range(N):
        if numbers[n] > maxi:
            maxi = numbers[n]
        if numbers[n] < mini:
            mini = numbers[n]
    answer = maxi - mini
    print('#{} {}'.format(i+1, answer))