"""
참고
https://hongcoding.tistory.com/22
"""
import sys
input = sys.stdin.readline

N = int(input())
time_slot = [list(map(int, input().split())) for _ in range(N)]
# 끝 시각 작은, 시작 시각 작은 순서대로 정렬
time_slot = sorted(time_slot, key=lambda x: (x[1], x[0]))

cnt = 1
end = time_slot[0][1]
for i in range(1, N):
    if time_slot[i][0] >= end:
        cnt += 1
        end = time_slot[i][1]
print(cnt)