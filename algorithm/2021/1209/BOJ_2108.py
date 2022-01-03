"""
최빈값 참고자료: https://codepractice.tistory.com/71
"""
import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
nums = [0] * N
for i in range(N):
    nums[i] = int(input())
# 산술평균
avg = round(sum(nums) / N)

# 중앙값
nums.sort()
mid = nums[N//2]

# 최빈값 (시간초과 -> 외부 자료 참고함)
def modefinder(numbers):
    c = Counter(numbers)
    order = c.most_common()
    maximum = order[0][1]

    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    if len(modes) == 1:
        return modes[0]
    else:
        modes.sort()
        return modes[1]

most = modefinder(nums)

# 범위
rng = nums[-1] - nums[0]

# 출력
print(avg)
print(mid)
print(most)
print(rng)