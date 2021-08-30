def omok(i, j, c, k):
    if c == 5:
        return 1
    move = [(0, 1), (1, 0), (1, 1), (1, -1)]
    ni, nj = i+move[k][0], j+move[k][1]
    if 0<=ni<N and 0<=nj<N and arr[ni][nj]=='o':
        return omok(ni, nj, c+1, k)
    return 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = 'NO'
    for i in range(N):
        if ans == 'YES':
            break
        for j in range(N):
            if ans == 'YES':
                break
            if arr[i][j] == 'o':
                for k in range(4):
                    if omok(i, j, 1, k):
                        ans = 'YES'
                        break
    print(f'#{t} {ans}')