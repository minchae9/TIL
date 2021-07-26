#0726

# 딕셔너리 생성방법에 따른 식별자 차이

## 1. 내장함수 `dict()`

인라인 코드 규칙을 따르므로, **key가 변수 규칙을 따름. 즉, 식별자 규칙을 따르게 됨!**

=> 변수 이름이 i) 숫자만, ii) 숫자로 시작, iii) '문자열' 형태가 허용되지 않음!

=> 이 경우, key를 변수를 만든다고 여기면 편하다.

✔[파이썬 튜터에서 보기](http://pythontutor.com/visualize.html#code=dict%28name%3D'tony'%29%0A%23%20dict%281%3D'tony'%29%0A%23%20dict%281tony%20%3D%20'apple'%29%0A%23%20dict%28'melon'%20%3D%2060%29&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) 

## 2. { }로 딕셔너리 만들기

key를 literal 그대로 받아들임. 따라서, 변수 규칙이 아니라 key값을 구성하는 규칙을 따르게 됨.

=> immutable 객체 사용하기

✔ [파이썬 튜터에서 보기](http://pythontutor.com/visualize.html#code=my_dict%20%3D%20%7B'name'%3A'tony',%201%3A'tony',%20'1name'%3A%20'tony',%20%281,%202%29%3A%20'a'%7D&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

