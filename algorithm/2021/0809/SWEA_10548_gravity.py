# 오른쪽 원소 중 작은 원소의 개수만큼 낙하. 그 중 최대는?
"""
max_v = 0
cnt = 0  #A[i] > A[j]인 개수
for i: 0 -> N-2
    for j: i+1 -> N-1
        if A[i] > A[j]: cnt ++
    if max V < cnt: maxV = cnt
"""
T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    max_v = 0
    for i in range(N-1):
        cnt = 0
        for j in range(i+1, N):
            if A[i] > A[j]:
                cnt += 1
        if max_v < cnt:
            max_v = cnt
    print(f'#{t+1} {max_v}')