T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N 컨테이너 수, M 트럭 수
    cargo = sorted(list(map(int, input().split())), reverse=True) # 화물 무게
    truck = sorted(list(map(int, input().split())), reverse=True) # 적재 용량
    total = 0
    i = 0
    moved = [0] * len(cargo)
    while i < len(truck):
        for j in range(len(cargo)):
            if moved[j] == 0 and truck[i] >= cargo[j]:
                moved[j] = 1
                total += cargo[j]
                break
        i += 1
    print(f'#{tc} {total}')
