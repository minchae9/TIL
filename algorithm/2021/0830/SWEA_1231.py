def inorder(n):
    if node[n]:
        inorder(left[n])
        print(node[n], end='')
        inorder(right[n])


for t in range(1, 11):
    N = int(input())    # 정점 개수
    info = [input().split() for _ in range(N)]
    node = [0]*(N+1)
    left = [0]*(N+1)
    right = [0]*(N+1)
    for i in range(len(info)):
        for j in range(len(info[i])):
            if j == 1:
                node[i+1] = info[i][j]
            elif j == 2:
                left[i+1] = int(info[i][j])
            elif j == 3:
                right[i+1] = int(info[i][j])
    print(f'#{t} ', end='')
    inorder(1)
    print()