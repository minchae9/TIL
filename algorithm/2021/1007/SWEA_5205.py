def partition(A, l, r):
    p = A[l]
    i, j = l, r
    while i <= j:
        while i <= j and A[i] <= p:	# 피봇보다 큰 수를 찾아 왼쪽에서부터 이동
            i += 1
        while i <= j and A[j] >= p:	# 피봇보다 작은 수를 찾아 오른쪽에서부터 이동
            j -= 1
        if i < j:	# 교차하지 않으면, 교환
            A[i], A[j] = A[j], A[i]
    A[j], A[l] = A[l], A[j]	# 교차하여 while 문을 벗어나면, 피봇과 작은 수 자리(j)를 교환 -> 분기점
    return j

def qsort(A, l, r):
    if l < r:
        p = partition(A, l, r)
        qsort(A, l, p-1)
        qsort(A, p+1, r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    qsort(arr, 0, N-1)
    print(f'#{tc} {arr[int(N/2)]}')