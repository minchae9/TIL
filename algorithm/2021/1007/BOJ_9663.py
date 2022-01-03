"""
PyPy3로 제출함 (Python3 는 시간초과...)
"""

def queens(t):
    global cnt
    if t == N:
        cnt += 1
        return
    else:
        for j in range(N):
            if y[j] == 0 and t+j not in plus and t-j not in minus:
                y[j] = 1
                plus[j] = t+j
                minus[j] = t-j
                queens(t+1)
                y[j] = 0
                plus[j] = 100
                minus[j] = 100
        else:
            return
import sys
N = int(sys.stdin.readline())
y = [0] * N
plus = [100] * N
minus = [100] * N
cnt = 0
queens(0)
print(cnt)