"""
dp 문제인데 백트래킹으로 풀어서 그런지 '시간초과.'
"""
import sys
input = sys.stdin.readline

def func(x, ttl, c):
    global mn
    if c == N:
        if ttl < mn:
            mn = ttl
        return
    if ttl >= mn:
        return
    for i in range(3):
        if i != x:
            func(i, ttl+cost[c][i], c+1)

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
mn = 1000 * N
func(N+1, 0, 0)
print(mn)