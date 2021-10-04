"""
풀이 참고한 사이트: https://yr-note.tistory.com/52
"""

import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(sys.stdin.readline())
for t in range(1, T+1):
    N, M = map(int, sys.stdin.readline().split())    # N 세로, M 가로
    code = ['211', '221', '122', '411', '132', '231', '114', '312', '213', '112']
    ans = 0
    visited = []

    for x in range(N):
        line = input()
        if line == '0' * M or line in visited:
            continue
        visited.append(line)

        # 16진수 -> 2진수
        binary = ''
        for char in range(M):
            for j in range(3, -1, -1):
                if int(line[char], 16) & (1 << j):
                    binary += '1'
                else:
                    binary += '0'

        # 2진수에서 암호코드를 해독해 (뒤에서부터 패턴 찾기)
        ## 이때 최소값으로 나누어 몇배수가 된 패턴을 최소 비로 줄여.
        deciphered = ''
        c1 = c2 = c3 = 0
        for m in range((4*M)-1, -1, -1):
            if c2 == 0 and c3 == 0 and binary[m] == '1':    # 4번째: 1
                c1 += 1
            elif c1 > 0 and c3 == 0 and binary[m] == '0':   # 3번쨰: 0
                c2 += 1
            elif c1 > 0 and c2 > 0 and binary[m] == '1':    # 2번쨰: 1
                c3 += 1
            if c1 > 0 and c2 > 0 and c3 > 0 and binary[m] == '0':
                mn = min(c1, c2, c3)
                c1 = c1 // mn
                c2 = c2 // mn
                c3 = c3 // mn
                pat = str(c3) + str(c2) + str(c1)
                idx = code.index(pat)
                deciphered = str(idx) + deciphered
                c1 = c2 = c3 = 0
            if len(deciphered) == 8:    # 암호코드 하나 완성!
                # 정상 코드인지 확인하고, 정상이면 합을 더해.
                # deciphered = deciphered[::-1]
                test = 0
                original = 0
                for j in range(8):
                    if j % 2:   # 짝수자리
                        test += int(deciphered[j])
                    else:
                        test += int(deciphered[j]) * 3
                    original += int(deciphered[j])
                if test % 10 == 0 and deciphered not in visited:
                    ans += original
                visited.append(deciphered)
                deciphered = ''
    print(f'#{t} {ans}')