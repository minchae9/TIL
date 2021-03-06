# PR-정렬-가장 큰 수

시간 초과로 풀지 못해서 검색하다가 답안을 참고한 사이트: [여기](https://mentha2.tistory.com/9)

---

# PR-완전탐색-소수찾기

```python
from itertools import permutations
lst = list(permutations(str_num, i))
```

str_num에서 i개의 요소를 뽑아 가능한 모든 조합을 만들어 list로 만들어준다.

```python
# 소수찾기 (13행)
for i in range(2, num//2 + 1)
```

범위를 num을 2를 나눈 몫까지로 설정했지만, num의 제곱근으로 설정하면 더 효율적이다.

예를 들어, 16의 약수를 보면 1, 2, 4, 8, 16이고, 4가 16의 제곱근이다. 1, 2, 4까지 구하고 나면, 4는 제곱근이므로 자기자신과 곱하면 16이 되고, 2는 8, 1은 16과 곱하면 16이 된다. 즉, 제곱근 이후의 숫자들은 제곱근 이전의 숫자들과 곱하여 원래의 수가 되는 것이기 때문에 제곱근 이후의 숫자들은 살펴보지 않아도 된다. (제곱근 이후의 숫자들은 이미 제곱근 이하의 숫자들로부터 원래의 숫자의 약수인지 아닌지가 판별되었다.)
