T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [p for p in range(1, N * N + 1)]  # 1부터 N*N 까지의 수
    word = 1
    snail = [[0] * N for _ in range(N)]     # 수 넣을 2차원 배열
    i, j = 0, -1
    k = 0
    while word <= N * N:
        if k % 4 == 0:                      # k 값 늘리며 나머지에 따라 다른 작업
            while j < N - 1:                # 오른쪽으로
                if snail[i][j + 1] == 0:
                    j += 1
                    snail[i][j] = word
                    word += 1
                else:
                    k += 1
                    break
            else:
                k += 1


        elif k % 4 == 1:                    # 아래쪽으로
            while i < N - 1:
                if snail[i + 1][j] == 0:
                    i += 1
                    snail[i][j] = word
                    word += 1
                else:
                    k += 1
                    break
            else:
                k += 1


        elif k % 4 == 2:                    # 왼쪽으로
            while j > 0:
                if snail[i][j - 1] == 0:
                    j -= 1
                    snail[i][j] = word
                    word += 1
                else:
                    k += 1
                    break
            else:
                k += 1


        else:                               # 위쪽으로
            while i > 0:
                if snail[i - 1][j] == 0:
                    i -= 1
                    snail[i][j] = word
                    word += 1
                else:
                    k += 1
                    break

            else:
                k += 1

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end = ' ')
        print()
