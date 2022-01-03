"""
출처: https://pacific-ocean.tistory.com/212
"""
n = int(input())
s = list(map(int, input().split()))
dp = []
dp.append(1)
for i in range(1, n):
    d = []
    for j in range(i):  # i 보다 앞에 있는 상자
        if s[i] > s[j]: # 상자 들어갈 수 있는 경우
            d.append(dp[j] + 1) # 누적해서 상자 더하기 (+1)
    if not d:   # d가 비어있는 경우, 즉, 앞에 더 작은 상자가 없었을 경우
        dp.append(1)    # 비어있는 상자 하나로, 1
    else:
        dp.append(max(d))
        # dp 리스트의 원소는 자기보다 작은 상자를 포함한 상자의 개수를 나타내게 된다.
print(max(dp))
