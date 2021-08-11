def f(A):
    for i in range(1, 1<<10)    # 10개 원소의 포함 여부 표시
        s = 0
        for j in range(10):
            if i & (1<<j):
                s += A[j]
                if s== 0:
                    return 1
    return 0

T = int(input())
for t in range(T):
    arr = list(map(int, input().split()))
    print(f'#{t+1} {f(arr)}')