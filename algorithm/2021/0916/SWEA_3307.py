def dfs(s):
    global mx
    if s == N:
        if max(q) > mx:
            mx = max(q)
        return
    else:
        for j in range(s):
            if arr[s] >= arr[j]:
                if q[j] > q[s] - 1:
                    q[s] = q[j] + 1
        if q[s] == 0:
            q[s] = 1
        dfs(s+1)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    q = [1] + [0] * (N-1)
    mx = 1
    dfs(0)
    print(f'#{t} {mx}')