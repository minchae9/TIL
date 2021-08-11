N = int(input())
A = list(map(int, input().split()))
length = []
answer = []
for i in range(N):
    for k in range(i, N-i):
        std = A[i]
        inc = [std]
        if A[i+k] > std:
            inc.append(A[i+k])
            std = A[i+k]
        length.append(len(inc))
print(length)