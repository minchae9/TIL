"""
오답 코드이긴 한데, 첫 번째 집이 각각 빨, 초, 파인 경우를 나눠야 한다는 점까진 접근함.
"""

def f(x, c, rec):
    if c == N:
        return
    cost = 1000
    idx = -1
    for i in range(3):
        if i != x and bills[c][i] < cost:
            cost = bills[c][i]
            idx = i
    ans = rec[c-1] + cost
    if ans < rec[c]:
        rec[c] = ans
    f(idx, c+1, rec)

N = int(input())
bills = [list(map(int, input().split())) for _ in range(N)]
rec1 = [bills[0][0]] + [1000] * N
rec2 = [bills[0][1]] + [1000] * N
rec3 = [bills[0][2]] + [1000] * N
f(0, 1, rec1)
f(1, 1, rec2)
f(2, 1, rec3)
print(min(rec1[N-1], rec2[N-2], rec3[N-2]))