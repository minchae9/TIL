"""
끝자리 개수로 구하기!
"""
N = int(input())
ls = [0] + [1] * 9
n = N
while n > 1:
    rec = [0] * 10
    for i in range(1, 9):
        rec[i] = ls[i-1] + ls[i+1]
    rec[0] = ls[1]
    rec[9] = ls[8]
    n -= 1
    ls = rec
print(sum(ls) % (10**9))