T = int(input())
for tc in range(T):
    H, W, N = map(int, input().split()) # H 층수, W 방의 개수, N 손님 순서

    if N % H:
        ans = str(N % H)
        hao = N // H + 1
    else:
        ans = str(H)
        hao = N // H
    if hao < 10:
        ans += '0'
    ans += str(hao)
    print(int(ans))