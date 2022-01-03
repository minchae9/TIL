A, B, V = map(int, input().split())

q = (V-A) // (A-B)
d = (V-A) / (A-B)
if d != q:
    q += 1
ans = q + 1
print(ans)

