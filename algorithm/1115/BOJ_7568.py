N = int(input())    # N 전체 사람 수

ppl = []
for i in range(N):
    ix, iy = map(int, input().split())
    ppl.append([ix, iy])

res = []
k = 0
while k < N:
    cnt = 1
    x, y = ppl[k][0], ppl[k][1]
    for p in range(N):
        if p != k:
            if x < ppl[p][0] and y < ppl[p][1]:
                cnt += 1
    res.append(cnt)
    k += 1

for r in range(N):
    print(res[r])