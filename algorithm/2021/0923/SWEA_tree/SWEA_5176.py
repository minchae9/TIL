def inorder(x): # 중위순회
    global k
    if x <= N:
        inorder(2*x)
        arr[x] = k
        inorder(2*x+1)
    else:
        k += 1


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [0] * (N+1)
    # 배열에 저장
    k = 0
    inorder(1)
    print(f'#{t} {arr[1]} {arr[N//2]}')