# 재귀: 여전히 시간초과
import sys

# 거꾸로 해당 계단에 대해 최대값인 경우를 한 경우 고르면 된다.
def getroute(n):
    if n <= 2:
        return sum(stairs[0:n+1])
    else:
        one = stairs[n] + stairs[n-1] + getroute(n-3)
        two = stairs[n] + getroute(n-2)
        return max(one, two)


N = int(sys.stdin.readline())    # 계단의 개수
stairs = [0] * (N+1)    # 0은 시작점, 1~N+1 까지 N개의 계단 정보
for i in range(1, N+1):
    stairs[i] = int(sys.stdin.readline())

ans = getroute(N)
print(ans)
