"""
새로운 탑을 쌓을 때 주사위 숫자와 같은 자리에 쌓아야 한다고 생각해서 헤매다가
오름차순으로 정렬을 해뒀으니 그럴 필요가 없다는 걸 깨달았다.
고민하다, 다음 블로그 글을 참고하여 풀었다:
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=jh05013&logNo=221470941917
"""


N = int(input())
dices = list(map(int, input().split()))
dices.sort()

q = []
q.extend(dices)
cnt = 0
while q:
    k = 0
    cnt += 1    # 탑 개수
    times = len(q)
    for i in range(times):
        t = q.pop(0)    # 작은 것부터
        if t >= k:
            k += 1      # 배열의 인덱스보다 같거나 크면 배열 가능
        else:
            q.append(t) # 작으면, 다른 탑에 쌓도록 q에 다시 넣기

print(cnt)