T = int(input())
for t in range(T):
    N = int(input())
    crts = list(map(int, input().split()))

    total = 0           # 전체 당근 개수
    for crt in crts:
        total += crt

    idx = 0
    diff = 10
    for i in range(1, N):      # 구역 나누고, 각 구역 당근 개수 구하기
        left, right = crts[0:i], crts[i:N]
        t_left = t_right = 0
        for l in left:
            t_left += l
        for r in right:
            t_right += r

        if 0 < t_left - t_right < diff: # 차이 계산
            idx = i
            diff = t_left - t_right
        elif 0 < t_right - t_left < diff:
            idx = i
            diff = t_right - t_left
    print('#{} {} {}'.format(t+1, idx, diff))


