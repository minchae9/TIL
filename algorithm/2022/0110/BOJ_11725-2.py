"""
참고: https://jinho-study.tistory.com/884
각 노드에 연결된 상대 노드를 저장하여 부모 찾기
어차피 1부터, 즉 루트부터 아래로 내려가며 찾으므로 부모노드가 저장되게 된다.
"""
import sys
input = sys.stdin.readline

def bfs():
    q = [1]
    while q:
        t = q.pop(0)
        for next in connection[t]:
            if parent[next] == 0:
                parent[next] = t
                q.append(next)

N = int(input())
connection = [[] for _ in range(N+1)]
parent = [0] * (N+1)
parent[1] = 1
for n in range(N-1):
    a, b = map(int, input().split())
    connection[a].append(b)
    connection[b].append(a)
bfs()
for i in range(2, N+1):
    print(parent[i])