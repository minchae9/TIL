def room(r, n):
    return (arr[r][n]+1) // 2

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    chk = [0] * 201
    cnt = 0
    mx = 0
    for i in range(N):
        if arr[i][0] < arr[i][1]:
            s, e = room(i, 0), room(i, 1)
        else:
            s, e = room(i, 1), room(i, 0)
        for r in range(s, e+1):
            chk[r] += 1
    for times in chk:
        if times > mx:
            mx = times
    print(f'#{t} {mx}')
