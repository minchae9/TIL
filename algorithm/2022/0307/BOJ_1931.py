"""
시간초과
"""
import sys
input = sys.stdin.readline

N = int(input())
time_slot = [list(map(int, input().split())) for _ in range(N)]
# 끝나는 시간 큰 순서대로 정렬
time_slot = sorted(time_slot, key=lambda x: x[1], reverse=True)
idx = -1
cnt = 0
end = time_slot[0][1]
while True:
    start = -1
    for i in range(idx+1, N):
        if time_slot[i][1] <= end and time_slot[i][0] > start:
            mx_idx = i
            start = time_slot[i][0]
    if start < 0:
        break
    cnt += 1
    idx = mx_idx
    end = start
print(cnt)