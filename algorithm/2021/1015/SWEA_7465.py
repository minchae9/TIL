def bfs(p):
    global visited
    q = [p]
    visited[p] = 1
    while q:
        t = q.pop(0)
        for j in range(1, N+1):
            if arr[t][j] == 1 and visited[j] == 0:
                q.append(j)
                visited[j] = 1   # 방문 표시

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 전체 사람 수, M 관계 수
    # 관계 표시
    arr = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        p1, p2 = map(int, input().split())
        arr[p1][p2] = arr[p2][p1] = 1
    cnt = 0
    visited = [0] * (N+1)
    for i in range(1, N+1):
        if visited[i] == 0:
            cnt += 1    # bfs 도는 횟수를 셈
            bfs(i)
            if sum(visited) == N:
                break
    print(f'#{tc} {cnt}')