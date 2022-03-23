T = int(input())
for tc in range(1, T+1):
    record = input()
    cnt = 0
    for i in range(len(record)):
        if record[i] == 'o':
            cnt += 1
    if cnt + (15 - len(record)) >= 8:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')