T = int(input())
for tc in range(T):
    ttl, pa, pb = map(int, input().split())
    a_times = 0
    b_times = 0
    la = lb = 1
    ra = rb = ttl
    while la < ra:              # A 계산
        c = (la+ra)//2
        a_times += 1
        if c == pa:
            break
        elif c < pa:
            la = c
        else:
            ra = c
    while lb < rb:              # B 계산
        c = (lb + rb) // 2
        b_times += 1
        if c == pb:
            break
        elif c < pb:
            lb = c
        else:
            rb = c
    if a_times < b_times:       # 이긴 사람 출력
        print(f'#{tc + 1} A')
    elif a_times > b_times:
        print(f'#{tc + 1} B')
    else:
        print(f'#{tc + 1} 0')

