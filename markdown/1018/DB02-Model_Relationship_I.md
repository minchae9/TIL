# Model Relationship 01

**1:N 관계에 대해 알아보자!**

## Foreign Key (외래 키)

> RDBMS에서 한 테이블의 필드 중, 다른 테이블의 행을 식별할 수 있는 키
>
> - (주로) 참조되는 테이블의 Primary key(기본 키)를 가리킨다. (유일한 값이어야 함)	***참조무결성**
> - 참조하는 테이블의 행에는 참조되는 테이블에 없는 값이 나타날 수 없다.
> - 여러 행이 참조되는 테이블의 한 행을 동시에 참조할 수 있다.
> - 외래 키는 *참조하는* 테이블에 존재한다. 참조<u>되는</u> 테이블에 존재하지 않는다.

![19화 19. 외래키 이해하기](https://t2.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/brunch/service/user/1ai5/image/pjJuT7d48leZ27dFgUpwCjYVeZg.jpg)

> **참조 무결성**
>
> 데이터베이스 관계 모델에서 관련된 두 테이블의 일관성을 의미한다.
>
> : 참조하는 테이블의 외래 키 필드의 값은, 참조되는 테이블의 기본 키 값으로 존재해야 한다.
>
> ***"자식은 무조건 부모가 있다!"***

<br/>

#### 모델 관계 형성

- Comment 모델 클래스 예시

  ```python
  class Article(models.Model):
      pass	# 부모(참조되는) 클래스
  
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE) # ✔
      content = models.CharField(max_length=300)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      
      def __str__(self):
          return self.content
  ```

  - Django에서 외래 키는 ForeignKey field를 사용해서 만들어진다. 

  - 2개의 위치 인자가 반드시 필요하다:

    - 참조되는 model 클래스

    - `on_delete` 옵션

      : 참조되는 객체가 사라지면 참조하는 객체를 어떻게 처리할지를 정의한다.	***데이터 무결성**

      (주로 `on_delete=models.CASCADE`로, CASCADE 옵션이 주를 이룬다. 

      CASCADE 옵션은, 참조되는 테이블이 삭제되는 참조하는 테이블도 연쇄적으로 삭제되도록 하는 것이다.)

  - 외래 키 필드의 이름은 참조되는 클래스를 소문자로, 그리고 단수형으로 바꿔서 만든다. (국룰)

    → 지정된 이름에 '_id'가 붙은 이름의 외래 키 필드가 형성된다.

    > ✔ comment라는 Comment 클래스의 인스턴스 객체를 생성했을 때,
    >
    > arTicle을 Article 클래스의 인스턴스 객체라고 한다면
    >
    > comment.article 에는 arTicle가 대응되고, comment.article_id에는 arTicle.pk이 대응된다.
    >
    > comment.article에 객체를 넣으면 그 객체의 PK를 article_id 필드에 넣어준다. (실제로 생성되는 필드는 article_id 하나다.)
    >
    > comment.article_id는 말 그대로 컬럼을 가리키기 때문에 참조되는 모델의 기본키가 대응되는 것이다.
    >
    > **즉, `comment.article_id`는 참조되는 article의 pk 값을 가리키고, `comment.article.pk`와 같다. `comment.article`은 참조되는 객체를 가리킨다.**

> **데이터 무결성**
>
> 데이터의 정확성과 일관성을 유지하고 보증하는 것이다. DB와 RDBMS에서 중요한 개념이다.
>
> **복합 키**
>
> 하나의 컬럼으로는 데이터의 구분이 불가능할 때, 여러 컬럼을 합쳐서 키로 사용하는 것

<br/>

### 0. 댓글 구현

**클래스의 인스턴스 생성 ⇢ 값 넣고 ⇢ save()로 저장**

```shell
comment = Comment()
comment.content = '내용'
# 여기서는 comment.save() 해도 저장되지 않는다. 외래 키 필드 값이 빠졌기 때문.

article = Article.objects.get(pk=1)
comment.article = article	# 객체를 comment.article에 할당하면 pk값을 추출하여 저장해줌.
comment.save()

# comment.article과 comment.article_id 비교
comment.article_id
>> 1
comment.article
>> <Article: title>
```



#### '참조'와 '역참조'

- **참조**

  : 1:N 관계에서 N이 1을 참조하는 것

  즉, 참조하는 테이블이 참조되는 테이블을 참조하는 것.

  >  Comment(N)에서 Article(1)을 참조하려면, `comment.article.메서드()`로 사용하면 된다.

- **역참조**

  : 1:N 관계에서 1이 N을 참조하는 것

  참조되는 테이블이 역으로 참조하는 테이블을 참조하는 것.

  > Article(1)에서 Comment(N)을 참조하려면, `article.comment_set.메서드()`로 사용하면 된다.

  ✔ 외래 키 클래스 이름에 **'_set'**이 붙은 manager가 생성된다. (∵ 1은 N에 대한 정보가 없으므로)

※ 'related_name' 옵션

역참조 시에, 참조하는 모델의 외래 키 필드에서 'related_name' 옵션을 지정함으로써

외래 키 이름에 '_set' 이 붙은 이름 외에 새롭게 지정한 이름으로 매니저를 사용할 수 있다.

(이때, 변경되기 전 _set이 붙은 이름은 더 이상 사용할 수 없게 된다.)

### 1. 댓글 생성

1. 댓글 폼 작성

   → 이때, 외래 키 필드는 사용자 입력을 받지 않도록 하기

   ```python
   # forms.py
   from .models import Comment
   
   class CommentForm(forms.ModelForm):
       
       class Meta:
           model = Comment
           exclude = ('article',)
   ```

2. url 작성

   ```python
   # urls.py
   app_name = 'articles'
   urlpatterns = [
   	path('<int:pk>/comments/', views.comments_create, name='comments_create'),
   ]
   ```

3. detail 페이지에서 폼 보이기

   ```python
   # views.py
   from .forms import CommentForm
   
   def detail(request, pk):
       article = get_object_or_404(Article, pk=pk)
       comment_form = CommentForm()	# CommentForm() 객체 전달하기
       context = {
           'article': article,
           'comment_form': comment_form,
       }
       return render(request, 'article/detail.html', context)
   ```

   ```django
   <!-- detail.html -->
   ...
   <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
     {% csrf_token %}
     {{ comment_form }}
     <input type="submit">
   </form>
   ```

4. 생성 view 작성

   ```python
   # views.py
   
   @require_POST
   def comments_create(request, pk):
       if request.user.is_authenticated:	# 인증된 사용자만 허용
           article = get_object_or_404(Article, pk=pk)
           comment_form = CommentForm(request.POST)
           if comment_form.is_valid():
               comment = comment_form.save(commit=False)   # 인스턴스 생성, 저장은 X
               comment.article = article # 사용자 입력을 받지 않으므로, article 넣어주기
               comment.save()  # 저장
           return redirect('articles:detail', article.pk)
       return redirect('accounts:login')	# 인증되지 않았다면 로그인 페이지로 이동
   ```

   ✔ `save()`메서드의 commit 인자

   - 기본값: True

   - False로 설정하면, 데이터베이스에 저장하지 않고, 객체를 리턴해준다.

     저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용된다.

### 2. 댓글 조회

article에서 comment를 역참조한다.

1. article에서 comment를 모두 가져와서 context로 전달

   ```python
   # views.py
   from .models import Article, Comment
   
   def detail(request, pk):
       article = get_object_or_404(Article, pk=pk)
       comment_form = CommentForm()
       comments = article.comment_set.all()	# 모든 댓글 가져오기
       context = {
           'article': article,
           'comment_form': comment_form,
           'comments': comments,
       }
       return render(request, 'article/detail.html', context)
   ```

2. detail 페이지에서 출력

   ```django
   <!-- detail.html -->
   ...
   <h4>댓글 목록</h4>
   <ul>
     {% for comment in comments %}
       <li>{{ comment.content }}</li>
     {% endfor %}
   </ul>
   ```

   

### 3. 댓글 삭제

1. urls.py

   댓글을 삭제한 후, 댓글이 있던 게시글 페이지에 머물도록 하려면 comment의 pk 외에도 article의 pk가 요구된다. 따라서, variable routing을 통해 별도의 pk를 하나 더 들고 오도록 한다.

   ```python
   # urls.py
   app_name = 'articles'
   urlpatterns = [
       path(
           '<int:article_pk>/comments/<int:comment_pk>/delete/',
       	views.comments_delete,
       	name='comments_delete'
       ),
   ]
   ```

2. delete 함수 만들기

   ```python
   # views.py
   
   @require_POST
   def comments_delete(request, article_pk, comment_pk):
       if request.user.is_authenticated:	# 인증된 사용자만 허용
           comment = get_object_or_404(Comment, pk=comment_pk)
           comment.delete()
       return redirect('articles:detail', article_pk)
   ```

3. detail.html에 삭제 버튼 만들기

   ```django
   <!-- detail.html -->
   
   ...
   <h4>댓글 목록</h4>
     {% if comments %}
       <p><b>{{ comments|length }}개의 댓글이 있습니다.</b></p>	<!-- 댓글 개수 -->
     {% endif %}
     <ul>
       {% for comment in comments %}
         <li>
           {{ comment.content }}
           <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST" class="d-inline">
             {% csrf_token %}
             <input type="submit" value="DELETE">
           </form>
         </li>
       {% empty %}			<!-- 댓글이 없는 경우, 대체 컨텐츠 출력 -->
         <p>댓글이 없어요.</p>
       {% endfor %}
     </ul>
   ```

