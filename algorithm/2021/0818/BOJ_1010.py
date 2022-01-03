def comb(n, m):                 # nCk 구하는 함수를 만듦 (조합)
    a, s = 0, 1
    i = j = n-1
    while i < m:                # 분모
        p = 1
        k = i
        for _ in range(n-1):
            p *= k
            k -= 1
        a += p   
        i += 1
    for _ in range(1, n):       # 분자
        s *= j
        j -= 1
    return int(a / s)

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    print(comb(N, M))