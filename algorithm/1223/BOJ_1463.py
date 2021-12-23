def f(x, times):
    global mn
    if x == 1:
        if times < mn:
            mn = times
        return
    else:
        if times >= mn:
            return
        if x % 3 == 0:
            f(x//3, times+1)
        if x % 2 == 0:
            f(x//2, times+1)
        f(x-1, times+1)

N = int(input())
mn = 10**6
f(N, 0)
print(mn)