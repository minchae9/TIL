def solution(n):
    a = n
    tens = ''
    result = 0
    while a >= 1:
        a, b = divmod(a, 3)
        tens = str(b) + tens
    for i in range(len(tens)):
        result += int(tens[i]) * (3**i)
    return result

"""
8~9행을 int() 빌트인 함수를 통해 간단하게 구현할 수 있다.
7행에서 문자열이 뒤에 추가되도록 tens += str(b)로 바꿔준 후,
int(tens, 3)
ㄴ tens 문자열을 3진법으로 인식하고 10진법으로 돌려준다.
"""