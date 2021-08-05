# 0804 워크샵 문제 (hws파일 보기)

#부트스트랩

1.

- list는 기본적으로 점이 생김 → `list-unstyled` 클래스 적용

- text는 기본적으로 상속이 되지만, a 태그 자체가 파랑 글씨 등의 형식을 갖고 있으므로, 텍스트 형식을 추가 적용하려면 a 태그 안에다 적용해줘야 함.

- flex 사용은, 부모 클래스에다 d-flex (혹은 d-inline-flex) 적고, 그 외에 축 등과 관련된 요소 적어서 사용하면 된다!
  간단!!!!

- 여기서는 sticky-top과 fixed-top의 차이점이 드러나지 않음.
  (sticky-top은 특정 영역이 있어서 그 안에서는 제자리를 유지하고, 아니면 따라내려 가는데, 여기서는 sticky의 영역이 문서 전체라서.)

2.

- d-flex 사용.
- 수평, 수직 정렬: justify-content와 align-items
  가로로 배치되어 있으니, flex-column으로 세로 배치로 바꿔준다.

4.

모든 p태그에는 bottom 마진이 들어있다! → p태그에 `mb-0`

# 0805 practice (shop)

1. nav
a 태그의 `href` 속성에 # 쓰면 이동없음 설정 가능.
navbar에 있는 space-between  이 navbar 요소들을 끝과 끝으로 보내준다.

2. section
class `img-fluid`: 반응형으로 맞춰줌.

3. article
✔ grid cards 이용! 

4. footer
url 뒤에 붙는 '/' 는 append slash인데, 쓰는 게 권장됨.
이미지의 크기 설정은 style 속성으로 수동으로 추가해 주기, 혹은 css로 클래스 만들어서 적용해주기!
`img-fluid`: a 태그 안에서 a 태그의 크기만큼.
a 태그에 icon-size 만든 거 적용시켜주고 img-fluid 넣으면 반응형 .

### 참고사이트
[animate.style](animate.style)
ㄴ 애니메이션 효과
[fontawesome.com](fontawesome.com)

