"""
heapq 모듈 (https://docs.python.org/ko/3/library/heapq.html#module-heapq)
(a.k.a. 우선순위 큐)
-----------------------------
힙: 모든 부모 노드가 자식보다 작거나 같은 값을 가지는 이진 트리
- heapq.heappop(heap): pop 메서드는 가장 작은 항목을 반환 (최소 힙)
- heapq.heappush(heap, item): 힙에 항목 추가 (힙의 특성 유지)
- heapq.heappushpop(heap, item): push하고, 가장 작은 항목을 pop
"""
import heapq
import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    num = int(input())
    if num > 0:
        heapq.heappush(lst, num)
    else:
        if lst:
            print(heapq.heappop(lst))
        else:
            print(0)