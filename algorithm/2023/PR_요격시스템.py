def solution(targets):
    # x좌표 오름차순으로 정렬: 요격을 x좌표에서 하므로
    targets.sort()
    # 기본 1발, 좌표 변경해야 하는 횟수를 더해줄 것
    ans = 1
    s, e = targets[0][0], targets[0][1]
    for i in range(1, len(targets)):
        if targets[i][0] >= e:
            ans += 1
            s, e = targets[i][0], targets[i][1]
        else:
            if targets[i][0] > s:
                s = targets[i][0]
            if targets[i][1] < e:
                e = targets[i][1]
    return ans
# 기존 미사일을 (s, e), 다음 미사일을 (x, y) 라고 했을 때,
# s <= x < e 라면 기존 요격으로도 미사일 제거가 가능하며,
# (오름차순 정렬이므로 x >= s 이고) x >= e 일 때 요격 좌표를 달리 해야 한다.