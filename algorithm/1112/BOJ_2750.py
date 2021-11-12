N = int(input())
lst = []
for _ in range(N):
    num = int(input())
    for i in range(len(lst)):
        if num < lst[i]:
            lst.insert(i, num)
            break
    else:
        lst.append(num)
for k in range(N):
    print(lst[k])