def dee(n):
    summ = 0
    for i in range(len(str(n))):
        summ += int(str(n)[i])
    return n + summ

notself = []
for n in range(1, 10001):
    if dee(n) <= 10000:
        notself.append(dee(n))

for num in range(1, 10001):
    if num not in notself:
        print(num)