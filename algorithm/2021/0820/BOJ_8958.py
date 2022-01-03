T = int(input())
for _ in range(T):
    ans = 0
    cnt = 0
    res = input()
    for c in res:
        if c == 'O':
            cnt += 1
            ans += cnt
        else:
            cnt = 0
    print(ans)