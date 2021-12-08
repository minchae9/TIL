POS_X = 0
POS_Y = 1
CNT = 2
DIR = 3
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# 상하좌우
dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]
# 방향전환용
rev_dir = [0, DOWN, UP, RIGHT, LEFT]

def move():
    microbe_check = {}  # 이동 후 미생물 중복을 제거

    for i in range(K):
        microbe = microbes[i]
        x, y, cnt, dir = microbe

        if cnt == 0:    # 미생물 수가 0이면 패쓰
            continue

        # 이동
        new_x, new_y = x + dx[dir], y + dy[dir]
        microbe[POS_X], microbe[POS_Y] = new_x, new_y

        # 약품 있는 테두리로 이동 시, 반감 후 방향 전환
        if new_x in (0, N-1) or new_y in (0, N-1):
            microbe[CNT] //= 2
            microbe[DIR] = rev_dir[microbe[DIR]]
            continue

        # i) 좌표에 아무것도 없으면
        if (new_x, new_y) not in microbe_check:
            microbe_check[(new_x, new_y)] = (i, cnt)    # 미생물 등록
            continue

        # ii) 좌표에 이미 뭐가 있으면 (겹침)
        prev_max_i, prev_max_cnt = microbe_check[(new_x, new_y)]

        if prev_max_cnt < cnt:
            microbe_check[(new_x, new_y)] = (i, cnt)    # 등록
            microbe[CNT] += microbes[prev_max_i][CNT]   # 흡수
            microbes[prev_max_i][CNT] = 0
        else:
            microbes[prev_max_i][CNT] += microbe[CNT]   # 흡수 당함
            microbe[CNT] = 0



T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    microbes = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(M):
        move()

    res = sum(map(lambda microbe: microbe[CNT], microbes))
    print('#%d' % tc, res)