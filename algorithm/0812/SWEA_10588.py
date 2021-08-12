T = int(input())
for tc in range(T):
    N = int(input())
    sq = [list(map(int, input().split())) for _ in range(N)]
    brd = [[0] * 10 for _ in range(10)]
    for s in sq:
        for i in range(s[0], s[2]+1):       # 가로 길이
            for j in range(s[1], s[3]+1):   # 세로 길이
                if s[-1] == 1:              # red
                    brd[i][j] += 1
                else:                       # blue
                    brd[i][j] += 2
    ans = 0
    for i in range(10):
        for box in brd[i]:
            if box == 3:                    # purple
                ans += 1
    print(f'#{tc+1} {ans}')

