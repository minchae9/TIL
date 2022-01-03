"""부분집합의 합이 10이 되는 모든 경우를 출력하라."""
# 2. 재귀
def f1(i, N):
    if i == N:  # 모든 원소에 대한 고려가 끝난 경우
        s = 0
        for j in range(N):
            if bit[j] == 1:
                s += A[j]
        if s == 10:
            for j in range(N):
                if bit[j] == 1:
                    print(A[j], end=' ')
            print()
    else:
        bit[i] = 0
        f1(i+1, N)
        bit[i] = 1
        f1(i+1, N)


def f2(i, N, s, rs):    # rs: 남은 애들의 총합
    if i == N:
        if s == 10:
            for j in range(N):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    elif s > 50:
        return
    elif s + rs < 50:   # 백트래킹
        return
    else:
        bit[i] = 0
        f2(i+1, N, s, rs-A[i])
        bit[i] = 1
        f2(i+1, N, s+A[i], rs-A[i])



A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2.
bit = [0] * len(A)
# f1(0, 10)
f2(0, 50, 0)

# 1.
for i in range(1, 1 << 10):   # 공집합은 제외하고
    s = 0                   # i가 나타내는 부분집합의 합
    for j in range(10):
        if i & (1 << j):
            s += A[j]
    if s == 10:
        for j in range(10):
            if i & (1 << j):
                print(A[j], end=' ')
        print()