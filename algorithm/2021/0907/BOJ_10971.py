def dfs(s, n, c):
    global cost, visited
    if n == 1:  # 출발점으로 돌아가야 함
        if arr[s][start]:   # 출발점으로 돌아갈 수 있는지 확인해야 함!!!
            c += arr[s][start]
            if c < cost:
                cost = c
        return
    else:
        if c > cost:
            return
        for d in range(N):
            if d != start and visited[d] == 0 and arr[s][d] > 0:
                visited[d] += 1
                dfs(d, n-1, c + arr[s][d])
                visited[d] -= 1


N = int(input())  # 도시의 수
arr = [list(map(int, input().split())) for _ in range(N)]
# arr의 요소가 0 이상인 경우만 갈 수 있고, visited로 표시하고, c 늘릴 것
cost = 1000000 * N
num = N
for s in range(N):
    start = s
    visited = [0] * N
    dfs(s, num, 0)
print(cost)

