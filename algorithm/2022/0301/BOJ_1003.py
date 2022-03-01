T = int(input())
zeros, ones = [1, 0] + [-1] * 39, [0, 1] + [-1] * 39
for t in range(T):
    N = int(input())
    for i in range(2, N+1):
        if zeros[i] == -1:
            zeros[i] = zeros[i-1] + zeros[i-2]
            ones[i] = ones[i-1] + ones[i-2]
    print(f'{zeros[N]} {ones[N]}')