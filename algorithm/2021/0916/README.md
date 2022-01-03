# SWEA_3307

```python
"""
실패본.
찾아보니 DP로 풀어야 한다고 한다.
아래 방법으로는 '1 90 91 92 93 100 10 11 12 13 14 15'의 테스트케이스를 풀지 못한다.
"""
T = int(input())
for t in range(1, T+1):
    N = int(input())    # 수열의 길이
    arr = list(map(int, input().split()))

    s = 0
    mx = 1
    while s < N-1:
        if N-s <= mx:
            break
        i = s
        cnt = 1
        p = 0
        while p < N-s-1:
            for j in range(1, N-s):
                k = arr[i]
                if i+j < N and k <= arr[i+j]:
                    cnt += 1
                    i += j
                    p += 1
                    break
                else:
                    p += 1

        if cnt > mx:
            mx = cnt
        s += 1
    print(f'#{t} {mx}')
```



DP로 풀려고 시도해봤는데, 아예 생각한 로직이 틀렸던 건지 잘 풀리지 않았다.

그래서 [블로그 글](https://velog.io/@daeungdaeung/SWEA-3307-%EC%B5%9C%EC%9E%A5-%EC%A6%9D%EA%B0%80-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4with-Python)을 보고 공부를 했다.

어떻게 이런 생각을 할 걸까! 😝

1. 먼저, 그림만 보고 코드를 만들어 보았다.

   성-공!

   

