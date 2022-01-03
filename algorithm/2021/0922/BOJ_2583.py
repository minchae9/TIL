"""
좌표를 통해 행과 열을 특정하는 부분에서 조금 헤맸다.
2차원 행렬에서 첫 인자는 행을, 두 번째 인자에서 열을 특정한다는 점 기억하기!
"""

M, N, K = map(int, input().split())
# 지도 채우기
arr = [[-1]*N for _ in range(M)] # 가로 N, 세로 M
for s in range(K):
    lx, ly, rx, ry = map(int, input().split())
    ly = abs(ly-M)
    ry = abs(ry-M)
    for c in range(lx, rx):
        for r in range(ry, ly):
            arr[r][c] = 0

# 함수: 한 구역 개수 세기
# 네 방향이 모두 0이면: 분리된 구역
# 한 방향이라도 -1 또는 1이면: 연결된 구역
def bfs(r, c):
    global cnt
    q = []
    dh = [1, 0, -1, 0]  # 오, 아래, 왼, 위
    dv = [0, 1, 0, -1]
    q.append((r,c))
    arr[r][c] = 1
    while q:
        t, s = q.pop(0)
        for m in range(4):
            if 0 <= t + dv[m] < M and 0 <= s + dh[m] < N and arr[t + dv[m]][s + dh[m]] == -1:
                cnt += 1
                arr[t+dv[m]][s+dh[m]] = 1
                q.append((t+dv[m], s+dh[m]))
    return cnt


# 구역 개수 세기
ans = []
for r in range(M):
    for c in range(N):
        if arr[r][c] == 0:
            continue
        elif arr[r][c] == -1:
            cnt = 1
            res = bfs(r, c)
            ans.append(res)
        else:   # arr[r][c] == 1
            continue
ans.sort()
print(len(ans))
for k in range(len(ans)):
    print(ans[k], end=' ')