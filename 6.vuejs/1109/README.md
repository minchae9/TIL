# 노트

- 상위 컴포넌트에서 하위 컴포넌트를 '사용'할 때:

  `<하위컴포넌트명 />` 태그를 만들기

  ↳ PascalCase로 작성된 컴포넌트명을 그대로 사용할 수도 있고,

  `<하위컴포넌트명></하위컴포넌트명`의 태그로 kebab-case의 컴포넌트명을 사용할 수도 있다 (이 경우, 자동완성을 활용할 수 있음).

- 컴포넌트 내 script에서 작성하는 name 속성은, Vue Devtools에서 확인할 때 뜨는 이름이다.

- props를 내려보내기

  ```html
  <Parent :appData="appData" />
  ```

  의미: 'appData' 라는 이름으로(좌변) appData(데이터, 우변)를 내려보냅니다.

  - payload에 데이터를 여러 개 넣으려면, 그냥 나열식으로 적어주면 된다.

  - 자식 컴포넌트에서는 props를 선언한 후 사용한다.

- 자식 컴포넌트에서 emit event 발생시키기

  ```javascript
  // 인스턴스에서는 this 키워드 사용
  this.$emit('event-name-in-kebab-case', this.payload_data)
  ```

  ↓

- 부모 컴포넌트에서 이벤트를 듣고, 특정 행위 실행하기

  ```html
  <Child @event-name-in-kebab-case="inputChild" />
  ```

  ```javascript
  export default {
    ...
    methods: {
      inputChild: function (data) {
        console.log('data from child')
      }
    },
  }
  ```

  

- 숨겨야 할 변수 (예: API key) 는 **.env.local** 파일에.

  - 프로젝트 내에 `.env.local` 파일을 생성하고,

  - VUE_APP_어쩌고=key

    의 형태로 작성한다. (띄어쓰기와 따옴표 없이)

  ↓

- 컴포넌트 파일에서 key 사용하기

  ```javascript
  const API_KEY = process.env.VUE_APP_어쩌고
  ```

- 글자 깨지는 문제 해결: lodash 라이브러리의 unescape

  [공식문서](https://lodash.com/docs/4.17.15#unescape)

- 필터 적용 방법

  ```html
  {{ video.snippet.title | stringUnescape}}
  ```

  파이프라인(|)을 사용한다. (stringUnescape는 메소드)

- 동영상을 화면에 embed 할 때, `<iframe>` 태그를 사용한다.

  [공식문서](https://developers.google.com/youtube/player_parameters)

