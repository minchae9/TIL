for _ in range(10):
    tc, num = map(int, input().split())
    s = list(map(int, input().split()))
    arr1 = [0] * 100
    arr2 = [0] * 100
    for i in range(num):
        if arr1[s[2*i]] == 0:					# 목적지 저장
            arr1[s[2 * i]] = s[2 * i + 1]
        else:
            arr2[s[2 * i]] = s[2 * i + 1]

    visited = [0] * 100
    stack = []
    s = 0
    G = 99
    ans = 0

    while s < G:
        if arr1[s] == G or arr2[s] == G:	# 도착지(99)로 연결되면, ans=1이고 종료
            ans = 1
            break
        if (arr1[s] != 0 or arr2[s] != 0) and visited[s] != 3:
            if visited[s] != 1:					  # arr1 시도
                visited[s] += 1
                stack.append(s)
                s = arr1[s]
            elif visited[s] != 2:				 # arr2 시도
                visited[s] += 2
                stack.append(s)
                s = arr2[s]
        else:
            if stack:							  # 후진
                a = stack.pop()
                s = a
            else:
                break

    print(f'#{tc} {ans}')