T = int(input())
for t in range(T):
    k = int(input())    # k층
    n = int(input())    # n호
    arr = [[0] * (n+1) for _ in range(k+1)]

    for i in range(k+1):
        for j in range(1, n+1):
            if i == 0:  # 0층
                arr[i][j] = j
            elif j == 1:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i][j-1] + arr[i-1][j]
    print(arr[k][n])