## 첫 번째 시도 (틀림)
"""
import sys

N, a, b = map(int, sys.stdin.readline().split())
a, b, loop = min(a, b), max(a, b), 0

while N > 0:
    loop += 1
    N -= 1
    if N >= b:
        N -= b
    elif N >= a:
        N -= a
print(loop)
"""
# 반례: 100 50 49 -> output: 50, answer: 2
# bfs로 풀어보자

## 두 번째 시도 (bfs, 틀림?)
# 기다리기, a, b의 3가지 옵션을 하나씩 가보면서 맨 첫번째에 오면 횟수 출력
"""
import sys

N, a, b = map(int, sys.stdin.readline().split())
p = [N]
loop = 0
flag = False
while True:
    if flag:
        break
    p, q = [-1] * len(p) * 2, p
    loop += 1
    for i in range(len(q)):
        k = q[i]
        if k - a - 1 >= 0:
            p[2*i] = k-a-1
        if k - b - 1 >= 0:
            p[2*i + 1] = k-b-1
        if 0 in p:
            flag = True
            break
print(loop)
"""
# 위 반례에 대한 답은 나오지만 '시간 초과'
# 구글링 해보니 dfs 로 풀어야 한다고 함

## 세 번째 시도 (dfs) (성공!)
# 참고: https://cochin-man.tistory.com/50
# 기다리기만 해서 갈 때를 초기 dp로 설정,
# 기다리기, a만큼 새치기, b만큼 새치기 하는 경우에 닿는 곳에 걸린 시간(초)을 갱신
import sys

N, a, b = map(int, sys.stdin.readline().split())
dp = [i for i in range(N+1)]
for k in range(N+1):
    if k + 1 <= N:
        dp[k+1] = min(dp[k+1], dp[k] + 1)
    if k + a + 1 <= N:
        dp[k+a+1] = min(dp[k+a+1], dp[k] + 1)
    if k + b + 1 <= N:
        dp[k+b+1] = min(dp[k+b+1], dp[k] + 1)
print(dp[N])
