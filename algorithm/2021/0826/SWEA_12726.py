T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for k in range(1, M + 1):
        if M % k == 0:      # M이 k의 배수: 전체 토글
            cnt += 1
        else:               # 아닐 때: 조건에 맞는 원소 토글
            for i in range(N):
                for j in range(N):
                    if (i+j+2) % k == 0:
                        arr[i][j] = (arr[i][j]+1)%2

    total = 0
    for i in range(N):
        for j in range(N):
            total += arr[i][j]

    if cnt % 2:         # 전체 토글 횟수가 홀수이면, (전체)-(1의 개수)
        ans = N**2 - total
    else:               # 전체 토글 횟수가 짝수이면, 1의 개수
        ans = total
    print(f'#{t} {ans}')