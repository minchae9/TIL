def postorder(n):
    global ans
    if n <= N:
        if arr[n] != 0:
            return arr[n]
        else:
            if 2 * n + 1 > N:
                arr[n] = postorder(2 * n)
            else:
                arr[n] = postorder(2 * n) + postorder(2 * n + 1)
            return arr[n]


T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split()) # N 노드 개수, M 리프 노드 개수, L 출력 노드
    arr = [0] * (N + 1)
    for _ in range(M):
        num, val = map(int, input().split())
        arr[num] = val
    postorder(1)
    print(f'#{t} {arr[L]}')