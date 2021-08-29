T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    arr = num + [0]*M
    front = 0
    rear = N-1
    for i in range(M):
        rear += 1                   # 저장할 위치
        arr[rear] += arr[front]     # 맨 앞 요소 저장
        front += 1                  # 첫 요소 위치 변경
    print(f'#{t} {arr[front]}')