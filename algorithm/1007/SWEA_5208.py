def dfs(s, cnt): # 출발 정류장, 이동 횟수(= 교체횟수 + 1)
    global mn
    if s >= N:
        if cnt < mn:
            mn = cnt
        return
    else:
        if cnt >= mn:
            return
        for j in range(M[s], 0, -1):
            dfs(s+j, cnt+1)

T = int(input())
for tc in range(1, T+1):
    M = list(map(int, input().split())) # (목적지 빼고) 배터리 용량
    N = M[0]   # 정류장 수
    mn = 100
    dfs(1, -1)  # 교체횟수로 세기 위해 -1에서 시작
    print(f'#{tc} {mn}')