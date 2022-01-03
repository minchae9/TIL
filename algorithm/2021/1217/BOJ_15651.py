N, M = map(int, input().split())
res = []
def permutations(t):
    if t == M:
        for item in res:
            print(item, end=' ')
        print()
        return
    else:
        for num in range(1, N+1):
            res.append(num)
            permutations(t+1)
            res.pop()
permutations(0)