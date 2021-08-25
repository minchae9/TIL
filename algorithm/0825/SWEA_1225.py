for _ in range(10):
    tc = int(input())
    numbers = list(map(int, input().split()))
    flag = False
    num = 1
    while True:
        if num <= 0:
            break
        for i in range(1, 6):
            num = numbers.pop(0)    # 맨 앞 숫자
            num -= i
            numbers.append(num)
            if numbers[-1] <= 0:    # 계산 결과가 0 이하면, 0으로 만들고, 종료
                numbers[-1] = 0
                break
    print(f'#{tc}', end=' ')
    for j in range(8):
        print(numbers[j], end=' ')