def tournament(i, j):
    if i == j:
        return i
    else:
        r1 = tournament(i, (i+j)//2)    # 그룹1
        r2 = tournament((i+j)//2+1, j)  # 그룹2
        if card[r1] == card[r2]:        # 가위바위보로 승자 정하기
            if r1 < r2:
                return r1
            else:
                return r2
        elif (card[r1], card[r2]) in [(1, 3), (2, 1), (3, 2)]:
            return r1
        else:
            return r2

T = int(input())
for t in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    print(f'#{t} {tournament(0, N-1) + 1}') # 인덱스로 접근했으므로 +1