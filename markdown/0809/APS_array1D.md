#0809

# APS 기본 - 1차원 배열

## 01. 알고리즘

> 문제를 해결하는 절차

### 표현방법

- pseudocode: 완전한 코드가 아닌, 논리적 구조를 이해할 수 있는 형태로 적는 것

  <img src="https://ars.els-cdn.com/content/image/3-s2.0-B9780080977683000064-f06-05-9780080977683.jpg" alt="Pseudocode - an overview | ScienceDirect Topics" style="zoom: 67%;" />

- 순서도

  <img src="http://tcpschool.com/lectures/img_codingmath_54.png" alt="코딩의 시작, TCP School" style="zoom:67%;" />

### 알고리즘의 성능을 측정하는 방법

- 시간 복잡도(Time Complexity): 수행에 소요되는 시간

  **빅-오 표기법(Big-O)**

  > 데이터량의 증가에 따라 시간이 어떻게 늘어나는지를 나타냄.

<img src="https://adrianmejia.com/images/time-complexity-examples.png" alt="How to find time complexity of an algorithm? - 极思路" style="zoom:50%;" />

## 02. 배열

> 메모리 안의 연속적인 공간에 저장하는 자료 구조
>
> ㄴ 파이썬에서는 '리스트(list)'로 구현됨

- 다수의 변수로는 하기 힘든 작업을 배열을 활용하면 쉽게 할 수 있다!
- 여러 개의 변수를 일일이 이용하는 비효율성을 제거

- 모든 원소에 접근 → for문

## 03. 정렬

> 둘 이상의 자료를 특정 기준에 따라 오름차순 또는 내림차순으로 배열하는 것

### 종류

- 버블 정렬 (Bubble Sort) ✔

  > 인접한 원소 두 개를 비교하며 자리를 계속 교환하는 방식
  >
  > - 시간 복잡도: O(n²)

  1. 일단, 정렬 구간을 정한다.

  2. 해당 구간에서 가장 큰 값이 맨 뒤로 가도록 한다.

     ㄴ 진행되면서 구간이 뒤에서부터 하나씩 줄어든다 (맨 뒤의 값이 정렬되므로).

     - 필요한 정보

       (크기가 n인 배열을 상정했을 때)

       (1) 구간의 끝: 인덱스를 기준으로, i는 (n - 1) 부터 1까지

       (2) 구간 내부에서는 두 개씩 비교하여, 더 큰 원소를 오른쪽으로 보내기: j는 0부터 (i - 1)까지

       ```python
       def bubblesort(arr):
           for i in range(len(a)-1, 0, -1):
               for j in range(i):
                   if arr[j] > arr[j+1]:
                       arr[j], arr[j+1] = arr[j+1], arr[j]
       ```

       

- 카운팅 정렬 (Counting Sort) ✔

  > 각 항목의 개수를 세어 정렬하는 알고리즘
  >
  > - 시간 복잡도: O(n+k) 
  >
  >   (n은 배열 길이, k는 정수의 최대값)

  ※ 정수나 정수로 표현할 수 있는 자료에 대해서만 적용이 가능하다.

  ​	ㄴ 값을 인덱스로 접근할 것이기 때문!

  ![img](https://miro.medium.com/max/1202/1*8cV2J9h2kJFNqOelZD_-eQ.png)

  1. 각 항목을 세어, 각 항목의 숫자를 인덱스로 가지는 리스트에 개수를 저장한다.

  2. 개수를 저장한 집합에서 (인덱스 활용을 위해) 누적 값을 구하여 배열에서의 순서를 구한다.

  3. (주로 뒤에서부터) 원래 데이터를 접근하여, 해당하는 숫자를 인덱스로 개수 집합에 접근하여, 개수 집합의 접근된 요소에서 1을 차감한다. 해당 인덱스의 숫자를 인덱스로 하는 새로운 배열에 값을 할당한다.

     ```python
     def countingsort(orgdata, srt, n):	# n은 orgdata(입력 배열)의 최대 값
         count = [0] * n
         
         for i in range(len(orgdata)):
             count[orgdata[i]] += 1
         for i in range(0, len(count)-1):
             count[i+1] += count[i]
         for k in range(len(orgdata)-1, -1, -1):
             count[orgdata[i]] -= 1
             srt[count[orgdata[i]]] = orgdata[i]
     ```

     

- 선택 정렬 (Selection Sort)
- 퀵 정렬 (Quick Sort)
- 삽입 정렬 (Insertion Sort)
- 병합 정렬 (Merge Sort)

## 04. Baby-gin Game

> 설명: 0~9 사이의 숫자 카드에서 임의로 6장을 뽑아, 3장의 카드가 연속적인 번호를 갖는 경우를 'run', 3장의 카드가 같은 번호를 갖는 경우를 'triplet'이라고 한다. run과 triplet으로만 구성된 경우를 'baby-gin'이라 한다.

> baby-gin 여부를 판별하는 프로그램 작성하기.

### 👉 완전 검색(Brute-force)

: 모든 가능한 경우의 수를 시도하여 확인하는 방법

- 일반적으로 경우의 수가 작을 때 유용하다.
- 수행 속도는 느리지만, 답을 찾아내지 못할 확률도 작다.

=> 순열로 접근하기

가능한 순열을 모두 생성하여, 3개씩 나누어 run과 triplet 여부를 테스트하여 판단한다.



### 👉 탐욕 알고리즘(Greedy)

: 순간순간에 가장 좋은 선택을 함으로써 최적의 답안을 찾아내는 방법

- 지역적으로는 최적이지만, 전체적으로는 최적이 아닐 수 있다.

- 동작 과정:

 1. 해 선택

    : 현 상태에서 부분 문제의 최적해를 구하고, 이를 부분해 집합(solution set)에[ 추가한다.

	2) 실행 가능성 검사

    : 새로운 부분해 집합이 실행 가능한지 확인한다. (문제의 제약조건을 위반하지 않는지 검사한다.)

	3) 해 검사

    : 새로운 부분해 집합이 문제의 해가 되는지 확인한다. 전체 문제의 해가 완성되지 않았다면, 1부터 다시 시작한다.

- 예) 거스름돈 문제 - 가장 적은 수의 동전으로 주려면?

  : 큰 단위의 동전부터 넣는 게 부분의 최적해!

  <img src="https://progressivecoder.com/wp-content/uploads/2020/08/greedy-algo-visualization.png" alt="Coin Change Problem using Greedy Algorithm | PROGRESSIVE CODER" style="zoom: 50%;" />

=> 

![img](https://blog.kakaocdn.net/dn/cB8Khd/btqzvoOBejN/X8pTAg98WTK5YahRj7gtF1/img.png)

​																																								(출처: [여기](https://playthegame00.tistory.com/60))