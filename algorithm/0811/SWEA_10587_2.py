T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr)
    every = []
    for i in range(1<<n):
        lst = []
        for j in range(n+1):
            if i & (1<<j):
                lst.append(arr[j])
                every.append(lst)
    for subst in every:
        if sum(subst) == 0:
            print(f'#{t} 1')
            break
    else:
        print(f'#{t} 0')
