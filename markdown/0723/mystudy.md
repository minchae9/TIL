#0723

##### 작성자: 김민채

### [프로그래머스] 완전탐색 > [모의고사]( https://programmers.co.kr/learn/courses/30/lessons/42840)



#### ✔ 문제

###### 문제 설명

수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

##### 제한 조건

- 시험은 최대 10,000 문제로 구성되어있습니다.
- 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
- 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

##### 입출력 예

| answers     | return  |
| ----------- | ------- |
| [1,2,3,4,5] | [1]     |
| [1,3,2,4,2] | [1,2,3] |

---

나의 풀이

```python
def solution(answers):
    answer = []
    #supoza1
    a1, b1 = divmod(len(answers), 5)
    supoza1 = [1, 2, 3, 4, 5] * a1 + [1, 2, 3, 4, 5][: b1+1]
    score1 = 0
    #supoza2
    a2, b2 = divmod(len(answers), 8)
    supoza2 = [2, 1, 2, 3, 2, 4, 2, 5] * a2 + [2, 1, 2, 3, 2, 4, 2, 5][: b2+1]
    score2 = 0
    #supoza3
    a3, b3 = divmod(len(answers), 10)
    supoza3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * a3 + [3, 3, 1, 1, 2, 2, 4, 4, 5, 5][: b3+1]
    score3 = 0
    
    for i in range(len(answers)):
        if answers[i] == supoza1[i]:
            score1 += 1
        if answers[i] == supoza2[i]:
            score2 += 1
        if answers[i] == supoza3[i]:
            score3 += 1
    result = max(score1, score2, score3)
    
    if result == score1:
        answer.append(1)
    if result == score2:
        answer.append(2)
    if result == score3:
        answer.append(3)
        
    return answer
```

