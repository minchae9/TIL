N = int(input())

"""
n=3 ['*']
n=9 ['***', '* *', '***']
"""

def stars(x, t):
    dev = []
    for i in x:
        # 1부분
        dev.append(i * 3)
    for i in x:
        # 2부분
        part = i + (' ' * t) + i
        dev.append(part)
    for i in x:
        # 3부분
        dev.append(i * 3)
    return dev

k = 3
x = ['*']
while k <= N:
    x = stars(x, k//3)
    k *= 3
for i in x:
    print(i)

"""
***
* *
***
"""
# 기본 (N=3)
"""
1부분
'*' * 3

2부분
'*' * 1
' ' * 1
'*' * 1

3부분
'*' * 3
"""

# 9
"""
1부분
- 1부분 대입
- 2부분 대입
- 3부분 대입

2부분
- 1부분 대입
- 2부분 대입
- 3부분 대입

3부분
- 1부분 대입
- 2부분 대입
- 3부분 대입
"""