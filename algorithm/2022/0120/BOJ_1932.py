"""
(0)
(0), (1)
(0, 1), (1, 2)
(0, 1), (1, 2), (2, 3)
(0, 1), (1, 2), (2, 3), (3, 4)
0 -> 0, 1
1 -> 1, 2
...
x -> x, x+1
"""
n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    for k in range(i+1):
        if k == 0:
            tri[i][k] += tri[i-1][k]
        elif k == i:
            tri[i][k] += tri[i-1][k-1]
        else:
            tri[i][k] += max(tri[i-1][k-1], tri[i-1][k])
print(max(tri[n-1]))