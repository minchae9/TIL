def bfs(x, y):
    q = []
    q.append((x, y))
    visited = [0] * (n+1)   # 편의점 n개 + 집 1개 방문 표시
    while q:
        x_t, y_t = q.pop(0)
        if (x_t, y_t) == (x_fest, y_fest):  # 페스티벌에 다다르면, happy
            return 'happy'
        for j in range(n+1):
            if visited[j] == 0:
                x_dist = abs(x_t - places[j][0])
                y_dist = abs(y_t - places[j][1])
                if x_dist + y_dist <= 1000:
                    q.append((places[j][0], places[j][1]))
                    visited[j] = 1
    else:
        return 'sad'


T = int(input())
for t in range(T):
    g = 32768
    n = int(input())    # n: 편의점 개수
    x_home, y_home = map(int, input().split())  # 집 좌표
    stores = [[0, 0] for _ in range(n)] # 가게 좌표 리스트
    for i in range(n):
        stores[i][0], stores[i][1] = map(int, input().split())
    x_fest, y_fest = map(int, input().split())  # 페스티벌 좌표
    places = stores + [[x_fest, y_fest]]    # 집에서 들를 수 있는 곳: 편의점 & 페스티벌
    ans = bfs(x_home, y_home)
    print(ans)