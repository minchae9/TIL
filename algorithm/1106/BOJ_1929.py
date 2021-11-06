"""
https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4
https://wikidocs.net/21638
참고함
"""

M, N = map(int, input().split())
numbers = [0, 0] + [i for i in range(2, N+1)]

for n in range(2, N+1):
    if numbers[n]:
        for k in range(2*n, N+1, n):    # step을 n으로 두는 것이 포인트!
            numbers[k] = 0

for el in numbers:
    if el >= M:
        print(el)