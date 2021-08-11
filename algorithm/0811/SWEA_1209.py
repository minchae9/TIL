for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    n = len(arr)
    total_rows = []
    total_columns = []
    left = 0
    right = 0
    for i in range(n):
        total = 0
        for j in range(n):
            total += arr[i][j]
        total_rows.append(total)
    for j in range(n):
        total = 0
        for i in range(n):
            total += arr[i][j]          # 주의하기: j로 컬럼 값 고정하려 했으므로 arr[j][i]로 쓰면 위 for문과 같아져버린다.
        total_columns.append(total)
    for i in range(n):
        for j in range(n):
            if i == j:
                left += arr[i][j]
            if i + j == n-1:
                right += arr[i][j]
    ALL = total_rows + total_columns + [left] + [right]
    ans = 0
    for a in ALL:
        if a > ans:
            ans = a
    print(f'#{tc} {ans}')