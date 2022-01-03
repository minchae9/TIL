x, y, w, h = map(int, input().split())
# 현위치 (x, y), w 가로 길이, h 세로 길이
print(min((h-y), y, x, (w-x)))