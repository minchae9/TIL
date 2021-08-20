T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        arr[s][e] = 1
    S, G = map(int, input().split())
    visited = [0]*(V+1)						# 방문한 노드는 1로 표시 (방문하지 않았다면 0)
    stack = []								   # 지나온 경로 저장할 스택
    v = S									   # 출발
    i = 1
    flag = False
    while True:
        if flag:
            break
        while i <= V:
            if arr[v][i] == 1 and visited[i] == 0:		# 현재 노드 v에서 타 노드 i로 이동 가능할 경우
                visited[v] = 1
                stack.append(v)
                v = i
                i = 1
                if v == G:
                    flag = True
                    ans = 1
                    break
            else:
                i += 1
        else:													# 현 노드에서 더이상 진행 불가
            if stack:
                visited[v] = 1
                v = stack.pop()
                i = 1
            else:
                ans = 0
                flag = True
                break
    else:
        ans = 0

    print(f'#{t} {ans}')