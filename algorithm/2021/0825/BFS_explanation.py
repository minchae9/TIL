'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
7 8
1 2 1 3 2 4 5 2 4 6 6 5 6 7 7 3
'''
"""
BFS 단계:
1) 큐 만들기
2) visited 만들기
3) 시작점 enque
4) 시작점의 visited 표시
"""

def bfs(s, V):  # s: 시작점, V: 정점 개수
    q = []  # 큐 생성
    visited = [0] * (V + 1)  # visited 생성
    q.append(s)  # 시작점 인큐
    visited[s] = 1  # 시작점 visited 표시
    while q:  # 큐가 비어있지 않으면 (처리할 정점이 남아 있으면)
        t = q.pop(0)  # 디큐 (꺼내서)해서 t에 저장
        print(t)  # t에 대한 처리
        for i in range(1, V + 1):  # t에 인접이고 미방문인 모든 i에 대해
            if adj[t][i] == 1 and visited[i] == 0:  # adj는 인접행렬
                q.append(i)  # enqueue(i)
                visited[i] = visited[t] + 1  # i visited로 표시 - 출발점으로부터의 거리를 나타내줌


def bfs2(s, V):
    q = []  # 큐 생성
    visited = [0] * (V + 1)  # visited 생성
    q.append(s)  # 시작점 인큐
    visited[s] = 1  # 시작점 visited 표시
    while q:  # 큐가 비어있지 않으면 (처리할 정점이 남아 있으면)
        t = q.pop(0)  # 디큐 (꺼내서)해서 t에 저장
        print(t)  # t에 대한 처리
        for i in adjList[t]:  # adjList는 인접 리스트. t에 인접이고 미방문인 모든 i에 대해
            if visited[i] == 0:
                q.append(i)  # enqueue(i)
                visited[i] = visited[t] + 1  # i visited로 표시


V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬
adjList = [[] for _ in range(V + 1)]        # 인접리스트

for i in range(E):  # 방향이 없는 그래프
    n1, n2 = edge[2 * i], edge[2 * i + 1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1

    adjList[n1].append(n2)
    adjList[n2].append(n1)

# bfs(1, V)
bfs2(1, V)

'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
7 8
1 2 1 3 2 4 5 2 4 6 6 5 6 7 7 3
'''


def bfs(s, V):
    q = [0] * V  # 큐생성
    front = -1  # 인덱스로 접근하는 방법: front와 rear 활용하기
    rear = -1
    visited = [0] * (V + 1)  # visited 생성
    rear += 1  # 시작점 인큐
    q[rear] = s     # rear이 데이터 저장
    visited[s] = 1  # 시작점 visited
    while front != rear:  # 큐가 비어있지 않으면
        front += 1  # 디큐해서 t에 저장
        t = q[front]    # front가 데이터 빼기
        print(t)
        for i in range(1, V + 1):  # t에 인접하고 미방문인 모든 i에 대해
            if adj[t][i] == 1 and visited[i] == 0:
                rear += 1  # 인큐 i
                q[rear] = i
                visited[i] = visited[t] + 1  # i 방문표시


V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0] * (V + 1) for _ in range(V + 1)]  # 인접행렬
adjList = [[] for _ in range(V + 1)]

for i in range(E):
    n1, n2 = edge[2 * i], edge[2 * i + 1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1  # 방향이 없는 그래프

    adjList[n1].append(n2)  # 인접리스트
    adjList[n2].append(n1)

bfs(1, V)