C = int(input())
for _ in range(C):
    arr = list(map(int, input().split()))
    N = arr[0]
    cnt = 0
    s = 0
    for i in range(1, N+1):
        s += arr[i]
    avg = s / N
    for j in range(1, N+1):
        if arr[j] > avg:
            cnt += 1
    print('{0:.3f}%'.format(round(cnt/N*100, 3)))
# 소수점 세 자리까지 남기기 위한 작성법 알아두기!
# 그냥 round() 함수를 사용하면, 소수점 아래가 0일 때 한 번만 나옴
