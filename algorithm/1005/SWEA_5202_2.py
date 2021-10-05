"""
다른 사람 코드 보고 시도한 또 다른 풀이:
시간을 마지막에서부터 출발하여, 시작시간이 가장 늦은 작업을 하나씩 해나감
"""

def maxitruck(cnt):
    global mx
    la = 24
    while True:
        voi = -1
        for j in range(N):
            if E[j] <= la and S[j] >= voi:
                voi = S[j]
        la = voi
        if voi == -1:
            break
        cnt += 1
    return cnt


T = int(input())
for t in range(1, T+1):
    N = int(input())    # 신청서
    S = [0] * N
    E = [0] * N
    for k in range(N):
        s, e = map(int, input().split())
        S[k] = s
        E[k] = e

    mx = maxitruck(0)
    print(f'#{t} {mx}')