"""
앞에 있는 상자들 중 포함할 수 있는 상자의 최대 개수를 표시
(나보다 작은 상자들 중 최대 개수 +1)
"""
n = int(input())
boxes = list(map(int, input().split()))
res = [1] + [0] * (n-1)

i = 1
while i < n:
    mx = 0
    for k in range(i):
        if boxes[k] < boxes[i]:
            if res[k] > mx:
                mx = res[k]
        res[i] = mx + 1
    i += 1
print(max(res))