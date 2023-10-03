import math

N = int(input())    #굴다리 길이: N
M = int(input())    #가로등의 개수: M
X = list(map(int, input().split())) #가로등 설치위치 list
h = max(X[0], N - X[-1])
for i in range(1, M):
    h = max(h, math.ceil((X[i] - X[i-1]) / 2))
print(h)