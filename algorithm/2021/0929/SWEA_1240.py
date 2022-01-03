def decipher(arr):
    w = [0] * 8     # 숫자 저장할 리스트
    total = 0
    for i in range(8):
        c = arr[7*i:7*(i+1)]
        n = nums.index(c)
        w[i] = n
        if i % 2:   # 인덱스가 홀수
            total += n
        else:   # 짝수
            total += 3*n
    if total % 10 == 0:
        return [1, sum(w)]
    else:
        return [0, 0]



T = int(input())
for C in range(1, T+1):
    N, M = map(int, input().split())    # 세로 N, 가로 M
    r = 0
    nums = ('0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011')
    while r < N:
        codes = input()
        if '1' in codes:   # 암호코드 발견
            code = codes
        r += 1
    k = 1
    while True:
        if code[-k] == '1':
            break
        k += 1
    code = code[-k-55:-k+1] # 실제 코드
    ans = decipher(code)
    print(f'#{C} {ans[1]}')

