from collections import deque

def bfs(n):
    global cnt
    q = deque()
    q.append(n)
    nq = deque()
    beenthere = set()
    while True:
        if q:
            t = q.popleft()
            d = [t+1, t-1, t*2, t-10]
            for i in range(4):
                if 0 < d[i] <= 1000000 and d[i] not in beenthere:
                    if d[i] == M:
                        return
                    beenthere.add(d[i])
                    nq.append(d[i])
        elif nq:
            cnt += 1
            q, nq = nq, q


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 원래 수, M 만들 수
    cnt = 1
    bfs(N)
    print(f'#{tc} {cnt}')