T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0 # 절대값 누적합
    # 각 원소에 먼저 접근하여, 주변 원소에 접근함
    for i in range(N):
        for j in range(N):
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj         # 주변 원소
                if 0 <= ni < N and 0 <= nj < N: # 배열을 벗어나지 않는 애들만
                    # ans += abs(arr[i][j] - arr[ni][nj])
                    ans += arr[i][j] - arr[ni][nj] if arr[i][j] > arr[ni][nj] else arr[ni][nj] - arr[i][j]
    print(f'#{t} {ans}')