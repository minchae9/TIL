
for t in range(1, 11):
    N = int(input())    # 정사각형 한 변의 길이
    table = [list(map(int, input().split())) for _ in range(100)]
    # # 90도 회전
    # table = [i for i in zip(*table)]

    cnt = 0 # 교착상태 개수
    for j in range(100):
        q = []
        for i in range(100):
            if table[i][j] == 1:
                if not q:
                    q.append(1)
            elif table[i][j] == 0:
                continue
            else:
                if q:
                    a = q.pop()
                    if a == 1:
                        cnt += 1


    print(f'#{t} {cnt}')