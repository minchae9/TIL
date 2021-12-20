N = int(input())
ppl = [0] * N
for n in range(N):
    age, name = input().split()
    ppl[n] = (int(age), name)
ppl.sort(key=lambda x: x[0])
for i in range(N):
    print(ppl[i][0], end=' ')
    print(ppl[i][1])