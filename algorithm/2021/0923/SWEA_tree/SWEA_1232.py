def postorder(x):
    if x <= N:
        if type(arr[x]) is int:
            return arr[x]
        else:
            e1 = postorder(left_c[x])
            e2 = postorder(right_c[x])
            arr[x] = calculate(e1, e2, arr[x])
            return arr[x]

def calculate(a1, a2, y):
    if y == '+':
        return a1 + a2
    elif y == '-':
        return a1 - a2
    elif y == '*':
        return a1 * a2
    else:   # y == '/'
        return a1 // a2

for t in range(1, 11):
    N = int(input())    # N: 노드 개수
    arr = [0] * (N+1)
    left_c = [0] * (N+1)
    right_c = [0] * (N+1)
    for _ in range(N):
        info = input().split()
        try:    # 정수 노드
           arr[int(info[0])] = int(info[1])
        except: # 연산자 노드
            arr[int(info[0])] = info[1]
            left_c[int(info[0])] = int(info[2])
            right_c[int(info[0])] = int(info[3])
    ans = postorder(1)
    print(f'#{t} {ans}')