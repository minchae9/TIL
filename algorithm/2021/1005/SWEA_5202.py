def maxitruck(e, cnt):
    global visited, mx
    if e == 24:
        if cnt > mx:
            mx = cnt
        return
    else:
        for j in range(N):
            if visited[j] == 0 and shift[j][0] >= e:
                visited[j] = 1
                maxitruck(shift[j][1], cnt + 1)
                visited[j] = 0
        if cnt > mx:
            mx = cnt
        return

T = int(input())
for t in range(1, T+1):
    N = int(input())    # 신청서
    shift = []
    for k in range(N):
        s, e = map(int, input().split())
        shift.append((s, e))
    mx = 0
    for i in range(N):
        visited = [0] * N
        visited[i] = 1
        maxitruck(shift[i][1], 1)
        if mx == N:
            break
    print(f'#{t} {mx}')