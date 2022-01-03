T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())    # N: 숫자의 개수, K: 크기 순서
    A = input() # 문자열
    nums = set()
    m = N // 4  # m: 한 변 숫자의 개수
    for i in range(m):
        k = i
        for j in range(4):
            if k + m >= N:
                num = A[k:] + A[:(k+m)%N]
            else:
                num = A[k:k+m]      # 각 변의 숫자
            nums.add(num)    # 전체 셋에 추가
            k += m
    # 생성 가능한 수 모아서 내림차순
    res = []
    for num in nums:
        res.append(int(num, 16))
    res.sort(reverse=True)
    # # K 번째로 큰 수
    ans = res[K-1]
    print(f'#{tc} {ans}')
