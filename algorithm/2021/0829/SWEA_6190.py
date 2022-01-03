T = int(input())
for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    ans = -1
    flag = False
    for i in range(N-1):
        for j in range(i+1, N):
            testnum = numbers[i] * numbers[j]
            if testnum > ans:
                for k in range(len(str(testnum))-1):
                    if str(testnum)[k] > str(testnum)[k+1]:
                        break
                else:
                    ans = testnum
    print(f'#{t} {ans}')