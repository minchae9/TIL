# 반복으로 푼 방법
def pascal(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        global lst                  # 2부터 돌면서 대입되는 lst 값을 갱신하도록 만듦
        nlst = []
        for i in range(n-1):
            a = lst[i] + lst[i+1]
            nlst.append(a)
        lst = [1] + nlst + [1]
        return lst

lst = [1, 1]
T = int(input())
for t in range(1, T+1):
    N = int(input())

    print(f'#{t}')                  # 하나씩 띄어쓰기 하여 출력
    for i in range(N):
        for j in pascal(i):
            print(j, end=' ')
        print()
