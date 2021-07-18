##### 작성자: 김민채

##### 날짜: 07-16-2021

##### ==주제: 네이버 API 사용하여 쇼핑 탭에서 최저가 검색==

---

0. `import requests`를 통해 라이브러리를 사용한다.

1. 네이버 개발자 센터의 Application > 애플리케이션 등록 메뉴로 이동하여 네이버 클라이언트 ID와 네이버 클라이언트 시크릿을 부여받는다.

2. 쇼핑 검색을 하면 json 형태로 출력해주는 API의 요청 URL을 기록한다:

   `https://openapi.naver.com/v1/search/shop.json`

3. headers를 설정한다.

4. 필수 매개변수인 query를 지정하고, 해당 변수가 요청 URL의 뒤에 `?query=검색어` 형태로 붙게끔 해준다.

5. `requests.get()`으로 요청URL과 headers를 전달하고, 필요한 항목을 딕셔너리의 key로 조사하여 출력할 수 있다.

   > 참고: '\n'은 줄바꿈

   