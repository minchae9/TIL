## 풀이중 ##
import sys

# def getroute(x, ttl):   # x: 계단 위치, ttl: 총합
#     global mx, myroute
#     if x > 0:
#         myroute[x] = 1
#     if x == N:
#         if ttl > mx:
#             mx = ttl
#         myroute[x] = 0
#         return
#     else:
#         if myroute[x-1] and myroute[x] and (x + 1 <= N):
#             getroute(x+1, ttl + stairs[x+1])
#         if x + 2 <= N:
#             getroute(x+2, ttl + stairs[x+2])
#         myroute[x] = 0
#         return

# 거꾸로 해당 계단에 대해 최대값인 경우를 한 경우 고르면 된다.
def getroute(n):
    if n < 2:
        return sum(stairs[0:n+1])
    else:
        one = stairs[n] + stairs[n-1] + getroute(n-3)
        two = stairs[n] + getroute(n-2)
        if one > two:
            myroute[n] = one
        else:
            myroute[n] = two


N = int(input())    # 계단의 개수
stairs = [0] * (N+1)    # 0은 시작점, 1~N+1 까지 N개의 계단 정보
for i in range(1, N+1):
    stairs[i] = int(input())
# 함수
# myroute = [0] * (N+1)
myroute = [0] * (N+2)
getroute(N)
print(myroute[N])

