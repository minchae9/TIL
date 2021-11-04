# Vue.js: 기초

## 0. Intro

### Vue.js란?

**Vue.js**는 React, Angular와 더불어 대표적인 프론트엔드 프레임워크이다.

> - 구글 Angular의 개발자 출신인 *Evan You*가 2014년에 발표한 프레임워크로, 단기간에 빠른 성장을 이룩하며 사용자수가 급증하고 있다.
> - 사용자 인터페이스를 만들기 위한 JavaScript 프레임워크
> - *SPA(Single Page Application)*을 지원한다.

***잠깐!*** SPA가 뭐야?

#### SPA (Single Page Application)

> 웹 애플리케이션을 <span style="color:navy;">*"단일 "* </span> 페이지로 구성하여 최초에만 페이지를 다운로드하고, 이후로는 동적으로 DOM을 렌더링하는 방식의 웹 애플리케이션이다.
>
> → 즉, 처음 이후부터는 데이터가 갱신될 때마다 그 내용을 '페이지(HTML 문서)'로 받는(MPA; Multi Page Application) 게 아니라, 변화된 부분만 동적으로 다시 작성하는 것. (이는 AJAX를 통해 할 수 있다.)
>
> - UX를 향상시킨다. (트래픽의 감소, 속도·사용성·반응성의 개선을 이루므로)
> - 렌더링 방식으로 CSR을 사용한다. (SSR을 지원하는 기술도 가지고 있다.)

**CSR**은 또 뭐람?

#### CSR (Client Side Rendering)

> SSR(Server Side Rendering)의 반대 개념으로, SSR은 서버 측에서 화면을 모두 구성했다면, CSR은 클라이언트에서 화면을 구성한다. (렌더링의 주체에 따라 구분된다!)

최초 요청 시에 HTML, CSS, JavaScript(JS) 등의 데이터를 제외한 각종 리소스(='뼈대')를 응답받고, 추후에 클라이언트 측에서 필요한 데이터(='살')를 요청해 JS로 DOM을 렌더링한다.



![Inked1_CRiH0hUGoS3aoZaIY4H2yg_LI](Vue.js_Basics.assets/Inked1_CRiH0hUGoS3aoZaIY4H2yg_LI.jpg)

서버의 응답을 받아서, 브라우저 측에서 JS와 프레임워크를 통해 페이지의 데이터를 채워 완성한다.

SSR과 비교해보자:

![Inked1_jJkEQpgZ8waQ5P-W5lhxuQ_LI](Vue.js_Basics.assets/Inked1_jJkEQpgZ8waQ5P-W5lhxuQ_LI.jpg)

서버가 보낸 HTML 응답은 이미 재료가 갖추어진 상태이고, 브라우저에서는 이를 보여주는 역할만을 담당한다.

##### CSR의 특징

SSR의 장단점과 반대!

- 장점

  - 서버와 클라이언트 간 트래픽 감소한다.

    : 정적 리소스를 최초에 한 번만 다운로드하고, 필요한 데이터만 갱신하므로

  - UX가 향상된다.

    : 전체 페이지가 새로 로드되는 대신에 변경되는 부분만 갱신하므로

- 단점

  - SSR에 비해, 전체 페이지 렌더링 완료 시점이 느리다.

    : SSR은 서버에서 응답이 올 때부터 갖추어진 상태이므로

  - SEO(검색 엔진 최적화)에 어려움이 있다.

    : 최초 문서에 데이터가 없기 때문에 데이터를 활용할 수 없...다 😢

    > **SEO (Search Engine Optimization)**
    >
    > : 웹 페이지 검색엔진이 자료를 수집하고, 순위를 매기는 방식에 맞게 웹 페이지를 구성해서 검색 결과의 상위에 노출될 수 있게 하는 작업
    >
    > - 구글에서 컨텐츠의 신뢰도를 파악하는 기초 지표로 사용함
    >
    > - 인터넷 마케팅 방법 중 하나로 사용됨
    >
    > - Vue.js나 React 등의 SPA 프레임워크에는 이에 대응할 수 있도록 SSR을 지원하는 기술이 있으므로, SEO에 대응할 수 있다.
    >
    >   (추가로 별도 프레임워크를 사용할 수도 있다: Vue.js는 Nuxt.js, React는 Next.js)

<br>

웹 애플리케이션의 필요에 따라 SSR, CSR, 또는 둘을 조합하여 사용할 수 있다.

![image](Vue.js_Basics.assets/image.PNG)

## 1. Vue.js를 사용하는 이유

웹 페이지의 규모가 커지고, 사용하는 데이터량이 증가하고, 사용자의 상호작용도 늘어남에 따라, 순수한 자바스크립트(Vanilla JS) 만으로는 이 모든 것을 관리하는 데에 어려움이 생겼다.

흔한 예시로, Facebook에서 이름을 수정했을 경우, 화면 상에서 변경이 요구되는 부분은 정말 많다. 나의 프로필에서 바뀌는 것은 물론이고, 내가 작성한 글의 모든 작성자 이름, 친구 목록에서의 나의 이름 등⋯. 

기존 JavaScript 단독으로는 각각에 대해 데이터를 변경해줘야 하는 번거로운 작업이 예상됐겠지만, 페이스북(現 메타)에서는 React 프레임워크를 개발함으로써 이를 해결했다.

Vue.js 도 React와 같은 결의 프론트엔드 프레임워크란 점에서 마찬가지이다. 

DOM과 Data를 중개하는 프레임워크를 통해 핵심이 되는 데이터만 변경하면, 해당 데이터를 참조하는 DOM의 구성요소가 변화된 데이터를 표시할 수 있게 되는 것이다. 즉, Data에 대한 관리가 DOM 까지 이어지게끔 함으로써를 용이성을 제공한다!

+

프론트엔드 프레임워크에서, 현 Vue.js가 가지는 장점?

(1) 직관적이고 쉽다.

(2) 공식문서의 한글화가 잘 되어 있다.



## 2. Concepts of Vue.js

### MVVM 패턴

> Vue.js의 디자인 패턴
>
> - Model
> - View
> - ViewModel (👈 Vue의 주요 역할)

![image-20211104211549228](Vue.js_Basics.assets/image-20211104211549228.png)

- Model

  ***"Vue.js에서 Model은 <u>Javascript 객체</u>이다."***

  Vue 인스턴스 내부에서 data로 사용되며, 값이 바뀌면 View(DOM)가 반응한다.

- View

  ***"Vue에서 View는 <u>DOM(HTML)</u>이다."***

  Data의 변화에 따라서 반응하며 바뀐다.

- ViewModel

  ***"Vue에서 ViewModel은 모든 Vue 인스턴스이다."***

  Vue 인스턴스를 만들어서 사용하게 되는데, 이것이 View와 Model 사이에서 DOM과 Data에 관한 일을 처리한다.



## 3. Quick Start

👉 [퀵 스타트](https://kr.vuejs.org/v2/guide/) ⭐

- 코드의 작성 순서

  (Django에서 코드를 작성할 때 데이터의 흐름에 맞춰 한 것처럼,) Vue.js에서는 Model의 데이터가 변경되면 DOM이 반응하여 변화가 일어나므로,

  1) Model의 Data 로직을 먼저 작성하고,
  2) DOM을 작성한다.

- [참고]

  - "반응형": Model의 data 변경에 따라 DOM이 바로바로 바뀐다는 의미
  - 보간법(interpolation): `{{ todo }}`

## 4. Basic Syntax

### Vue instance

모든 Vue 앱은 <u>Vue 함수로 새 인스턴스를 만드는 것에서부터</u> 시작한다.

```javascript
const app = new Vue({
    // Options 객체
})
```

중괄호로 options 객체를 전달하고, 안에 여러 option을 사용하여 원하는 동작을 구현할 수 있다. (JavaScript의 객체는 사전형(`{key: value}`)이라는 것⋯! 👽)

Vue 인스턴스는 하나의 컴포넌트라고 할 수 있다: [여기서 확인하기](https://kr.vuejs.org/v2/guide/#%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%9C-%EC%9E%91%EC%84%B1%EB%B0%A9%EB%B2%95)

<br>

### Options 객체에 들어가는 옵션

```javascript
const ap = new Vue({
  el: '#app',
  data: {
    content: 'Hello',
  },
  methods: {
      greeting: function () {
        console.log(this.content)
      }
  }
})
```

- #### el

  > Vue instance에 연결(mount)할 DOM 엘리먼트를  CSS 식별자로  문자열로 작성한다.

  - new를 통해 새롭게 Vue 인스턴스를 생성할 때에만 사용된다.

- #### data

  > Vue instance의 데이터 객체(object).
  >
  > Vue 인스턴스의 상태 데이터를 정의하는 곳이다.

  - 마운트된 HTML 태그(Vue template)에서는 (별도의 과정 없이) {{ interpolation }} 을 통해 접근할 수 있다.

  - directive에서도 사용이 가능하다. ~~(directive에 대한 내용은 뒤에)~~

  - Vue 인스턴스 내 함수에서 `this` 키워드를 통해 접근할 수 있다.

  - ※ 주의사항

    - <u>**data**에서는 화살표 함수를 사용할 수 없다!</u>

      (화살표 함수가 부모 컨텍스트를 바인딩하여, Vue 인스턴스를 가리키지 않고 상위 객체(window 등)를 가리키게 되어버린다.)

- #### methods

  > Vue instance에 추가할 메서드를 적는 곳.

  - Vue template에서 {{ interpolation }}을 통해 접근할 수 있다.

  - directive에서도 사용이 가능하다.

  - Vue 인스턴스 내 함수에서 `this` 키워드를 통해 접근할 수 있다.

  - ※ 주의사항

    - <u>**메서드 정의**에서는 화살표 함수를 사용할 수 없다!</u>

      (화살표 함수가 부모 컨텍스트를 바인딩하여, Vue 인스턴스를 가리키지 않고 상위 객체(window 등)를 가리키게 되어버린다.)

### 'this' 키워드

> Vue 함수 객체 내에서, vue instance를 가리키기 위해 사용하는 키워드.

#### [참고] JavaScript의 'this'

***JavaScript의 'this'는 "함수 호출 방식"에 의해 결정되는 this이다.***

>   JavaScript의 함수는 호출될 때 'this' 를 암묵적으로 전달 받는다. 인스턴스 자신을 가리키는 Python에서의 self와 유사하지만, JavaScript에서의 'this' keyword는 일반적인 프로그래밍 언어에서의 this와 조금 다르게 동작한다.
>
>    JavaScript는 해당 함수의 호출 방식에 따라 'this'에 바인딩 되는 객체가 달라진다. <u>즉, 함수를 선언할 때 'this'에 객체가 결정되는 것이 아니고, 함수를 호출할 때 함수가 어떻게 호출 되었는지에 따라 동적으로 결정된다는 말이다.</u>
>
>   특히, 화살표 함수는 JavaScript에서 호출의 위치와 상관없이 상위 스코프를 가리키게 된다. 이때문에 함수를 "어디서" 호출하는지가 아니라, "어디에 선언하였는지에" 따라 결정된다. (같은 이유로 `addEventListener`의 콜백 함수는 화살표 함수로 작성하면 안 된다. 상위 스코프인 window 객체가 바인딩 된다.)

#### [참고] Vue instance의 data 객체의 속성 접근법

Vue insatnce 의 data 객체의 속성에 접근할 때, `vm.data.a`가 아니라 `vm.a`로 접근한다. 중간에 있는 data는 어떻게 뛰어넘게 되는 것일까?

👉 이유: Vue instance는 data 객체의 모든 속성을 프록시하므로 ([자세히 보기 1](https://kr.vuejs.org/v2/api/#data)[, 2](https://kr.vuejs.org/v2/api/#vm-data))

​					↳ 즉, 인스턴스가 데이터 속성에 대한 접근을 대리(proxy)해준다는 의미.

---

이어서 Template Syntax...