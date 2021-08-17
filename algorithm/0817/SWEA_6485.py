T = int(input())
for t in range(1, T+1):
    ans = ''
    N = int(input())
    arr = [0] * 5001
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            arr[i] += 1
    P = int(input())
    for _ in range(P):
        i = int(input())
        ans += str(arr[i]) + ' '

    print(f'#{t} {ans}')