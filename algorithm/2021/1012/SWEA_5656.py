import copy

def bomb(lst, arr, cnt):
    global mn
    if cnt == N:
        res = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j] > 0:
                    res += 1
        if res < mn:
            mn = res
        return
    else:
        y = lst.pop(0)
        # 출발점 찾기
        for h in range(H):
            if arr[h][y] > 0:
                break
        # 폭파
        q = []
        q.append((h, y, arr[h][y]))
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]   # 위, 오, 아래, 왼
        while q:
            tx, ty, start = q.pop(0)
            for d in range(4):
                for k in range(1, start):
                    nx, ny = tx + dx[d]*k, ty + dy[d]*k
                    if 0<=nx<H and 0<=ny<W and arr[nx][ny] > 0 and (nx, ny, arr[nx][ny]) not in q:
                        q.append((nx, ny, arr[nx][ny]))
            arr[tx][ty] = 0
        # 아래로 정리하기
        for c in range(W):
            for r in range(H-1, -1, -1):
                for interval in range(H-r-1, 0, -1):
                    if arr[r][c] > 0 and arr[r+interval][c] == 0:
                        arr[r][c], arr[r+interval][c] = arr[r+interval][c], arr[r][c]
        # 다음 차례
        bomb(lst, arr, cnt+1)

def comb(n):
    global path
    if mn == 0: # 제한시간 초과 방지..
        return
    if n == N:
        arr = copy.deepcopy(org)
        lst = copy.deepcopy(path)
        bomb(lst, arr, 0)
        return
    else:
        for k in range(W):
            path[n] = k
            comb(n+1)


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split()) # N 횟수, W 가로, H 세로
    org = [list(map(int, input().split())) for _ in range(H)]
    path = [0] * N
    mn = W * H
    comb(0)
    print(f'#{tc} {mn}')