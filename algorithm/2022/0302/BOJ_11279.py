import heapq
import sys

input = sys.stdin.readline
N = int(input())
q = []
for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(q, (-x, x))  # -x를 기준으로 순서가 매겨진다.
    elif x == 0:
        if q:
            e = heapq.heappop(q)[1] # -x 기준으로 가장 작은 것의 index 1에 있는 수, 즉 원래 수
            print(e)
        else:
            print(0)