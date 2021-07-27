#0727

# 모음 제거하기

### List comprehension 활용

> 다음의 문장에서 모음(a, e, i , o, u)를 모두 제거하세요.
>
> **[입력 예시]**
>
> ```python
> words = 'Life is too short, you need python!'
> ```
>
> ------
>
> **[출력 예시]**
>
> ```
> Lf s t shrt, y nd pythn!
> ```

#### 1. 반복문 활용하기

```python
# 내 풀이 - 1
result = []
for word in words:
    for vowel in vowels:
        word = word.replace(vowel, '')
    result.append(word)
print(''.join(result))

# 내 풀이 - 2
for vowel in vowels:
    words = words.replace(vowel, '')
result = words
print(''.join(result))

# 선생님 풀이
result = []
for x in words:
    if x not in vowels:
        result.append(x)
print(''.join(result))    # words에서 문자열로 나뉜 공백도 vowels에 속하지 않기 때문에 추가됨
```

#### 2. List comprehension 활용하기 ✔

```python
# 선생님 풀이
result = [x for x in words if x not in vowels]
print(''.join(result))
```

##### 어려웠던 부분

'1. 반복문 활용하기'는 해냈는데, 반복문을 그대로 list comprehension으로 옮기려니 잘 되지 않았다. 그래서 다른 형태의 반복문을 만들어보려고 했으나, list comprehension에 바로 적용할 수 있는 풀이를 찾지 못하고 있었다.

---

# 딕셔너리 구축하기 (counter)

### dict[key], count 메서드, get 메서드

> 리스트가 주어질 때, 각각의 요소의 개수를 value 값으로 갖는 딕셔너리를 만드세요.
>
> **[입력 예시]**
>
> ```python
> book_title =  ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']
> ```
>
> **[출력 예시]**
>
> ```python
> {'great': 2, 'expectations': 1, 'the': 2, 'adventures': 2, 'of': 2, 'sherlock': 1, 'holmes': 1, 'gasby': 1, 'hamlet': 1, 'huckleberry': 1, 'fin': 1}
> ```

#### 1. dict[key]로 접근하는 방법 ✔

```python
# 선생님 풀이
title_counter = {}
for title in book_title:
    if title in title_counter:
        title_counter[title] += 1
    else:
        title_counter[title] = 1
        
print(title_counter)
```

#### 2. count 메서드를 활용하는 방법

```python
# 내 풀이
howmany = {}
for title in book_title:
    howmany[title] = book_title.count(title)
print(howmany)
```

#### 3. get 메서드를 활용하는 방법 ✔

```python
# 선생님 풀이
title_count = {}
for title in book_title:
    title_count[title] = title_count.get(title, 0) + 1
print(title_count)
```



##### 어려웠던 부분

(1) *'dict[key]로 접근하는 방법'* 에서 value 값을 증가시키는 방법을 떠올리기는 했지만, 실제로 작성하지는 못했다.

`for title in book_title:`이라는 반복 구문을 중복 작성함으로써 구현하려고 했는데, 방향을 잘못 잡았던 것 같다. 오히려 코드가 더 복잡해지고 내가 의도한 바를 표현하지 못했다.

(2) *'get 메서드를 활용하는 방법'* 에서, get 메서드가 key로 value 값을 가져다주고 상응하는 key가 없을 때에도 오류를 발생시키지 않는다는 특징을 알고 있었지만, 어떻게 사용하라는 건지 문제 의도를 파악하지 못했다. 그래서 (1)번과 풀이 방법의 차별화를 어떻게 해야 할지 잘 몰랐다. 선생님의 풀이는, get 메서드의 default 값으로 0을 설정함으로서 초기에 key-value 쌍을 추가할 때 (에러 없이) value 값이 0이 되도록 하고, 이후 1씩 늘어나게 하는 방법이었다. get 메서드의 디폴트 값을 그렇게 활용할 수 있다는 점이 새로웠다.

---

# Dictionary comprehension + 조건

### 조건문에 참인 식으로 딕셔너리 생성하기

> **입력값**
>
> ```python
> dusts = {'서울': 72, '인천': 82, '제주': 29, '동해': 45}
> ```

#### 1. 미세먼지 농도가 80 초과인 지역과 값을 가진 딕셔너리 생성

```python
result = {key: value for key, value in dusts.items() if value > 80}
print(result)	# {'인천': 82}
```

#### 2. 미세먼지 농도가 80 초과는 '나쁨', 80 이하는 '보통'으로 하는 value를 가지는 딕셔너리 생성 ✔

```python
result = {key: ('나쁨' if value > 80 else '보통') for key, value in dusts.items()}
print(result)	# {'서울': '보통', '인천': '나쁨', '제주': '보통', '동해': '보통'}
```

<u>=> value 자리에 if 문을 삼항연산자로 작성한다 (특정한 값 대신에, 하나의 값으로 수렴하는 표현식을 넣음)</u>

#### 3. 미세먼지 농도가 150 초과는 '매우나쁨', 80 초과는 '나쁨', 30 초과는 '보통', 30 이하는 '좋음'으로 하는 value를 가지는 딕셔너리 생성 ✔

```python
result = {key: ('매우나쁨' if value > 150 else '나쁨' if value > 80 else '보통' if value > 30 else '좋음') for key, value in dusts.items()}
print(result)
```

=> <u> `<True일 때 값 (1) > if <표현식 (1) > else <True일 때 값 (2)> if <표현식 (2)> else <False일 때 값 (2)>`의 형태</u>로, 앞에서부터 순차적으로 조건식을 거치면서 value 값이 정해진다. 앞의 표현식에서 False가 나왔다면, 뒤의 조건식에서 판정을 받게 되는 식으로, 기존의 if-else 문과 같은 구조로 해석하면 된다.

---

# iterable 객체의 unpack

> ### 나의 질문 😶
>
> ```python
> a, b = [1, 2]
> print(a)	# 1
> print(b)	# 2
> ```
>
> 이때, 어떻게 리스트 객체가 쪼개져서 각 항목이 변수들에 할당이 되는지 궁금했다.

#### 답변 (by. 동급생)

=> iterable한 객체이기 때문에 unpack 되어 변수들에 각각 할당이 된다 - 문자열, 리스트, 튜플 등등!

#### 추가 검색

[Unpacking Iterables in Python](https://www.pylenin.com/blogs/unpacking-iterables-in-python/)

-> 길이를 알 때, 같은 개수만큼의 변수로 unpack하거나, star expression(*)으로 풀 수 있다.

