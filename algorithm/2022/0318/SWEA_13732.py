T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sharps = []
    ans = ''
    for i in range(N):
        line = input()
        for j in range(len(line)):
            if line[j] == '#':
                sharps.append((i, j))
    sharps.sort(key=lambda x: (x[0], x[1]))
    if len(sharps) ** (1/2) > int(len(sharps) ** (1/2)):
        ans = 'no'
    if ans == '':
        for r in range(sharps[0][0], sharps[-1][0]+1):
            if ans:
                break
            for c in range(sharps[0][1], sharps[-1][1]+1):
                if (r, c) not in sharps:
                    ans = 'no'
                    break
        else:
            ans = 'yes'
    print(f'#{tc} {ans}')
