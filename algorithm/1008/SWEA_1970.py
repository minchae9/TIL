T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 액수
    ans = [0] * 8

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in range(8):
        if (N // money[i]) > 0:
            ans[i] = N // money[i]
            N -= (N//money[i]) * money[i]
            if N == 0:
                break
    print(f'#{tc}')
    for a in ans:
        print(a, end=' ')
    print()
