"""
참고자료
설명) https://m.blog.naver.com/occidere/220785383050
코드) https://velog.io/@wjdtmdgml/%EB%B0%B1%EC%A4%80RGB%EA%B1%B0%EB%A6%AC1149%EB%B2%88Python%ED%8C%8C%EC%9D%B4%EC%8D%ACDP
"""

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

# 각 자리를 이전 값까지 더한 최소 비용으로 갱신하기
for i in range(1, N):
    cost[i][0] += min(cost[i-1][1], cost[i-1][2])
    cost[i][1] += min(cost[i-1][0], cost[i-1][2])
    cost[i][2] += min(cost[i-1][0], cost[i-1][1])
print(min(cost[N-1]))