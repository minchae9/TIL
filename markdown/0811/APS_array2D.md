#0811

# 배열 2

## 1. 2차원 배열

> 1차원 배열로 구성된 배열

- `arr[i][j]`는 전체 배열의 i번째 요소의 j번째 요소로, i 번째 행 - j번째 열의 요소를 가리킨다.

### ✔ 0으로 채워진 배열 만들기

```python
arr = [[0] * M for _ in range(N)]
```

- N개 행, M개 열로 이루어진 배열

- 참고: 그저 순회만 할 때에는 for문의 변수를 종종 '_'로 둔다.

- **※주의**: `[[0] * M] * N`으로 만들면 안 된다! 

  이렇게 하면, 내부의 리스트는 모두 같은 객체를 참조하는 리스트들이 된다.
  
  <img src="../../../../캡처.PNG" alt="캡처" style="zoom:67%;" />

### 순회

```python
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 1. 행 우선 (기본)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j]
        
# 2. 열 우선
for j in range(len(arr[0])):
    for i in range(len(arr)):
        arr[i][j]			# 주의: j를 먼저 고정시켰으므로 똑같이 뒤에 적어주기. 얘도 바꿔적으면 안 됨

# 3. 지그재그
for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr[i][j + (m - 1 - 2*j) * (i % 2)]
        # i가 짝수이면 arr[i][j] 가 되어 왼쪽에서 오른쪽으로
        # i가 홀수이면 arr[i][m-1-j] 가 되어 오른쪽에서 왼쪽으로 (전체 열 크기가 m일 때)
```

- len(arr): 행의 크기
- len(arr[i]): 열의 크기
- 지그재그 순회는 행 번호에 따라 `if ~ else`문으로 표현할 수도 있다.
- 지그재그 순회 모양:

<img src="https://mblogthumb-phinf.pstatic.net/20150213_217/azure0777_1423798443236wsgI2_PNG/2%25EC%25B0%25A8%25EC%259B%2590_%25EB%25B0%25B0%25EC%2597%25B4_%25EC%25A7%2580%25EA%25B7%25B8%25EC%259E%25AC%25EA%25B7%25B8%25EB%25A1%259C_%25EC%25B1%2584%25EC%259A%25B0%25EA%25B8%25B0_%25EC%2598%2588%25EC%25A0%259C_001.png?type=w800" alt="img" style="zoom:67%;" />



### 2차 배열의 접근 - 델타를 이용

- 위, 아래, 왼쪽, 오른쪽의 인접한 4요소를 탐색하기

```python
# 1번 방법
# 위, 아래, 왼쪽, 오른쪽 순서
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for i in range(N):
	for j in range(M):
		for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:		# 배열을 벗어나지 않을 때
                arr[ni][nj]
                
# 2번 방법
for i in range(N):
    for j in range(M):
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = i + dr
            nj = j + dc
            if 0 <= ni < N and 0 <= nj < M:
                arr[ni][nj]
```

- 전치 행렬

  : 대각선을 기준으로 양쪽이 바뀌도록

  : i와 j의 크기를 비교해본다. (대각선은 i==j인 칸)

  

  ```python
  arr = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
  
  for i in range(len(arr)):
      for j in range(len(arr[i])):
          if i < j:				# 대각선의 위쪽을 기준으로
              arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
      
  ```

  ![numpy.transpose - Codetorial](https://codetorial.net/numpy/_images/numpy_transpose_01.png)



## 2. 부분집합 생성

### 완전 탐색

```python
bit = [0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[0] = j
        for k in range(2):
            bit[0] = k
            print(bit)
```



### 비트 연산자 활용

👉 [이해를 도와준 사이트](https://itzjamie96.github.io/2020/10/15/python-bitwise-powersets/)

#### 비트 연산자

> **&** : 모두 1일 때 1
>
> **|** : 하나라도 1일 때 1
>
> **<<** : 피연산자의 비트 열을 왼쪽으로 이동. 이동한 자리는 0으로 채워짐.
>
> **>>** : 피연산자의 비트 열을 오른쪽으로 이동.

```python
arr = [1, 2, 3, 4, 5]
n = len(arr)

for i in range(1<<n):	#'1<<n'은 2^n으로 보면 됨. 즉, 가능한 부분집합 모두를 탐색.
    for j in range(n+1): # 0부터 n까지의 값을 가지는 j
        if i & (1<<j):	# j번 비트가 1일 때, i의 j번 자리도 1이면 1이 나옴 -> True
            print(arr[j], end=', ')
    print()
print()
```



## 3. 바이너리 서치 (이진 탐색)

*순차검색

: 처음부터 끝까지 찬찬히 찾아나가다, 찾으면 검색 완료.

정렬되지 않은 자료에서 시간 복잡도는 O(n)이다.

정렬된 자료에서 시간 복잡도는 O(n)이지만, 검색 실패를 반환하는 경우 비교 횟수가 반으로 줄어든다.

### 이진 탐색

> 자료의 가운데 값과 비교하여 다음의 검색 위치를 결정하여 검색을 진행하는 방법
>
> - 할 때마다 검색 범위가 반으로 줄어들기 때문에 빠르다.
> - **단, 이진 탐색을 하기 위해서는 자료가 정렬되어 있어야 한다!**

1. start와 end를 정한다. (구간의 처음과 끝 값)

2. 둘의 중간이 mid 값으로 자료를 접근한다.

3. i) 목표값이 mid 값보다 작으면, end = mid - 1로 범위를 앞의 부분으로 새로이 한정한다.

   ii) 목표값이 mid 값보다 크면, start = mid + 1로 범위를 뒷 부분으로 새로이 한정한다.

   iii) 목표값이 mid값과 일치하면, 검색을 종료한다.

4. start <= end일 때 탐색을 수행하다가, 값을 찾지 못하고 start가 end를 넘어서면 탐색을 종료한다 - 검색 실패.

```python
arr = [3, 4, 9, 15, 24, 25, 52, 87]
key = 52

start = 0
end = len(arr) - 1

while start <= end:
    middle = (start + end) // 2
    if arr[middle] == key:
        return True			# 검색 성공
    elif arr[middle] > key:
        end = middle - 1
    else:
        start = middle + 1
else:
    return False			# 검색 실패
    
```



## 4. 선택 정렬

> 주어진 자료 중 최소값을 찾아 맨 앞의 요소와 위치를 교환하는 방법
>
> → 앞부터 정렬되며 정렬할 구간이 줄어든다.
>
> - 시간 복잡도: O(*N*^2)

1. 정렬할 구간에서 최소값을 찾고

2. 정렬 구간의 맨 앞의 요소와 교환한다.

   ```python
   for i in range(0, len(arr)-1):
       min = i
       for j in range(i+1, len(a)):
           if arr[min] > a[j]:
               min = j				# 최소값 구하기
       a[i], a[min] = a[min], a[i]	 # 맨 앞 요소와 교환
   ```

   

## 5. 셀렉션 알고리즘

> 자료에서 k번째로 큰/작은 요소를 찾는 방법
>
> - k가 비교적 작을 때 유용
>
> - 시간 복잡도: O(kn)

1. 정렬하고

2. 인덱스로 k번째 요소 가져오기

   → k번째 까지만 선택정렬을 하면 됨.