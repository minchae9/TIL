def bfs(x, y):
    el = L
    cnt = 1
    q = []
    newq = []
    q.append((x, y))
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1
    while q and el > 1:
        while True:
            tx, ty = q.pop(0)
            start = arr[tx][ty]
            for k in range(1, 8):
                if start == k:
                    for i in range(4):
                        if 0 <= tx + dx[i] < N and 0 <= ty + dy[i] < M and visited[tx+dx[i]][ty+dy[i]] == 0 and arr[tx + dx[i]][ty + dy[i]] in possible[k][i]:
                            cnt += 1
                            visited[tx + dx[i]][ty + dy[i]] = 1
                            newq.append((tx+dx[i], ty+dy[i]))
                    break
            if not q:
                el -= 1
                if el > 1:
                    q = newq
                    newq = []
            else:       # start를 바꾸기 위함
                continue
            break
    return cnt


T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())   # L: 소요된 시간
    arr = [[0] * M for _ in range(N)]
    for n in range(N):
        arr[n] = list(map(int, input().split()))
    cnt = 1
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 위, 오른, 아래, 왼
    possible = [[],
                [(1, 2, 5, 6), (1, 3, 6, 7), (1, 2, 4, 7), (1, 3, 4, 5)],
                [(1, 2, 5, 6), (-1,), (1, 2, 4, 7), (-1,)],
                [(-1,), (1, 3, 6, 7), (-1,), (1, 3, 4, 5)],
                [(1, 2, 5, 6), (1, 3, 6, 7), (-1,), (-1,)],
                [(-1,), (1, 3, 6, 7), (1, 2, 4, 7), (-1,)],
                [(-1,), (-1,), (1, 2, 4, 7), (1, 3, 4, 5)],
                [(1, 2, 5, 6), (-1,), (-1,), (1, 3, 4, 5)]
                ]
    print(f'#{t} {bfs(R, C)}')