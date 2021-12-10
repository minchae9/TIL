"""
5 3 일 때
[1, 2, 3, 4, 5]
인덱스
0 1 2
0 1 3
0 1 4

0 2 1
0 2 3
0 2 4

0 3 1
0 3 2
0 3 4

...

1 0 2
1 0 3
1 0 4

1 2 0
1 2 3
1 2 4

"""


def num(res):
    if len(res) == M:
        for k in res:
            print(k, end=' ')
        print()
        return
    else:
        for i in range(1, N+1):
            if i not in res:
                res.append(i)
                num(res)
                res.pop()


N, M = map(int, input().split())
ans = []
num(ans)