"""
부분집합의 합
"""
def f(i, N, K): # 합이 K인 부분집합을 출력 #i: 위치, N: 배열 크기, K: 구하고자 하는 합
    # global cnt1   # 몇 번 돌았는지 보기 위한 부분
    # cnt1 += 1
    if i==N: # 부분집합 생성완료
        s = 0
        for j in range(N):  # 완성된 부분집합 합 구하기
            if bit[j]==1:
                s += A[j]
        if s == K: # 합이 찾는 값이면
            print(bit, end= ' ')
            for j in range(N):
                if bit[j]==1:
                    print(A[j], end =' ')  # 부분 집합 출력
            print()
    else:   # 부분집합 생성 미완료
        bit[i] = 1  #넣거나
        f(i+1, N, K)
        bit[i] = 0  #말거나
        f(i+1, N, K)

def f2(i, N, K, S, RS): # S: 중간합, RS: 남은 원소들의 합
    # global cnt2
    # cnt2 += 1
    if S==K:    # 부분집합의 합이 구하고자 하는 값이면, 완료
        print(bit, end=' ')
        for j in range(N):
            if bit[j] == 1:
                print(A[j], end=' ')  # 부분 집합 출력
        print()
    elif i==N:  # 합이 K 값이 아닌데 이미 고려할 요소가 동남: 종료
        return
    elif S > K: # 이미 구할 K 값을 넘어버림: 종료
        return
    elif S+RS < K:  # 앞에서 요소를 너무 많이 배제해서, 뒤에 있는 요소를 모두 포함해도 K값이 나오지 않을 때
        return
    else:   # 계속 부분집합 만들어보기
        bit[i] = 1
        f2(i + 1, N, K, S+A[i], RS-A[i])
        bit[i] = 0
        f2(i + 1, N, K, S, RS-A[i]) # A[i] 포함하지 않아도 고려된 요소이니 RS에서 -A[i] 해줘야 함

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0]*10
cnt1 = 0
f(0, 10, 10)
print(cnt1)
cnt2 = 0
f2(0, 10, 25, 0, sum(A))
print(cnt2)