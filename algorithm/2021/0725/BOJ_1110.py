N = input()

if int(N) < 10:
    N = '0' + N

def getnew(n):
    total = 0
    for i in range(len(n)):
        total += int(n[i])
    new = str(n)[-1] + str(total)[-1]
    return new

times = 1
result = getnew(N)
while result != N:
    times += 1
    result = getnew(result)

print(times)

