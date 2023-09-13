stat = list(map(int, input().split()))
original = [1, 1, 2, 2, 2, 8]
for i in range(6):
    print(original[i] - stat[i], end=' ')