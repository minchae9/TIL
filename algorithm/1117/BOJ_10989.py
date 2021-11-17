# 각 숫자의 개수를 세어 카운트 배열을 만든다. (숫자는 인덱스 번호로, 개수를 값으로)
# 카운트 배열을 누적 배열로 만든다.
# 기존 배열을 뒤에서부터 접근하여, 카운트 배열에서 해당 인덱스의 숫자가 무엇인지 확인하고, 거기에서 1을 빼서 그 인덱스에 접근한 값을 넣는다.
"""
메모리 초과로 구현 방법을 바꿈
"""
import sys


N = int(sys.stdin.readline())
# nums = [0] * N
count = [0] * 10001

for n in range(N):
    num = int(sys.stdin.readline())

# # 1단계
# maxNum = max(nums)
# count = [0] * (maxNum + 1)

    count[num] += 1

# # 2단계
# for j in range(1, maxNum+1):
#     count[j] += count[j-1]
#
# # 3단계
# ans = [0] * N
# for num in range(N-1, -1, -1):
#     val = count[nums[num]] - 1
#     ans[val] = nums[num]
#     count[nums[num]] -= 1


# 출력
for e in range(10001):
    if count[e]:
        for v in range(count[e]):
            print(e)