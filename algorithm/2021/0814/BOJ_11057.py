n = int(input())

if n == 1:                  # 1은 그냥 해줌
    print(10)
else:                       # [9, 8, 7, 6, ..., 2, 1]
    s = [1]*10              # [(9+8+7+...+2+1), (8+7+...), ...]
    e = []                  # 이런 식으로 진행이 되는 것 같아서 아래와 같이 코드를 짬 
    for _ in range(n-1):
        total = 0
        for i in range(10):
            total += sum(s)     # 전체 합 넣어주고
            e.append(sum(s))    # 새로운 리스트에도 넣어주고
            s.pop(0)            # 맨 처음 값 빼내기 -> 다음 합 구할 때는 첫 요소가 빠짐
        s, e = e, []
    print(total%10007)



# 재귀로 푸니까 RecursionError 발생
s = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
def asc(n, s):
    e = []
    total = 0
    if n == 1:
        return 10
    elif n == 2:
        for _ in range(10):
            total += sum(s)
            e.append(sum(s))
            s.pop(0)
        return e, total
    else:
        s = asc(n-1, s)[0]
        return asc(n-1, s)
print(asc(n, s)[1]%10007)
