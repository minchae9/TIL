N = int(input())
m = N // 5
for k in range(m, -1, -1):
    if (N - (5 * k)) % 3 == 0:
        ans = k + (N - (5 * k))//3
        print(ans)
        break
else:
    print(-1)