T = int(input())
for t in range(1, T+1):
    arr = [input() for _ in range(5)]
    ans = ''
    for j in range(15):
        for i in range(5):
            if j < len(arr[i]):         # j가 인덱스 범위 벗어나지 않을 때
                ans += arr[i][j]
    print(f'#{t} {ans}')