# SWEA_5204

def mergesort(i, N):  # 병합구간의 시작 인덱스, 원소 수
    global cnt
    if N == 1:
        return i
    else:
        mergesort(i, N // 2)
        mergesort(i + N // 2, N - N // 2)
        idxL = i
        idxR = i + N // 2

        if arr[i + N // 2 - 1] > arr[i + N - 1]:
            cnt += 1
        tmp = [0] * N
        k = 0
        while k < N:
            if idxL < i + N // 2 and idxR < i + N:
                if arr[idxL] < arr[idxR]:
                    tmp[k] = arr[idxL]
                    idxL += 1
                else:
                    tmp[k] = arr[idxR]
                    idxR += 1
            elif idxL < i + N // 2:
                tmp[k] = arr[idxL]
                idxL += 1
            else:
                tmp[k] = arr[idxR]
                idxR += 1
            k += 1
        for k in range(N):
            arr[i + k] = tmp[k]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    mergesort(0, N)
    # print(arr)
    print(f'#{tc} {arr[N//2]} {cnt}')