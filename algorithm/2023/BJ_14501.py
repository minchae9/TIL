"""pseudo code
money = 0
def f(x, now):
    if x > N:
        money = now
        return
    if x <= N:
        f(x + T[x], now + P[x])
        f(x+1, now)
"""
# 그날 일을 하거나, 하지 않거나(다음 날 탐색)를 모두 찍고 와보는 방식
# 함수로 정의하여 재귀적으로 구현. N+1 조건은 마지막 날에 1일짜리 일을 하는 경우, 돈은 벌지만 거기서 끝나야 하므로.

N = int(input())
T, P = [0] * (N+1), [0] * (N+1)
for n in range(1, N+1):
    T[n], P[n] = map(int, input().split())
money = 0

def iLuvMoney(x, now):
    if x <= N+1:
        global money
        money = max(money, now)
        if x == N + 1: return
        iLuvMoney(x + T[x], now + P[x])
        iLuvMoney(x + 1, now)
    else:
        return

iLuvMoney(1, 0)
print(money)