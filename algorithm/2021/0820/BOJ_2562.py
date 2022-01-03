mx = 0
idx = -1
for i in range(9):
    a = int(input())
    if a > mx:
        mx = a
        idx = i + 1
print(mx)
print(idx)