#0722

# ✔ 개념

### 1. [컨테이너] Mutable과 Immutable 🔐

### 										 & 시퀀스형과 非시퀀스형 🚋

차이: 변경 가능성 / 순서의 유무

- Mutable: List, **Set, Dictionary**

- Immutable: Literal(Number, String, Bool), Tuple, Rangㄷ

  (*Set, Dictionary는 비시퀀스형. 나머지는 시퀀스형.)

  

### 2. [컨테이너] 딕셔너리(dictionary)

#### 1. 딕셔너리 만드는 방법 2가지

(1) dict() 사용

- <u>key로 사용되는 문자열에 ' ' (또는 " ")를 붙이지 않는다.</u>

- key와 value를 잇는 기호는 **' = '** 를 사용한다.

```python
dict_1 = dict(sally = 25, monica = 33, robert = 48)
```

(2) { } 사용

- { } 를 사용할 경우, set가 아닌 dictionary가 만들어진다.
- key와 value를 잇는 기호는 **' : '** 를 사용한다.
- 즉, 딕셔너리 실물(?)과 똑같이 만들면 된다.

```python
dict_1 = {'sally' : 25, monica : 33, robert : 48}
```

- 공통: key에는 immutable 데이터만 가능하다. (List 안 됨.)

  

#### 2. 딕셔너리 요소 추가하기

(1) `딕셔너리명[key] = value` 로 할 수 있다. 

해당 key가 기존에 있다면 value값이 수정되고, 없다면 새로운 key-value 쌍이 생성된다.

(2) `update()` 함수 사용

`딕셔너리명.update({'key' : 'value', 'key2' : 'value2'})`로 여러 값을 수정 (또는 추가)할 수 있다.



#### 3. for 문에서 딕셔너리 사용하기

key와 value를 한거번에 for문으로 반복하려면, `items()`를 사용한다.

→ `items()` 함수는 <u>key와 value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다</u>.

```python
>>> a = {'jennifer': 1997, 'alice': 1996, 'rebecca': 1989}
>>> for key, val in a.items()
	print(f'key = {key}, value = {val}')
# 결과값
key = jennifer, value = 1997
key = alice, value = 1996
key = rebecca, value = 1989
```



### 3. [함수] 기타

- `print()`**문의 옵션: end, sep**

  - end

    - 기본값 '\n' (줄바꿈). 

      (값을 별도로 지정하지 않으면 결과값은 행을 달리하여 출력됨 

      & `print()`를 했을 때 공백이 출력되고 해당 코드 앞뒤로 한 줄 띄워짐)

  - sep

    - 구분기호. 기본값 ' ' (공백).

- **자료형 비교**

  `type()` 함수를 씌워서 비교한다.

  ```python
  type(3+4j) is complex
  ```

- **sorted()**

  iterable 객체에 대해 오름차순으로 정렬

  `list.sort()`로 리스트에 대해 정렬할 수도 있다.

- **.remove()**

  item 제거

- **all()**

  인자로 받는 iterable 객체(range, list)에서 <u>i) 모든 요소가 참이거나</u>, <u>ii) 비어 있으면</u> True를 반환

- **any()**

  인자로 받는 iterable 객체(range, list)의 요소 중 하나라도 참이면 True를 반환하고, 비어 있으면 False를 반환

- **.append()**

  (리스트에 쓰여서) 리스트에 끝에 item을 추가

- **slice(start=0, end, step=1)**

  - 범위는 'start 포함, end 미포함'
  - end를 비워놓으면, 끝까지 슬라이싱 된다.

# ✔ 문제

## 1. 가변 인자 리스트를 사용해보자.

> 정수를 여러 개 받아서 가장 큰 값을 반환(return)하는 함수 `my_max()`를 작성하세요.
>
> max 내장 함수 사용은 금지합니다.

```python
def my_max(*args):
    a = args[0]			# 하나의 값을 지정해두고,
    for arg in args:
        if arg > a:		# 다른 값을 그 값과 비교하며 큰 값으로 변경
            a = arg
    return a
```

<br/>

---

## 2. URL 생성기

> `my_url()` 함수를 만들어 완성된 URL을 반환하는 함수를 작성하세요.
>
> 입력받은 가변 키워드 인자를 활용하여 'https://api.go.kr?'를 BASE_URL로 사용하는 URL을 생성해봅시다.
>
> 가변 키워드 인자(kwargs)를 사용하는 my_url 함수를 직접 작성해보세요.

```python
# 예시)
my_url(sidoname='서울', key='asdf')
# https://api.go.kr?sidoname=서울&key=asdf&
```

```python
def my_url(**kwargs):
    BASE_URL = 'https://api.go.kr?'
    for key, value in kwargs.items():		# key와 value 값을 items() 함수로 같이 사용
        BASE_URL += f'{key}={value}&'
    return BASE_URL
```

<br/>

---

## 3. 불쌍한 달팽이

> 달팽이는 낮 시간 동안에 기둥을 올라간다. 하지만 밤에는 잠을 자면서 어느 정도의 거리만큼 미끄러진다. (낮 시간 동안 올라간 거리보다는 적게 미끄러진다.)
>
> 달팽이가 기둥의 꼭대기에 도달하는 날까지 걸리는 시간을 반환하는 함수 `snail()`을 작성하시오.

> 함수의 인자는 다음과 같다.
>
> 1. 기둥의 높이(미터)
> 2. 낮 시간 동안 달팽이가 올라가는 거리(미터)
> 3. 달팽이가 야간에 잠을 자는 동안 미끄러지는 거리(미터)

```python
# 내가 한 풀이 - 틀림!
# 낮 시간에 도달할 수 있음을 간과하고 하루 치의 양으로 계산함

def snail(height, day, night):
    n = 0
    while True:
        if height <= n * (day - night):
            return n
        else:
            n += 1
-------------------------------------------------------------------------------------------------
# 정답 풀이

def snail(height, day, night):
    count = 0
    while True:
        count += 1
        height -= day			# 낮 시간 동안 올라서 가야 할 거리가 줄어듦
        if height <= 0:			# 꼭대기에 도달했다면,
            return count		# 며칠 걸렸는지 반환한다.
        height += night			# 낮시간에 아직 도달 못했다면, 밤시간에 미끄러져서 거리가 늘어남
```

<br/>

---

## 4. 자릿수 더하기 (SWEA #2058)

> 자연수 number를 입력 받아, 각 자릿수의 합을 계산하여 출력하시오.

```python
# 예시)
sum_of_digit(1234) #=> 10
sum_of_digit(4321) #=> 10
```

```python
# 내 풀이

def sum_of_digit(number):
    i = 0
    total = 0
    while number / (10 ** i) > 1:		# 가장 큰 단위의 자릿수부터 계산할 수 있도록 i를 늘림
        i += 1
    for k in range(i - 1, -1, -1):
        a = number // (10 ** k)			# 몫을 구하면, 자릿수를 알 수 있다.
        total += a
        number -= a * (10 ** k)
    return total
-------------------------------------------------------------------------------------------------
# 다른 풀이: 재귀적 접근

def sum_of_digit(number):
    if number < 10:							  # 10 미만이면 본래 값 반환
        return number
    else:
        number, remainder = divmod(number, 10)	# 몫과 나머지를 저장하여,
        return sum_of_digit(number) + remainder # 일의 자리 숫자부터 구해서 더해나간다.
```

<br/>

---

## 5. 회문 판별

> 회문 또는 팰린드롬은 거꾸로 읽어도 제대로 읽는 것과 같은 문장이나 낱말, 숫자, 문자열 등을 말한다.
>
> 입력으로 짧은 영어단어 word가 주어질 때, 해당 단어가 회문이면 True 회문이 아니면 False를 반환하는 함수를 작성하시오.
>
> 이때, 반복문(`while`)과 재귀 함수를 사용해서 각각 작성하시오.

```python

# 내 풀이
# while

def is_pal_while(word):
    i = 0
    while i < len(word):
        if word[i] == word[-i-1]:		# 인덱스의 합이 -1이 되는 문자가 같아야 한다.
            return True
        else: 
            return False
-------------------------------------------------------------------------------------------------
# 다른 풀이
# 내 풀이 아님
# 재귀
'''
핵심 - 재귀
양쪽 끝부터 확인하면서 비교하기.
racecar 라는 단어가 있다고 하면,

racecar의 양 끝 r - r 비교,
aceca의 양 끝을 비교하는 함수를 호출하여 a - a 비교,
...
만약에 글자가 하나 이하로 남는다면 return True => 종료조건
'''
def is_pal_recursive(word):
    if len(word) <= 1:						# 1. 종료조건 선언
        return True
    if word[0] == word[-1]:					# 2-1. 양 끝이 같으면 => 다음 subword를 넣어 함수 호출
        return is_pal_recursive(word[1:-1])
    else:								   # 2-2. 다르면 => False
        return False
```

