import sys

input = sys.stdin.readline

n = int(input())
to = []
point = [a for a in range(1, n+1)]
check = [1] * n
ans = '+'
for _ in range(n):
    to.append(int(input()))
p = 0
for t in range(n):
    goal = to[t]
    while True:
        if point[p] == goal:
            ans += '-'
            check[p] = 0
            while check[p] == 0 and p >= 0:
                p -= 1
            break
        elif point[p] < goal:
            if check[p+1] == 0:
                pass
            else:
                ans += '+'
            p += 1

for s in ans:
    print(s)