"""
잘 안 됨.
파이썬으로 돌리니 시간 초과가 떴고,
pypy로 돌리니 틀렸다고 떠서, 뭐 결국 틀림.
뒤에서부터 작은 상자를 경신하면서 구하려 했었따.

다음 사이트를 참고하여 공부했다:
https://pacific-ocean.tistory.com/212
"""

import sys

def box(i, j, N):
    cnt = 1
    while j >= 0:
        if boxes[i] > boxes[j]:
            i = j
            cnt += 1
        j -= 1
    return cnt


n = int(sys.stdin.readline())    # 상자의 개수
boxes = list(map(int, sys.stdin.readline().split()))
mx = 0

for i in range(n-1, 0, -1):
    for j in range(i-1, -1, -1):
        res = box(i, j, n)
        if res > mx:
            mx = res

print(mx)

