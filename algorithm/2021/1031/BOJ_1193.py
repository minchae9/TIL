X = int(input())

start = 1
for j in range(1, 10000000):
    if X >= start and X < start+j:
        if j % 2:   # 오른쪽으로 커짐
            print(f'{j-(X-start)}/{1 + X - start}')
        else:   # 왼쪽으로 커짐
            print(f'{1+X-start}/{j-(X-start)}')
        break
    start += j