def getanswer(s, x, y):
    e = 1000000000
    z_org = y*100//x
    if z_org >= 99:         # <- 이 부분 넣어야 하는 것 다른 사람 풀이 참고함!
        return -1
    while s <= e:
        n = (s+e) // 2
        if (y+n)*100//(x+n) > z_org:
            result = n
            e = n - 1
        else:
            s = n + 1
    return result

X, Y = map(int, input().split())
print(getanswer(1, X, Y))