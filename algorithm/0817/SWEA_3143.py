T = int(input())
for t in range(T):
    A, B = input().split()
    cnt = 0
    i = j = 0
    while i < len(A):
        if A[i] == B[j]:
            i += 1
            j += 1
            if j == len(B):
                cnt +=1
                j = 0
        else:
            if j != 0:
                j = 0
            else:
                i += 1

    total = len(A) - (len(B)-1)*cnt
    print(f'#{t+1} {total}')