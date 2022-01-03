T = int(input())
for t in range(1, T+1):
    N, hexa = input().split()
    ans = ''
    for h in hexa:
        num = int(h, 16)
        for j in range(3, -1, -1):
            if num & (1 << j):
                ans += '1'
            else:
                ans += '0'
    print(f'#{t} {ans}')