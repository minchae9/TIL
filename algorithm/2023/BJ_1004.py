# main idea: 출발점/도착점이 행성계(원)의 바깥에 있으면 피해갈 수 있다. 안에 있으면 1번 지나가게 된다.
# 조건 1): 각 행성계 끼리 겹치지 않음 -> 하나씩 개별로 살펴볼 수 있음.
# 조건 2): 행성계와 출발/도착 겹치지 않음 -> 계산식 부등호에 등호 없음.
# 공식: (x좌표 차이)^2 + (y좌표 차이)^2 가 r^2보다 크면 피해갈 수 있고, r^2보다 작으면 뚫고 가게 된다.
## 놓쳤던 점: 출발점과 도착점이 "모두" 행성계 안에 있으면 지나가지 않는다.
T = int(input())
for tc in range(T):
    x1, y1, x2, y2 = map(int, input().split())  # (x1, y1): 출발, (x2, y2): 도착
    n = int(input())    # n: 행성계 개수
    answer = [-1] * (n+1)
    for k in range(1, n+1):
        X, Y, r = map(int, input().split())   # (cx, cy): 행성계 중점, r: 반지름
        if ((x1 - X) ** 2 + (y1 - Y) ** 2) < r ** 2:
            answer[k] = answer[k] * (-1)
        if ((x2 - X) ** 2 + (y2 - Y) ** 2) < r ** 2:
            answer[k] = answer[k] * (-1)
    print(answer.count(1))