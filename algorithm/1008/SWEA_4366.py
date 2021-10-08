T = int(input())
for tc in range(1, T+1):
    s_bi = input()
    s_tri = input()
    bi = int(s_bi, 2)
    tri = int(s_tri, 3)
    pb = [0] * len(s_bi)
    for k in range(len(s_bi)):
        b = len(s_bi) - 1 - k
        if s_bi[k] == '0':
            pb[k] = bi + (2 ** b)
        else:   #'1'
            pb[k] = bi - (2 ** b)
    for t in range(len(s_tri)):
        h = len(s_tri) - 1 - t
        if s_tri[t] == '0':
            can = [1, 2]
        elif s_tri[t] == '1':
            can = [-1, 1]
        else:   # '2'
            can = [-2, -1]
        for j in can:
            e = tri + j * (3 ** h)
            if e in pb:
                print(f'#{tc} {e}')
                break
