import sys
input = sys.stdin.readline

N = int(input())
nums = [0] * N
for n in range(N):
    nums[n] = int(input())
nums = list(set(nums))
nums.sort()
for i in range(N):
    print(nums[i])