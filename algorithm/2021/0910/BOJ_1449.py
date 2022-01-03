N, L = map(int, input().split())
place = list(map(int, input().split()))
sorted(place)
visited = [0] * 1001       # 테이프 범위 내에 속하는지 확인하기 위함
c = 0

for i in range(1, 1001):
    tape = i + L - 0.5
    if i in place and visited[i] == 0:  # 구멍이 난 부분이고 & 앞의 테이프로 막히지 않았다면:
        c += 1  # 테이프 하나 추가
        for j in place:
            if i-0.5 <= j <= tape:  # 테이프 하나 당 커버가 가능한 구멍에 대해 visited 표시
                visited[j] = 1

print(c)
