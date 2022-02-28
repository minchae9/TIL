import sys
input = sys.stdin.readline

def bfs(n, k):
    q = [n]
    while q:
        if check[k] > 0:
            return check[k]
        start = q.pop(0)
        num = [start-1, start+1, 2*start]
        for i in range(3):
            if (0 <= num[i] <= 100000) and (check[num[i]] == 0):
                q.append(num[i])
                check[num[i]] = check[start] + 1


N, K = map(int, input().split())
if N >= K:
    print(N-K)
else:
    check = [0] * 100001
    print(bfs(N, K))