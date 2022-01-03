for tc in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    end = ladder[-1].index(2)
    i, j = 99, end
    K = [0, 1, 2]
    k = 1
    while i >= 0:
        if j-1 >= 0 and ladder[i][j-1] == 1:
            j -= 1
            while j-1 >= 0 and ladder[i-1][j] == 0:
                j -= 1
            else:
                i -= 1
        elif j+1 <= 99 and ladder[i][j+1] == 1:
            j += 1
            while j+1 <= 99 and ladder[i-1][j] == 0:
                j += 1
            else:
                i -= 1
        else:
            i -= 1
    print(f'#{T} {j}')


