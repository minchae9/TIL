#0802

# [Web] > **HTML**

## 0. Web π

---

### 1. Webμ λ°°μ°λ μ΄μ 

**A. μΉ μ νλ¦¬μΌμ΄μ κ°λ°μ νμ΅ν¨μΌλ‘μ¨, SW κ°λ° λ°©λ²κ³Ό νμ΅ κ³Όμ μ μ΅ν μ μκΈ° λλ¬Έμ΄λ€.** μΉμ μννΈμ¨μ΄μ μ΄λ€ λΆμΌλ  κ°μ κ°μ₯ κΈ°λ°μ΄ λλ κΈ°μ μ΄λ€.

### 2. Web νμ€

> νΉμ  λΈλΌμ°μ μ μ’μλμ§ μλ, μΉμ νμ€μ μΈ κΈ°μ  λλ κ·μΉ

κΈ°μ‘΄μ μΉ νμ€μ W3C(Worldwide Web Consortium)μμ HTML νμ€μ μ μ νμλλ°, μλ νλ¦μ μ λμ λ°λΌκ°μ§ λͺ»νλ©΄μ WHATWG(μμκ·Έ)μ μν΄ λμ²΄λμλ€("νλ ₯νκ² λμλ€").

WHATWGμ μ ν, κ΅¬κΈ, λ§μ΄ν¬λ‘μννΈ, λͺ¨μ§λΌ κΈ°μμ΄ μ°Έκ°νκ³  μμΌλ©°, μ΄λ€ κΈ°μμ κ³΅ν΅μ μ κ°κ°μ λΈλΌμ°μ λ₯Ό κ°μ§κ³  μλ€λ μ μ΄λ€ (μ¬νλ¦¬, ν¬λ‘¬, μ£μ§, νμ΄μ΄ν­μ€).

### 3. [Can I use?](https://caniuse.com/)

μΉ νμ€μλ λΆκ΅¬νκ³  κ° λΈλΌμ°μ λ§λ€ νμ€μ μ€μνλ μ λκ° μλ‘ λ€λ₯΄λ€. ("μΉ ννΈν")

λ°λΌμ, μ¬μ©μλ€μ μ μ¬μ΄νΈλ₯Ό ν΅ν΄ μ΄λ€ μΉ κΈ°μ μ΄ νΉμ  λΈλΌμ°μ μμ μ§μλλμ§ νμΈν  μ μλ€.

<span style="color:red">λΉ¨κ°: X</span>	<span style="color:green">μ΄λ‘: O</span>	<span style="color:lightgreen">μ°λ: β³</span>

### 4. λΈλΌμ°μ μ μ­ν 

> μλ²μ urlμ ν΅ν΄ μμ²­μ λ³΄λ΄λ©΄, html λ¬Έμ λ°μλ‘ μλ΅μ λ°λλ€.
>
> **λΈλΌμ°μ λ html λ¬Έμλ₯Ό ννμ΄μ§λ‘ λ°κΏμ€λ€.**

### 5. ν¬λ‘¬ κ°λ°μ λκ΅¬ 

- λ§μ°μ€ μ°ν΄λ¦­ > κ²μ¬ > μ’μΈ‘ μλ¨μ λ²νΌ(![image-20210802225047975](web_html.assets/image-20210802225047975.png)) ν΄λ¦­νμ¬ νλ©΄μ ν­λͺ© μ ν
- Ctrl+Shift+I (κ°λ°μ λκ΅¬ νΌμΉκΈ°) > Ctrl+Shift+C (ν­λͺ© μ ννκΈ°) ν΅ν΄ νλ©΄μ ν­λͺ© μ ν

ν­λͺ©μ μ ννλ©΄ ν΄λΉ ν­λͺ©μ λνλ΄λ html λ¬Έμμ λ΄μ©μ νμΈν  μ μλ€.

μ¬κΈ°μ μ°ν΄λ¦­ > Copy > Copy Selectorμ ν΅ν΄ CSS μ νμλ₯Ό νμΈν  μ μλ€.

<br/>



## 1. HTML π

---

### 0. HTML μ΄λ?

> Hyper Text Markup Language

β	**μΉ μ»¨νμΈ μ <u>μλ―Έ</u>μ <u>κ΅¬μ‘°</u>λ₯Ό μ μνλ μΈμ΄.**

- Hyper Text: 'μ΄μ 'κ³Ό 'λ€μ'λ§ μ‘΄μ¬νλ κΈ°μ‘΄μ μ νμ  νμ΄μ§ κ΅¬μ‘°μμ λ²μ΄λ, μ°Έμ‘°λ₯Ό ν΅ν΄ ν λ¬Έμμμ λ€λ₯Έ λ¬Έμλ‘ μ¦μ μ κ·Ό κ°λ₯ν, λΉμ νμ  κ΅¬μ‘°μ νμ€νΈ(***νμ΄νΌλ§ν¬*** νμ€νΈ)

- Markup: νμ€νΈμ μ­ν μ λΆμ¬νλ κ², λ¬Έμμ κ° λΆλΆμ΄ μ΄λ€ μ­ν /μλ―Έλ₯Ό κ°μ§λμ§ λͺλͺνλ κ² (μ λͺ©μ μ λͺ©, λ³Έλ¬Έμ λ³Έλ¬Έμ΄λΌκ³  λ§νΉνλ κ²)

  γ΄ κ΅¬μ‘°λ₯Ό μ‘λ κ²

  γ΄ Markup Language: νκ·Έ λ±μ μ΄μ©ν΄ νμ€νΈμ κ΅¬μ‘°λ₯Ό λͺμνλ μΈμ΄

  β	(μ) HTML, Markdown

  β	*β»μ£Όμ: HTMLμ νλ‘κ·Έλλ° μΈμ΄κ° μλλ€!*

  β	![Html is not a programming language aprogrammerlife.com](web_html.assets/html_is_not_a_programming_language.jpg)

  νλ‘κ·Έλλ° μΈμ΄λ <u><μ μ₯, μ‘°κ±΄, λ°λ³΅></u>μ μΈ κ°μ§ νΉμ±μΌλ‘ μ μν  μ μλ€.

  μ΄μ λ¬λ¦¬, HTMLμ μ­ν μ λ°μ΄ν°λ₯Ό κ΅¬μ‘°ννμ¬ νννλ κ²μ΄λ€.

(β» μ°Έκ³ : [μ΅μ΄μ μΉμ¬μ΄νΈ](http://info.cern.ch/))

### 1. κΈ°λ³Έκ΅¬μ‘°

```html
<!DOCTYPE html>			<!--HTML λ¬Έμ μμμ κΌ­ μμ±! html5λ‘ λ λ¬Έμμμ νμν¨-->
<html lang="en">
<head>
    <meta charset="UTF-8">		<!--<meta>: λ©νμ λ³΄-->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>		<!--λΈλΌμ°μ  ν­ λ±μ μ νλ μ΄λ¦-->
</head>
<body>
    
</body>
</html>
```

(VS Codeμμ `html:5`λ₯Ό ν­ν€λ‘ μλμμ±νλ©΄ μμ κΈ°λ³Έκ΅¬μ‘°λ₯Ό λ°λ‘ μ»μ μ μλ€.)

* html μμ: <html> ~ </html>
  * HTML λ¬Έμμ μ΅μμ μμ
  * λ¬Έμμ rootμ λ»ν¨
  * headμ bodyλ‘ μ΄λ£¨μ΄μ§
* head μμ: <head> ~ </head>
  - HTML λ¬Έμμ λ©νμ λ³΄*
  - CSS μ μΈλ μ¬κΈ°μ ν¨
  - <u>λΈλΌμ°μ μ λνλμ§ μμ</u>
* body μμ: <body> ~ </body>
  * <u>λΈλΌμ°μ  νλ©΄μ λνλλ μ λ³΄</u>

**β» μ°Έκ³ **

<details>
<summary>Open Graph Protocol π±</summary>
<div markdown="1">
    - HTML λ¬Έμμ λ©νμ λ³΄λ₯Ό λνλ΄λ κ² <br>
    - νμ΄μ€λΆμμ λ§λ€μ΄μ, νμ¬ μμ£Ό λ§μ κ³³μμ μ¬μ©λκ³  μμ<br>
    <img src="web_html.assets/20210815-211613.jpg">
    </div>
</details>


   <br/>

#### βΊ DOM(Document Object Model) νΈλ¦¬

<img src="web_html.assets/1200px-DOM-model.svg.png" alt="Document Object Model - Wikipedia" style="zoom:25%;" />

- κ° νκ·Έλ₯Ό κ°μ²΄λ‘μ μ κ·Όν  μ μλλ‘ νΈλ¦¬ λͺ¨μμΌλ‘ κ΅¬μ‘°νν κ² (for λ¬Έμμ κ΅¬μ‘°νλ νν)

- λ€μ¬μ°κΈ°λ₯Ό κΈ°μ€μΌλ‘ κ° νκ·Έλ₯Ό κ°μ²΄λ‘ λ³Έλ€ β κ°μ²΄λ³λ‘ μ‘°μ Β· μμ  Β· μ­μ κ° κ°λ₯ν κ΅¬μ‘°

- μ¦, μΉνμ΄μ§μ κ°μ²΄ μ§ν₯μ  νν.

- HTMLμ λ€μ¬μ°κΈ°λ '2 spaces'λ₯Ό κΈ°μ€μΌλ‘ νκΈ°λ‘ νλ€. 

  (μ¬μ€ λ€μ¬μ°κΈ°κ° λ¬Έμμ κΈ°λ₯μ μν₯μ λ―ΈμΉμ§λ μμ§λ§, κ°λμ±κ³Ό μ μ§λ³΄μμ μ©μ΄μ±μ μν΄ ν΅μΌλ κΈ°μ€μ κ°λ κ²μ΄ μ€μνλ€.)

<br/>

#### βΊ μμ(element)

- μμ νκ·Έ, μ’λ£ νκ·Έ, λ΄μ©

  ```html
  <h1>
      contents
  </h1>
  ```

- λ΄μ©μ΄ μλ νκ·Έλ μλ€: br, hr, img, input, link, meta
- μμλ€μ΄ μ€μ²©λ (nested) μ μλ€.
- μ¬λ«λ μμ΄ λ§λλ‘ μ λλ€ β HTML νΉμ±μ μ€λ₯λ₯Ό μλ €μ£Όμ§ μμ λλ²κΉμ΄ νλ€λ―λ‘.

#### β Semantic Tags

***μλ―Έ*** λ₯Ό κ°μ§ νκ·Έ.

`<div>` λ± μλ―Έλ‘ μ  μμκ° κ²°μ¬λ νκ·Έλ₯Ό, μλ―Έκ° λΆμ¬λ μ¬λ¬ μ’λ₯μ νκ·Έλ‘ κ΅¬λΆνκΈ° μμνλ€.

μλ―Έλ₯Ό κ°μ§κ³  μλ―Έλ₯Ό ν΅ν΄ μ°κ²°λ μ κΈ°μ μΈ λ°μ΄ν°λ‘ κ΅¬μΆνκ³ μ νλ λ°μμ μλ©ν± μΉ κ°λμΌλ‘ μ°κ²°λλ€.

β λ¨λ½μ κ΅¬λΆκ³Ό λ΄μ© μ§μμ΄ κ°λ₯ν΄μ§μΌλ‘μ¨ μ½λ νμμ΄ μ¬μμ§ (κ°λμ± ν₯μ, μ μ§λ³΄μ μ©μ΄ν΄μ§)

β μκ° μ₯μ μΈμ μΉ μ¬μ©μ λμμ£Όλ λκ΅¬μΈ μ€ν¬λ¦° λ¦¬λμ κ²½μ°, μλ§¨ν± νκ·Έλ₯Ό μΈμνμ¬ λ§νκΈ°μ λ³νλ₯Ό μ€ μ μλ€κ³  νλ€. λ΄μ© μ λ¬μ μλ§¨ν± νκ·Έκ° λμ± μ μ©νλ€.

β SEO(Search engine optimization)

β	βΈ [''μΉ μ κ·Όμ±''μ΄λ?](http://www.wa.or.kr/m1/sub1.asp)  π¬ (μ: [λ€μ΄λ² λλ¦¬](https://nuli.navercorp.com/))

- `div`: κ΅¬μ‘°λ₯Ό μ‘μμ£Όλ μ©λμ νκ·Έ (λΈλ­ μμ)

  ---

- `header`: ν€λ(λ¨Έλ¦¬λ§)

- `nav`: λ΄λΉκ²μ΄μ λ°

- `aside`: μ¬μ΄λ λ°

- `section`: λ¬Έμμ μΌλ°μ μΈ κ΅¬λΆ

- `article`: λ¬Έμ, νμ΄μ§, μ¬μ΄νΈ λ΄μμ λλ¦½μ μΌλ‘ κ΅¬λΆλ μμ­

- `footer`: νλ¨ λΆλΆ

<br/>

#### βΊ μμ±(attribute)

νκ·Έ μμ μ°μΈλ€.

```html
<img src="../image/my_photo.png" alt="logo">
```

```html
μμ±λͺ: src
μμ±κ°: ../image/my_photo.png
```

- νκ·Έλ§λ€ κ°μ§ μ μλ μμ±μ΄ λ€λ₯΄λ€.
- μμ±μ μ¬λ νκ·Έμ μμ±νλ€.
- κ·μΉ
  - '=' κΈ°νΈμ μμͺ½μ κ³΅λ°±μ λμ§ μκΈ°λ‘ νλ€.
  - μμ±κ°μ ν°λ°μ΄ν(" ")λ₯Ό μ¬μ©ν΄ λνλ΄κΈ°λ‘ νλ€.

<details>
<summary>HTML Global Attribute</summary>
<div markdown="1">
    - νκ·Έμ μκ΄μμ΄ μ¬μ©μ΄ κ°λ₯ν μμ± <br>
    - id, class, hidden, lang, style, tabindex, title<br>
    </div>
</details>

<br/>

### 2. HTML λ¬Έμ κ΅¬μ‘°ν

[πλ§μ΄ μ¬μ©λλ νκ·Έ μμλ³΄κΈ°](https://www.advancedwebranking.com/html/ )

- κ·Έλ£Ή μ»¨νμΈ 

`<p>`: paragraph

`<hr>`: horizontal rule (κ°λ‘μ  μκΉ)

`<ol>, <ul>`: ordered list, unordered list

- νμ€νΈ κ΄λ ¨ μμ

`<a>`: λ§ν¬ μ°κ²°

`<b>`μ `<strong>`: λ³Όλμ²΄ (<strong>μ΄ μλ§¨ν± νκ·Έ)

`<i>`μ `<em>`: μ΄ν€λ¦­μ²΄(<em>μ΄ μλ§¨ν± νκ·Έ)

`<span>`: `<div>`μ²λΌ κ΅¬μ‘°λ₯Ό μ‘μμ£Όμ§λ§, μΈλΌμΈ μμ

`<br>`: line break

`<img>`: μ΄λ―Έμ§

- table

`<tr>, <td>, <th>`: table rows, table data, table height

`<thead>, <tbody>, <tfoot>`: table head, body, foot

`<caption>`

`<colspan>, <rowspan>`: μ λ³ν© μμ±

`<col>, <colgroup>`

`scope μμ±`: νμ΄λΈμ th λλ td λ±μ μμκ² μ¬μ©, μ»¬λΌ(column)μΈμ§ ν(row)μΈμ§ μλ €μ€.

- **form** β

  : μλ ₯ μ λ³΄λ₯Ό μλ²λ‘ λ³΄λ΄μ€ (`<input>`κ³Ό ν¨κ» λ§μ΄ μ¬μ©λ¨)

  (μ) λ‘κ·ΈμΈ μ°½, κ²μ μ°½

  - action μμ±: μ΄λλ‘ λ³΄λΌμ§ (εΏ)
  - method μμ±: μ΄λ€ http methodλ₯Ό μ νν μ§

- **input** β

  : μ¬μ©μκ° μλ ₯ν  μ μλ κ³΅κ°

  - type μμ±: κΈ°λ³Έκ°μ "text". "password" μ°λ©΄ ****λ‘ λ§μ€νΉ λ¨.

    [πνμ μ’λ₯ νμΈνκΈ°](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input)

  - autofocus μμ±: λ¬Έμ μλ‘κ³ μΉ¨ μ λ°λ‘ μ»€μ κΉλ°κ±°λ¦¬λ©° μλλ‘ ν΄μ€

  - required μμ±: μ νμ΄ νμκ° λλλ‘

  - checked μμ±: κΈ°λ³Έκ°μ΄ μ²΄ν¬λ μνκ° λλλ‘

  - `<label>`: for μμ±κ³Ό μΌμΉνλ id κ°μ μμμμ, λΌλ²¨λ§ λλ¬λ μ νλκ² ν΄μ€
  - `<select>` νκ·Έ + μλμ κ°κ°μ `<option>` νκ·Έ: λλλ€μ΄

---

### VS Code λ¨μΆν€

- Alt + ν΄λ¦­: μ»€μ μ¬λ¬ κ°
- ! + Tab: μλμμ±(emmit)
- Alt + λ°©ν₯ν€: μμλ μ€ μ΄λ κ°λ₯
- Alt + Shift + λ°©ν₯ν€: λ³΅μ¬
- Ctrl + D: κ°μ λ¨μ΄λ₯Ό μ°Ύμ (D μ°μν΄μ λλ¬μ μ¬λ¬ κ° κ³ λ₯Ό μ μμ) - ν λ²μ μμ νκΈ°

### μ°Έκ³  μ¬μ΄νΈ

- html-css-js.com
- web.dev/learn/css
- bootstrap
