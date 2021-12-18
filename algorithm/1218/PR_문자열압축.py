def solution(s):
    length = 10000
    # 길이가 1
    if len(s) < 2:
        length = 1
    # 길이가 2 이상
    else:
        for interval in range(1, len(s)):   # interval: 압축 단위
            prev = ''
            cnt = 0
            res = ''
            start = 0
            while True:
                finish = start + interval
                if finish > len(s): # 남은 문자열 개수보다 압축 단위가 클 경우
                    if start < len(s):
                        if cnt > 1:
                            res += str(cnt)
                        res += prev
                        cnt = 1
                        prev = s[start:]
                    break
                term = s[start:finish]
                start += interval
                if prev == '':
                    prev = term
                    cnt += 1
                else:
                    if term == prev:
                        cnt += 1
                    else:
                        if cnt > 1:
                            res += str(cnt)
                        res += prev
                        prev = term
                        cnt = 1
            if cnt > 1:
                res += str(cnt)
            res += prev
            if len(res) < length:
                length = len(res)
    return length