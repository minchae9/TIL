T = int(input())
for t in range(1, T+1):
    N = float(input())
    ans = ''
    for i in range(1, 13):
        if N <= 0:
            break
        k = 2 ** (-i)
        if N >= k:
            N -= k
            ans += '1'
        else:
            ans += '0'
    if N > 0:
        print(f'#{t} overflow')
    else:
        print(f'#{t} {ans}')