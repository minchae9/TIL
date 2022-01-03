def team(p, t, n):
    global one, two, mn
    if t == n:
        # 2팀 만들고
        for k in range(1, N+1):
            if k not in one:
                two.append(k)
        # 각 합 구하고
        sum_one = 0
        for i in range(n-1):
            for j in range(i+1, n):
                sum_one += (power[one[i]-1][one[j]-1] + power[one[j]-1][one[i]-1])
        sum_two = 0
        for a in range(n-1):
            for b in range(a+1, n):
                sum_two += (power[two[a]-1][two[b]-1] + power[two[b]-1][two[a]-1])
        # mn 갱신
        if abs(sum_one - sum_two) < mn:
            mn = abs(sum_one - sum_two)
        two = []
        return
    else:
        for i in range(p+1, N+1):
            one.append(i)
            team(i, t+1, n)
            one.pop()


N = int(input())    # 총 N명
power = [[]*N for _ in range(N)]
for n in range(N):
    power[n] = list(map(int, input().split()))
one = []
two = []
mn = 100
team(0, 0, N//2)
print(mn)