##### 작성자: 김민채

##### 날짜: 07-16-2021

##### ==주제: 챗봇 만들기==

---

Telegram Bot API를 사용하여 텔레그램 봇을 만들고, 특정 채팅방에 메시지를 전송하기.

0. `import requests`를 통해 라이브러리 사용

1. 텔레그램 내 'BotFather' 계정을 통해 new bot을 생성, 이름을 정하고, auth token을 부여받는다. 

2. `https://api.telegram.org/bot<token>/METHOD_NAME`의 형태로 쿼리를 전송할 수 있다. 

3. getUpdates 메소드로 chat_id(채팅방 번호)를 찾는다.

4. `sendMessage` 메소드를 사용하여,

   `https://api.telegram.org/bot<token>/sendMessage?chat_id=CHAT_ID&text=TEXT` 형태의 message url을 생성한다.

5. `requests.get(message_url)`로 메시지 전송을 실행한다.

> 참고: 4번에서, 메소드 뒤에 '?' 붙이고, 뒤이어 부가정보를 '&'로 연결하여 적는다.
>
> `sendMessage` 메소드에서 chat_id와 text는 필수 매개변수이다.

