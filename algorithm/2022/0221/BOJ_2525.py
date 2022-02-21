hour, minute = map(int, input().split())
duration = int(input())
minute += duration
if minute >= 60:
    add = minute // 60
    hour += add
    minute -= (60 * add)
if hour >= 24:
    hour -= 24
print(hour, end=' ')
print(minute)