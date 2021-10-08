import sys

N, M = map(int, sys.stdin.readline().split())    # N 작업 개수, M 순서 정보 개수
arr = [[] for _ in range(N+1)]
for m in range(M):
    A, B = map(int, sys.stdin.readline().split())
    arr[B].append(A)  # 후 -> 선
X = int(sys.stdin.readline()) # 필수 작업

q = [X]
c = 0
visited = [0] * (N+1)
visited[X] = 1
while q:
    t = q.pop()
    for i in arr[t]:
        if visited[i] == 0:
            c += 1
            visited[i] = 1
            q.append(i)
print(c)