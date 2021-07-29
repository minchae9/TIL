#0729

# 0. 객체지향 프로그래밍(OOP)

> **컴퓨터 프로그래밍의 패러다임의 하나로, 컴퓨터 프로그램을 명령어의 목록으로 바라보는 시각에서 벗어나, 상호작용하는 독립적인 객체들의 집합으로 파악하고자 한다.**

<br/>

### 1. 절차지향 프로그래밍 vs 객체지향 프로그래밍

- 절차 지향: 함수 호출을 통해 코드의 추상화와 재사용성을 얻어낸다. 함수가 주체로 기능함.
- 객체 지향: 데이터와 기능(메서드)을 각각의 객체로 분리하고, 데이터 객체가 메서드를 호출함으로써 기능을 사용함. 추상화된 구조(인터페이스)

#### ※ OOP의 느낌 잡기

```python
# 1
lower('Hi')
# 2 (✔)
'Hi'.lower()
```

첫 번째 방식은 *함수* 가 *데이터 객체* 를 처리하는 거라면, 두 번째 방식은 *데이터 객체* 가 *메서드* 를 호출해 내는 것에 가깝다고 볼 수 있다.

<br/>

### 2. 객체지향 프로그래밍의 이유

***현실세계를 프로그램 설계에 반영하기 위해 !***(추상화)

<br/>

### ※ 객체지향 프로그래밍의 기본 기법 💭 

<u>추상화, 상속, 캡슐화, 다형성</u>

(파이썬은 객체지향 프로그래밍 구현이 유리한 객체지향 언어. ~~다만, 파이썬은 캡슐화와 다형성 부분이 약하다고 함.~~)

<br/>

---

# 1. 객체(object)

>  ***파이썬은 모두 객체로 이루어져 있다.* **💬

>  ***객체는 특정 타입(type)의 인스턴스(instance)이다.* **💬
>
> — 참고: 모든 클래스는 메타클래스 type의 인스턴스이다.

- 특징

  **타입**, **속성**, 그리고 **메서드**를 지닌다.

  - 타입(type): 어울릴 수 있는 연산자(operator)가 구분됨

  - 속성(attribute): 상태/데이터

    ㄴ 변수 ❕

  - 조작법(method): 행위/함수

    ㄴ 메서드 ❕

### ▷ 타입(type)

▸ 연산자

- `is` 연산자

  ```python
  type(3) is int	#True
  ```

  객체의 아이덴티티를 검사한다.

- `isinstance` 연산자

  `isinstance(object, classinfo)`로 쓰여, object가 classinfo의 i) 인스턴스이거나, ii) 자식클래스(subclass)면 True.

  - classinfo가 튜플인 경우, 하나라도 일치하면 True
  - classinfo의 부모 클래스가 있는 경우, object가 classinfo의 인스턴스이면 그 부모 클래스의 인스턴스이기도 하다.

### ▷ 속성(attribute)

```python
<object>.<attribute>
```

- 속성은 뒤에 ()가 붙지 않음
- 클래스의 인스턴스 메서드에서 정의될 때, 변수로 정의됨

### ▷ 메서드(method)

```python
<object>.<method>()
```

- 메서드는 뒤에 ()가 붙어 사용되며, 필요 시 인자가 들어감
- 일반적으로 클래스 내에서 정의된 함수
- `dir(list)` 처럼, `dir()` 안에 타입을 입력하면, 해당 타입의 속성과 메서드를 볼 수 있음

<br/>

---

# 2. 클래스 & 인스턴스

*클래스는 집짓기를 위한 청사진, 인스턴스는 실제 집*

```python
class Person:						# 클래스
    population = 0					# 클래스 변수
    
    def __init__(self, name, age):	# 생성자 함수
        self.name = name			
        self.age = age
        Person.population += 1
        
    def __del__(self):				# 소멸자 함수
        Person.population -= 1
        
    def introduce(self):
        print(f'I am {self.name}. I am {self.age}. Nice to meet you.')
    
    def sing(self):
    	print('lalala~~')
    
   	@classmethod					# 클래스 메서드
	def get_population(cls):
        print(f'Total population is: {cls.population}')
        return cls.population
    
    @staticmethod					# 스태틱(정적) 메서드
    def yourinput(arg):
        return f'You just typed {arg}'
    
 
# 인스턴스 생성
p1 = Person('Emily', 36)
# 인스턴스 속성
p1.name		# Emily
p1.age		# 36
# 인스턴스 메서드
p1.introduce()	# I am Emily. I am 36. Nice to meet you.
p1.sing()		# lalala~~
# 클래스 메서드
Person.get_population()	# Total population is: 1
# 스태틱 메서드
Person.yourinput('hehe')	# You just typed hehe
# 소멸자 함수 사용
del p1
```



## 클래스(class)

- 객체들의 추상화된 분류.

- 클래스를 정의하고, 이를 기반으로 인스턴스라는 객체를 만든다.

- 클래스의 이름엔 Pascal case가 적용된다: 어절 단위의 첫 글자를 대문자로 함

  

  ### ▸ 클래스 변수

  클래스에 있는 변수(속성)

  - 클래스 안, 인스턴스 메서드 밖에서 선언한다.
  - 특정 인스턴스에 묶여있지 않다.

  - 클래스 변수는 모든 인스턴스가 공유한다. (인스턴스도 클래스 변수에 접근할 수 있다.)

    (단, 클래스는 인스턴스 변수에 접근이 불가능하다 - 이름공간 규칙(MRO))

  

  ### ▸ 생성자 함수(`__init__`)

  인스턴스 객체가 생성될 때 호출되는 메서드

  

  ### ▸ 소멸자 함수(`__del__`)

  인스턴스 객체가 소멸되기 직전에 호출되는 메서드

  - 인스턴스 객체의 소멸은 `del` 키워드를 통해 이루어진다.

    

  ### ※ 매직 메서드

  - 더블 언더스코어('__') (또는 "던더스코어")가 있는 메서드로, 특수한 동작을 위한 메서드이다.

  - (예)

    ```python
    __str__(self), __len(self)__, __repr(self)__
    __lt__(self, other), __le__(self, other), __eq__(self, other)
    __gt__(self, other), __ge__(self, other), __ne__(self, other)
    ```

    - `__str__(self)`: 해당 객체의 출력 형태(informal)를 지정한다.

      ```python
      class Person:
          def __init__(self, name):
              self.name = name
          
          def __str__(self):
              return f'나는 {self.name}'
      #    
      p2 = Person('mary')
      print(p2)	# 나는 mary
      ```

    - `__repr__(self)`: 해당 객체의 공식적인(official) 문자열 출력 형태를 계산한다.

    - lt(less than), le(less or equal), eq(equal), gt(greater than), ge(greater or equal), ne(not equal)

      ▻ 작동방식

      > The correspondence between operator symbols and method names is as follows: 
      >
      > `x<y` calls `x.__lt__(y)`, `x<=y` calls `x.__le__(y)`, `x==y` calls `x.__eq__(y)`, 
      >
      > `x!=y` calls `x.__ne__(y)`, `x>y` calls `x.__gt__(y)`, and `x>=y` calls `x.__ge__(y)`.
      >
      > (출처: [Python Documentation](https://docs.python.org/3/reference/datamodel.html?highlight=__gt__#object.__gt__))

      

<br/>

## 인스턴스(instance)

- 클래스로 만들어진 하나하나의 실체

  

  ### ▸ self

  인스턴스 자기자신

  

  ### ▸ 인스턴스 속성

  클래스의 생성자 함수(`__init__`)에 정의된 변수

  특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미한다.

  - 항상 특정한 인스턴스에 묶여있다.

  - 메서드에서 `self.<name>`으로 정의된다.
  - 인스턴스가 생성된 이후, `<instance>.<name>`으로 접근·할당된다.

  

  ### ▸ 인스턴스 메서드

  인스턴스가 할 수 있는 행동

  특정 데이터 타입/클래스의 객체들에 공통적으로 적용 가능한 행위를 의미한다.

  - **첫 번째 인자로 self를 가진다  *(꼭❗)***

    `<인스턴스>.메서드`로 호출함은, 메서드의 첫 번째 매개변수로 인스턴스를 전해주는 것과 같다.

    예) `'apple'.capitalize()`의 실제 구조는 `str.capitalize('apple')`

    (`<class>.<instance method>(<instance>)` 는 `<instance>.<instance method>()`와 같다.)

<br/>



## 메서드(method)

### 1) 인스턴스 메서드

<u>인스턴스</u>가 사용할 메서드

- 첫 번째 인자로 self(인스턴스)를 전달한다.

### 2) 클래스 메서드

<u>클래스</u>가 사용할 메서드

- 함수 위에 `@classmethod`라고 데코레이터(decorator)가 붙음

  (* *데코레이터* : 함수를 꾸며주는 함수)

- 첫 번째 인자로 cls(클래스)를 전달한다.

- 클래스의 변수(속성) 등을 변경하는 역할 등을 한다. 

### 3) 스태틱 메서드 (정적 메서드)

<u>클래스</u>가 사용할 메서드

- 함수 위에 `@staticmethod`라고 데코레이터가 붙음

- 인자로 `self`나 `cls`가 전달되지 않음 - 일반 함수처럼 작성이 됨

  → 즉, 클래스 정보에 접근·수정이 불가하다.

  → 객체지향과 절차지향의 사이를 연결하는 역할을 하기도 한다.

#### ※ 주의점

- 인스턴스에서 클래스 메서드와 스태틱 메서드를 호출할 수 있지만, 그러지 않는다.

  애초에 역할/목적을 나누어 작성한 것이므로, 그것을 따른다.

  <br/>

▢ 참고: MRO(Method Resolution Principle)

- 인스턴스에서 특정 속성에 접근하면, 인스턴스 - 클래스 - 부모 클래스 순으로 탐색한다.

  → 클래스의 속성을 참조하고 있다가, 동일한 이름의 속성을 인스턴스에서 정의하면 더이상 클래스의 속성을 참조할 수 없게 된다.

  

---

# 3. 상속

모든 파이썬 클래스는 object를 상속받고 있으며, 상속을 통해 객체 간 관계가 구축된다.

**상속의 장점**

- 부모 클래스의 속성, 메서드가 자식 클래스에 상속되므로, 코드 재사용성이 높아진다.
- 유지보수가 용이하다.

**연산자**

- `isinstance(object, classinfo)`: object가 classinfo의 인스턴스이거나, 자식 클래스인 경우 True

- `issubclass(class, classinfo)`: class가 classinfo의 자식 클래스인 경우 True

  ㄴ classinfo가 튜플로 주어진 경우, 하나라도 True면 True 를 반환함

#### `super()`

- 자식 클래스에서 부모 클래스의 생성자 함수(`__init__`)나 메서드 등을 사용하고 싶은 경우, `super()`을 이용해서 들고 올 수 있다.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Student(Person):
    def __init__(self, name, age, birthday, school):
        super().__init__(name, age)		# <---
        self.birthday = birthday
        self.school = school
```



**메서드 오버라이딩(method overriding)**

부모 클래스로부터 상속받은 메서드를 자식 클래스에서 재정의하는 것

- 같은 이름의 메서드로 덮어쓴다.

```python
class Person:
    def talk(self):
        print('호호호 안녕하세요?')
        
class Child(Person):
    def talk(self):
        print('안녕하세요? 오늘 날씨가 좋네요.')
```

(※참고: 메서드 오버로딩(method overloading)

하나의 클래스 내에서 (주로 파라미터의 개수/종류만 바꿔서) 같은 이름의 함수를 여러 개 정의하는 것.

즉, 같은 이름의 메서드인데, 다르게 동작한다.)



**다중상속**

둘 이상의 클래스로부터 상속을 받는 것.

이름공간을 탐색할 때, 작성된 순서대로 탐색한다.

```python
def Child(Mom, Dad):		# <-- Child 클래스에 없으면, Mom 클래스, 그다음 Dad 클래스 순
    pass
```



<br/>

---

### ▢  참고: `==` 와 `is`

- `==`: 내용이 같음 ("동등함")
- `is`: 동일한 객체를 가리킴 ("동일함")









 



