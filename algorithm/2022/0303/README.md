# 더 효율적인 풀이

출처: [sol1874님 풀이](https://www.acmicpc.net/source/36135302)

```python
import sys

input = sys.stdin.read


def sol1874():
    n, *nums = map(int, input().split())
    cur = 1
    st = []
    answer = []
    for num in nums:
        while cur <= num:
            st.append(cur)
            answer.append('+')
            cur += 1
        if st[-1] != num:
            answer = ['NO']
            break
        st.pop()
        answer.append('-')
    print('\n'.join(answer))
```

1~n 까지의 수가 들어있는 배열을 미리 만들지 않고 스택으로 사용하면서, 증가하는 수는 별도의 변수를 사용했다.

LIFO 구조를 취하는 스택에서 .append()로 맨 뒤에 저장된 수가 아닌 수를 필요로 하는 수열은 만들어질 수 없다.
