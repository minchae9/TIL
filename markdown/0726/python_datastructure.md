#0726

# 0. 데이터구조 (Data structures)

> 데이터를 편리하게 접근하고, 변경하기 위해 데이터를 저장/조작하는 법

살펴볼 내용:

- 시퀀스: 문자열(string), 리스트(list)
- 비 시퀀스: 세트(set), 딕셔너리(dictionary)
- iterable: string, tuple, list, set, dictionary

데이터 구조들은 다양한 <u>메서드</u>들을 가지고 있다.

# 1. 문자열

: immutable(-> <u>조작 시, 새로운 객체를 반환</u>), ordered (-> sequence)(인덱스로 접근 가능), iterable(순회 가능)

### 1. slicing

문자열[start : stop : step]

- step은 생략 가능 (default = 1)
- start는 포함, stop 은 미포함
  - start 생략시 0, stop 생략시 끝까지(`len(문자열)`)
- 거꾸로는 음수 인덱스로 접근 가능
- 슬라이싱 된 객체는 <u>새로운 객체!</u>: immutable 하므로

```python
s = 'abcde12345'
s[::] = 'abcde12345'	# s[0:len(s):1] 과 같음
```

### 2. `.find(x)`

x의 첫 번째 위치를 반환. **없으면, -1을 반환함**

### 3.  `.index(x)`

x의 첫 번째 위치를 반환. **없으면, 오류 발생**

### 4.  `.replace(old, new[, count])`

old 글자를 new 글자로 바꿔서 반환. (글자 길이는 문자 하나 이상도 가능함)

- 선택적 인자인 `count`를 지정하면 앞에서부터 해당 개수만큼만 바꿈. (지정하지 않으면, 모든 old 글자에 대해서)

  ~~*참고: 선택적 인자에 대한 표기는 배커스-나우르 표기법을 따름~~

- 변화된 문자열은 리턴값! 고로 사용하려면 변수에 담아서 써야 한다.

### 6. `.strip([chars])`

양쪽 제거: strip / 왼쪽 제거: lstrip / 오른쪽 제거: rstrip

지정한 문자가 제거된 문자열을 반환.

- 선택적 인자인 `chars`: 제거할 문자 **집합**을 지정하는 문자열. 

  - 지정하지 않거나 None이면, (개행을 포함한) 공백을 제거.

  ```python
  >>> 'www.example.com'.strip('cmowz')
  'example'
  ```

### 7. `.split(sep=None)`

문자열을 구분자를 기준으로 나누어 **리스트로 반환.**

- 구분자를 지정하지 않고 `.split()`으로 쓰면 공백을 기준으로 구분함.
- `.split('_')` 처럼 구분자를 지정해줄 수 있음.

### 8. `.join(iterable)`

iterable 요소들을 구분자로 합쳐 **문자열을 반환**. (즉, 요소들이 문자열이어야 함)

요소들 사이사이에 구분자를 넣음.

- *주의*: 문자열이 괄호 안에 들어감. 구분자를 . 앞에 적음.

  ```python
  >>> '_'.join(['3', '5'])
  '3_5'
  ```

### 9. 기타

- `.capitalize()`: 앞글자를 대문자로
- `.title()`: ' 또는 공백 이후를 대문자로 (기본적으로 각 단어의 첫 글자를 대문자로 변경)
- `.upper()`: 모두 대문자로
- `.lower()`: 모두 소문자로
- `.swapcase()`: 대문자는 소문자로, 소문자는 대문자로 변경

### 10. 문자열 관련 검증 메소드

boolean 값 (True, False)을 반환함

- `.isalpha()`: 알파벳 문자 여부 (한글 포함)

- `.isupper()`: 대문자 여부

- `.islower()`: 소문자 여부

- `.istitle()`: 타이틀 형식 여부

- `.isdecimal()` - `.isdigit()` - `.isnumeric()`: 특수기호에 대해 판단할 때. (오른쪽으로 갈수록 범위가 큼, 왼쪽으로 갈수록 더욱 엄격함.)

  

# 2. 리스트

: mutable(-> <u>조작 시, 원본 데이터를 변경</u>), ordered (-> sequence)(인덱스로 접근 가능), iterable(순회 가능)

### 1. `.append(x)`

x 의 값을 리스트의 끝에 추가함.

### 2. `.extend(iterable)`

iterable 의 요소(항목)들을 리스트에 추가함.

- 연산자 '+='와 같게 동작한다.

- *주의*: 바로 값이 들어가는 게 아니라, iterable 객체를 이루는 요소들을 분해해서 추가한다.

  ```python
  >>> chocolate = ['ghana', 'hersheys', 'reeses']
  >>> chocolate.extend(['cadburys'])
  ['ghana', 'hersheys', 'reeses', 'cadburys']					# 리스트의 항목인 'cadburys'가 추가됨
  
  >>> chocolate = ['ghana', 'hersheys', 'reeses']
  >>> chocolate.extend('cadburys')
  >>> chocolate = ['ghana', 'hersheys', 'reeses',
                   'c', 'a', 'd', 'b', 'u', 'r', 'y', 's']	 # 'cadburys'의 각 항목인 각 문자가 추가됨
  ```

### 3. `insert(i, x)`

인덱스 i 에 값 x를 추가함.

i 값이 리스트 길이보다 큰 경우 (많이 커도), 맨 뒤에 추가됨 - 에러 발생 X

### 4. `.remove(x)`

값이 x인 첫 번째 항목을 삭제. (전체 항목이 아님에 주의!)

없는 경우, ValueError 발생.

### 5. `.pop(i)`

인덱스를 받아, 인덱스 i 위치의 값을 삭제하고 **+ 해당 항목을 반환함** (즉, 반환값을 변수에 할당하여 사용할 수 있음)

i 값이 주어지지 않고 `.pop()`로 쓰이면, 마지막 항목을 삭제하고 반환함.

### 6. `.clear()`

리스트의 모든 항목을 삭제함. (리스트 자체를 삭제하는 것은 아님)

### 7. `.index(x)`

첫 번째 x 값을 찾아 index 값을 반환.

없는 경우, ValueError 발생.

### 8. `.count(x)`

x값의 개수를 반환.

### 9. `.sort()`

원본 리스트를 정렬함. 반환값은 None.

> 참고: `sorted 함수` 👁‍🗨
>
> 1) `.sort()`는 리스트의 메서드, `sorted`는 내장함수
>
> 2) `.sort()`는 원본 리스트를 정렬함 (리스트는 mutable 객체이므로) : None을 반환
>
>    반면에, `sorted`는 iterable 객체의 정렬된 *복사본* 을 반환함: 새로운 객체를 반환

### 10. `.reverse()`

원본 리스트를 뒤집음 (정렬 X). 반환값은 None, 즉 복사본을 생성하지 않음.

### 11. 리스트의 복사

리스트의 복사는 같은 주소를 참조하게 된다. 즉, 복사본이나 원본 중 하나라도 변경하면 모든 객체에 변화가 일어난다. 이는 mutable 객체의 특징이다. (immutable한 객체는 변경할 수 없으므로 복사본이 서로 다른 객체를 참조하고, 변화도 각자의 객체에만 반영됨.) 

그렇다면, 다른 주소를 참조하게 하려면?

- slice를 사용하여 <u>연산된 결과</u>를 복사한다. (모양만 같고, 주소는 다르게)

- `list()`로 복사한다.

- *주의*: 이중 리스트일 때, 내부 리스트는 여전히 같은 객체를 참조하고 있다.

  -> *참고* : 깊은 복사(deep copy) 방법

  ```python
  import copy
  a = [1, 2, ['alice']]
  b = copy.deepcopy(a)
  ```

### 12. List comprehension

```python
[<expression> for <변수> in <iterable> if <조건식>]
```

- 리스트를 생성하는 방법 중 하나: [ ] 기호로 둘러쌈

- 한 줄로 씀

- 반복문이 여러 개면, 먼저 나오는 큰 범위의 for문을 먼저 작성하고, 뒤이어 다른 반복문도 작성함

  ```python
  # 기존
  odd_num = []
  for i in range(1, 5):
      if i % 2:
          odd_num.append(i)
  # list comprehension
  [x for x in range(1, 5) if x % 2]
  ```

### 13. `map(function, iterable)` 👁‍🗨

iterable의 각 항목에 function을 적용하고, 결과를 map object로 반환.

- map object는 리스트 형변환을 통해 결과를 직접 확인할 수 있다.

- 사용자가 직접 만든 함수도 적용할 수 있는, 확장성이 높은 함수이다.

  ```python
  >>> a, b = map(int, input().split())		# 입력값: 3 5
  3 5		# 각각 정수 형태가 됨
  ```

  

### 14. `filter(function, iterable)`

iterable 의 각 항목 중, function을 통과했을 때 True인 것들만 filter object로 반환.

***filter를 거친 결과가 아니라, iterable의 요소를 반환한다는 점!!***

~~(공식문서: function이 참을 돌려주는 iterable 의 요소들로 이터레이터를 구축합니다.)~~

- filter object도 리스트 형변환을 통해 결과를 직접 확인할 수 있다.

```python
>>> def odd(n):
        return n % 2
>>> data = [1, 2, 3, 4, 5]
>>> result = filter(odd, data)
>>> print(list(result))
[1, 3, 5]
```

### 15. `.zip(*iterables)`

복수의 iterable을 모아서 튜플을 원소로 하는 zip object를 반환.

- 각각의 요소를 순서가 맞는 것끼리 모아 튜플로 만든다.
- zip object도 리스트 형변환을 통해 결과를 직접 확인할 수 있다.

```python
>>> meal = ['breakfast', 'lunch', 'dinner']
>>> food = ['toast', 'rice', 'waffles']
>>> perfect_pair = zip(meal, food)
>>> print(list(perfect_pair))
[('breakfast', 'toast'), ('lunch', 'rice'), ('dinner', 'waffles')]
```



# 3. 세트

: mutable(-> <u>조작 시, 원본 데이터를 변경</u>), unordered(인덱스로 접근 X), iterable(순회 가능), 중복 없음

### 1. `.add(elem)`

세트에 값을 추가

- 세트는 순서가 없다는 점!

### 2. `.update(*others)`

여러 값을 추가

- *주의*: iterable 객체의 각 항목을 대입한다! (즉, 일반 문자열을 넣으면 각 문자를 추가한다.)

  참고: [파이썬 튜터 보기](http://pythontutor.com/visualize.html#code=taste%20%3D%20%7B'chocolate',%20'vanilla'%7D%0Ataste.update%28%5B'raspberry'%5D%29%0Ataste.update%28'yoghurt'%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) 👁‍🗨

### 3. `.remove(elem)`

세트에서 값 삭제. **없으면, KeyError 발생.**

### 4. `.discard(elem)`

세트에서 값 삭제. **없어도, 에러 발생하지 않음.**

### 5. `.pop()`

임의의 원소를 제거하고 **+ 반환함**

- 인자를 받지 않음 (unordered!)
- 세트가 비어 있는 경우, KeyError 발생

# 4. 딕셔너리

: mutable(-> <u>조작 시, 원본 데이터를 변경</u>), unordered(인덱스로 접근 X), iterable(순회 가능), Key-Value 쌍으로 이루어짐

### 1. `.get(key[, default])`

key에 대응하는 value를 가져옴 (`dict[key]`와 같음)

<u>key가 없어도 에러가 발생하지 않음</u> - default 값을 돌려줌 (기본: None)

### 2. `pop(key[, default])`

key가 딕셔너리에 있으면 제거하고 **+ 해당 값 반환**

key가 없으면 default를 반환. default 값도 없으면 KeyError.

### 3. `.update()`

값을 제공하는 key, value로 갱신 (기존에 존재하는 key는 덮어씀)

```python
mydict.update(apple="A+")
```

### 4. 딕셔너리 순회

딕셔너리는 기본적으로 key를 순회한다.

- 추가 메서드를 활용하여 순회할 수 있다:

  - `.keys()`: Key들

  - `.values()`: Value들

  - `.items()`: (Key, Value) 튜플로 구성된 결과

    (모두 리스트로 형변환하여 활용할 수 있다.)

    ```python
    >>> dessert = {'chocolate': 60, 'waffles': 80, 'coffee': 70}
    >>> print(dessert.keys())
    dict_keys(['chocolate', 'waffles', 'coffee'])
    >>> print(dessert.values())
    dict_values([60, 80, 70])
    >>> print(dessert.items())
    dict_items([('chocolate', 60), ('waffles', 80), ('coffee', 70)])
    
    # .items() 활용
    >>> for key, value i dessert.items():
    >>>     print(key, value)
    chocolate 60
    waffles 80
    coffee 70
    ```

### 5. Dictionary comprehension

```python
{key: value for <변수> in <iterable> if <조건식>}
```

- 조건식이 if-else 구조라면, 뒤가 아닌 앞에 붙게 된다.
