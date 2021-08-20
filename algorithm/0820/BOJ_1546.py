N = int(input())
sc = list(map(int, input().split()))
M = max(sc)
new_sc = [0]*N
for i in range(N):
    new_sc[i] = sc[i]/M*100
avg = sum(new_sc)/len(new_sc)
print(avg)