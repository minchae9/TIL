T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()
    N, M = len(str1), len(str2)
    ans = 0
    k = 0
    for i in range(N):
        for j in range(M):
            if str1[i] == str2[j]:
                i += 1
                j += 1
                if i == N:
                    ans = 1
                    break
            else:
                k += 1
                i = 0
                j = k
    print(f'#{t} {ans}')