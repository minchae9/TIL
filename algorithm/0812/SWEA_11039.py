T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    w = h = 0
    area = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                w = h = 1
                a, b = i, j
                while arr[a][b+1] == 1:
                    w += 1
                    b += 1
                while arr[a+1][b] == 1:
                    h += 1
                    a += 1
            area.append(w*h)
    mx = 0
    for a in area:
        if a > mx:
            mx = a
    print(f'#{tc+1} {mx}')


