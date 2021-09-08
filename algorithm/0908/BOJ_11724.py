"""
input() 대신 sys.stdin.readline() 사용하니 시간 초과가 나지 않음.\

bfs를 활용하여 각 노드를 탐색하여 노드가 연결되면 visited 표시를 하도록 했다.
해당 함수에 대해 for문을 돌려서 노드가 방문하지 않은 노드이면 함수를 실행하도록 했는데, 
이는 한 번에 돌 수 있는 그래프라면 모두 방문 노드로 표시될 것이고,
아니라면 다른 그래프일 것이기 때문이다.
함수를 실행하는 횟수를 세어 연결요소의 개수를 세었다.
"""
import sys

def bfs(s):
    global visited
    q = []
    q.append(s)
    visited[s] = 1
    while q:
        if 0 not in visited:
            return
        t = q.pop(0)
        for d in range(N):
            if arr[t][d] and visited[d] == 0:
                q.append(d)
                visited[d] = visited[t] + 1

N, M = map(int, sys.stdin.readline().split())    # N: 정점 개수, M: 간선 개수
arr = [[0]*N for _ in range(N)]
for e in range(M):
    u, v = map(int, sys.stdin.readline().split())
    arr[u-1][v-1] = arr[v-1][u-1] = 1
count = 0
visited = [0] * N
for s in range(N):
    if visited[s] == 0:
        count += 1
        bfs(s)

print(count)