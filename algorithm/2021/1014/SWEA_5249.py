def dijkstra(cur):
    visited = [0] * (V+1)
    visited[cur] = 1
    distance = [1000000] * (V+1)
    distance[cur] = 0
    # 인접 노드까지의 거리 갱신
    for d in range(V+1):
        if arr[cur][d] > 0:
            distance[d] = arr[cur][d]
    # 각 지점에서 최소인 곳으로 거리 갱신하며
    while sum(visited) < (V+1):
        mn = 1000000
        for j in range(1, V+1):
            if visited[j] == 0 and distance[j] < mn:
                mn = distance[j]
                idx = j
        visited[idx] = 1

        for p in range(V+1):
            if arr[idx][p] > 0 and visited[p] == 0:
                distance[p] = min(distance[p], arr[idx][p])
    return sum(distance)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())    # (V+1) 노드, E 간선
    arr = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        arr[n1][n2] = arr[n2][n1] = w
    ans = dijkstra(0)
    print(f'#{tc} {ans}')