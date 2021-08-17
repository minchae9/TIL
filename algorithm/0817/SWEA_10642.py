T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    ans = ''
    # 행
    for i in range(N):
        for j in range(N-M+1):
            s = ''
            for k in range(M):
                s += arr[i][j+k]
            for p in range(M//2):
                if s[p] != s[M-1-p]:
                    break
            else:
                ans = s
    # 열
    if ans == '':
        for i in range(N):
            for j in range(N-M+1):
                s = ''
                for k in range(M):
                    s += arr[j+k][i]
                for p in range(M):
                    if s[p] != s[M-1-p]:
                        break
                else:
                    ans = s

    print(f'#{t} {ans}')
