T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split()) # N 노드 개수, M 리프 노드 개수, L 출력 노드
    arr = [0] * (N + 1)
    for _ in range(M):
        num, val = map(int, input().split())
        arr[num] = val
    for n in range(N-M, 0, -1):
        if 2*n+1 > N:   # 리프 노드가 하나인 노드
            arr[n] = arr[2*n]
        else:
            arr[n] = arr[2*n] + arr[2*n+1]
    print(f'#{t} {arr[L]}')
