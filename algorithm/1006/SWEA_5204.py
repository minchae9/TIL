# 병합정렬, 오름차순
def merge(left, right):
    global cnt
    res = []
    i = j = 0
    if left[-1] > right[-1]:
        cnt += 1
    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
                # cnt += 1
        elif i < len(left):
            res.append(left[i])
            i += 1
        elif j < len(right):
            res.append(right[j])
            j += 1
    return res

def divide(n, s, e):
    if n == 1:
        return elements[s:e]
    else:
        left = divide(n//2, s, (s+e)//2)
        right = divide(n-n//2, (s+e)//2, e)
        return merge(left, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 정수의 개수
    elements = list(map(int, input().split()))
    cnt = 0
    ans = divide(N, 0, N)
    print(f'#{tc} {ans[N//2]}', end=' ')
    print(cnt)