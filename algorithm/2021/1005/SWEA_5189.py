def findpath(c, total):
    global office, mn
    if c == N:
        ans = total + arr[office[-1]][0]
        if ans < mn:
            mn = ans
        return
    else:
        if total >= mn:
            return
        for j in range(c, N):
            office[c], office[j] = office[j], office[c]
            findpath(c+1, total + arr[office[c-1]][office[c]])
            office[c], office[j] = office[j], office[c]


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    office = [0] + [i for i in range(1, N)]

    mn = 300
    findpath(1, 0)
    print(f'#{t} {mn}')
