import math
def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        if math.sqrt(n) == n//math.sqrt(n):
            answer -= n
        else:
            answer += n
    return answer