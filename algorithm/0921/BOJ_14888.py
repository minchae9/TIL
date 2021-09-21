"""
기호의 순열 조합 구하고
하나씩 뽑아서 숫자 사이에 넣는다.
그리고 연산 결과 구하기
(PyPy3으로 채점함)
"""
# 순열 조합
def dfs(i):
    global signs, mx, mn
    N = len(signs)
    if i == N:
        res = calculate()
        if res > mx:
            mx = res
        if res < mn:
            mn = res
        return
    else:
        for j in range(i, N):
            signs[i], signs[j] = signs[j], signs[i]
            dfs(i+1)
            signs[i], signs[j] = signs[j], signs[i]
# 계산
# 리스트는 = 으로 복사하면 shallow copy 된다는 점 유의하기!
def calculate():
    ans = nums[0]
    p, q = 0, 1
    while p < len(signs):
        t1 = ans
        s = signs[p]
        t2 = nums[q]
        if s == '+':
            ans = t1 + t2
        elif s == '-':
            ans = t1 - t2
        elif s == '//':
            if t1 < 0 and t2 > 0:
                ans = -((-t1)//t2)
            else:
                ans = t1 // t2
        else:   # s == '*'
            ans = t1 * t2
        p += 1
        q += 1
    return ans

N = int(input())
nums = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())
signs = ['+'] * plus + ['-'] * minus + ['*'] * multi + ['//'] * div
mx, mn = -1000000000, 1000000000
dfs(0)
print(mx, mn)