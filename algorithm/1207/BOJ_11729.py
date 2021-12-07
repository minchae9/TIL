def d(a, b, c, x):
    if x == 1:
        return [a, c]
    else:
        return d(a, c, b, x-1) + d(a, b, c, 1) + d(b, a, c, x-1)


N = int(input())

res = d(1, 2, 3, N)
print(len(res) // 2)
for i in range(0, len(res), 2):
    print(f'{res[i]} {res[i+1]}')

