import sys

N = int(sys.stdin.readline())

times = list(map(int, sys.stdin.readline().split()))
times = sorted(times, reverse=True)

total = 0
i = 0
while i < N:
    total += times[i] * (i+1)
    i += 1

print(total)