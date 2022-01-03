N = int(input())    # 재료의 개수
ans = 1000000000
# 재료 리스트
ingredients = []
for _ in range(N):
    s, b = map(int, input().split())
    ingredients.append((s, b))

# 부분집합 만들기
for i in range(2**N):
    dish = []
    s, b = 1, 0
    for j in range(N):
        if i & (1<<j):
            dish.append(1)
        else:
            dish.append(0)
    for n in range(N):
        if dish[n]: # 넣는 재료
            s *= ingredients[n][0]
            b += ingredients[n][1]
    if s != 0 and b != 0 and abs(s-b) < ans:
        ans = abs(s-b)
print(ans)