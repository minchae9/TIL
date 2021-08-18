T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [input().split()for _ in range(N)]
    answer = [['']*3 for _ in range(N)]
    # 90도
    for j in range(N):
        for i in range(N-1, -1, -1):
            answer[j][0] += arr[i][j]
    # 180도
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            answer[N-1-i][1] += arr[i][j]
    # 270도
    for j in range(N-1, -1, -1):
        for i in range(N):
            answer[N-1-j][2] += arr[i][j]
    # 출력
    print(f'#{t}')
    for i in range(N):
        for j in range(3):
            print(answer[i][j], end=' ')
        print()