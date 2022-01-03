# 재귀함수로 푼 방법
# 실행시간이 어마무시하다
def pascal(n):
    lst = []
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        for i in range(n - 1):
            a = pascal(n - 1)[i] + pascal(n - 1)[i + 1]
            lst.append(a)
        return [1] + lst + [1]


T = int(input())
for t in range(1, T + 1):
    N = int(input())

    print(f'#{t}')
    for i in range(N):
        for j in range(i + 1):
            print(pascal(i)[j], end=' ')
        print()