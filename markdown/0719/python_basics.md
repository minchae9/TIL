#### 작성자: 김민채

#### 날짜: 2021-07-19

#### 주제: 파이썬 기초 (1)

---

### 0. 파이썬의 특징
#### 1) 인터프리터(Interpreter) 언어
- 컴파일러와 대비되는 개념
('컴파일러'가 전체를 번역하여 넘겨주는 것이라면, '인터프리터'는 한 줄씩 통역해주는 것)
- 소스 코드를 컴파일하지 않기 때문에 개발이 빠르지만, 실행속도가 느림
#### 2) 객체지향 프로그래밍(OOP: Object-Oriented Programming)
#### 3) 동적 타이밍(Dynamic Typing)
- 변수에 타입을 별도로 지정하지 않아도 된다.

### 1. 기초 문법
#### 1) 주석(comment)
- 일반적으로 주석은 `#`를 이용해서 적는다.
- 통상, 함수 또는 클래스의 설명을 적는 **docstring**을 적을 때 ```"""``` 사이에 적어넣는다.

### 2. 변수와 식별자
#### 1) 변수(variables)
할당 연산자(=)로 변수에 값을 넣는 것을 "할당(assignment)"이라고 표현한다.
- 예시
```python
x = y = 3
```
: 두 변수에 동시에 같은 값을 할당
```python
x, y = 1, 2
```
: 두 변수에 동시에 다른 값을 할당(multiple assignment) - 파이썬 내부적으로 이 과정은 튜플로 이루어짐
- 함수
	
    - `type()`: 데이터 타입
    - `id()`: 변수에 할당된 값의 메모리 주소
    _(*참고: 변수에 할당된 값이 같더라도 메모리 주소는 다를 수 있다.)_
    
#### 2) 식별자(Identifiers)
- 예약어 출력하기
```python
import keyword
print(keyword.kwlist)
```
> ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

### 3. 데이터 타입
#### 1) 숫자(int, float, complex)
- 정수형(int)
    - 특징: 파이썬에서는 가용 메모리를 활용해 수를 표현하기 때문에, 매우 큰 수를 나타낼 때에도 오버플로(overflow)가 발생하지 않는다.
    - 2진수: 0b / 8진수: 0o / 16진수: 0x
- 부동소수점(float)
	
    - **Floating point rounding error**
    : 실수 비교 시 유의할 점
    : 컴퓨터가 2진수(비트)로 숫자를 표현하는 과정에서 실수를 유한개의 비트로 정확하게 표현할 수 없으므로 근사값을 저장함. 이때 근사값과 기준값을 비교할 때 정확하게 일치하지 못해 발생하는 것.
    - 예시
    ```0.1 * 3 == 0.3``` => False
    실제로 `0.1 * 3` 은 0.30000000000000004 의 값으로 나오기 때문이다.
    - 따라서, 다음과 같이 두 실수를 비교할 수 있다:  
```python
    num1 = 0.1 * 3
    num2 = 0.3
    
    #1. 임의의 작은 수
    abs(num1 - num2) <= 1e-10
    
    #2. system의 machine epsilon
    import system
    print(abs(num1 - num2) <= sys.float_info.epsilon)
    
    #3. isclose
    import math
    math.isclose(num1, num2)
```
- 복소수(complex)
: 실수부 + 허수부(j)

#### 2) 문자열(string)
- 이스케이프 시퀀스(escape sequence)
	: 문자열 내에서 특정 문자를 표현하거나, 문자열 모양을 바꾸기 위해 사용
    - `\n`: 줄바꿈
    - `\t`: 탭
    - `\\`: 백슬래시
    - `\'`, `\"`: 인용부호(', ")
  
- String interpolation
: 문자열 사이에 변수 값 넣기

**(1) str.format()**
```python
weather = '맑음'
print('오늘 날씨는 {}이야'.format(weather)
```

**(2) f-strings**
```python
weather = '맑음'
print(f'오늘 날씨는 {weather}이야')
```

#### 3) True/False(boolean)
- False: 0, 0.0, ( ), [ ], { }, ' ', None
#### 4) None
값이 없음을 표현하기 위한 NoneType
- None 확인은 `is None`으로 한다.
#### 5) 타입 변환(Type conversion)
- _암시적(Implicit) 변환_ : 파이썬 내부적으로 변환
    - bool
    - 숫자(int, float, complex)
    - 예시
```python
>>> True + 2
3
>>> 1 + 2.0
3.0
>>> 2 + 3j + 4
(6+3j)
```
- _명시적(Explicit) 변환_ : 사용자가 수동적으로 변환
    - int로: str(형식에 맞을 때), float(소수점 아래를 _버림_ )
    - float로: str(형식에 맞을 때), int
    - str로: int, float, list, tuple, dict
    
    
### 4. 연산자
#### 1) 산술 연산자
- 기본
> +, -, *, /

 > // : 몫

 > ** : 거듭제곱

- `divmod(피제수, 제수)`: 튜플 형식으로 (몫, 나머지)를 반환함
#### 2) 비교 연산자
값을 비교하여 True/False 값을 반환
- 기본
> <, >, <=, >=, ==, !=
- 객체 아이덴티티 판별
> is, is not

#### 3) 논리 연산자
> and, or, not

- **단축평가**:  첫 번째 값으로 결과가 확실한 경우, 두 번째 값은 확인하지 않음
    - and: 요소가 모두 참이어야 True이므로, 첫 번째 값이 True여도 두 번째 값까지 확인
      **=> 두 번째** 값이 할당됨
      첫 번째 값이 False이면 무조건 False이므로 두 번째 값은 확인하지 않음
      **=> 첫 번째** 값이 할당됨

    - or: 요소가 하나라도 참이면 True이므로, 첫 번째 값이 True이면 두 번째 값은 확인하지 않음
      **=> 첫 번째** 값이 할당됨
      첫 번째 값이 False이면 두 번째 값까지 확인해야 함
      **=> 두 번째** 값이 할당됨

      

#### 4) 복합 연산자

연산과 대입을 함께 하는 경우
> +=
> -=
>
> -=
> -=
>
> *=
> /=
> -=

#### 5) 기타 연산자: 결합, 포함 여부, identity, indexing/slicing
- 결합(concatenation): **`+`**
문자열 연결
```'Hello, ' + 'World!'```
- 포함 여부(containment test): `in`
```'d' in 'driving'```
- Identity: `is`
  동일한 객체(object)인지 여부
	- 값이 같다고 해도 객체는 서로 다를 수 있음
    - _-5_ 부터 _256_ 까지의 숫자는 id가 동일, 그 외에는 다를 수 있음
- Indexing: `[숫자]`
- Slicing: `[a:b]`
(*팁: 요소 사이를 쪼개는 선에 순서를 붙여 생각하면 쉬움)

### 5. 표현식/문장
1) (표현)식: 하나의 값으로 환원될 수 있는 것
2) 문/문장: **실행 가능한** 최소한의 코드 단위
- 모든 표현식은 문장이다.
- 할당문, 조건문은 표현식이 아닌 문장이다.

### 6. 컨테이너
여러 개의 값을 저장할 수 있는 것
#### 1) 시퀀스형 컨테이너
순서가 있다 (doesn't mean 정렬 여부)
- 리스트, 튜플, 레인지, 문자열, 바이너리
##### (1) 리스트(list)
- 생성: `list()` 또는 `[]`
- 값 변경이 **가능**하다.
```python
>>> [0] * 4
[0, 0, 0, 0]
```
##### (2) 튜플(tuple)
- 생성: `tuple()` 또는 `()`
- 값 변경이 **불가능**하다(immutable).
- 항목이 1개인 튜플을 만들 때에는 값 뒤에 쉼표(,)를 붙인다.
```python
tp = (1, )
```

##### (3) 레인지(range)
- `range(n)`: 0부터 n-1까지
- `range(n, m)`: n부터 m-1까지
- `range(n, m, s)`: n부터 m-1까지, s 간격으로 (s는 증감량)

- range의 값은 list로 형변환을 하여 볼 수 있다.
##### (4) 문자열(string)
##### (5) 바이너리(binary)

#### 2) 비 시퀀스형 컨테이너
순서가 없다 == 인덱스로 호출할 수 없다
- 세트(집합), 딕셔너리
##### (1) 세트(set)
- 생성: `set()` 또는 `{}`
(빈 세트를 만들려면 반드시 `set()`로 만들어야 함.
빈 {}는 딕셔너리 개체가 됨.)
- **순서가 없다** == 특정 값에 접근 X
- **중복된 값이 존재하지 않음**
- 집합 연산자
> `-` `|` `&`
##### (2) 딕셔너리(dictionary)
- 생성: `dict()` 또는 `{}`
(생성방법이 조금 다르다)
```python
>>> dicta = {1 : 'a', 2 : 'b', 3 : [0]}
>>> dicta
{1 : 'a', 2 : 'b', 3 : [0]}

>>> dictb = dict(1 = 'a', 2 = 'b', 3 = [0]}
>>> dictb
{1 : 'a', 2 : 'b', 3 : [0]}
```
- key : value 쌍으로 이루어짐
    - **key에는 변경 불가능한(immutable) 데이터만 가능하다 (list 안 됨).**
    - value는 모든 값이 가능하다.
- (인덱스를 사용할 수 없으므로) key를 통해 value에 접근함
#### 3) 함수
- `len()`: 시퀀스의 길이
- `min()`/`max()`: 최소값/최대값 (문자열의 경우, ASCII코드에 따름)
- `count(원소)`: 시퀀스에서 특정 원소의 개수 (없는 경우, 0을 반환)

### 7. 제어문
#### 1) 조건문(conditional statement): if~ elif~ else~
- 조건식은 동시에 검사되는 게 아니라, 위에서부터 아래로 순차적으로 검사
-> 따라서, 특정 조건식 이하의 조건식은 특정 조건식을 만족시키지 못함을 전제로 하고 있는 것이다.
* **조건 표현식(Conditional Expression)** or 삼항 연산자(Ternary Operator)
	`변수 = <true인 경우 값> if <조건식> else <false인 경우 값>`
	- 예시)
```python
	# 절댓값
	value = num if num > = 0 else -num
```

#### 2) 반복문(loop statement): for, while, 반복 제어
##### (1) for 문
```python
	for <변수명> in <iterable>:
    		#코드 블럭
```

- 반복가능한(iterable) 객체를 모두 순회하면 종료
- 종료조건 X

- `enumerate()`: 인덱스와 객체의 튜플을 반환함
```python
>>> fruits = ['apple', 'banana', 'blueberry']

# start = 0 (default)
>>> list(enumerate(fruits))
[(0, 'apple'), (1, 'banana'), (2, 'blueberry')]

# start = 1 (인덱스 값 1로 시작)
>>> list(enumerate(fruits))
[(1, 'apple'), (2, 'banana'), (3, 'blueberry')]
```


##### (2) while 문
```python
while <조건식>:
    # 코드 블럭
```
- 종료조건 O
- 조건식이 참인 경우 반복적으로 코드 실행 == 조건식이 False가 될 때까지 반복
- 무한루프를 조심하자!

##### (3) 반복 제어: break, continue, for-else
- break: 반복문 종료
```python
>>> k = 0
>>> while True:
        if k == 4:
            break
        print(k)
        k += 1
>>>
0
1
2
```
- continue: continue 이후의 코드는 수행하지 않고, 반복문으로 되돌아감
```python
>>> for i in range(7):
        if i % 2 == 1:
            continue
        print(i)
>>>
0
2
4
6
```
- for-else: 반복문을 끝까지 수행한 후, else 문 수행
```python
>>> for c in 'turtle':
        if c == 'a':
            print('a가 있어요!')
            break
    else:
        print('a가 없어요.')
>>>
a가 없어요.
```
다만, break로 반복문이 중단되어 끝까지 수행되지 못한 경우, else문이 실행되지 않음.
```python
>>> for c in 'turtle':
        if c == 'u':
            print('u가 있어요!')
            break
    else:
        print('u가 없어요.')
>>>
u가 있어요!
```

- pass문
아무 일도 하지 않음
-> 코드 작성 시 오류가 발생하지 않도록 자리를 채우는 용도로 사용
```python
>>> for t in range(5):
        if i == 4:
            pass
        print(i)
>>>
0
1
2
3
4
```

