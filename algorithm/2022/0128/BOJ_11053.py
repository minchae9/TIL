N = int(input())
A = list(map(int, input().split()))
rec = [1] + [0] * N
for i in range(1, N):
    mx = 0
    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            if rec[j] > mx:
                mx = rec[j]
    rec[i] = mx + 1
print(max(rec))
