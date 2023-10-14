# [ASCII] A = 65, B = 66, C = 67, D = 68, E = 69, F = 70, G = 71, H = 72
# 65 빼서 사용하기
## R이 숫자(행), C이 알파벳(열). 알파벳이든 수든 증가하는 방식으로 계산(2차 배열X)
def safe(org_r, org_c, r, c):
    if org_r + r < 0 or org_r + r > 7:
        return False
    if org_c + c < 0 or org_c + c > 7:
        return False
    return True

king, stone, N = input().split()
idxs = { "R": 0, "L": 1, "B": 2, "T": 3}
R, C = [0, 0, -1, 1], [1, -1, 0, 0]
kr, kc, sr, sc = int(king[1]) - 1, ord(king[0]) - 65, int(stone[1]) - 1, ord(stone[0]) - 65
for _ in range(int(N)):
    move = input()
    r = c = 0
    for l in move:
        r += R[idxs[l]]
        c += C[idxs[l]]
    # 움직일 칸에 돌 있는지 확인
    if kr + r == sr and kc + c == sc:   # 돌 있음
        if safe(sr, sc, r, c):
            sr += r
            sc += c
            kr += r
            kc += c
    else:   # 돌 없음
        if safe(kr, kc, r, c):
            kr += r
            kc += c
        else:
            continue
print(chr(kc + 65) + str(kr+1))
print(chr(sc + 65) + str(sr+1))