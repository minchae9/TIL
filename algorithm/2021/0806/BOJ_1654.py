import sys
K, N = list(map(int, sys.stdin.readline().split()))
lines = [int(sys.stdin.readline().strip()) for i in range(K)]

def getme(mid):
    total = 0
    for line in lines:
        total += (line // mid)
    return total

s = 1
e = max(lines)
while s<=e:
    total = 0
    mid = (s+e) // 2
    if getme(mid) >= N:
        if getme(mid+1) >= N:
            s = mid+1
        else:
            print(mid)
            break
    else:
        e = mid