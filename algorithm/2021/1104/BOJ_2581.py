M = int(input())
N = int(input())
ls = []
for num in range(M, N+1):
    if num == 1:
        continue
    elif num == 2:
        ls.append(num)
    else:
        for k in range(2, num//2 + 1):
            if num % k == 0:
                break
        else:
            ls.append(num)
if len(ls):
    print(sum(ls))
    print(ls[0])
else:
    print(-1)