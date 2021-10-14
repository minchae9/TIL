def dijkstra(cur):
    visited = [0] * (N + 1)
    visited[cur] = 1
    distance = [100000000] * (N + 1)
    distance[cur] = 0

    for d in range(N + 1):
        if arr[cur][d] > 0:
            distance[d] = arr[cur][d]

    while sum(visited) < (N + 1):
        mn = 100000000
        for j in range(1, N + 1):
            if visited[j] == 0 and distance[j] < mn:
                mn = distance[j]
                idx = j
        visited[idx] = 1

        for p in range(N + 1):
            if arr[idx][p] > 0 and visited[p] == 0:
                distance[p] = min(distance[p], mn + arr[idx][p])  # 출발점에서 정점까지의 거리 계산
    return distance[-1]  # 목적지까지의 거리


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())  # N 목적지 E 도로 수
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        arr[s][e] = w
    ans = dijkstra(0)
    print(f'#{tc} {ans}')