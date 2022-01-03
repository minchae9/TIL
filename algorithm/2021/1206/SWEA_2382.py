T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # N: 한 변 셀의 개수, M: 격리 시간, K: 군집의 수
    mp = [[[] for _ in range(N)] for _ in range(N)]    # 전체 지도
    position = [[0] * N for _ in range(N)]  # 미생물 현위치
    for _ in range(K):
        r, c, p, d = map(int, input().split())  # (순서대로) 세로위치, 가로위치, 미생물 수, 이동방향
        mp[r][c] = [p, d]
        position[r][c] = 1
    # 격리시간을 while 문으로 돌리며
    # 군집 이동시키고, r이나 c가 0 또는 N-1이면 i) 미생물 반 제거 ii) 방향 반전, 합쳐지면 합치기 등
    m = 0
    while m < M:
        # 각 군집에 대해 이동시키기
        new_mp = [[[] for _ in range(N)] for _ in range(N)]
        new_position = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if position[i][j] == 1:
                    cell = mp[i][j]
                    if cell[1] == 1:    # 위
                        new_mp[i-1][j].extend([cell[0], cell[1]])
                        new_position[i-1][j] = 1
                    elif cell[1] == 2:  # 아래
                        new_mp[i+1][j].extend([cell[0], cell[1]])
                        new_position[i+1][j] = 1
                    elif cell[1] == 3:  # 왼
                        new_mp[i][j-1].extend([cell[0], cell[1]])
                        new_position[i][j-1] = 1
                    else:               # 오
                        new_mp[i][j+1].extend([cell[0], cell[1]])
                        new_position[i][j+1] = 1
        # 이동한 군집에 대해 필요한 조치 취하기
        for i in range(N):
            for j in range(N):
                cell = new_mp[i][j]
                # 여러 개의 군집 모임
                if len(cell) > 2:
                    new = [0, 0]
                    mx = 0
                    for c in range(0, len(cell), 2):
                        new[0] += cell[c]   # 미생물 수
                        if cell[c] > mx:
                            mx = cell[c]
                            new[1] = cell[c+1]
                    new_mp[i][j] = new
                # 테두리
                cell = new_mp[i][j]
                if cell != [] and (i in (0, N - 1) or j in (0, N - 1)):
                    cell[0] //= 2
                    if cell[1] % 2:
                        cell[1] += 1
                    else:
                        cell[1] -= 1
        mp = new_mp
        position = new_position
        m += 1

    # 남아있는 미생물의 총합
    ans = 0
    for i in range(N):
        for j in range(N):
            cell = mp[i][j]
            if len(cell) > 0:
                ans += cell[0]
    print(f'#{tc} {ans}')