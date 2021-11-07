# 노트

## 0. 프로젝트 관련 참고내용

- json 파일의 내용을 로드하려면:

```shell
$ python manage.py loaddata <filename>
# 앱 안의 fixtures 폴더를 자동으로 탐지하므로, 이후 경로를 적어주면 된다.
```

- 데이터를 파일로(fixtures로) 만들려면:

```shell
$ python manage.py dumpdata <app_name>[.ModelName]
# 앱 이름만 적어도 되고, 특정 모델의 데이터로 특정하고 싶으면 모델명까지 적어준다.

$ python manage.py dumpdata --indent 4 movies > test.json
# 의미: 출력된 값을 4칸씩 들여쓰기 옵션을 적용해서 오른쪽 파일에 입력/저장하겠다.
# (pip freeze > requirements.txt 와 동일 문법)
```

- 이때, 한글에 대한 인코딩을 완료하려면?

  메모장을 열고, '다른 이름으로 저장', 인코딩을 ANSI가 아닌 UTF-8로 지정하고 저장해준다.

## 1. infinite scroll

무한 스크롤이란, 스크롤을 내리면 자동으로 다음 데이터가 로드되도록 하는 기법이다.

무한 스크롤을 구현하려면, 쿼리셋 데이터를 잘라서 순차적으로 보여줘야 할텐데,

이를 위해 우리는 Django의 pagination 기능을 사용할 수 있다: [공식문서 보러가기](https://docs.djangoproject.com/en/3.2/topics/pagination/)

<br>

기존에는 한 페이지에 모든 데이터 정보를 전해줬다면, 이번에는 paginator로 정보를 분할하여 부분 정보를 대신 전달해주는 방법을 사용할 것이다.

→ 한 페이지의 정보를 보는 게 완료되면, axios로 다음 페이지에 대한 요청을 전송하고 응답을 받아올 수 있다.

<br>

그렇다면, 한 페이지의 문서를 모두 읽었고 다음 페이지가 필요하다는 정보를 우리는 어떻게 자동으로 전달할 수 있을까?

무한 스크롤이라는 말에서 짐작할 수 있듯이, 스크롤이 끝까지 내려가면 새로운 정보가 로드되게 만들면 된다. 이를 위해 우리는 `Element.scrollHeight` 속성을 이용한다: [공식문서 보러가기](https://developer.mozilla.org/ko/docs/Web/API/Element/scrollHeight)

- 문서 전체의 길이: `document.documentElement.scrollHeight`

- 사용자가 보고 있는 영역: `document.documentElement.clientHeight`

- 내려간 길이: `document.documentElement.scrollTop` 

  ↳ `scrollTop`의 경우, 정수로 나와야하지만 소수로 계산되는 버그가 있으므로 수동으로 정수화시켜 주기로 한다.

여기에 대해 아래와 같은 공식을 이용하면, 끝까지 스크롤한 상태임을 판단할 수 있다:

```tex
element.scrollHeight - element.scrollTop === element.clientHeight
```



## 2. social login

해당 홈페이지에 회원가입을 하지 않고, 소셜 계정으로 로그인하여 타 소셜 미디어의 인증을 거쳐 해당 홈페이지에 대한 이용 권한을 부여하는 것을  ['소셜 로그인'](https://auth0.com/learn/social-login/)이라고 한다. 이를 위해서는 **'OAuth'** 라는 개념이 사용된다. 자세한 정보는 다음 문서에서 확인할 수 있다: [Naver D2: OAuth와 춤을](https://d2.naver.com/helloworld/24942)

<br>

Django에서는 oauth를 위한 라이브러리를 제공한다: [Django allauth 라이브러리](https://django-allauth.readthedocs.io/en/latest/index.html)

(자세한 구현 방법은 위 라이브러리에 대한 공식문서의 installation 페이지를 따라하면 쉽게 할 수 있다.)

참고로, OAuth로 user의 회원가입과 로그인을 승인하더라도, user 정보는 기존과 똑같이 Django에서 사용될 수 있다.

---

*끝*