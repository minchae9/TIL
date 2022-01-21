"""
메모리 초과
"""
N = int(input())
ls = [str(x) for x in range(1, 10)]
n = N
while n > 1:
    rec = []
    for num_str in ls:
        c = int(num_str[-1])
        if 0 <= c - 1 < 10:
            rec.append(num_str + str(c-1))
        if 0 <= c + 1 < 10:
            rec.append(num_str + str(c+1))
    ls = rec
    n -= 1
print(len(ls) % (10**9))