"""
1
1 1
(1+1)2 (0+2)2
(1+2)3 (1+3)4 (1+4)5
(2+5)7 (2+7)9
(3+9)12
(4+12)16
(5+16)21
(7+21)28
(9+28)37
(12+37)49
(16+49)65
n번째 = n-1번째 + n-5번째 (n이 6이상일 때)
n: 1~5는 1 1 1 2 2
"""
def P(n):
    num = [0, 1, 1, 1, 2, 2] + [0] * n
    if n >= 6:
        for i in range(6, n+1):
            num[i] = num[i-1] + num[i-5]
    return num[n]

T = int(input())
for tc in range(T):
    N = int(input())
    print(P(N))