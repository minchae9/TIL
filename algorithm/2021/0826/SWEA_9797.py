def shortest(s, e):
    q = [] # 큐 생성
    visited = [0]*(V+1)# visited 생성
    q.append(s)# 시작점 enqueue
    while q:# 처리
        t = q.pop(0)
        if t == e:
            return visited[t]
        else:
            for i in range(1, V+1):
                if arr[t][i] == 1 and visited[i] == 0:
                    q.append(i) # 인접 정점 enqueue
                    visited[i] = visited[t] + 1 # 인접 정점 visited 표시
    return 0

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]   # 인접 그래프 만들기
    for _ in range(E):
        i, j = map(int, input().split())
        arr[i][j] = arr[j][i] = 1
    S, G = map(int, input().split())
    ans = shortest(S, G)
    print(f'#{t} {ans}')