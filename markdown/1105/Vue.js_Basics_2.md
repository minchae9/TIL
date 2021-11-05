# Vue.js: 기초

## 4. Basic Syntax > Template Syntax

렌더링된 DOM을 Vue instance의 데이터에 선언적으로 바인딩할 수 있는, HTML 기반의 템플릿 구문을 사용한다. 즉, HTML에서 Vue.js의 기능을 쓰기 위한 문법이라고 보면 된다.

### 1) 보간법(Interpolation): {{  }}

- text

  '{{ }}' 사이에 변수 넣기

  ```html
  <span>{{ msg }}</span>
  ```

- raw HTML

  ```html
  <span v-html="rawHtml"></span>
  ```

  **단, 이 기능은 해킹의 위험이 있기 때문에 거의 (특히 사용자 입력을 받는 부분에서) 사용 금지라고 보면 된다!!!**

- attributes

  ```html
  <div v-bind:id="dynamicId"></div>
  ```

  속성에 속성값 지명하기

- JS 표현식

  ```html
  {{ number + 1}}
  {{ message.split('').reverse().join('') }}
  ```

  하나의 값으로 결과값이 나오는 구문을 표현식이라고 하는데, 위와 같이 '{{ }}' 사이에 표현식을 넣을 수 있다.

  

### 2) Directive: v-*

👁‍🗨 Directive에 대한 자세한 내용은 [공식 문서](https://kr.vuejs.org/v2/api/#%EB%94%94%EB%A0%89%ED%8B%B0%EB%B8%8C) 참고하기!

Vue instance에서 표현식의 값이 변경되면 "반응적으로" DOM에 적용될 수 있게 하는 역할을 한다.

- 전달인자 (arguments)는 **: (콜론)**을 통해 전달한다.
- 수식어 (modifiers)는 **. (dot notation)**을 통해 표현된다. 객체의 속성 안으로 깊이 들어간다고 생각하면 된다.

```html
<!--전달인자-->
<a v-bind:href="URL">이걸 눌러요!</a>
<a v-on:click>다음에는 이거요!</a>

<!--수식어-->
<form v-on:submit.prevent="onSubmit">...</form>
```

- #### v-text

  > element의 textContent를 업데이트한다. 보간법으로 내용을 넣는 것과 동일하다. 
  >
  > (보간법이 내부적으로 v-text로 컴파일 되기 때문이다.)

  ```html
  <div id="app">
    <p v-text="message"></p>
    <!-- <p>{{ message }}</p> 와 동일함 -->
  </div>
  ```

  ```javascript
  // script
  const app = new Vue({
    el: '#app',
    data: {
      message: 'Hello',
    }
  })
  ```

  

- #### v-html

  > element의 innerHTML을 업데이트 한다. (즉, 마크업을 작성하면 해석되어 출력된다.)
  >
  > **XSS 공격에 취약하므로, 특히 사용자 입력을 받는 부분은 *<span style="color:red;">절대</span>* 사용 금지!!!**

  ```html
  <div id="app">
    <div v-html="myHtml"></div>
  </div>
  ```

  ```javascript
  // script
  const app = new Vue({
    el: '#app',
    data: {
        myHtml: '<b>Hello</b>'
    }
  })
  ```

  

- #### v-show

  > 조건부 렌더링 하나.
  >
  > element의 display CSS 속성을 토글한다. 
  >
  > - element는 토글에 관계없이 <u>늘 렌더링된다.</u> 보였다 보이지 않았다 할 뿐.
  > - 보이지 않는 건 `style="display: none;"`이 적용된다. (자리 차지하지 않음)
  >
  > ⇒ 여러 번 토글이 필요한 경우에는 v-show

  ```html
  <div id="app">
    <p v-show="isTrue">
      Value is 'True'.
    </p>
    <p v-show="isFalse">
      Value is 'False'.
    </p>
  </div>
  ```

  ```javascript
  // script
  const app = new Vue({
    el: '#app',
    data: {
      isTrue: true,
      isFalse: false,
    }
  })
  ```

  

- #### v-if

  > 조건부 렌더링 둘.
  >
  > 조건에 따라 블록을 렌더링한다. 즉, directive의 표현식이 true여야 렌더링이 되고, 그렇지 않으면 렌더링 자체가 되지 않는다.
  >
  > - element는 표현식의 참/거짓에 따라 <u>렌더링 되거나, 되지 않는다.</u>
  > - element는 표현식의 참/거짓 변경에 따라 작성되고, 삭제되고, 다시 작성된다.
  >
  > ⇒ 토글이 빈번하지 않다면, 혹은 한 번만 렌더링 돼야 하는 경우에는 v-if

  ```html
  <div id="app">
    <div v-if="myType === 'A'">
      A입니다.
    </div>
    <div v-else-if="myType === 'B'">
      B입니다.
    </div>
    <div v-else>
      C입니다.
    </div>
  </div>
  ```

  ```javascript
  // script
  const app = new Vue({
    el: '#app',
    data: {
        myType: 'C',
    }
  })
  ```

#### [짚고가기] v-show와 v-if

- `v-show`: Expensive initial load, Cheap toggle

  토글이 될 때마다 렌더링은 완전히 새로 하는 게 아니다.

  처음에는 전체를 렌더링 하므로 최초 렌더링 비용은 높지만, 이후에는 추가 렌더링이 없이 토글만 하므로 비용이 낮다.

- `v-if`: Cheap initial load, Expensive toggle

  초기 로드는 싸지만, 토글이 비싸다.

  처음에는 directive의 표현식이 true인 것만, 즉 선별적으로 렌더링 하면 되므로 최초 비용은 낮지만, 이후에는 토글에 따라 추가적으로 태그를 작성하고 삭제해야 하므로 비용이 높다.

- 따라서, 딱 한 번만 렌더링 돼야 하는 경우에는 `v-if`가, 여러 번 로드 되는 경우에는 `v-show`가 경제적이다.

- #### v-for

  > 원본 데이터 객체를 순회하면서 element 또는 템플릿 블록을 여러 번 렌더링한다.
  >
  > - `item in items` 구문을 사용한다.
  >
  > - <u>반드시 **key 속성**을 각 요소에 작성해야 한다.</u>
  >
  > - `v-for`과 `v-if`를 동시에 사용하지 말 것이 권장된다. (함께 사용하는 경우, for이 우선순위가 더 높다.)
  >
  >   [참고 문서](https://kr.vuejs.org/v2/style-guide/#v-if%EC%99%80-v-for%EB%A5%BC-%EB%8F%99%EC%8B%9C%EC%97%90-%EC%82%AC%EC%9A%A9%ED%95%98%EC%A7%80-%EB%A7%88%EC%84%B8%EC%9A%94-%ED%95%84%EC%88%98)

  ```html
  <div id="app">
    <div v-for="(fruit, index) in fruits" :key="`fruit-${index}`">
      {{ fruit }}
    </div>
      
    <div v-for="todo in todos" :key="todo.id">
      {{ todo.title }} - {{ todo.completed }}
    </div>
  </div>
  ```

  ```javascript
  // script
  const app = new Vue({
    el: '#app',
    data: {
      fruits: ['apple', 'banana', 'coconut'],
      todos: [
        { id:1, title: 'todo1', completed: True },
        { id:2, title: 'todo2', completed: True },
        { id:3, title: 'todo3', completed: False },
      ]
    }
  })
  ```

  

- #### v-on

  > element에 eventListener를 연결한다. (keyup.enter, keypress.enter 등)
  >
  > `v-on:이벤트="실행할 함수"`
  >
  > - 약형
  >   - v-on: 을 @ 로
  >   - `v-on:click="alert"` ⇢ `@click="alert"`

  ```html
  <div id="app">
    <button v-on:click="doAlert">Button</button>
    <button @click="onInputEnter('hello')">Button</button>
  </div>
  ```

  ```javascript
  // script
  const app = new Vue({
    el: '#app',
    methods: {
      doAlert: function () {
        alert('Hello~')
      },
      onInputEnter: function (onInputValue) {
        console.log(onInputValue)
      }
    }
  })
  ```

  

- #### v-bind

  > **단방향** 바인딩 (Vue → DOM). (반대로는 X)
  >
  > 속성명 앞에 `v-bind:`를 붙이면, 속성값을 data 값으로 치환할 수 있다.
  >
  > - 약형
  >   - v-bind: 를 : 로
  >   - `v-bind:href` ⇢ `:href`

  ```html
  <div id="app">
    <!-- 속성 바인딩 -->
    <img :src="imageSrc">
    
    <!-- 클래스 바인딩 -->
    <div :class="{ active: isRed }">클래스 바인딩</div>
      
    <p :class="[activeRed, myBackground]">여러 개</p>
  </div>
  ```

  ```javascript
  // script
  const app = new Vue({
    el: '#app',
    data: {
      imageSrc: 'https://nnn.nnn/333/444/',
      isRed: true,
      activeRed: 'active',
      myBackground: 'my-background-color',
    }
  })
  ```

  

- #### v-model

  > **양방향** 바인딩. (Vue ↔ DOM)
  >
  > HTML form 요소의 값과 data가 서로 연동되도록 해준다.
  >
  > △ 그런데, 한글, 중문, 일문 등 IME가 필요한 언어는 한 박자 늦게 업데이트 된다. [공식문서](https://kr.vuejs.org/v2/guide/forms.html#%EA%B8%B0%EB%B3%B8-%EC%82%AC%EC%9A%A9%EB%B2%95)
  >
  > → input 이벤트를 발생시키고, 해당 이벤트가 발생할 때마다 data 값을 업데이트 하는 로직을 설계해야 한다.

  ```html
  <div id="app">
    <h3>{{ myMessage }}</h3>
    <input v-model="myMessage" type="text">
      
    <h3>Checkbox</h3>
    <input type="checkbox" id="checkbox" v-model="checked">
    <label for="checkbox">{{ checked }}</label>
  </div>
  ```

  ```javascript
  // script
  const app = new Vue({
    el: '#app',
    data: {
      myMessage: '',
      checked: True,
    }
  })
  ```

  - 수식어
    - `.lazy`: input 대신 change 이벤트 이후에 동기화
    - `.number`: 문자열을 숫자로 변경
    - `.trim`: 입력에 대한 trim을 진행

- #### `computed` 옵션

  > **data를 기반으로 계산된 속성**
  >
  > - 함수의 반환값이 바인딩 된다. (반드시 반환값이 있어야 한다.)
  >
  > - 종속된 데이터에 따라 저장(캐싱)되고, 종속된 데이터가 변하지 않는 이상 업데이트 되지 않는다.
  >
  >   **캐싱: 미리 저장해둔다.*
  >
  > - *즉, <u>종속된 데이터가 변경될 때만 함수가 새로이 실행된다.</u>*

  ```html
  <div id="app">
    <p>{{ num }}</p>
    <p>{{ doubleNum }}</p>
  </div>
  ```

  ```javascript
  // script
  const app = new Vue({
    el: '#app',
    data: {
      num: 2,
    },
    computed: {
        doubleNum: function () {
            return this.num * 2
        }
    },
  })
  ```

  ##### methods와의 차이점

  - methods는 함수이므로 호출을 해야 하지만 (`함수명()`), computed는 일정한 값이므로 함수 호출이 아니다.
  - computed 속성은 종속 데이터에 따라 저장(캐싱)되므로, 호출되어도 계산을 다시 하지 않고 계산되어 저장했던 결과를 반환한다.
  - methods는 호출할 때마다 함수를 다시 실행한다.

- #### `watch` 옵션

  > 데이터를 감시하고 있다가, 데이터에 변화가 일어나면 함수를 실행한다.
  >
  > - 함수 앞에는 감시되는 데이터의 이름을 적어준다. (this 키워드 안 써도 됨)
  >
  > - 변경 후의 값과 변경 전의 값을 각각 첫 번째, 두 번째 인자로 받을 수 있다.

  ```html
  <div id="app">
    <p>{{ num }}</p>
    <button @click="num += 1">add 1</button>
  </div>
  ```

  ```javascript
  // script
  const app = new Vue({
    el: '#app',
    data: {
      num: 2,
    },
    watch: {
      num: function () {
        console.log(`${this.num}이 변경되었습니다.`)
      }
    },
  })
  ```

- #### computed와 watch의 차이점

  [공식 문서](https://kr.vuejs.org/v2/guide/computed.html)

  **역할이 다르다!**

  - computed:

    "특정 값이 바뀌면 해당 값을 다시 계산해서 보여준다."

    - 종속 데이터에 대한 계산 결과로서, 리턴값이 있어야 한다. 특정 데이터를 직접 사용할 때 사용한다.

    - 계산해야 하는 목표 데이터를 정의한다는 면에서 '선언형 프로그래밍' 방식

  - watch

    "특정 값이 바뀌면 다른 작업을 한다."

    - 종속 데이터로 인해 다른 데이터가 바뀌어야 할 때 주로 사용되며, 리턴값이 없을 수 있다.

    - 데이터의 변화에 따라 특정 함수를 실행시킨다는 면에서 '명령형 프로그래밍' 방식

- #### `filter` 옵션

  > 텍스트 형식화를 적용할 수 있는 필터.
  >
  > - interpolation 또는 v-bind를 이용할 때 사용할 수 있다.
  > - 필터는 JS 표현식 마지막에 **| (파이프라인)**과 함께 추가되어야 한다.
  > - chaining이 가능하다.
  > - 필터 메서드의 인자는 파이프라인 앞의 변수이다.
  > - filters 라는 key값으로 작성된다.

  ```html
  <div id="app">
    <!-- 순서대로 필터링 되며 앞의 결과의 리턴값을 인자로 받는다 -->
    <p>{{ numbers | getOddNums | getUnderTenNums }}</p>
  </div>
  ```

  ```javascript
  // script
  const app = new Vue({
    el: '#app',
    data: {
      numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    },
    filters: {
      getOddNums: function (nums) {
        const oddNums = nums.filter(function (num) {
            return num % 2
        })
        return oddNums
      },
      getUnderTenNums: function (nums) {
        const underTen = nums.filter(function (num) {
          return num < 10
        })
        return underTen
      }
    },
  })
  ```

  

## 5. Lifecycle Hooks

생명주기 훅. 특정 시점을 가리키며, 해당 시점들에 특정 작업이 자동으로 일어나게 하고 싶을 때 사용한다. 공식문서는 [여기](https://vuejs.org/v2/guide/instance.html#Lifecycle-Diagram).

각 Vue 인스턴스는 생성될 때 일련의 초기화 단계를 거치게 된다. 인스턴스를 DOM에 마운트하고, 데이터가 변경되어 DOM을 업데이트 하는 경우 등이 여기에 포함된다. 그 과정에서 사용자 정의 로직을 실행할 수 있는 Lifecycle Hooks도 함께 호출된다.

![lifecycle](Vue.js_Basics_2.assets/lifecycle.png)

- 예시 코드

  ```javascript
  // script
  new Vue({
    data: {
      a: 1,
    },
    created: function () {
      console.log('a is: ' + this.a)	// => 'a is: 1'
    }
  })
  ```

  - lifecycle hook, 즉 시점 이름을 key로 가지고, 뒤에 실행할 함수를 적는다.
  - `created`는 Vue instance가 생성된 후, 템플릿이 생성되기 전에 호출된다.



## 6. Lodash library

JavaScript 유틸리티 라이브러리로, 모듈성, 성능 및 추가 기능을 제공한다.

특히, array나 object 등 자료구조를 다룰 때 사용할 수 있는 유용하고 간편한 유틸리티 함수들을 제공한다.

- 외부 라이브러리이므로 사용 전에 CDN으로 사전 설치가 필요하다.
- '_' (언더 바) 객체 안에서 사용하는 메서드들을 호출한다.
- [공식 문서](https://lodash.com/docs/4.17.15)

---

*끝*