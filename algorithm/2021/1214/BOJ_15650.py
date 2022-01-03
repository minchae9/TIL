def numcomb(prev, c):
    global res
    if c == M:
        for i in range(c):
            print(res[i], end=' ')
        print()
        return
    else:
        for p in range(prev+1, N+1):
            res.append(p)
            numcomb(p, c+1)
            res.pop()

N, M = map(int, input().split())    # 1부터 N까지, 중복없이 M개
res = []
numcomb(0, 0)