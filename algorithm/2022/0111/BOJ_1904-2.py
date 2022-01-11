"""
참고: https://sungmin-joo.tistory.com/21
앞이 막힌 긴 상자, 스택처럼 생각해야 한다.
일관되게 뒤에 붙여나가며 길이를 맞추기로 하므로, 뒤에 붙는 경우만 고려해야 한다.
(앞에 붙이면 중복되는 경우가 생기기 때문에 안 되지만, 난 자꾸 헷갈리므로 위와 같이 이해해보자.)
----------------------------------------------------------------------------------
[1]

[00] [11]

[100] [001] [111]

[0000] [1100] [1001] [0011] [1111]

...

즉, n개를 만들려면, n-2개 짜리에 2짜리 1개를 붙이는 방법과, n-1개 짜리에 1짜리 1개를 붙이는 방법이 있다.
n-2개 짜리에 1짜리 2개를 붙이는 것은, n-2에서 n-1을 만든 후 n-1개 짜리에 1짜리 1개를 붙이는 것에 해당하므로
이렇게 생각하면 안 된다.

"""
# 재귀 호출: 런타임에러
"""
def f(n):
    if n < 3:
        return n
    else:
        return f(n-2) + f(n-1)
"""
N = int(input())
res = [0, 1, 2] + [0] * N
for i in range(3, N+1):
    res[i] = (res[i-2] + res[i-1]) % 15746  # 나머지만 구하면 됨 (이렇게 안 하면 메모리초과)
print(res[N])