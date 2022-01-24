"""
참고: https://sihyungyou.github.io/baekjoon-1912/
DP 문제는 어려워 ㅜㅜ
"""
n = int(input())
ls = list(map(int, input().split()))
mx = -1000
res = 0
for i in range(n):
    if res >= 0:
        res += ls[i]
    else:
        res = ls[i]
    if res > mx:
        mx = res
print(mx)