def includewho(cnt, s):
    global mn
    if cnt == N:
        if s >= B and s < mn:
            mn = s
        return
    else:
        # if s >= mn:
        #     return
        includewho(cnt+1, s+clerks[cnt])
        includewho(cnt+1, s)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    clerks = list(map(int, input().split()))
    mn = 10000*N
    includewho(0, 0)
    ans = mn - B
    print(f'#{tc} {ans}')