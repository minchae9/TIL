T = int(input())

dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]   # 왼, 위, 오, 아래

def bfs(x, y, C):
    global mx
    cnt = 0
    q = [(x, y)]
    while q:
        tx, ty = q.pop()
        for d in range(4):
            nx, ny = tx + dx[d], ty + dy[d]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == C and check[nx][ny] == 0:
                q.append((nx, ny))
                check[nx][ny] = 1
                cnt += 1
    if cnt > mx:
        mx = cnt
    return


for tc in range(1, T+1):
    N, M = map(int, input().split())    # 세로 N, 가로 M
    board = []
    a = b = 0   # 개수
    mx = 1
    check = [[0] * M for n in range(N)]
    for _ in range(N):
        board.append(list(input()))
    for r in range(N):
        for c in range(M):
            if check[r][c] == 0 and board[r][c] != '_':
                if board[r][c] == 'A':
                    a += 1
                else:
                    b += 1
                bfs(r, c, board[r][c])
    print(f'#{tc} {a} {b} {mx}')