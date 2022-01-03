T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())    # 퍼즐 길이 N, 단어 길이 K
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # 1인 부분이 단어가 들어갈 수 있는 부분
    ans = 0
    # 가로 탐색하면서, 길이가 딱 K 나오면 +1
    for i in range(N):
        row = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                row += 1
            else:
                if row == K:
                    ans += 1
                row = 0
        if row == K:
            ans += 1

    # 세로 탐색하면서, 길이가 딱 K 나오면 +1
    for p in range(N):
        col = 0
        for q in range(N):
            if puzzle[q][p] == 1:
                col += 1
            else:
                if col == K:
                    ans += 1
                col = 0
        if col == K:
            ans += 1

    print(f'#{tc} {ans}')