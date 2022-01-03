# 순열 구하기
"""
dfs 순열 구하기 어렴풋하게만 떠올라서 조금 고민했는데,
순서도를 떠올리기 힘들다보니
1) 어떤 조건에서 순열이 끝났다고 판단할 수 있는지
2) 재귀 함수의 인자는 어떻게 줘야 할지
두 가지가 막막했다.
그래서 예전에 내가 정리해둔 글을 보고 약간의 변형을 통해 문제를 풀었다.
순열 공부 다시..
"""
def get_abs(n):
    total = 0
    for i in range(n-1):
        total += abs(nums[i]-nums[i+1])
    return total

def dfs(t, n):
    global mx, nums
    if t == n:
        s = get_abs(n)
        if s > mx:
            mx = s
        return
    else:
        for j in range(t, n):
            nums[t], nums[j] = nums[j], nums[t]
            dfs(t+1, n)
            nums[t], nums[j] = nums[j], nums[t]





N = int(input())
nums = list(map(int, input().split()))
mx = 0
dfs(0, N)
print(mx)

