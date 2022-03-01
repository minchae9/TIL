# 참고: https://littlefoxdiary.tistory.com/3
# PyPy3 채점하여 통과 (Python3은 시간초과)
## 더 나은 풀이: http://melonicedlatte.com/2021/04/14/010700.html
import heapq
import sys
input = sys.stdin.readline

N = int(input())
q = []
abs_list = []
for _ in range(N):
    x = int(input())
    if x != 0:
        q.append(x)
        heapq.heappush(abs_list, abs(x))
    else:
        if not q:
            print(0)
        else:
            sml = heapq.heappop(abs_list)
            if -sml in q:
                print(-sml)
                q.remove(-sml)
            elif sml in q:
                print(sml)
                q.remove(sml)