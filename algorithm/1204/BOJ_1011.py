# 재귀로 풀었을 땐 RecursionError
# def findroute(s, d, t):
#     global times
#
#     if s == (y - 1 - x):    # 목표지점 1광년 전 도착
#         if t + 1 < times:
#             times = t + 1
#         return
#     elif s > (y - 1 - x):
#         return
#     else:
#         if d - 1 > 0:
#             findroute(s + (d-1), d-1, t+1)
#         if d > 0:
#             findroute(s + d, d, t + 1)
#         if d + 1 > 0:
#             findroute(s + (d+1), d+1, t+1)

"""
규칙성
거리(= y-x)에 따라 횟수가:
1
2
3 3
4 4
5 5 5
6 6 6
7 7 7 7
8 8 8 8
...
이런 식으로 증가함
"""

T = int(input())
for tc in range(T):
    x, y = map(int, input().split())    # x: 현재위치, y: 목표위치
    distance = y - x
    idx = 0
    for k in range(1, 2**31):
        if k % 2 == 0:  # 짝수
            idx += (k // 2)
        else:   # 홀수
            idx += ((k+1) // 2)
        if distance <= idx:
            print(k)
            break