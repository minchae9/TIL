T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input()))
    print(f'#{t}', end=' ')
    i = 0
    total = 0
    while i < 70:
        if arr[i]:
            total += arr[i] * (2 ** (6-(i%7)))
        if i % 7 == 6:
            print(total, end=' ')
            total = 0
        i += 1
    print()