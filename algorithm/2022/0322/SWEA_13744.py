## 시간초과
# import time
#
# start = time.time()

def dfs(x, y, cnt):
    global visited, res
    if (x, y) in restricted or (x, y) in visited:
        return
    if cnt >= (H * W - N) and x != org_i and y != org_j:
        res = 'yes'
        return
    if cnt > 0:
        visited.append((x, y))
    dfs((x+1) % H, y, cnt + 1)
    dfs(x, (y+1) % W, cnt + 1)
    if visited:
        visited.pop()


T = int(input())
for tc in range(1, T+1):
    H, W, N = map(int, input().split())
    # 방문 기록: (x, y)의 형태
    visited = []
    # 금지구역
    restricted = []
    for _ in range(N):
        i, j = map(int, input().split())
        restricted.append((i, j))
    # (0,0)부터 (H-1, W-1)까지
    # 행과 열이 visited에 없으면 pass, 있으면 이동할 수 있는 자리 계산
    res = ''
    flag = False
    for i in range(H):
        if flag:
            break
        for j in range(W):
            if (i, j) not in restricted:
                org_i, org_j = i, j
                dfs(i, j, 0)
                flag = True
                break
    if res == '':
        res = 'no'
    print(f'#{tc} {res}')
# print(f'Time: {time.time() - start}')