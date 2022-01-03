N, M = map(int, input().split())    # N: 세로, M: 가로
inp = list(input() for _ in range(N))
mn = 64
black = []
white = []
for i in range(8):
    if i % 2:
        black.append('WBWBWBWB')
        white.append('BWBWBWBW')
    else:
        black.append('BWBWBWBW')
        white.append('WBWBWBWB')

for n in range(N-8+1):
    for m in range(M-8+1):
        black_cnt = 0
        white_cnt = 0
        for lv in range(8):
            for cell in range(8):
                if inp[n+lv][m+cell] != black[lv][cell]:
                    black_cnt += 1
                if inp[n+lv][m+cell] != white[lv][cell]:
                    white_cnt += 1
        if min(black_cnt, white_cnt) < mn:
            mn = min(black_cnt, white_cnt)

print(mn)