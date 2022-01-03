N = input()
nums = []
for i in range(len(N)):
    nums.append(int(N[i]))
nums.sort(reverse=True)
ans = ''
for j in nums:
    ans += str(j)
print(ans)