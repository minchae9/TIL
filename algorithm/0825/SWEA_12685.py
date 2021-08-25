T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    mx = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            ans = 0
            for r in range(M):
                ans += arr[i+r][j+r]        # 파리채와 영역이 겹치면, 죽인 파리 수에 합함
                if r != M-1-r:              # 중복 방지
                    ans += arr[i+r][j+M-1-r]
            if ans > mx:
                mx = ans
    print(f'#{t} {mx}')