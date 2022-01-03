def synergy(lst):
    global mn
    cust_2 = []
    # cust_2의 식재료 정하기
    for i in range(N):
        if i not in lst:
            cust_2.append(i)
    # cust_1의 시너지 합
    syn_one = 0
    for a in range(len(cust_1)):
        for b in range(len(cust_1)):
            syn_one += arr[cust_1[a]][cust_1[b]]
    # cust_2의 시너지 합
    syn_two = 0
    for x in range(len(cust_2)):
        for y in range(len(cust_2)):
            syn_two += arr[cust_2[x]][cust_2[y]]
    # 차이
    diff = abs(syn_one - syn_two)
    # 최소값 갱신
    if diff < mn:
        mn = diff
    return

def firstcome(s, n):	# cust_1의 식재료 정하기
    if n == N/2:
        synergy(cust_1)
    else:
        for k in range(s, N):
            cust_1[n] = k
            firstcome(k+1, n+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 식재료의 수
    arr = [list(map(int, input().split())) for _ in range(N)]
    cust_1 = [0] * (N//2)
    mn = 99999
    firstcome(0, 0)
    print(f'#{tc} {mn}')