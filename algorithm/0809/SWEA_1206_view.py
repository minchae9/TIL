for n in range(10):
    N = int(input())
    T = list(map(int, input().split()))
    total = 0
    for i in range(2, N-2):
        floor = T[i]
        for j in range(i-2, i+3):
            if i != j and T[i] - T[j] < floor:
                floor = T[i] - T[j]
        if floor > 0:
            total += floor
    print(total)