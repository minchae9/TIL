def solution(numbers, target):
    n = len(numbers)
    cnt = 0
    for i in range(1<<n):          # 부분집합 만들기 사용
        s = 0
        for j in range(n):
            if i & (1<<j):
                s += numbers[j]    # 해당 원소가 포함되는 경우라면 더하고,
            else:
                s -= numbers[j]    # 아니면 빼줌으로써 모든 더하고 뺀 경우의 합을 구함
        if s == target:            # 그렇게 구한 합이 타겟 넘버면 방법의 수 += 1
            cnt += 1
    return cnt