#0724

출처: [백준](https://www.acmicpc.net/problem/1065)

오늘의 진도: '단계별로 풀어보기' 의 **while문, 함수, 재귀** (못 푼 문제 있음!)

## 문제

어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

## 입력

첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

## 출력

첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

## _내 풀이_

```python
N = int(input())
hansu = []
for n in range(1, N+1):
    if len(str(n)) <= 2:
        hansu.append(n)
    else:
        if int(str(n)[0]) - int(str(n)[1]) == int(str(n)[1]) - int(str(n)[2]):
            hansu.append(n)
print(len(hansu))
```

