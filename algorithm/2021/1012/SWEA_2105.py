def cafetour(x, y, c):
    global mx, visited

    if c > 3:   # 범위 벗어나므로 return
        return

    moves = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    nx, ny = x + moves[c][0], y + moves[c][1]

    if c == 3 and (nx, ny) == start:    # 출발점에 돌아옴
        if len(visited) > mx:
            mx = len(visited)
        return

    if 0<=nx<N and 0<=ny<N and arr[nx][ny] not in visited:
        visited.append(arr[nx][ny])
        cafetour(nx, ny, c) # 가던 방향으로 계속 진행
        cafetour(nx, ny, c+1)   # 방향 꺾음
        visited.pop()
    else:
        return


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 한 변 길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = -1
    for r in range(N-2):
        for s in range(1, N-1):
            start = (r, s)
            visited = [arr[r][s]]
            cafetour(r, s, 0)
    print(f'#{tc} {mx}')