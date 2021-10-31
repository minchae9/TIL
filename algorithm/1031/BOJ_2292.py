N = int(input())

interval = 0
for j in range(1000000000):
    interval += j
    if N <= 6*interval + 1:
        print(j+1)
        break