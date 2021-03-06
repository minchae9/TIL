# 첫 시도: 조합의 개수 구하여 풀기 - 시간초과
"""
4
- 0: 1111 [1개] 1111
- 1: 0011, 1001, 1100 [3개] 211, 121, 112
- 2: 0000 [1개] 22
5
- 0: 11111 [1개] 11111
5C0 * 5C5
- 1: 00111, 10011, 11001, 11100 [4개] 2111, 1211, 1121, 1112
4C1 * 3C3 = 4
- 2: 00001, 00100, 10000 [3개] 221, 212, 122
3C2*1C1 = 3
6
- 0: 111111 [1개] 111111
6C0 * 6C6 = 1
- 1: 001111, 100111, 110011, 111001, 111100 [5개]21111
5C1 * 4C4 = 5
- 2: 000011, 001001, 001100, 100001, 100100, 110000 [6개]2211
4C2 * 2C2 = 6
- 3: 000000 [1개]222
3C3 = 1
"""
import sys
input = sys.stdin.readline
# 조합 개수 구하는 함수(num C k)
def f(k):
    p_m = k
    c_m = N-k
    parent = child = 1
    for n in range(k):
        parent *= p_m
        child *= c_m
        p_m -= 1
        c_m -= 1
    return child // parent

N = int(input())
mx = N // 2
ans = 1
for i in range(1, mx+1):
    ans += f(i)
print(ans % 15746)
