N = int(input())
lst = list(map(int, input().split()))
mn, mx = 1000000, -1000000
for num in lst:
    if num < mn:
        mn = num
    if num > mx:
        mx = num
print(mn, mx, sep=' ')