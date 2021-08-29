T = int(input())
for t in range(1, T+1):
    N = int(input())
    cards = list(input().split())
    if N%2:
        halfidx = (N+1)//2
    else:
        halfidx = N//2
    print(f'#{t}', end=' ')
    for i in range(N//2):
        print(cards[i], end=' ')
        print(cards[halfidx+i], end=' ')
    if N%2:
        print(cards[halfidx-1], end=' ')
    print()