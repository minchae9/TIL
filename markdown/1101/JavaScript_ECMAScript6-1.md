# ECMAScript 6 📑: Intro, 변수·식별자, 데이터 타입, 연산자

ECMA는 정보 통신에 대한 표준을 정하는 기구인데, 여기서 JavaScript에 대해 정한 6번째 표준 명세를 "ECMAScript 6" 라고 한다.

## 0. Introduction

#### 세미콜론(;)

👉 선택적으로 사용한다.

구문의 끝에 삽입해야 한다는 주장과 그러지 않아도 된다는 주장이 서로 대립하고 있는데, JavaScript에서는 세미콜론을 삽입하지 않으면 ASI(자동 세미콜론 삽입 규칙)에 의해 자동으로 삽입해준다.

## 1. 변수와 식별자

### 1) 식별자

> **식별자(Identifier)**
>
> 변수를 구분할 수 있는 변수명

- **문자, 달러 기호($), 또는 밑줄(_)**로 시작해야 한다.
- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작한다.

#### 식별자 작성 스타일

- 카멜 케이스(camelCase): 변수, 객체, 함수
- 파스칼 케이스(PascalCase): 클래스, 생성자
- 대문자 스네이크 케이스(SNAKE_CASE): 상수

### 2) 변수

#### 변수 선언 키워드: const, let

> **const**
>
> ```javascript
> const number = 10
> // number = 10 : 재할당 불가
> // const number = 5 : 재선언 불가
> ```
>
> - 재할당 X
> - 재선언 X
> - 블록 스코프

> **let**
>
> ```javascript
> let number = 10
> number = 10 	// 재할당 가능
> // let number = 5 : 재선언 불가
> ```
>
> - 재할당 O
> - 재선언 X
> - 블록 스코프

※ 참고

- *선언* : 변수를 생성
- *할당* : 선언된 변수에 값을 저장
- *초기화* : 선언된 변수에 '처음으로' 값을 저장
- *블록 스코프* : **if문, for문, 함수 등**의 <u>중괄호 내부</u>. 블록 스코프를 가지는 변수는 <span style="color:red;">블록 바깥에서 접근 불가.</span>

##### 변수 선언 키워드: var

> **var**
>
> <span style="color: blue;">호이스팅 문제 때문에 사용을 권장하지 않음.</span>
>
> - 재할당 O
>
> - 재선언 O
>
> - 함수 스코프 (if문과 for문에서는 자유로움)
>
> - *호이스팅(hoisting)* 특성
>
>   : 변수를 선언하기 전에 참조할 수 있는 현상 - undefined를 반환한다.
>
>   (const나 let은 'Uncaught ReferenceError'를 반환한다.)
>
>   ```javascript
>   console.log(username)	// undefined
>   var username = '아무개'
>   ```
>
>   

※ 참고

- *함수 스코프* : **함수**의 중괄호 내부 (if문, for문에서는 자유로움).  <span style="color:red;">함수 바깥에서 접근 불가.</span>

![image-20211101195321916](JavaScript_ECMAScript6.assets/image-20211101195321916.png)

<br/>

## 2. 데이터 타입

![image-20211101195411800](JavaScript_ECMAScript6.assets/image-20211101195411800.png)

​                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

JavaScript의 모든 값은 *원시 타입* 과 *참조 타입* 으로 분류된다.

### 참조 타입 (Reference type)

> - 객체(object) 타입
> - 변수에 해당 객체의 **참조값**이 담김
> - 실제 값이 아닌, 참조 값이 복사됨

- 종류: 함수(function), 배열(array), 객체(object)

<br/>

### 원시 타입 (Primitive type)

> - 객체(object) 가 아닌, 기본 타입
> - 변수에 해당 타입의 **실제 값**이 직접 담김
> - 실제 값이 복사됨

- #### 숫자(number) 타입

  - 정수와 실수 구분 없음
  - 부동소수점 형식을 따름
  - (참고) **NaN**: 계산이 불가능한 경우 반환됨

- #### 문자열(string) 타입

  - 텍스트 데이터

  - 작은 따옴표(' ')와 큰 따옴표(" ") 모두 OK

  - **템플릿 리터럴 (Template Literal)**

    > (파이썬의 f-string 이랑 유사한 것)
    >
    > - (따옴표 대신) backtick (`)
    > - 변수는 *${expression}* 형태로 씀 ($ 기호와 중괄호)

- #### undefined 타입

  - 변수의 **값이 없음**을 나타냄 (**자동**으로 부여되는 값)
  - 변수 선언 이후, 직접 값을 할당하지 않으면 자동으로 undefined가 할당된다.

- #### null 타입

  - 변수의 **값이 없음을 의도적으로 표현**할 때
  - typeof 연산자(자료형 평가 연산자)로 null 타입을 따지면, 결과는 <u>객체(object)</u>이다. ❗

- #### Boolean 타입

  - 논리적 참 또는 거짓을 나타냄
  - true 또는 false

#### [참고] 자동 형변환 정리

![image-20211101201318044](JavaScript_ECMAScript6.assets/image-20211101201318044.png)

<br/>

## 3. 연산자

- 할당 연산자: `=`

  : 오른쪽 값을 왼쪽 피연산자에 할당

  - Increment 연산자: `++`

    피연산자의 값을 1 증가시킴

  - Decrement 연산자: `--`

    피연산자의 값을 1 감소시킴

  - `+=`, `-=` 로도 적을 수 있다.

- 비교 연산자: `<`, `>`

  - 결과값: Boolean
  - 문자열은 유니코드 값을 사용하여 비교
    - 알파벳 순서상 후순위가 더 큼
    - 소문자가 대문자보다 더 큼

- 동등 비교 연산자: `==`

  같은 값이기만 하면 true를 반환

  → 예상치 못한 결과가 발생할 수 있으므로 사용을 권장하지 않음❗

  ```javascript
  const a = 1004
  const b = '1004'
  console.log(a == b)	// true
  console.log(a + b) // 10041004 👽 자동 형변환 일어남
  
  const c = 1
  const d = true
  console.log(c == d)	// true
  console.log(c + d) // 2 👽 자동 형변환 일어남
  ```

- 일치 비교 연산자: `===`

  타입과 값이 모두 같은지 비교하여 boolean 값을 반환

  (피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별한다.)

  - <u>자동 형변환이 일어나지 않음</u>

  → 이걸 사용한다 ✔

- 논리 연산자: `&&`, `||`, `!`

  - 각각 and, or, not에 해당
  - 단축 평가를 지원한다.

- 삼항 연산자: `조건식 ? 참인경우 : 거짓인경우`

---



