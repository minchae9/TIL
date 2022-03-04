# 질문해둠

import sys

input = sys.stdin.readline

n = int(input())
point = [a for a in range(1, n+1)]
check = [1] * n
ans = '+'

p = 0
for _ in range(n):
    goal = int(input())
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