import sys

input = sys.stdin.readline

n = int(input())
point = [a for a in range(1, n+1)]
check = [1] * n
ans = '+'

p = 0
flag = False
for _ in range(n):
    goal = int(input())
    while not flag:
        if point[p] == goal:
            ans += '-'
            check[p] = 0
            while check[p] == 0 and p > 0:
                p -= 1
            break
        elif point[p] < goal:
            if check[p+1] == 0:
                pass
            else:
                ans += '+'
            p += 1
        else:
            if check[p] == 0:
                p -= 1
            else:
                ans = 'NO'
                flag = True
                break

if ans == 'NO':
    print(ans)
else:
    for s in ans:
        print(s)