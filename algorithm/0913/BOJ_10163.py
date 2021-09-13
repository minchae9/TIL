"""
서브태스크가 포함된 문제로, 53점을 얻었다.
그런데 PyPy3로 돌리니 100점이 나온다.
무슨 이유일까?
"""

N = int(input())    # 색종이 개수
arr = [[0]*1001 for _ in range(1001)]
for k in range(1, N+1):
    x1, y1, w, h = map(int, input().split())
    for i in range(x1, x1+w):
        for j in range(y1, y1+h):
            arr[i][j] = k


for p in range(1, N+1):
    cnt = 0
    for r in range(1001):
        cnt += arr[r].count(p)
    print(cnt)