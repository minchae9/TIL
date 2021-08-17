"""
파이썬의 zip(*iterable)
예)
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
nums, chars = zip(*pairs)
nums -> (1, 2, 3, 4)
chars -> ('a', 'b', 'c', 'd')
"""
def palindrome(word, m):
    for i in range(m//2):
        if word[i] != word[-i-1]:
            return False
    return True

for _ in range(10):
    tc = int(input())
    n = 100
    words = []
    for _ in range(n):
        words.append(input())
    words_h = [''.join(i) for i in zip(*words)]

    res = 1
    flag = False

    for m in range(100, 1, -1):
        for i in range(n):
            for j in range(n-m+1):
                if palindrome(words[i][j:j+m], m) or palindrome(words_h[i][j:j+m], m):
                    res, flag = m, True
                    break
        if flag:
            break

    print(f'#{tc} {res}')
