TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    for j in range(N):  # 뒤에서부터 비트 체크
        if M & (1 << j):
            continue
        else:
            print(f'#{tc} OFF')
            break
    else:
        print(f'#{tc} ON')