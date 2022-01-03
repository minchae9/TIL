for t in range(10):
    tc = input()
    pt = input()
    s = input()
    i = j = 0
    cnt = 0
    while i <= len(s)-len(pt)+1:
        if s[i] == pt[j]:
            i += 1
            if j == len(pt)-1:
                cnt += 1
                j = 0
            else:
                j += 1
        else:
            if j != 0:
                j = 0
            else:
                i += 1

    print(f'#{tc} {cnt}')