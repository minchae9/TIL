def dijkstra(start, arr, distance):
    # visited
    visited = [0] * (N+1)
    visited[start] = 1
    # distance
    distance[start] = 0
    # 인접 노드 거리 갱신
    for p in range(1, N+1):
        if arr[start][p] > 0:
            distance[p] = arr[start][p]

    # 최소값 갱신하며 돌기
    while sum(visited) < N:
        mn = 1000000
        for q in range(1, N+1):
            if visited[q] == 0 and distance[q] < mn:
                mn = distance[q]
                idx = q
        visited[idx] = 1

        for k in range(1, N+1):
            if arr[idx][k] > 0 and visited[k] == 0:
                distance[k] = min(distance[k], mn + arr[idx][k])
    return

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split()) # N 집 개수, M 도로 수, X 인수 집
    # 도로 저장
    org = [[0] * (N+1) for _ in range(N+1)]
    rev = [[0] * (N+1) for _ in range(N+1)] # 거꾸로 행렬
    for _ in range(M):
        x, y, c = map(int, input().split())
        org[x][y] = c
        rev[y][x] = c


    dist_org = [1000000] * (N + 1)
    dist_rev = [1000000] * (N + 1)

    mx = 0

    dijkstra(X, org, dist_org)
    dijkstra(X, rev, dist_rev)

    for i in range(1, N+1):
        ans = dist_org[i] + dist_rev[i]
        if ans > mx:
            mx = ans

    print(f'#{tc} {mx}')