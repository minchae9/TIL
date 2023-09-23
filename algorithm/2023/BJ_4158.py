import sys

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N + M == 0:
        break
    together = set()
    for i in range(N+M):
        together.add(sys.stdin.readline())
    print(N + M - len(together))

# set에서는 중복값이면 한 번만 보유하므로 이를 이용.
# 전체 개수 = 중복 개수 + 유일 개수