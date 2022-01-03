"""
런타임 에러(RecursionError)
"""

def dfs(k, s, times):
    global travel
    if s == distance:
        if times < travel:
            travel = times
        return
    else:
        if s > distance or times >= travel:
            return
        if k-1 > 0:
            dfs(k-1, s+(k-1), times+1)
        if k > 0:
            dfs(k, s+k, times+1)
        if k + 1 > 0:
            dfs(k+1, s+(k+1), times+1)

T = int(input())
for t in range(T):
    x, y = map(int, input().split())
    travel = 2 ** 31
    distance = y - x - 1
    dfs(0, 0, 0)
    print(travel+1)