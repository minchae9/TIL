# 팔로우 기능을 JavaScript로 구현하기

## 팔로우를 할 수 있는 프로필 페이지 (profile.html)

```django
<!-- profile.html -->
{% extends 'base.html' %}

{% block content %}
...
{% with followings=person.followings.all followers=person.followers.all %}
  <div>
    <div>
      팔로잉 : {{ followings|length }} / 팔로워 : 
        <span id="followers-count">{{ followers|length }}</span>   <!--팔로워 수 갱신-->
    </div>
    {% if request.user != person %}
      <div>
        <form id="follow-form" data-profile="{{ person.pk }}">
          {% csrf_token %}
          {% if request.user in followers %}
            <button id="follow-button" class="btn">언팔로우</button>
          {% else %}
            <!--기본 색상 지정-->
            <button id="follow-button" class="btn btn-primary">팔로우</button>	
          {% endif %}
        </form>
      </div>
    {% endif %}
  </div>
{% endwith %}
...
<!-- 여기에 <script> -->
{% endblock %}
```

## 팔로우 기능 함수 (views.py)

```python
# views.py

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        # 팔로우 받는 사람
        you = get_object_or_404(get_user_model(), pk=user_pk)
        me = request.user

        # 나 자신은 팔로우 할 수 없다.
        if you != me:
            if you.followers.filter(pk=me.pk).exists():
            # if request.user in person.followers.all():
                # 팔로우 끊음
                you.followers.remove(me)
                following = False
            else:
                # 팔로우 신청
                you.followers.add(me)
                following = True

            follow_status = {
                'following': following,	# 팔로우 여부
                'count': you.followers.count(),	# 팔로워 수
            }
        return JsonResponse(follow_status)	# Json 형식으로 위 정보를 보냄
    return HttpResponse(status=401)	# 인증 기준 충족 미달 시, 상태 정보 전송 (에러)
```

## 팔로우 데이터를 주고받는 javascript 

```javascript
/* profile.html의 script */

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  // 팔로우 구현을 하려면
  // 1. 팔로우 폼 선택하여, submit 시 콜백 함수 실행하도록
  const followForm = document.querySelector('#follow-form')
  followForm.addEventListener('submit', function (event) {
    // 폼의 기본 기능 끄고
    event.preventDefault()
    // 요청 보내서 필요한 정보(팔로우 여부, 팔로워 수) 응답 받기
      // 그러려면 프로필 주인 pk, csrf token 필요
    const person = event.target.dataset.profile
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    axios.post(`http://127.0.0.1:8000/accounts/${person}/follow/`, {}, {
      headers: {'X-CSRFToken': csrftoken}
    })

    /*
    (다른 형태)
    axios({
     method: 'post',
     url: `http://127.0.0.1:8000/accounts/${person}/follow/`,
     headers: {'X-CSRFToken': csrftoken}
    })
    */

    // 응답에서 받은 정보를 변수에 저장하기
    .then(response => {
      // console.log(response)
      const following = response.data.following
      const count = response.data.followers_count
      
      // 2. 팔로우 버튼 변경하기
      const followButton = document.querySelector('#follow-button')
      if (following) {
        followButton.innerText = '언팔로우'
        followButton.className = "btn-secondary"
        // followButton.setAttribute('class', 'btn-secondary')
      } else {
        followButton.innerText = '팔로우'
        followButton.className = "btn-primary"
        // followButton.setAttribute('class', 'btn-primary')
      }
      
      // followButton.classList.toggle('btn-primary')

      // 3. 팔로워 수 변경하기
      const followCount = document.querySelector('#followers-count')
      followCount.innerText = count
    })
    // 로그인하지 않았으면, 에러 코드 비교 후 로그인 화면으로
    .catch(error => {
      if (error.response.status === 401) {
        window.location.href = '/accounts/login/'
      }
    })
  })
</script>
```

- csrf token: [axios 공식 문서](https://github.com/axios/axios#axiosposturl-data-config) 먼저 보고, [django 공식 문서](https://docs.djangoproject.com/en/3.1/ref/csrf/#setting-the-token-on-the-ajax-request) 보기, [속성 선택자 관련 자료](https://wallel.com/css-%EC%86%8D%EC%84%B1-%EC%84%A0%ED%83%9D%EC%9E%90-%EC%A0%95%EB%A6%AC-css-attribute-selector/)

  - axios에서는 `axios.post(url[, data[, config]])` 형식으로 인자를 넣는다.

  - django에서는 CSRF token을 아래와 같이 넣는다: (headers를 위의 config 자리에 넣으면 된다.)

    ```javascript
    const request = new Request(
        /* URL */,
        {headers: {'X-CSRFToken': csrftoken}}	// 👈
    	);
    	fetch(request, {
          method: 'POST',
          mode: 'same-origin'  // Do not send CSRF token to another domain.
          }).then(function(response) {
        // ...
          }
        );
    ```

  - 속성 선택자: `태그명[속성=속성값]` 과 같이 접근할 수 있다.

- dataset: [공식 문서](https://developer.mozilla.org/ko/docs/Learn/HTML/Howto/Use_data_attributes)

  - 시작 태그에 `data-`로 시작하는 속성을 만들고 거기에 속성값을 입력하면,

    JavaScript에서 접근할 때 `요소.dataset.*`(*는 data-의 뒷부분)으로 해당 값에 접근할 수 있다.

- HTTP 401: Unauthorized (인증이 안 됐을 때)

- HTTP 403: Forbidden (접근 권한이 없을 때)

- 팔로우 버튼의 색을 바꿀 때, class를 변경하는 방법: [참고자료1(Stack Overflow)](https://stackoverflow.com/questions/195951/how-can-i-change-an-elements-class-with-javascript), [참고자료2(ko.javascript.info)](https://ko.javascript.info/styles-and-classes#ref-424)
  - [classList](https://developer.mozilla.org/ko/docs/Web/API/Element/classList)
  - [className](https://developer.mozilla.org/ko/docs/Web/API/Element/className)
  - [setAttribute()](https://developer.mozilla.org/ko/docs/Web/API/Element/setAttribute)
  - [toggle](https://developer.mozilla.org/en-US/docs/Web/API/DOMTokenList/toggle)

