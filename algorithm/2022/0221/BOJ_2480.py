a, b, c = map(int, input().split())
if a == b == c:
    ans = 10000 + (1000 * a)
elif a == b or b == c:
    ans = 1000 + (100 * b)
elif a == c:
    ans = 1000 + (100 * a)
else:
    ans = 100 * max(a, b, c)
print(ans)