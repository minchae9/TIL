"""
참고: https://myjamong.tistory.com/313
그림으로 나타내 보았다:
(i-3)   (i-2)   (i-1)   (i)
[?]     [X]     [O]     [O]     --- i와 i-1번째가 O라면, i-2는 X, i-3 이전은 모름
        [?]     [X]     [O]     --- i가 O이고 i-1이 X라면, i-2 이전은 모름
                [?]     [X]     --- i가 X라면, i-1 이전은 모름
"""

n = int(input())
wines = []
for _ in range(n):
    wines.append(int(input()))
wines += [0] * 3    # wines[:3] 있으므로
rec = [0] * (n+2)   # index 까지의 최대값 저장할 배열, 인덱스-3까지 가므로
rec[0] = wines[0]
rec[1] = rec[0] + wines[1]
rec[2] = sum(wines[:3]) - min(wines[:3])
for i in range(3, n):
    rec[i] = max(rec[i-3] + wines[i-1] + wines[i], rec[i-2] + wines[i], rec[i-1])
print(rec[n-1])