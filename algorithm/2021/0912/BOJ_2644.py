def bfs(s):
    q = []
    visited = [0] * (n+1)
    q.append(s)
    while q:
        t = q.pop(0)
        if t == p2:
            return visited[t]
        for j in range(1, n+1):
            if t != j and visited[j] == 0 and arr[t][j]:
                q.append(j)
                visited[j] = visited[t] + 1 # 간선 수 계산하는 bfs 방법
    return -1


n = int(input())    # 전체 사람 수
p1, p2 = map(int, input().split())    # 구해야 할 대상
m = int(input())    # 부모-자식 관계의 수
arr = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    p, c = map(int, input().split())
    arr[p][c] = arr[c][p] = 1
print(bfs(p1))