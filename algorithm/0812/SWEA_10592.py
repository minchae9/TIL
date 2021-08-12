T = int(input())
for tc in range(T):
    N = int(input())
    number = list(map(int, input().split()))

    # 선택정렬(오름차순)
    for i in range(N-1):
        mn = i
        for k in range(i+1, N):
            if number[k] < number[mn]:
                mn = k
        number[i], number[mn] = number[mn], number[i]
    
    # 앞에서부터 10개 숫자만 지시대로 정렬
    arr = [0] * 10
    for n in range(-1, -6, -1):
        arr[(-2)*n -2] = number[n]
    for p in range(5):
        arr[2*p + 1] = number[p]
    print(f'#{tc+1}', end=' ')
    for num in arr:
        print(num, end=' ')
    print()