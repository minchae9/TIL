T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())    # N: 화덕 크기, M: 피자 개수
    C = [0] + list(map(int, input().split())) # 피자에 있는 치즈 양
    add = M-N
    idx = [0] * (N+1)
    Q = [0]
    cnt = 0
    for k in range(1, N+1):
        Q.append(C[k])          # 화덕에 피자
        idx[k] = k              # 피자 번호
    while cnt < N-1:            # 피자 하나 남을 때까지
        for i in range(1, N+1):
            if cnt == N-1:
                break
            Q[i] //= 2
            if Q[i] == 0 and idx[i]!=0:
                if add:
                    Q[i] = C[M-add+1]
                    idx[i] = M - add + 1
                    add -= 1
                else:
                    idx[i] = 0
                    cnt += 1


    for c in idx:
        if c:
            print(f'#{t} {c}')