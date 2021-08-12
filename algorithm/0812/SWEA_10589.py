T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for tc in range(T):
    N, K = map(int, input().split())

    ans = []
    num = 0
    for i in range(1<<12):
        arr = []
        for j in range(12):
            if i & (1<<j):
                arr.append(A[j])    # 부분집합 요소 arr에 넣기
        if len(arr) == N:
            ans.append(arr)         # 부분집합 길이가 N이면 ans에 해당 부분집합을 넣기

    res = 0                         # 부분집합의 합이 K인 개수 출력
    for lst in ans:
        total = 0
        for a in lst:
            total += a
        if total == K:
            res += 1
    print(f'#{tc+1} {res}')

