"""
참고자료: https://wikidocs.net/21638
"""
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())    # n은 짝수
    """
    # n까지 이르는 소수 (시간초과)
    for num in range(3, n):
        check_range = num//2
        for ck in range(2, check_range + 1):
            if num % ck == 0:
                break
        else:
            prime.append(num)
    """
    # n까지 이르는 소수 (에라토스테네스의 체)
    prime_or_not = [False, False] + [True] * (n-1)
    for num in range(2, n+1):
        if prime_or_not[num] is True:
            for k in range(2*num, n+1, num):
                prime_or_not[k] = False
    # 큰 수부터 체크하여, 소수면 출력하고 break
    for i in range(n//2, 1, -1):
        if prime_or_not[i] and prime_or_not[n-i]:
            print(f'{i} {n-i}')
            break