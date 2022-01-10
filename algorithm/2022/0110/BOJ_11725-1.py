"""
틀려서, 찾아보니 BFS 로 푸는 방법 있기에 시도해봄
-> 시간초과
"""
import sys
input = sys.stdin.readline

def bfs():
    # 1부터 시작
    q = [1]
    # 간선에 1 들어가면, 부모 배열에 1 추가, 자식은 queue
    while q:
        t = q.pop(0)
        for edge in edges:
            if t in edge:
                if edge[0] == t:
                    p = edge[1]
                elif edge[1] == t:
                    p = edge[0]
                if parent[p] == 0:
                    parent[p] = t
                    q.append(p)
        # 차례차례


N = int(input())
edges = []
parent = [0] * (N+1)
for n in range(N-1):
    a, b = map(int, input().split())
    edges.append((a, b))
bfs()
for i in range(2, N+1):
    print(parent[i])