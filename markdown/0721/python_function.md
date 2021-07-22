#### 작성자: 김민채

#### 날짜: 2021-07-21

#### 주제: 파이썬 기초 (2)

---

# 0. 함수의 기초

1. 함수란?

   > 특정한 기능을 수행하는 코드 조각(묶음)

   - 높은 재사용성: 같은 함수를 여러 상황에서 호출하여 사용할 수 있음
   - 유지보수의 용이함: 수정이 쉬움

* 함수의 구성요소

  함수의 이름, 매개변수(parameters), 바디(body): docstring과 code, 반환값(return)
  ```python
  def 함수이름(매개변수):
      """docstring
      """
      코드셋
      return 반환값
  ```

  - **def** 키워드

    : 함수를 선언

  - **Docstring** (Documentation String)

    : 함수나 클래스에 대한 설명. (선택적으로 작성)

    * """ """ 의 문자열로 작성한다.
    * `함수명.__doc__`로 볼 수 있다. ~~("매직메소드")~~

  - **매개변수(parameters)**

    :  함수에 입력으로 전달된 값을 받는 변수 (함수가 선언될 때 작성됨)

    > ※ 참고
    >
    > **인자(arguments)**: 함수를 호출할 때 함수에 전달하는 입력값

  - **return**

    : ==_**하나**_== 의 객체를 반환하며, 함수가 종료됨

  - 함수의 호출: `함수명()`

    > <u>※주의: 선언과 호출 구분하기!</u>

---

# 1. 함수의 output

<u>함수는 **반드시 _"하나"_ 의 객체를 _"반환"_** 한다.</u>

- 복수의 값을 출력하는 경우? => 사실은 <u>1개의 튜플!</u>

  ```python
  >>> def two(a, b):
          return a + b, a - b
  >>> print(two(2, 1))
  (3, 1)
  >>> print(type(two(2, 1)))
  <class 'tuple'>
  ```

- 명시적인 반환값이 없는 경우? => <u>None을 반환하고 있다!</u>

  ```python
  >>> def hello():
      	print('hello')
  >>> print(hello())
  hello
  >>> print(type(hello()))
  <class 'NoneType'>
  ```

---

# 2. 함수의 input

1. 위치 인자(Positional Arguments)

   기본적으로 인자는 위치에 따라 함수에 전달된다.

   ```python
   >>> def plus(a, b):
           return a + b
   >>> plus(1, 2)		# a에 1, b에 2가 전달됨
   ```

2. 기본 인자 값(Default Arguments Values)

   인자에 기본값을 지정하여, 정의된 것보다 더 적은 개수의 인자로도 호출될 수 있으며 이때 기본값이 사용된다.

   ```python
   >>> def plus(a, b=0):
           return a + b
   >>> plus(1)			# a에 1이 전달되고, b에 기본값 0이 사용됨
   ```

3. 키워드 인자(Keyword Arguments)

   변수를 직접 지정하여 인자를 전달할 수 있다.

   **단, '키워드 인자'를 '위치 인자'보다 앞에 사용할 수 없다.**

   ```python
   >>> def plus(a, b):
           return a + b
   >>> plus(b=1, a=2)		# 위치가 뒤바뀌었음에도, a에 2, b에 1이 전달됨
   >>> plus(a=2, 1)		# (X)
   ```

***

### 정해지지 않은 수의 인자를 처리하는 방법

4. 가변 인자 리스트(Arbitrary Argument Lists)

   함수가 <u>임의의 개수의 인자</u>로 호출될 수 있도록 지정하는 것으로, 매개변수에 ***(asterisk)**를 붙여 표현한다.

   이는 함수가 받을 수 있는 인자의 개수를 유연하게 만든 것이다. 인자들은 **tuple로 묶여(packing) 처리**된다.

   가변 인자 리스트는 `*args`로 표시하는 것이 관습이다.

   ```python
   >>> def make(*args):
           for arg in args:
               print(arg)
   >>> add(2)				# 인자를 1개 전달해도 되고,
   >>> add(1, 2, 3, 4)		 # 인자를 여러 개 전달할 수도 있음 - 튜플로 묶여 처리됨
   ```

5. 가변 키워드 인자(Arbitrary Keyword Arguments)

   함수가 <u>임의의 개수의 키워드 인자</u>로 호출될 수 있도록 지정하는 것으로, 매개변수에 ******를 붙여 표현한다.

   인자들은 **dictionary로 묶여(packing) 처리**된다.

   가변 키워드 인자는 `*kwargs`로 표시하는 것이 관습이다.

   ```python
   >>> def members(**kwargs):
           for key, value in kwargs:
               print(key, ":", value)
   >>> members(num1='유재석', num2='지석진', num3='송지효', num4='김종국')
   ```

**※ 주의사항**

1. '기본 인자 값'은 '위치 인자'보다 앞에 정의될 수 없다.
   - 매개변수보다 적은 개수의 인자로 호출됐을 때, 기본값이 있는 매개변수에 인자가 전달되어 기본값이 없는 매개변수에는 인자가 전달되지 않는다.
2. '키워드 인자'는 '위치 인자'보다 앞에 정의될 수 없다.
3. '가변 인자 리스트'와 '가변 키워드 인자'도 '위치 인자'보다 앞에 정의될 수 없다.
   - 위치 인자가 앞에 위치해 있으면, 전달되고 남은 부분을 모두 가변 인자에 전달하면 되지만, 가변 인자가 앞에 위치해 있을 경우 어디까지 가변인자에 전달할 지 알 수 없게 된다.

=> 인자 순서: **위치 인자 - (기본 인자 값, 키워드 인자) - 가변 인자 리스트 - 가변 키워드 인자**

---

# 3. 함수 scope

0. 스코프와 변수

   - 빌트인 스코프(built-in scope): 파이썬 공간

   - 전역 스코프(global scope): 코드 어디에서든 참조할 수 있는 공간

     - 전역 변수(global variable): 전역 스코프에 정의된 변수

   - 지역 스코프(local scope): 함수가 만든 스코프. 함수 내부에서만 참조할 수 있음.

     - 지역 변수(local variable): 지역 스코프에 정의된 변수

       

1. 변수의 수명주기(lifecycle)

   - Built-in scope

     -> 파이썬 실행 이후로 영원히 유지

   - Global scope

     -> 모듈이 호출된 (`import 모듈`) 시점 이후, 또는 인터프리터가 끝날 때까지 유지

   - Local scope

     -> 함수가 호출될 때 생성되어, 함수가 종료될 때까지 유지

     

2. 이름 검색 규칙(Name Resolution): **LEGB Rule**

   파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장이 되어 있고, 이름이 사용될 때 다음과 같은 순서로 이름을 찾아나간다:

   => _작은 곳에서 큰 곳으로!_ 	<u>(바깥에서 안으로는 절대 못 찾음!)</u>

   => _함수 내에서 바깥 스코프에 접근 O, 수정 X_

   **L**ocal scope(함수 내) -> **E**nclosed scope(상위 함수) -> **G**lobal scope(함수 밖 변수, import 모듈) -> **B**uilt-in scope(파이썬의 내장함수 또는 속성)

   

   => 이를 통해 <u>예약어를 식별자로 사용해서는 안 되는 이유</u>를 설명할 수 있다. 

   예약어로 식별자를 사용하여 global scope에서 선언하면, 이후에 예약어를 사용하려 할 때에 built-in scope에 있는 원래 기능을 찾기 전에 global scope에서 선언된 변수를 찾아버리기 때문에 예약어로 실행되지 않게 된다.

   

3. 예외를 만드는 방법: global, nonlocal

   변수 앞에 붙여서 사용한다.

   * ==주의사항==
     1) global/nonlocal에 나열된 이름은, 같은 코드 블록에서 선언되기 이전에 참조(등장)될 수 없다.
     2) global/nonlocal에 나열된 이름은 매개변수, for 루프 대상, 클래스나 함수 정의 등으로 정의되지 않아야 한다.

   (1) global

   해당 식별자가 전역 변수임을 나타낸다. 즉, local scope 안에서 이 global a를 쓰겠다고 말하는 것.

   기존에 존재하는 이름이 아니어도 사용할 수 있다.

   ```python
   a = 5
   def this():
       global a
       a = 8
   
   print(a)		# 5
   this()			# 함수 호출 후,
   print(a)		# 8
   ```

   Local scope에서 global 변수 a가 8로 변경되었다. Global 변수의 변화는  global scope에도 적용이 된다.

   

   (2) nonlocal

   전역(global scope)을 제외하고 가장 가까운 (둘러 싸고 있는) 스코프의 변수를 연결하도록 한다.

   이미 존재하는 이름과의 연결만 가능하다.

   ```python
   x = 0
   def this():
       x = 1
       def that():
           nonlocal x	# Enclosed scope(this)의 변수 x에 연결
           x = 2		# this()의 변수 x의 변경
       that()
       print(x)
      
   this()
   print(x)
   ```

* 참고
  * 특수한 상황이 아니라면, 사용하지 않는다.
  * 함수 내에서 필요한 상위 스코프의 변수는 인자로 넘겨서 활용한다. (return값을 받아서 사용하라.)

---

# 4. 재귀 함수

**재귀함수(recursive function)**

> - 자기 자신을 호출하는 함수
> - 하나 이상의 base case(종료되는 상황)을 만들고, 이로 수렴하도록 작성한다.
> - 큰 문제를 작은 문제로 나누어 해결책을 찾도록 하는 방법

* 사용하는 이유:
  * 알고리즘을 잘 나타낼 수 있는 경우가 있다.
  * 변수의 사용을 줄일 수 있다.
  * 가독성이 높다.
* 단점: 함수를 계속 호출하므로, 깊이가 깊어질수록 오래 걸릴 수 있다.
* 주의사항
  1. base case에 도달할 때까지 함수가 계속 호출된다 -> <u>base case 필수 작성!</u>
  2. 파이썬에서 재귀 함수의 최대 깊이는 1,000번으로, 이를 넘어가면 RecursionError가 발생한다.

* _예시 1) 팩토리얼_

  1! = 1

  2! = 1 * 2 = 2 * 1!

  3! = 1 * 2 * 3 = 3 * 2!

  4! = 1 * 2 * 3 * 4 = 4 * 3!

  ...

  n! = 1 * 2 * 3 * ... * (n-1) * n = n * (n-1)!

  즉, n의 팩토리얼은 (n-1)의 팩토리얼을 참조하여 구할 수 있다.

  ```python
  def fact(n):
      if n == 1:
          return n	# base case
      else:
          return n * fact(n - 1)
  ```

  

* _예시 2) 피보나치 수열_

  1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

  어떤 항의 값은 앞의 두 항을 합한 값이다.

  즉, n번째 (n > 2) 항의 값은 (n - 1)번째 항과 (n - 2)번째 항을 참조하여 구할 수 있다.

  ```python
  def fibo(n):
      a, b = 1, 1
      if n < 3:
          return 1		# base case
      for i in range(1, n - 1):
          a, b = b, a + b
      return b
  ```

  

