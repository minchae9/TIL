#### 작성자: 김민채

#### 날짜: 2021-07-22

#### 주제: 파이썬 에러/예외 처리 (Error/Exception Handling)

---

### 0. 디버깅

# 1. 에러

문법 에러(Syntax Error)를 가리킨다.

SyntaxError가 발생하면 프로그램은 실행이 되지 않는다.

- ```python
  while
  
  # SyntaxError: invalid syntax
  ```

- ```python
  3 = 1
  
  # SyntaxError: cannot assign to literal
  ```

- EOL (End of Line)

- EOF (End of File)

# 2. 예외(Exception)

문법 에러(Syntax Error)를 제외한 모든 에러를 가리킨다. 

즉, <u>문법적으로 틀린 게 없지만</u> 에러가 발생하는 경우이다.

- ZeroDivisionError

- NameError: namespace 상에 이름이 없는 경우

- TypeError

  ```python
  # 1) 타입 불일치
  >>> 1 + '1'
  >>> round('2.5')
  
  # 2) argument 누락
  >>> divmod()
      
  # 3) argument 개수 초과
  >>> divmod(1, 2, 3)
  
  # 4) argument type 불일치
  >>> import random
      random.sample(1, 2)		# "Population must be a sequence or set."
  ```

- ValueError

  ```python
  # 타입은 올바르지만, 값이 적절하지 않거나 없는 경우
  int('7.7')
  range(2).index(4)
  ```

- IndexError

  ```python
  # 인덱스가 존재하지 않거나, 범위를 벗어나는 경우
  two_list = [1, 2]
  two_list[5]
  ```

- KeyError

  ```python
  # 해당 키가 존재하지 않는 경우
  feelings = {'smiling': 'happy', 'crying': 'sad'}
  feelings['shouting']
  ```

- ModuleNotFoundError

  ```python
  # 존재하지 않는 모듈을 import 하는 경우
  import iamhappyhehe
  ```

- ImportError

  ```python
  # 모듈은 있으나, 존재하지 않는 클래스 또는 함수를 가져오는 경우
  from random import sampel
  ```

- KeyboardInterrupt: 임의로 프로그램을 종료했을 때

- IndentationError: indentation이 적절하지 않은 경우

# 3. 예외 처리 (handling exception)

**try문/except절을 이용한다.**

==장점==: 일반적으로 에러가 발생하면 프로그램이 멈추지만, 예외 처리를 통해 정상적으로 프로그램을 유지시키면서 다른 처리를 하게끔 할 수 있다.

```python
try:
    실행할 코드
except 에러이름 as 변수:		# 에러이름은 생략가능
    에러 발생 시 실행 코드
else:
    에러 발생하지 않을 시 실행 코드
finally:
    에러 발생과 무관하게 항상 실행할 코드
```

- except 절에서 예외이름은 생략이 가능하다. 생략한다면, 모든 예외에 대해 코드가 실행된다.

- except 절에 여러 개의 예외를 적고 싶다면 tuple로 적는다.

- except 절을 여러 개 두어 에러 별로 별도의 에러 처리를 할 수 있다.

  단, 위에서부터 한 줄씩 순차적으로 실행되므로, <u>작은 범위의 에러부터 작성해야 한다.</u>

- as 키워드를 사용하여 에러 메시지를 사용할 수 있다.

  ```python
  except IndexError as err:
      print(f'{err}, 오류가 발생했습니다.')	# 에러 메시지가 err에 들어가 출력됨
  ```

✔ `finally`를 사용하는 이유

try문이나 except절에서 `return`을 만나면, 함수가 종료된다.

이때, `finally`를 쓰면 return으로 종료되기 전에 "무조건" 실행시킬 수 있다.

무조건 실행된다는 것은, try 구문에 속하는 finally가 모두 끝난 다음에야 return으로 함수 전체가 종료된다는 것이다.

예)

```python
def first(a):
    try:
        result = int(a)
        return result
    except:
        return False
    finally:
        print(a)

print(first('3.5'))			  # '3.5'
							# False
        
def second(a):
    try:
        result = int(a)
        return result
    except:
        return False
    print(a)
       
print(first('3.5'))			  # False
```

# 4. 예외 발생시키기

* raise 문

  예외를 강제로 발생시킨다.

  ```python
  raise <표현식>(메시지)
  ```

  - <표현식>에 예외 타입을 지정한다 - 주어지지 않을 경우, 현재 스코프에서 활성화된 마지막 예외를 다시 일으킨다.

  ```python
  raise
  # RuntimeError
  # raise 만 적어도 됨
  
  raise ValueError('값 에러 발생')
  # ValueError: 값 에러 발생
  ```

  

* assert 문

  예외를 강제로 발생시킨다.

  ```python
  assert <표현식>, <메시지>
  ```

  - <표현식>이 False인 경우, AssertionError
  - 무조건 AssertionError를 발생시킴
  - 디버깅 용도로만 사용함

  ```python
  assert len([1, 2, 3]) == 4, '길이가 4가 아닙니다.'
  # AssertionError: 길이가 4가 아닙니다.
  ```

# 참고

### ==try문과 if문의 차이점==

## try

- (if 문과는 달리,) 코드를 밀고 나간다.

- EAFP(easier to ask for forgiveness than permission) 스타일

  즉, 실행부터 하고, 예외처리는 이후에 진행.

- Python의 철학은 이쪽에 더 가까움.

## if

- LBYL(look before you leap) 스타일

  즉, 검사부터 하고, 실행.
  
- 더 빠르다.

### 코드의 차이

```python
# try문
try:
    x = my_dict['key']

# if문
if 'key' in my_dict:
    x = my_dict['key']
```

('key'의 검색 횟수에도 차이가 있다.)