N = int(input())
i = 2
res = []
while N > 1:
    if N % i == 0:
        res.append(i)
        N //= i
    else:
        i += 1
for el in res:
    print(el)