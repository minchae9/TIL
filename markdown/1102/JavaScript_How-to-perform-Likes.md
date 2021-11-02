# 좋아요 기능을 JavaScript로 구현하기

## 좋아요 페이지 (index.html)

```django
<!-- index.html -->
{% extends 'base.html' %}

{% block content %}
	...
    <div>
      <!-- class 지정하여 선택 & data-id 이름에 값 넣어줌으로써 data에 접근 가능하게 -->
      <!-- form으로 데이터 보내는 거 아니므로, action과 method 지우기 -->
      <form id="like-form" data-pk="{{ article.pk }}">
        {% csrf_token %}
        {% if request.user in article.like_users.all %}
          <button class="like-{{ article.pk }}">♥</button>
        {% else %}
          <button class="like-{{ article.pk }}">♡</button>
        {% endif %}
      </form>
    </div>

    <p>
      <!-- id 값을 부여하여 태그를 유일하게 선택할 수 있게 함 -->
      <span id="like-count-{{ article.pk }}">
        {{ article.like_users.all|length }}
      </span>
      명이 이 글을 좋아합니다.
    </p>
    ...
  {% endfor %}
  <!-- 여기에 <script> 태그 -->
{% endblock %}

```

## 좋아요 기능 함수 (views.py)

```python
# views.py

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)

        if article.like_users.filter(pk=request.user.pk).exists():
        # if request.user in article.like_users.all():
            # 좋아요 취소
            article.like_users.remove(request.user)
            liked = False	# 좋아요 정보를 전달하기 위해
        else:
            # 좋아요 누름
            article.like_users.add(request.user)
            liked = True

        status_data = {
            'like': liked, # 좋아요 여부
            'count': article.like_users.count(),	# 좋아요 개수
        }
        return JsonResponse(status_data)	# html 문서가 아니라 json 데이터를 보내기
    return HttpResponse(status=401)	# 로그인 html 문서가 아니라 상태 정보를 보내기
```

## 좋아요 데이터를 주고받는 javascript (index.html의 script)

```javascript
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  // 좋아요 기능 구현하기
  // 1. 좋아요 누르면, 버튼 바뀌기
  // 2. 좋아요 누르면, 좋아요 누른 사람 수 바뀌기
  <script>
    const likeforms = document.querySelectorAll('#like-form')
    likeforms.forEach(function (form) {
      form.addEventListener('submit', function (event) {
        // 0. 기존 form 기능(데이터 전송) 때문에 제기능 못함 -> 기본 기능 끄기
        event.preventDefault()

        // 1. 요청을 통해 필요한 정보 받기(json): 좋아요 여부, 좋아요 수
          // 그러려면 article.pk 정보와 csrf token이 필요하다.
          // article.pk 정보: data-* 이름으로 정보를 저장하고, dataset.*으로 접근할 수 있다.
          // csrf token: 속성 선택자로 가져옴
        const articleId = event.target.dataset.pk
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken').value
        axios.post(`http://127.0.0.1:8000/articles/${articleId}/likes/`, {}, {
          headers: {'X-CSRFToken': csrftoken}
        })
        .then(response => {
          // console.log(response)
          const like = response.data.like
          const count = response.data.count
        
          // 1. 좋아요 버튼 변경: 버튼도 article.pk 정보 가지고 있어야 한다!
          const likeButton = document.querySelector(`.like-${articleId}`)
          if (like) {
            likeButton.innerText = '♥'
          } else {
            likeButton.innerText = '♡'
          }
          // 2. 좋아요 수 갱신: article.pk 정보 가지고 있어야 한다!
          const likeCount = document.querySelector(`#like-count-${articleId}`)
          likeCount.innerText = count
        })
        // 로그인하지 않았다면, view에서 에러를 발생시킴 -> 에러면 로그인 화면으로
        .catch((error) => {
          if (error.response.status === 401) {
            window.location.href = '/accounts/login/'
          }
        })
      })
    })
  </script>
```

- (2), (4)번 참고자료 (csrf token): [axios 공식 문서](https://github.com/axios/axios#axiosposturl-data-config) 먼저 보고, [django 공식 문서](https://docs.djangoproject.com/en/3.1/ref/csrf/#setting-the-token-on-the-ajax-request) 보기

- (3)번 참고자료: [공식 문서](https://developer.mozilla.org/ko/docs/Learn/HTML/Howto/Use_data_attributes)

