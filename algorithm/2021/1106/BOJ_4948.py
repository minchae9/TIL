"""
에라토스테네스의 체를 응용함
"""
def prime(N):
    global numbers
    for x in range(2, 2 * N + 1):
        if numbers[x]:
            for k in range(2 * x, 2 * N + 1, x):
                numbers[k] = 0

while True:
    N = int(input())
    if N == 0:
        break

    numbers = [0, 0] + [1 for _ in range(2*N-1)]
    prime(N)
    print(sum(numbers[(N+1):]))