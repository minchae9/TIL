N = int(input())
nums = list(map(int, input().split()))
ans = 0
for i in range(N):
    num = nums[i]
    if num == 1:
        continue
    elif num == 2:
        ans += 1
    else:
        for t in range(2, num//2 + 1):
            if num % t == 0:
                break
        else:
            ans += 1
print(ans)