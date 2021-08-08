import sys
N, M = map(int, sys.stdin.readline().split())
times = []
for i in range(N):
    times.extend(list(map(int, sys.stdin.readline().split('/n'))))

s = 1
e = max(times)*M
while s <= e:
    num = (s+e)//2
    total = 0
    for time in list(times):
        total += num // time
    if total >= M:
        result = num
        e = num-1
    else:
        s = num+1
print(result)