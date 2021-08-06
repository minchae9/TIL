# 원래 코드 - 시간초과 발생
N = int(input())

s = 0
e = N
while True:
    mid = (s+e)//2
    if mid ** 2 == N:
        print(mid)
        break
    elif mid ** 2 < N:
        s = mid + 1
    else:
        e = mid + 1

# 블로그 글 참고 - 함수로 풀었길래 따라함(https://moongchi-is-here.tistory.com/24?category=911905)
N = int(input())

def findanswer(e):
    s = 0
    N = e
    while True:
        mid = (s+e)//2
        if mid ** 2 == N:
            return mid
        elif mid ** 2 < N:
            s = mid + 1
        else:
            e = mid - 1

print(findanswer(N))