for t in range(10):
    dump = int(input())
    box = list(map(int, input().split()))
    for i in range(99, 0, -1):                    # 버블 정렬
        for j in range(i):
            if box[j] > box[j + 1]:
                box[j], box[j + 1] = box[j + 1], box[j]

    for d in range(dump):
        box[0] += 1                               # 더하기 1, 빼기 1 해주고
        box[-1] -= 1
        for i in range(100):                      # 다시 정렬해줌
            if box[i] > box[i+1]:
                box[i], box[i+1] = box[i+1], box[i]
            else:
                break
        for i in range(-1, -101, -1):
            if box[i-1] > box[i]:
                box[i], box[i-1] = box[i-1], box[i]
            else:
                break

        if box[-1] - box[0] <= 1:
            break
    print('#{} {}'.format(t+1, box[-1] - box[0]))