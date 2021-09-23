def postorder(x): # 후위순회
    global cnt
    if 0 < x <= V:
        postorder(child_1[x])
        postorder(child_2[x])
        cnt += 1



T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())    # E 간선 개수, N 루트 노드
    arr = list(map(int, input().split()))

    # 자식 노드 배열에 표현
    V = E + 1   # V 노드 개수
    child_1 = [0] * (V + 1)
    child_2 = [0] * (V + 1)
    for e in range(E):
        p, c = arr[2*e], arr[2*e+1]
        if child_1[p]:
            child_2[p] = c
        else:
            child_1[p] = c
    cnt = 0
    postorder(N)
    print(f'#{t} {cnt}')