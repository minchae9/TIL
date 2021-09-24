def price(n, s):    # n: 월, s: 총액
    global mn
    if n > 12:  # 계산 끝
        if s < mn:
            mn = s
    elif s >= mn:   # 백트랙킹
        return
    else:
        # 1개월치: 1일권, 1달권
        res = min(plans[n-1]*D, M)
        price(n+1, s+res)
        # 3개월치: 3달권
        price(n+3, s+Q)


T = int(input())
for t in range(1, T+1):
    D, M, Q, Y = map(int, input().split())
    plans = list(map(int, input().split()))
    mn = Y
    price(1, 0)
    print(f'#{t} {mn}')