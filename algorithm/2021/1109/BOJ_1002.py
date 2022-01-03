T = int(input())
for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distancesq = (x1 - x2) ** 2 + (y1 - y2) ** 2
    if x1 == x2 and y1 == y2:   # 원의 중심 일치
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif abs(r2 - r1) ** 2 == distancesq:   # 내접
        print(1)
    elif abs(r2 - r1) ** 2 > distancesq:    # 원 안에 원 (접하지 않음)
        print(0)
    else:
        if distancesq > (r1 + r2) ** 2:     # 원 떨어져 있음
            print(0)
        elif distancesq == (r1 + r2)**2:    # 외접
            print(1)
        else:
            print(2)                        # 교차