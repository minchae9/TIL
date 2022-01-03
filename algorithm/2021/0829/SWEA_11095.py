T = int(input())
for t in range(1, T+1):
    N = int(input())
    commands = [list(map(int, input().split())) for _ in range(N)]
    floor = [[0]*10 for _ in range(10)]     # 전체 타일
    cnt = 0     # 새로 칠하는 타일 개수를 세는 변수
    for c in range(N):  # 각 명령에 대해
        r1, c1, r2, c2 = commands[c][0], commands[c][1], commands[c][2], commands[c][3]
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if floor[i][j] == 0:
                    cnt += 1    # 안 칠한 타일이면 cnt += 1
                floor[i][j] = 1
    print(f'#{t} {cnt}')