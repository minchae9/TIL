T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # A 정수 개수, B 정수 개수
    A = list(map(int, input().split()))
    A = sorted(A)
    B = list(map(int, input().split()))

    # 리스트 B의 각 원소에 대하여, A에 속해있는지, 그렇다면 번갈아 탐색되는지 확인
    cnt = 0
    for b in B:
        if b in A:  # A의 원소라면
            l, r = 0, N-1
            d = 0   # 처음
            while True:
                m = (l + r) // 2
                if b == A[m]:
                    cnt += 1
                    break
                elif b < A[m]:
                    if d >= 0:
                        d = -1  # 왼쪽
                    else:
                        break
                    r = m-1
                elif b > A[m]:
                    if d <= 0:
                        d = 1   # 오른쪽
                    else:
                        break
                    l = m+1
    print(f'#{tc} {cnt}')