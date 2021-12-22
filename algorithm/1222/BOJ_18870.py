"""
참고: https://gudwns1243.tistory.com/52
나도 index 메서드를 사용해서 시간초과가 났다.
딕셔너리 방법을 사용해보게 됐다.
"""
import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
sorted_nums = sorted(list(set(nums)))
res = {sorted_nums[i]: i for i in range(len(sorted_nums))}
for item in nums:
    print(res[item], end=' ')