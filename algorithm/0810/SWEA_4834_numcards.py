T = int(input())
for t in range(T):
    N = int(input())
    cards = list(map(int, input()))
    count = [0]*10
    big = 0								# 모두 같은 개수면 최대 숫자 출력하도록, 초기값에 최대값 넣어줌
    for num in cards:
        count[num] += 1
        if num > big:
            big = num

    answer = big
    max_num = count[answer]
    for n in range(N):
        if count[cards[n]] > max_num:	# 개수가 초기값보다 크면 경신하도록
            answer = cards[n]
            max_num = count[answer]
    print(f'#{t+1} {answer} {max_num}')