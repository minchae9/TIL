n = int(input())
nums = list(map(int, input().split()))
"""
n개의 수를 모두 선택하여 그 합을 기준으로,
양쪽에서 작은 수부터 제외해가며 합이 최대인 경우 갱신되도록 함.
"""
mx = sum(nums)
k = mx
s, e = 0, n-1
while e-s > 0:
    if nums[s] >= nums[e]:
        k -= nums[e]
        e -= 1
    else:
        k -= nums[s]
        s += 1
    if k > mx:
        mx = k
print(mx)