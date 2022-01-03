def func1(n):
    global ans
    if n == 0:
        for i in range(N):
            print(ans[i], end=' ')
        print()
        return
    else:
        for j in range(1, 7):
            ans.append(j)
            func1(n-1)
            ans.pop()

def func3(n):
    global ans
    if n == 0:
        for i in range(N):
            print(ans[i], end=' ')
        print()
        return
    else:
        for j in range(1, 7):
            if j not in ans:
                ans.append(j)
                func3(n-1)
                ans.pop()

def func2(i, n):
    global ans
    if n == 0:
        for i in range(N):
            print(ans[i], end=' ')
        print()
        return
    else:
        for j in range(i, 7):
            ans.append(j)
            func2(j, n-1)
            ans.pop()



N, M = map(int, input().split())
ans = []
if M == 1:
    func1(N)
elif M == 2:
    func2(1, N)
else:
    func3(N)