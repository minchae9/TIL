T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 방 한 변의 길이 N
    brd = [list(map(int, input().split())) for _ in range(N)]   # 지도
    mx = 100  # 정답

    # 계단을 찾고, 사람도 기록
    ppl = []
    stair_one = [0, 0]
    stair_two = [0, 0]
    one = 0
    for r in range(N):
        for a in range(N):
            if 2 <= brd[r][a] <= 10:
                if one == 0:
                    stair_one = [r, a, brd[r][a]]
                    one += 1
                else:
                    stair_two = [r, a, brd[r][a]]
            # 사람들에 인덱스로 번호 매기기
            elif brd[r][a] == 1:
                ppl.append((r, a))

    # 비트 연산: 0이면 1번 계단, 1이면 2번
    for i in range(2 ** len(ppl)):
        s_one = []
        s_two = []
        plan = []
        for j in range(len(ppl)):
            if i & (1 << j):
                plan.append(1)
            else:
                plan.append(0)

        # 각 계단에 ppl의 인덱스가 들어가 있고, 계단까지의 거리를 구한다.
        for k in range(len(ppl)):
            if plan[k] == 0:
                s_one.append(abs(ppl[k][0] - stair_one[0]) + abs(ppl[k][1] - stair_one[1]))
            else:
                s_two.append(abs(ppl[k][0] - stair_two[0]) + abs(ppl[k][1] - stair_two[1]))

        # 1번 계단
        s_one.sort()
        for p in range(len(s_one)):
            if p < 3:
                s_one[p] = s_one[p] + 1 + stair_one[2]
            else:
                s_one[p] = max(s_one[p-3], s_one[p] + 1) + stair_one[2]
        if s_one:
            mx_one = max(s_one)
        else:
            mx_one = 0

        # 2번 계단
        s_two.sort()
        for q in range(len(s_two)):
            if q < 3:
                s_two[q] = s_two[q] + 1 + stair_two[2]
            else:
                s_two[q] = max(s_two[q-3], s_two[q] + 1) + stair_two[2]
        if s_two:
            mx_two = max(s_two)
        else:
            mx_two = 0

        # 최종
        ans = max(mx_one, mx_two)
        if ans < mx:
            mx = ans

    print(f'#{tc} {mx}')