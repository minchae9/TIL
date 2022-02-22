N, K = map(int, input().split())
coins = [0] * N
ans = 0
for i in range(N):
    coins[i] = int(input())
for j in range(N-1, -1, -1):
    if coins[j] <= K:
        ans += (K // coins[j])
        K = (K % coins[j])
    if K == 0:
        break
print(ans)