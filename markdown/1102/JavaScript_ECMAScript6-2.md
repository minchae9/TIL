# ECMAScript 6 ๐: ์กฐ๊ฑด๋ฌธยท๋ฐ๋ณต๋ฌธ, ํจ์, ๋ฐฐ์ด๊ณผ ๊ฐ์ฒด

## 1. ์กฐ๊ฑด๋ฌธ๊ณผ ๋ฐ๋ณต๋ฌธ

### ์กฐ๊ฑด๋ฌธ(conditions)

- #### if ๋ฌธ

  > ์กฐ๊ฑด์์ ๊ฒฐ๊ณผ๊ฐ์ Boolean์ผ๋ก ๋ณํํ ํ ์ฐธ, ๊ฑฐ์ง์ ํ๋จํ๋ค.
  >
  > - ์กฐ๊ฑด์ ์๊ดํธ ์, ์ฝ๋๋ ์ค๊ดํธ ์์ ์์ฑ
  > - ๋ธ๋ก ์ค์ฝํ๋ฅผ ์์ฑํ๋ค.

  ```javascript
  if (condition) {
      // ์ฒ๋ฆฌ
  } else if (condition) {
      // ์ฒ๋ฆฌ
  } else {
      // ์ฒ๋ฆฌ
  }
  ```

  

- #### switch ๋ฌธ

  > ์กฐ๊ฑด์์ ๊ฒฐ๊ณผ๊ฐ์ด ์ด๋ case(๊ฐ)์ ํด๋นํ๋์ง ํ๋ณํ๋ค.
  >
  > ๊ฐ๋ฅํ ๊ฒฝ์ฐ์ ์๊ฐ ๋ง์์๋ก ๊ฐ๋์ฑ์ด if๋ฌธ๋ณด๋ค ์ข์ ์ ์๋ค.
  >
  > - break์ default ๋ฌธ์ optional
  >
  > - break ๋ฌธ์ด ์์ผ๋ฉด break๋ฌธ์ ๋ง๋๊ฑฐ๋, default๋ฌธ์ ์คํํ  ๋๊น์ง ๋ค์ ์กฐ๊ฑด๋ฌธ์ ๊ณ์ ์คํํ๋ค.
  > - ๋ธ๋ก ์ค์ฝํ๋ฅผ ์์ฑํ๋ค.

  ```javascript
  switch(expression) {
    case 'first value': {
        // ์ฒ๋ฆฌ
        [break]
    }
    case 'second value': {
        // ์ฒ๋ฆฌ
        [break]
    }
    [default: {
        // ์ฒ๋ฆฌ
    }]
  }
  ```

<br/>

### ๋ฐ๋ณต๋ฌธ(loops)

- #### while

  > ์กฐ๊ฑด๋ฌธ์ด ์ฐธ์ธ ๋์ ๋ฐ๋ณต
  >
  > - ์กฐ๊ฑด์ ์๊ดํธ ์์, ์คํํ  ์ฝ๋๋ ์ค๊ดํธ ์์
  > - break๋ฌธ์ ์ ํ์ ์ผ๋ก ์์ฑํ  ์ ์๋ค.
  > - ๋ธ๋ก ์ค์ฝํ๋ฅผ ์์ฑํ๋ค.

  ```javascript
  while (condition) {
      // ์ฒ๋ฆฌ
  }
  ```

  

- #### for

  > - initialization: ์ต์ด ๋ฐ๋ณต๋ฌธ ์ง์์ 1ํ๋ง ์คํ๋๋ ๋ถ๋ถ
  > - condition: ๋งค ๋ฐ๋ณต ์ํ ์  ํ๊ฐ๋๋ ๋ถ๋ถ
  > - expression: ๋งค ๋ฐ๋ณต ์ํ ์ดํ ํ๊ฐ๋๋ ๋ถ๋ถ
  > - ๋ธ๋ก ์ค์ฝํ๋ฅผ ์์ฑํ๋ค.

  ```javascript
  for (initialization; condition; expression) {
      // ์ฒ๋ฆฌ
  }
  ```

  

- #### for ... <span style="color:navy;">in</span>

  > <span style="color:crimson;">**๊ฐ์ฒด(object)์ ์์ฑ**์ ์ํํ  ๋</span>
  >
  > - ***๋ฐฐ์ด X*** (๊ถ์ฅ๋์ง ์์)
  > - ๋ธ๋ก ์ค์ฝํ๋ฅผ ์์ฑํ๋ค.

  ```javascript
  for (variable in object) {
      // ์ฒ๋ฆฌ
  }
  ```

  ```javascript
  // ์์
  
  const capitals = {
      Korea: '์์ธ',
      France: 'ํ๋ฆฌ',
      US: '์์ฑํด D.C.',
  }
  
  for (let capital in capitals) {
      console.log(capital)
  }
  ```

  - ๊ฒฐ๊ณผ: Korea

    โ		  France

    โ		  US

- #### for ... <span style="color:navy;">of</span>

  > <span style="color:crimson;">**๋ฐ๋ณต๊ฐ๋ฅํ ๊ฐ์ฒด**๋ฅผ ์ํํ  ๋</span>
  >
  > โณ <u>Array</u>, Map, Set, String ๋ฑ
  >
  > - ๋ธ๋ก ์ค์ฝํ๋ฅผ ์์ฑํ๋ค.

  ```javascript
  for (variable of iterables) {
      // ์ฒ๋ฆฌ
  }
  ```

  ```javascript
  // ์์
  
  const fruits = ['๋ธ๊ธฐ', '๋ฐ๋๋', '์๋ฐ']
  
  for (let fruit of fruits) {
      console.log(fruit)
  }
  ```

  - ๊ฒฐ๊ณผ: ๋ธ๊ธฐ

    โ		  ๋ฐ๋๋

    โ		  ์๋ฐ

![image-20211102193037460](JavaScript_ECMAScript6-2.assets/image-20211102193037460.png)

<br/>

๐ ์ฐธ๊ณ 

JavaScript ๊ฐ์ฒด์ value๋ ์ (.) ๋๋ ๋๊ดํธ ํ๊ธฐ๋ฒ์ ์ฌ์ฉํ์ฌ key ๊ฐ์ ํตํด ์ ๊ทผ์ด ๊ฐ๋ฅํ๋ค.

์) obj.key ๋๋ obj[key]

๋๋ก๋ . ์ด ๊ธฐ๋ฅํ๊ณ , ๋๋ก๋ [] ๊ฐ ๊ธฐ๋ฅํ๋ค.

<br/>

## 2. ํจ์(functions)

> - ์ฐธ์กฐ ํ์ ์ค ํ๋. function ํ์์ ์ํ๋ค.
> - JavaScript์ ํจ์๋ ***์ผ๊ธ ๊ฐ์ฒด(First-class citizen)***์ ํด๋นํ๋ค.
>   - **์ผ๊ธ ๊ฐ์ฒด**
>     - ๋ณ์์ ํ ๋น ๊ฐ๋ฅํ๊ณ 
>     - ํจ์์ ๋งค๊ฐ๋ณ์๋ก ์ ๋ฌ ๊ฐ๋ฅํ๊ณ 
>     - ํจ์์ ๋ฐํ๊ฐ์ผ๋ก ์ฌ์ฉ ๊ฐ๋ฅํ ๊ฐ์ฒด

- ### ํจ์ ์ ์ธ์ (function statement, declaration)

  : ํจ์์ ์ด๋ฆ๊ณผ ํจ๊ป ์ ์ํ๋ ๋ฐฉ์

  - hoisting์ด ๋ฐ์ํ  ์ ์๋ค - ์ฌ์ฉ์ด ๊ถ์ฅ๋์ง ์์.

  ํจ์ ์ด๋ฆ, ๋งค๊ฐ๋ณ์, ๊ทธ๋ฆฌ๊ณ  ๋ชธํต(์ค๊ดํธ)์ผ๋ก ์ด๋ฃจ์ด์ ธ ์๋ค.

  ```javascript
  function name(args) {
      // do something
  }
  ```

  

- ### ํจ์ ํํ์ (function expression) โ

  : ํจ์๋ฅผ ํํ์ ๋ด์์ ์ ์ํ๋ ๋ฐฉ์

  โ	(*ํํ์: ์ด๋ค ํ๋์ ๊ฐ์ผ๋ก ๊ฒฐ์ ๋๋ ์ฝ๋์ ๋จ์)

  - ํจ์์ ์ด๋ฆ์ ์๋ตํ๊ณ  ์ต๋ช ํจ์๋ก ์ ์ํ  ์ ์๋ค. (์ต๋ช ํจ์๋ ํจ์ ํํ์์์๋ง ๊ฐ๋ฅ)
  - ํจ์ ์ด๋ฆ (์๋ต ๊ฐ๋ฅ), ๋งค๊ฐ๋ณ์, ๊ทธ๋ฆฌ๊ณ  ๋ชธํต(์ค๊ดํธ)์ผ๋ก ์ด๋ฃจ์ด์ ธ ์๋ค.

  ```javascript
  const myFunction = function (args) {
      // do something
  }
  ```

- #### ๊ธฐ๋ณธ ์ธ์

  : ์ธ์ ์์ฑ ์์, '=' ๋ฌธ์๋ฅผ ์ฌ์ด์ ๋์ด ๊ธฐ๋ณธ ์ธ์๋ฅผ ์ ์ธํ  ์ ์๋ค.

  ```javascript
  // ์์
  
  const greeting = function (name = 'noName') {
      console.log(`Hi, ${name}`)
  }
  
  greeting()	// Hi, noName
  ```

![image-20211102193649939](JavaScript_ECMAScript6-2.assets/image-20211102193649939.png)

### ํ์ดํ ํจ์ (Arrow Function) โญ

> *์์ฃผ ์ฌ์ฉ๋๋ค.*
>
> ํจ์๋ฅผ ๋น๊ต์  ๊ฐ๊ฒฐํ๊ฒ ์ ์ํ  ์ ์๋ ๋ฌธ๋ฒ.
>
> - **function ํค์๋** ์๋ต ๊ฐ๋ฅ
> - ํจ์์ ๋งค๊ฐ๋ณ์๊ฐ ์ค์ง ํ๋๋ผ๋ฉด, **'( )'** ์๋ต ๊ฐ๋ฅ
> - ํจ์์ ๋ชธํต์ด ํํ์ ํ๋๋ผ๋ฉด, **'{ }'๊ณผ return ํค์๋**๋ฅผ ์๋ต ๊ฐ๋ฅ

```javascript
// ๊ธฐ๋ณธ (ํจ์ ํํ์)
const arrow = function (name) {
    return `hello! ${name}`
}


// 1. function ํค์๋ ์๋ต, ํ์ดํ(=>) ์ถ๊ฐ
const arrow = (name) => {return `hello! ${name}`}

// 2. ํจ์์ ๋งค๊ฐ๋ณ์๊ฐ ์ค์ง ํ๋์ด๋ฏ๋ก, () ์๋ต
const arrow = name => {return `hello! ${name}`}

// 3. ๋ฐ๋์ ํํ์์ด 1๊ฐ์ด๋ฏ๋ก, {}์ return ํค์๋ ์๋ต
const arrow = name => `hello! ${name}`
```

<br/>

## 3. ๋ฐฐ์ด๊ณผ ๊ฐ์ฒด

### ๋ฐฐ์ด(arrays)

> ํค์ ์์ฑ์ ๋ด๊ณ  ์๋, ์ฐธ์กฐ ํ์์ ๊ฐ์ฒด
>
> - ์์๋ฅผ ๋ณด์ฅ (โข 0 ์ด์์ ์ ์ ์ธ๋ฑ์ค๋ก ์ ๊ทผ์ด ๊ฐ๋ฅ)
> - ๋ฐฐ์ด ๊ธธ์ด๋ ๋ฐฐ์ด.length

- ์ฃผ์ ๊ธฐ๋ณธ ๋ฉ์๋

  - `array.reverse()`: ์๋ณธ ๋ฐฐ์ด์ ์์๋ค์ ๋ฐ๋๋ก ์ ๋ ฌ
  - `array.push()`: ๋ฐฐ์ด์ ๋ง์ง๋ง์ ์์ ์ถ๊ฐ
  - `array.pop()`: ๋ฐฐ์ด์ ๋ง์ง๋ง ์์๋ฅผ ์ ๊ฑฐ
  - `array.unshift()`: ๋ฐฐ์ด์ ๊ฐ์ฅ ์์ ์์ ์ถ๊ฐ
  - `array.shift()`: ๋ฐฐ์ด์ ์ฒซ ๋ฒ์งธ ์์ ์ ๊ฑฐ
  - `array.includes(value)`: ๋ฐฐ์ด์ด ํน์  ๊ฐ์ ํฌํจํ๋์ง ํ๋ณ ํ ์ฐธ/๊ฑฐ์ง ๋ฐํ
  - `array.indexOf(value)`: ๋ฐฐ์ด์ ํน์  ๊ฐ์ด ์กด์ฌํ๋ ๊ฒฝ์ฐ ์ฒซ ๋ฒ์งธ ์ผ์นํ๋ ์์์ ์ธ๋ฑ์ค ๋ฐํ, ์์ผ๋ฉด -1์ ๋ฐํ.
  - `array.join([separator])`: ๋ฐฐ์ด์ ๋ชจ๋  ์์๋ฅผ separator(๊ตฌ๋ถ์)๋ฅผ ์ฌ์ด์ ๋๊ณ  ์ฐ๊ฒฐํ์ฌ ๋ฐํ. (๊ตฌ๋ถ์ ์๋ต ์, ์ผํ๊ฐ ๊ธฐ๋ณธ๊ฐ)

- #### Array Helper Methods โ (์ค์)

  > ๋ฐฐ์ด์ ์ํํ๋ฉฐ ํน์  ๋ก์ง์ ์ํํ๋ ๋ฉ์๋
  >
  > - ๋ฉ์๋ ํธ์ถ ์, ์ธ์๋ก callback ํจ์๋ฅผ ๋ฐ๋ ๊ฒ์ด ํน์ง์ด๋ค.
  >
  >   *callback ํจ์: ์ด๋ค ํจ์์ ๋ด๋ถ์์ ์คํ๋  ๋ชฉ์ ์ผ๋ก ์ธ์๋ก ๋๊ฒจ๋ฐ๋ ํจ์

  ![image-20211102202827324](JavaScript_ECMAScript6-2.assets/image-20211102202827324.png)

- ##### forEach

  `array.forEach(callback(element[, index[, array]]))`

  > ๋ฐฐ์ด์ ๊ฐ ์์์ ๋ํด ์ฝ๋ฐฑ ํจ์๋ฅผ ํ ๋ฒ์ฉ ์คํํ๋ค.
  >
  > ์ฝ๋ฐฑํจ์์ ๋งค๊ฐ๋ณ์ 3๊ฐ์ง: ๋ฐฐ์ด์ ์์, ๋ฐฐ์ด ์์์ ์ธ๋ฑ์ค, ๋ฐฐ์ด ์์ฒด
  >
  > - ๋ฐํ(return)๊ฐ์ด ์๋ค.

  ```javascript
  // (array function์ผ๋ก ํํ)
  
  array.forEach((element, index, array) => {
      // do something
  })
  ```

  ```javascript
  const places = ['๊ด์ฃผ', '๋์ ', '๊ตฌ๋ฏธ', '์์ธ']
  
  places.forEach((region, index) => {
      console.log(region, index)
      // ๊ด์ฃผ 0
      // ๋์  1
      // ๊ตฌ๋ฏธ 2
     	// ์์ธ 3
  })
  ```

- ##### map

  `array.map(callback(element[, index[, array]]))`

  > ๋ฐฐ์ด์ ๊ฐ ์์์ ๋ํด ์ฝ๋ฐฑ ํจ์๋ฅผ ํ ๋ฒ์ฉ ์คํํ๊ณ , <u>์ฝ๋ฐฑ ํจ์์ ๋ฐํ ๊ฐ์ ์์๋ก ํ๋ ์๋ก์ด ๋ฐฐ์ด์ ๋ฐํํ๋ค.</u>

  ```javascript
  array.map((element, index, array) => {
      // do something
  })
  ```

  ```javascript
  const numbers = [1, 2, 3, 4, 5]
  const doubleNums = numbers.map((num) => {
      return num * 2
  })
  
  console.log(doubleNums)	// [2, 4, 6, 8, 10]
  ```

- ##### filter

  `array.filter(callback(element[, index[, array]]))`

  > ๋ฐฐ์ด์ ๊ฐ ์์์ ๋ํด ์ฝ๋ฐฑ ํจ์๋ฅผ ํ ๋ฒ์ฉ ์คํํ๊ณ , <u>์ฝ๋ฐฑ ํจ์์ ๋ฐํ๊ฐ์ด **์ฐธ์ธ ์์๋ค๋ง** ๋ชจ์์ ์๋ก์ด ๋ฐฐ์ด์ ๋ฐํํ๋ค.</u>

  ```javascript
  array.filter((element, index, array) => {
      // do something
  })
  ```

  ```javascript
  const numbers = [1, 2, 3, 4, 5]
  const oddNums = numbers.filter((num, index) => {
      return num % 2
  })
  
  console.log(oddNums)	// [1, 3, 5]
  ```

- ##### reduce

  `array.reduce(callback(acc, element[, index[, array]])[, initialValue])`

  > ๋ฐฐ์ด์ ๊ฐ ์์์ ๋ํด ์ฝ๋ฐฑ ํจ์๋ฅผ ํ ๋ฒ์ฉ ์คํํ๊ณ , <u>์ฝ๋ฐฑ ํจ์์ ๋ฐํ๊ฐ๋ค์ ํ๋์ ๊ฐ(acc)์ ๋์  ํ ๋ฐํํ๋ค.</u>
  >
  > - acc: ์ด์  callback ํจ์์ ๋ฐํ๊ฐ์ด ๋์ ๋๋ ๋ณ์
  > - initialValue (optional): ์ต์ด callback ํจ์ ํธ์ถ ์ acc์ ํ ๋น๋๋ ๊ฐ. ๊ธฐ๋ณธ๊ฐ์ ๋ฐฐ์ด์ ์ฒซ ๋ฒ์งธ ๊ฐ.
  > - ๋น ๋ฐฐ์ด์ ๊ฒฝ์ฐ์๋ initialValue๋ฅผ ์ ๊ณตํด์ผ ํ๋ค. (๊ทธ๋ ์ง ์์ผ๋ฉด, ์๋ฌ ๋ฐ์)

  ```javascript
  array.reduce((acc, element, index, array) => {
      // do something
  }, initialValue)
  ```

  ```javascript
  const numbers = [1, 2, 3]
  
  const result = numbers.reduce((acc, num) => {
      return acc + num
  }, 0)
  
  console.log(result)	// 6
  ```

- ##### find

  `array.find(callback(element[, index[, array]]))`

  > ๋ฐฐ์ด์ ๊ฐ ์์์ ๋ํด ์ฝ๋ฐฑ ํจ์๋ฅผ ํ ๋ฒ์ฉ ์คํํ๊ณ , <u>์ฝ๋ฐฑ ํจ์์ ๋ฐํ ๊ฐ์ด ์ฐธ์ด๋ฉด ํด๋น ์์๋ฅผ ๋ฐํํ๋ค.</u>
  >
  > - ์ฐพ๋ ๊ฐ์ด ๋ฐฐ์ด์ ์กด์ฌํ์ง ์์ผ๋ฉด, undefined๋ฅผ ๋ฐํํ๋ค.

  ```javascript
  array.find((element, index, array) => {
      // do something
  })
  ```

  ```javascript
  const friends = [
      { name: 'Tiffany', age:36 },
      { name: 'Fred', age:73 },
      { name: 'Gabriel', age: 15 },
  ]
  
  const result = friends.find((friend) => {
      return friend.name === 'Fred'
  })
  
  console.log(result)	// { name: 'Fred', age:73 }
  ```

- ##### some

  `array.some(callback(element[, index[, array]]))`

  > ๋ฐฐ์ด์ ์์ ์ค <u>ํ๋๋ผ๋ ์ฃผ์ด์ง ํ๋ณ ํจ์๋ฅผ ํต๊ณผํ๋ฉด ์ฐธ์ ๋ฐํํ๋ค.</u>
  >
  > - ๋น ๋ฐฐ์ด์ ํญ์ ๊ฑฐ์ง(false)์ ๋ฐํํ๋ค.

  ```javascript
  array.some((element, index, array) => {
      // do something
  })
  ```

  ```javascript
  const numbers = [1, 3, 5, 7, 9]
  
  const hasEvenNumber = numbers.some((num) => {
      return num % 2 === 0
  })
  console.log(hasEvenNumber) // false
  
  const hasOddNumber = numbers.some((num) => {
      return num % 2
  })
  console.log(hasOddNumber)	// true
  ```

- ##### every

  > ๋ฐฐ์ด์ <u>๋ชจ๋  ์์๊ฐ ์ฃผ์ด์ง ํ๋ณ ํจ์๋ฅผ ํต๊ณผํ๋ฉด ์ฐธ์ ๋ฐํํ๋ค.</u>
  >
  > - ๋น ๋ฐฐ์ด์ ํญ์ ์ฐธ(true)์ ๋ฐํํ๋ค.

  ```javascript
  array.every(element, index, array) => {
      // do something
  }
  ```

  ```javascript
  const numbers = [2, 4, 6, 8, 10]
  
  const isEveryNumberEven = numbers.every((num) => {
      return num % 2 === 0
  })
  console.log(isEveryNumberEven)	// true
  
  const isEveryNumberOdd = numbers.every((num) => {
      return num % 2
  })
  console.log(isEveryNumberOdd)	// false
  ```

<br/>

### ๊ฐ์ฒด(objects)

> ์์ฑ(property)์ ์งํฉ.
>
> ์ค๊ดํธ ๋ด๋ถ์์ key์ value์ ์์ผ๋ก ํํํ๋ค.
>
> - key: <u>๋ฌธ์์ด</u> ํ์๋ง ๊ฐ๋ฅ (๋์ด์ฐ๊ธฐ ๋ฑ์ ๊ตฌ๋ถ์๊ฐ ์์ผ๋ฉด ๋ฐ์ดํ๋ก ๋ฌถ์ด์ผ ํ๋ค.)
>
> - value: ๋ชจ๋  ํ์ ๊ฐ๋ฅ
>
> - ๊ฐ์ฒด ์์ ์ ๊ทผ์ **์ (.)** ๋๋ **๋๊ดํธ**๋ก ๊ฐ๋ฅํ๋ค. 
>
>   (key ์ด๋ฆ์ ๊ตฌ๋ถ์๊ฐ ์๋ ๊ฒฝ์ฐ๋ ๋๊ดํธ ์ ๊ทผ๋ง ๊ฐ๋ฅํ๋ค.)

#### ๊ฐ์ฒด ๊ด๋ จ ES6 ๋ฌธ๋ฒ

- ##### ์์ฑ๋ช ์ถ์ฝ

  > ๊ฐ์ฒด๋ฅผ ์ ์ํ  ๋ *key์ ๋ณ์์ ์ด๋ฆ์ด ๊ฐ์ ๊ฒฝ์ฐ*

  ```javascript
  // ์์
  let books = ['Learning JS', 'Eloquent JS']
  let magazines = null
  
  // ES5
  var bookShop = {
      books: books,
      magazines: magazines,
  }
  
  // ES6
  var bookShop = {
      books,
      magazines,
  }
  
  console.log(bookShop.books) // ['Learning JS', 'Eloquent JS'] ๋ก ๊ฒฐ๊ณผ ๊ฐ์
  ```

  

- ##### ๋ฉ์๋๋ช ์ถ์ฝ

  > ๋ฉ์๋ ์ ์ธ ์, *function ํค์๋ ์๋ต ๊ฐ๋ฅ*

  ```javascript
  // ES5
  var obj = {
      greeting: function () {
          console.log('Hi')
      }
  }
  obj.greeting()	// Hi
  
  // ES6
  const newObj = {
      greeting() {
          console.log('Hi')
      }
  }
  newObj.greeting()	// Hi
  ```

  

- ##### ๊ณ์ฐ๋ ์์ฑ๋ช ์ฌ์ฉํ๊ธฐ

  > ๊ฐ์ฒด๋ฅผ ์ ์ํ  ๋, *key์ ์ด๋ฆ์ ํํ์์ ์ด์ฉํ์ฌ ๋์ ์ผ๋ก ์์ฑ ๊ฐ๋ฅ*

  ```javascript
  const key = 'regions'
  const value = ['๊ด์ฃผ', '๋์ ', '๊ตฌ๋ฏธ', '์์ธ']
  
  const country = {
      [key]: value,
  }
  
  console.log(country)	// { regions: Array(4) }
  console.log(country.regions)	// ['๊ด์ฃผ', '๋์ ', '๊ตฌ๋ฏธ', '์์ธ']
  ```

  

- ##### ๊ตฌ์กฐ ๋ถํด ํ ๋น โ

  > ๋ฐฐ์ด ๋๋ ๊ฐ์ฒด๋ฅผ ๋ถํดํ์ฌ ์์ฑ์ ๋ณ์์ ์ฝ๊ฒ ํ ๋นํ  ์ ์๋ ๋ฌธ๋ฒ
  >
  > *๋ฐฐ์ด๋ ๊ฐ๋ฅํ๋ค.*

  ```javascript
  const userInformation = {
      name: 'Taehee Kim',
      userId: 'lalalahappy123',
      phoneNumber: '010-0000-1111',
      email: 'taehee@taehee.com'
  }
  
  // ES5
  const name = userInformation.name
  const userId = userInformation.userId
  const phoneNumber = userInformation.phoneNumber
  const email = userInformation.email
  
  // ES6
  // 1)
  const { name } = userInformation
  const { userId } = userInformation
  const { phoneNumber } = userInformation
  const { email } = userInformation
  // 2)
  const { name, userId } = userInformation
  ```

#### JSON์ ์กฐ์ํ๋ ๋ด์ฅ ๋ฉ์๋

- **JSON.parse()**

  json ํ์ผ์ ์๋ฐ์คํฌ๋ฆฝํธ ๊ฐ์ฒด๋ก ๋ฐ๊ฟ์ค๋ค.

  ```javascript
  const json = '{"result":true, "count":42}'
  const parsedData = JSON.parse(json)
  
  console.log(parsedData)	// {result: true, count: 42}
  console.log(typeof parsedData)	// object
  ```

  

- **JSON.stringify()**

   ์๋ฐ์คํฌ๋ฆฝํธ ๊ฐ์ฒด๋ฅผ json ํํ๋ก ๋ฐ๊ฟ์ค๋ค.

  ```javascript
  const jsonData = JSON.stringify({
      coffee: 'Americano',
      iceCream: 'Cookie and cream',
  })
  
  console.log(jsonData)	// {"coffee":"Americano","iceCream":"Cookie and cream"}
  console.log(typeof jsonData)	// string
  ```



---

*๋*

