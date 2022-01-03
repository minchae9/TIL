# 퀵소트
# 배열 A에 저장해서 오름차순 정렬했을 때 A[500000]의 값은?
import sys
sys.stdin = open('백만개.txt', 'r')

def lomuto(A, p, r):
    i = p - 1
    x = A[r]
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1



def hoare(A, l, r):
    i, j = l, r
    x = A[l]    # 피봇
    while i <= j:
        while i <= j and A[i] <= x:
            i += 1
        while i <= j and A[j] >= x:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j    # 피봇 위치


def qsort(A, l, r):
    if l < r:
        # p = hoare(A, l, r)
        p = lomuto(A, l, r)
        qsort(A, l, p-1)
        qsort(A, p+1, r)


# 선택정렬
def ssort(A, N):
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if A[minIdx] > A[j]:
                minIdx = j
        A[i], A[minIdx] = A[minIdx], A[i]



A = list(map(int, input().split()))
# qsort(A, 0, len(A)-1)
ssort(A, len(A))
print(A[500000])

