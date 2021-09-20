"""
메모리 초과로 문제가 풀리지 않았다.
찾아보니 대부분 pypy3로 돌려 메모리 초과 문제를 극복하고 있었다.
처음에는 외부 모듈을 사용하지 않고 했는데, 도저히 안 돼서 블로그 글을 찾아보며
내 코드 일부분을 수정했다.
전체적인 골격(bfs, for문 등)은 거의 같았다.
다만, 그래프를 만드는 과정에서 전체 그래프를 만들지 않고
간선이 있는 노드만 적도록 arr를 설계한 점이 메모리에 가장 영향이 크고
가장 달라진 부분일 것이다.
기존 부분을 주석으로 남겨놓는다!
"""
import sys
from collections import deque

def depth(x):
    q = deque() # q = []
    visited = [0] * (N+1)
    q.append(x)
    visited[x] = 1
    while q:
        t = q.popleft() # t = q.pop(0)
        for d in arr[t]:
            if visited[d] == 0:
                q.append(d)
                visited[d] = 1
    return sum(visited)


N, M = map(int, sys.stdin.readline().split())
# arr = [[0]*(N+1) for _ in range(N+1)]
arr = [[] for _ in range(N+1)]
for i in range(M):
    e, s = map(int, sys.stdin.readline().split())
    arr[s].append(e)
    # 기존 arr에서는 arr[s][e] = 1

ans = []
mx = 0

for j in range(1, N+1):
    if arr[j]:
        res = depth(j)
        if res > mx:
            mx = res
            ans = []
            ans.append(j)
        elif res == mx:
            ans.append(j)

# for n in range(len(ans)):
#     print(ans[n], end=' ')
print(*ans)