def makeitwork(A, i, s):
    global mx
    if i == N:
        if s > mx:
            mx = s
        return
    else:
        if s <= mx:
            return
        for j in range(i, N):
            A[i], A[j] = A[j], A[i]
            makeitwork(A, i+1, s*(probs[i][nums[i]]/100))
            A[i], A[j] = A[j], A[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 직원 수이면서 일의 개수
    probs = [list(map(int, input().split())) for _ in range(N)]
    nums = [i for i in range(N)]
    mx = 0
    makeitwork(nums, 0, 1)
    mx = '%0.6f' % (mx*100)
    print(f'#{tc} {mx}')
