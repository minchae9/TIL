#0813

# 문자열(string)

## 1. 문자열

### 1) 컴퓨터에서의 문자 표현

컴퓨터에서의 문자 표현, 각 문자에 대응되는 숫자를 정하고 이를 사용하는 방법이 사용된다.

⇒ **ASCII 코드**

> 7-bit 인코딩으로 문자를 128 문자를 표현함
>
> : 33개의 출력 불가능한 제어문자(줄바꿈 등) + 95개의 출력 가능한 문자(32~126)

> ※ 참고: 확장 아스키 문자
>
> 1B내의 8-bit를 모두 활용하여 표준 문자 외에도 악센트, 도형, 특수문자 및 기호를 128개 추가할 수 있게 하는 부호.
>
> 컴퓨터 생산자 또는 개발자가 할당하여 사용하게 되므로 서로 다른 프로그램이나 컴퓨터 사이에 교환되지 못한다. (표준이 아님)

- 다국어 처리를 위해 새로운 표준이 필요하게 되었다.

⇒ **Unicode (유니코드)**

유니코드를 저장하는 바이트 순서는 표준화되지 못했기 때문에, 외부 인코딩이 필요하다.

- big-endian, little-endian ⇢ 어쨌든, 순서가 다르게 되어 있으면 서로 해석할 수 없다.

- 유니코드 인코딩 (UTF; Unicode Transformation Format)

  - UTF-8 (웹): 1byte 단위

    ㄴ Python 3버전 부터는 기본적으로 UTF-8 인코딩. 다른 인코딩 방식으로 처리할 때만 인코딩 방식을 지정해주면 된다.

    (첫 줄에, `#-*- coding: utf-8-*-` 따위를 적어주면 됨. )

  - UTF-16 (윈도우, 자바): 2byte 단위

  - UTF-32 (유닉스): 4byte 단위

    - UTF-8 과 UTF-16은 가변 길이, UTF-32는 4바이트 짜리

### 2) 문자열의 분류

- java: 가변 길이. 몇 글자인지 따로 관리함. 유니코드(UTF-16, 2byte)로 저장.

  ㄴ Python은 자바와 비슷하다.

- c언어: 널문자(`\0`)를 넣어서 문자열의 끝을 표시함. 아스키 코드로 저장.

#### Python에서의 문자열 처리

- 유니코드(UTF-8)로 저장.
- char 타입 없음
- 텍스트 데이터의 취급방법이 통일
- ', ", ''', """
- `+`: concatenation
- `*`: 반복

#### 

## 2. 패턴 매칭

> 긴 문자열 안에서 작은 문자열(패턴) 찾기

### 1) Brute-force

- 방법

  처음부터 끝까지 돌면서 패턴 내 문자와 일일이 비교한다. 틀리면 전체 문자열에서 탐색을 시작할 부분을 한 칸 뒤로 밀고, 패턴의 처음 부분부터 다시 비교한다.

- 최악의 경우, 시간 복잡도는 O(M*N)이 된다. (전체 문자열 길이 x 패턴 길이)

![Academic Stuffs: Brute Force(Naive) String Matching Algorithm](http://1.bp.blogspot.com/-YJDalyxz6XY/UFCYnd2_nBI/AAAAAAAAAB4/uewJpXgs9Mc/s1600/Brute+Force.jpg)

### 2)  KMP 알고리즘

- 방법

  접두사와 접미사 개념을 사용함. 패턴 문자열의 앞부분과 뒷부분이 같으면, 틀려서 문자열을 다시 비교해야 할 때 공통부분만큼은 뛰어넘을 수 있다.

- 시간 복잡도: 파이(n)

<img src="https://miro.medium.com/max/868/1*hGaxEHtNvfYJDxHeFV171g.png" alt="img" style="zoom:50%;" />

<img src="https://miro.medium.com/max/868/1*kPepYjAnJqlP495bjI0p8w.png" alt="img" style="zoom:50%;" />

### 

### 3) 보이어-무어 알고리즘

- 방법

  끝에서부터 비교 (오 → 왼).

  패턴의 문자가 불일치할 때,

  i) 해당 문자가 패턴 안에 있다면 일치하는 패턴 속 문자부터 비교함

  ii) 해당 문자가 패턴 안에 없다면, 패턴 길이 만큼 건너뜀

- 시간 복잡도: 파이(n)

<img src="https://slidetodoc.com/presentation_image_h2/3c67324f7a48362913f3b119694d967e/image-8.jpg" alt="Tuned Boyer Moore Algorithm Raita Algorithm Horspool Algorithm" style="zoom:67%;" />



## 3. 문자열 암호화

- 시저 암호 (Caesar cipher)

  알파벳을 일정 수만큼 평행이동함으로써 암호화하는 방법

- 단일 치환 암호

  각 문자마다 대응되는 문자를 정해둔 문자 변환표를 이용하여 암호화하는 방법

- bit 열의 암호화

  XOR 연산 이용 - 1과 대응시키면 반전된다.

  두 번 적용하면 해독 된다. 



