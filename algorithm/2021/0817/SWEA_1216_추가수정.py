"""
파이썬의 zip(*iterable)
예)
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
nums, chars = zip(*pairs)
nums -> (1, 2, 3, 4)
chars -> ('a', 'b', 'c', 'd')
"""
# 노션 스터디 게시글 보고 공부한 내용

def pal(wrd, m):									# 회문 판별하는 함수 만들기 (길이 반만큼만 돌면 된다.)
    for i in range(m//2):
        if wrd[i] != wrd[-1-i]:
            return False
    return True

for _ in range(10):
    tc = int(input())
    arr = [input() for _ in range(100)]
    r_arr = [''.join(i) for i in zip(*arr)]			# 컬럼 고정, 행별로 도는 과정을 단순화하기 위해 다른 배열을 하나 만듦

    ans = 0

    for m in range(100, 1, -1):					# 회문 길이를 가장 바깥 for문으로. i와 j 바뀌어가면서 봐야 하니까.
        for i in range(100):
            if ans:
                break
            for j in range(100-m+1):		   # 인덱스 범위 값 설정하는 방법 기억해두기: (전체 길이)-(단어 길이)까지 앞머리 인덱스 가능
                if pal(arr[i][j:j+m], m) or pal(r_arr[i][j:j+m], m): # 동시에 비교
                    ans = m
                    break
    if ans == 0:                               # 글자 하나짜리가 최소 회문이므로
        ans += 1
    print(f'#{tc} {ans}')