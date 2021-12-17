N, M = map(int, input().split())
res = []
def permutations(t, prev):
    if t == M:
        for item in res:
            print(item, end=' ')
        print()
        return
    else:
        for i in range(prev, N+1):
            res.append(i)
            permutations(t+1, i)
            res.pop()
permutations(0, 1)