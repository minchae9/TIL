def align(R, i, s):
    global mn
    if i == N:
        total = 0
        for c in range(N):
            total += arr[R[c]][c]
        if total < mn:
            mn = total
        return
    else:
        if s >= mn:
            return
        for j in range(i, N):
            R[i], R[j] = R[j], R[i]
            align(R, i+1, s+arr[R[i]][i])
            R[i], R[j] = R[j], R[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 제품 수
    arr = [list(map(int, input().split())) for _ in range(N)]   # 공장별 생산비용
    product = [i for i in range(N)]
    # 0~N-1까지의 순열을 만들어서, 각 인덱스를 공장 순서로 하여 비용 계산하여 최소 비용 갱신
    mn = 99 * N * N
    align(product, 0, 0)
    print(f'#{tc} {mn}')