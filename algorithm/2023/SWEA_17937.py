T = int(input())

for t in range(1, T+1):
    a, b = map(int, input().split())
    if b == a:
        ans = a
    else:
        ans = 1
    print(f'#{t} {ans}')