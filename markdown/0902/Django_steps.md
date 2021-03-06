# π Django λ¨κ³

## κ°μνκ²½ μμ± ~ νλ‘μ νΈ λ° μ± μμ±

```bash
# [1] κ°μνκ²½
$ python -m venv venv
$ source venv/Scripts/activate

# [2] django μ€μΉ
# (1)
$ pip install django
$ pip freeze > requirements.txt			# μ€μΉ νλ‘κ·Έλ¨ λͺ©λ‘ μμ±
$ pip list							  # νμΈ
# (2)
$ pip install -r requirements.txt


# [3] νλ‘μ νΈ μμ±
$ djago-admin startproject pjtname .	# μ£Όλ‘ config

# [4] μ± μμ±
$ python manage.py startapp appname

# [5] λ‘μΌ νμΈ (μλ² κ°λ)
$ python manage.py runserver

# [*] μΆκ° λ¨κ³: .gitignore νμΌ λ§λ€κΈ°
# gitignore.io λ‘ μ μνμ¬ .gitignore νμΌμ λ§λ€μ΄ μ μ₯νλ€.
```

### 1. `settings.py` μΆκ° μ€μ 

- '[4] μ± μμ±' μ΄ν, `INSTALLED_APPS`μ μμ±λ μ±μ λ±λ‘ν΄μ€λ€. **(μ€μβ­)**
- `LANGUAGE`λ₯Ό 'ko-kr' λ‘ μ€μ νλ€.
- `TIME_ZONE`μ 'Asia/Seoul' λ‘ μ€μ νλ€.

```python
INSTALLED_APPS = [
    'articles',
    ...
]

LANGUAGE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```

---

## `templates` ν΄λ μμ±

#### 1. κΈ°λ³Έ ννλ¦Ώ

κΈ°λ³Έ ννλ¦Ώ μμμ μμ±νμ¬ νμ©ν  μ μλλ‘, μ±κ³Ό νλ‘μ νΈ λ λ²¨μ `templates` ν΄λλ₯Ό μΆκ°λ‘ μμ±νκ³ , μμ `base.html` νμΌμ λ§λ€μ΄μ€λ€.

- `! + Tabν€`λ‘ htmlμ boilerplateλ₯Ό λ§λ€κ³ ,

- bootstrap CDNμ κ°μ Έμ¨λ€ (CSSμ Js).

- `<body>` λΆλΆμ λ€μκ³Ό κ°μ΄ λ§μΆ°μ€λ€:

  ```django
  <body>
      <div class="container">
          {% block content %}
          {% endblock content %}
      </div>
  </body>
  ```

- νλ‘μ νΈ ν΄λμ `settings.py`μμ ννλ¦Ώ λλ ν λ¦¬λ₯Ό ν΄λΉ ν΄λλ‘ μμ ν΄μ€λ€. (μμ§ λ§β)

  ```python
  TEMPLATES = [
      {
          ...,
          'DIRS': [BASE_DIR / 'templates'],
          ...
      }
  ]
  ```

  

#### 2. μ± ννλ¦Ώ

- μ± λ΄μ `templates` ν΄λλ₯Ό μμ±νκ³ , νμ ν΄λλ‘ μ± μ΄λ¦μ ν΄λλ₯Ό νλ λ λ§λ λ€.

  μμΌλ‘λ ν΄λΉ ν΄λ λ΄μ html νμΌμ ννλ¦Ώμ μ μ₯νλ€.

  μ΄νμ ννλ¦Ώ html νμΌμ `extends` νκ·Έλ₯Ό νμ©νμ¬, λ§λ€μ΄λ `base.html`μ κ°μ Έμμ νμ©νλ€.

  ```django
  {% extends 'base.html' %}
  
  {% block content %}
  <!--template λ΄μ©-->
  {% endblock content %}
  ```

---

## `models.py`μ λ°μ΄ν° κ΄λ¦¬νλ class μμ±νκΈ°

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    # id
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}λ² κΈ - {self.title} / {self.content}'
```

- Modelμ classλ‘ μ μλλ€. 

  - Djangoμ `models.Model` ν΄λμ€λ₯Ό κΈ°λ³ΈμΌλ‘ μμλ°λλ€.
  - `.`μ ν΅ν΄ μΈμ€ν΄μ€μμ ν΄λμ€ λ³μμ μ κ·Όν  μ μλ€.

- κΈ°λ³Έ ν€(PK) νλ(id)λ Djangoμ μν΄ μλμΌλ‘ μμ±λλ€.

- κ·Έ μΈ νλλ₯Ό μ μν΄μ€λ€.

  γ΄ κ° νλμ νμμΈμμ μ μνκΈ° π [django documentation](https://docs.djangoproject.com/en/3.2/ref/models/fields/)

- `__str__` ν¨μλ λ°μ΄ν° μ μ₯ μ λ³΄μ¬μ§λ μΆλ ₯κ°μ μ§μ νκΈ° μν΄ μ¬μ©λλ€.

  μ§μ νμ§ μμΌλ©΄, `<appname: appname object (pk)>` ννλ‘ μΆλ ₯λλ€.

---

## 3λ¨κ³λ‘ μΉ νμ΄μ§ μμ±νκΈ°

## : <u> urls.py 	β 	views.py	β 	templates</u>

### 1. `urls.py`

#### 1. νλ‘μ νΈμ `urls.py`λ₯Ό, νΉμ ν μ±μΌλ‘ κ²½λ‘λ₯Ό μ λ¬νλ κ΄λ¬ΈμΌλ‘ λ§λ λ€.

- `include` λͺ¨λμ μΆκ°νμ¬, νΉμ  μ±μ κ²½λ‘λ₯Ό ν¬ν¨νκ³  μλ urlμ 1μ°¨μ μΌλ‘ λΆλ₯νμ¬, ν΄λΉνλ μ±μ `urls.py` λ‘ ν΅νλλ‘ ν΄μ€λ€.

```python
from django.contrib import admin
from django.urls import path, include	# include μΆκ°

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    # κΈ°λ³Έ μ£Όμ λ€ articles/κ° λΆμΌλ©΄, 
    # articles μ±μ urls.pyλ‘ ν₯νμ¬ λλ¨Έμ§ κ²½λ‘λ₯Ό μ΄ν΄λ³΄κ² νλ€.
]
```



#### 2. μ± ν΄λμ μ `urls.py`λ₯Ό μμ±νκ³ , μΈλΆ κ²½λ‘λ₯Ό μ μ₯νλ€.

```python
from django.urls import path
from . import views				# νμ¬ ν΄λμμ views.py κ°μ Έμ¨λ€.

app_name = 'articles'			# app_name
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'), 
    path('<int:pk>/delete/', views.delete, name='delete'),   # DELETE
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),      # UPDATE
]
```

- ```python
  from . import views
  ```

  νμ¬ ν΄λμμ views.pyλ₯Ό κ°μ Έμ¨λ€.

- ```python
  app_name = 'articles'
  urlpatterns = [
      path('', views.index, name='index'),
      ...
  ]
  ```

  (1) `app_name`κ³Ό pathμ `name`μ μ€μ νκ³  μ΄νμ urlμ μμ±ν  λ μ μ΄μ€μΌλ‘μ¨, urlμ νλμ½λ©νμ§ μκ³  κ°λ¨νκ² ννν  μ μμΌλ©°, μ±μ΄ μ¬λ¬ κ°μΌ λ κ²½λ‘κ° μμ΄λ κ²μ λ°©μ§νλ μ­ν μ νλ€.

  β	(μ) `{% url 'articles:index' %}`

  (2) articles μ±μΌλ‘ λ€μ΄μ¨ κ²½λ‘μ λλ¨Έμ§ λΆλΆμ΄ `''` μ κ°μΌλ©΄ (λ³Έ κ²½μ°μλ, κΈ°λ³Έ κ²½λ‘), `views.py`μ index ν¨μλ‘ μ΄λνμ¬ μ€ννλ€. 

- ```python
  path('<int:pk>/', views.detail, name='detail'),
  ```

  ***Variable Routing***

  > urlμ λ³μλ₯Ό ν¬ν¨μν΄μΌλ‘μ¨, νλμ pathλ‘ μ¬λ¬ κ²½λ‘λ₯Ό κ°λ¦¬ν¬ μ μκ² ν΄μ€λ€. 
  >
  > λ³μμ λ°λΌ κ°λ¦¬ν€λ κ²½λ‘κ° λ¬λΌμ§λ€.

  (μ) μμ κ²½μ°, `http://127.0.0.1:8000/articles/1`μ μ£Όμκ° μ λ¬λμλ€λ©΄,  pk(κΈ°λ³Έ ν€)κ° 1μΈ κ²½μ°λ₯Ό κ°λ¦¬ν€λ©°, μ¬κΈ°μλ μ¬λ¬ κ²μκΈ μ€μμλ 1λ² κ²μκΈμ μμΈ νμ΄μ§λ₯Ό κ°λ¦¬ν€λ ν¨μλ‘ μ°κ²°λλ€.

### 2. `views.py`

νΉμ  urlμ ν΅ν΄ μΉ μ¬μ΄νΈμ μ μνλ©΄ μ΄λ€ λ°μ΄ν°λ₯Ό μ΄λ€ νμμΌλ‘ λ΄λ³΄λΌμ§λ₯Ό κ²°μ νλ ν¨μλ€μ΄ μλνλ€. `views.py`μ κ·Έλ° ν¨μλ€μ΄ λͺ¨μ¬μλ€. Viewλ Model κ·Έλ¦¬κ³  Templateκ³Ό μ°κ²°λμ΄ μ΄λ₯Ό μ΄λ»κ² μ²λ¦¬ν μ§ κ²°μ νλ€.

```python
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
#READ
def index(request):
    articles = Article.objects.all()[::-1]  # μμ λ°λλ‘ (νμ΄μ¬)
    # articles = Article.objects.order_by('-id') # μμ λ°λλ‘ (ORM)
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    article = Article(title=title, content=content)
    article.save()
    # return render(request, 'articles/create.html') # create.html νμ΄μ§ λμ΄
    return redirect('articles:detail', article.pk)  # detail νμ΄μ§λ‘ redirect

def detail(request, pk):
    # urlμμ pk λ°μμ€κ³ , ν΄λΉ pkμ ν΄λΉνλ κ±° μ°Ύμμ€κΈ°
    article = Article.objects.get(pk=pk) 
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)  # μ£Όμμ°½μ μΉλ©΄ GETλ°©μ -> μ­μ  X

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article, # μμ ν  κ²μκΈ λ³΄μ¬μ£ΌκΈ°
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    # μ¬μ©μκ° editμμ μλ ₯ν κ°μΌλ‘ μμ νλ κ²
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)  # μμ λ κΈμ μμΈ νμ΄μ§λ‘ μ΄λ
```

- model κ°μ Έμ€κΈ°

  ```python
  from .models import Article
  ```

  ν¨μ λ΄μμ λͺ¨λΈμ μ¬μ©νκΈ° μν΄ νμνλ€.

- render

  ```python
  def index(request):
      articles = Article.objects.all()[::-1]
      context = {
          'articles': articles,
      }
      return render(request, 'articles/index.html', context)
  ```

  <img src="Django_steps.assets/μΊ‘μ².PNG" alt="μΊ‘μ²" style="zoom:80%;" />

  (1) `urls.py`μμ `path('', views.index, name='index')`λ₯Ό ν΅ν΄ μ¨ κ²½λ‘λ μ ν¨μλ₯Ό κ±°μΉκ² λλ€.

  ν¨μλ μμ²­μ μΈμλ‘ λ°μ, `render()`μ ν΅ν΄ μλ΅μ λλ €μ€ μ μλ€.

  (2) μμ²­κ³Ό ννλ¦Ώ(`'articles/index.html'`)μ νμμΈμμ΄λ©°, ννλ¦Ώμμ νμ©ν  μΈμλ₯Ό `context`λΌλ κΎΈλ¬λ―Έλ‘ λ¬Άμ΄ μ λ¬ν  μ μλ€.

  (3) μ ν¨μμμλ `Article` ν΄λμ€μ λͺ¨λ  κ°μ²΄λ₯Ό κ°μ Έμ€λ λ©μλλ₯Ό νμ©νμ¬ ν΄λΉ QuerySet κ°μ²΄λ₯Ό λ³μ `articles` μ μ μ₯νκ³  μλ€.

  μ΄λ₯Ό ννλ¦Ώμμ νμ©νκΈ° μν΄ contextλ₯Ό κ΅¬μ±νλ©°, contextλ {'key': value} λΌλ λμλλ¦¬ ννλ‘ λ§λ€μ΄μ§λ€. ννλ¦Ώμμ key κ°μΌλ‘ ν΄λΉ λ³μμ μ κ·Όν  μ μλ€.

- redirect

  ```python
  from django.shortcuts import render, redirect
  
  def update(request, pk):
      article = Article.objects.get(pk=pk)
      # μ¬μ©μκ° editμμ μλ ₯ν κ°μΌλ‘ μμ νλ κ²
      article.title = request.POST.get('title')
      article.content = request.POST.get('content')
      article.save()
      return redirect('articles:detail', article.pk)
  ```

  - `redirect` λͺ¨λ μΆκ°ν΄μ£ΌκΈ°

  - (1) `redirect`λ μ§μ ν urlλ‘ μ΄λμμΌμ€λ€.

    (2) `article` λ³μλ κΈ°λ³Έ ν€ κ°μ΄ μΈμλ‘ μ λ¬λ°μ κ°μ΄ λ°μ΄ν° νλλ₯Ό μ μ₯ν λ³μλ€. λ°μ΄ν°λ₯Ό `get()`μΌλ‘ κ°μ Έμ¬ λλ ν΄λΉνλ κ°μ΄ νλμ¬μΌ νκΈ° λλ¬Έμ κΈ°λ³Έ ν€ κ°μΌλ‘ νλ¨νλ κ² μΌλ°μ μ΄λ€.

    (3) μ¬μ©μκ° μλ ₯κ°μ `<input>`μ μλ ₯νκ² λλ©΄, λμλλ¦¬ ννλ‘ μ λ¬μ΄ λλ€. μ΄λ, ν΄λΉ html νμΌμμ λ°μ΄ν°λ₯Ό μ λ¬νλ λ°©μ(GET, POST)μ λ°λΌ GET λλ POSTμ λ°μ΄ν° κ°μ΄ λ€μ΄μλ€. λ°λΌμ, get() ν¨μμ key κ°μ μ λ¬νμ¬ μνλ λ°μ΄ν°λ₯Ό μΆμΆν  μ μλ€.

    μ¬κΈ°μ μ λ¬λλ key κ°μ λ°μ΄ν°κ° μλ ₯λ `<input>`μ `name` μμ±κ°μ λ°λ₯Έ κ²μ΄λ€.

    (4) λ°μ΄ν°λ₯Ό μ λ¬λ°μ ν, λ°λμ saveλ₯Ό ν΄μ€μΌ λ°μ΄ν°λ² μ΄μ€μ μ μ₯μ΄ λλ€!

    (5) μμ ν¨μλ μλ ₯κ°μΌλ‘ μ λ¬λ°μ λ°μ΄ν°λ₯Ό μ λ¬λ°μ κΈ°λ³Έν€μ μΌμΉνλ λ°μ΄ν°μ μ μ₯νκ³ , λ°μ΄ν°μ κΈ°λ³Έν€ κ°κ³Ό ν¨κ» urlμ μ΄λμμΌμ€λ€.

### 3. ννλ¦Ώ νμΌ(html)

μμμ μΈκΈν λ°μ κ°μ΄, νμ ν΄λλ₯Ό μΆκ°ν΄μ ννλ¦Ώ νμΌμ μ μ₯νλ€.

<img src="Django_steps.assets/image-20210902171838692.png" alt="image-20210902171838692" style="zoom:80%;" />

- κΈ°λ³Έ μμ

  ```django
  {% extends 'base.html' %}
  
  {% block content %}
  <!--template λ΄μ©-->
  {% endblock content %}
  ```

- μ μμ 

  - `form`

    - ν΅μ¬ μμ± 2κ°λ₯Ό μ μν΄μ€λ€:

      - action: μ΄λλ‘ λ³΄λΌμ§

        url νκ·Έλ₯Ό μ¬μ©νμ¬ λ―Έλ¦¬ μ§μ ν μ΄λ¦μΌλ‘ urlμ κ΅¬μ±νμ¬ μμ±ν  μ μλ€.

      - method: μ΄λ»κ² λ³΄λΌμ§

        - GET: DBμ λ³νλ₯Ό μΌκΈ°νμ§ μλ κ²½μ° (λ¨μ μ‘°ν)
        - POST: DBμ λ³νλ₯Ό κ°μ Έμ€λ κ²½μ° (μμ , μ­μ  λ±)

    - `csrf_token`μ λ£μ΄μ€λ€. (μμ§ λ§β)

      γ΄ djangoλ‘ νμ¬κΈ ν΄λΉ νμλ₯Ό μ λ’°ν  μ μλλ‘ ν΄μ€. λ£μ§ μμΌλ©΄ μλνμ§ μλλ€.

  - `{% url '' %}`

    - ν΄λΉ λ¬Έμμ΄ μμ urlμ μμ±ν  λλ `articles:index`μ κΌ΄λ‘ μ μ΄μ€λ€.

    - μ΄λν  κ²½λ‘μ ν¨μκ° μΆκ° μΈμλ₯Ό μκ΅¬νλ κ²½μ° (μ: pk), λ¬Έμμ΄ λ€μ λνμ¬ μμ±ν΄μ€λ€.

      ```django
      {% url 'articles:delete' article.pk %}
      ```

---

## Admin νμ΄μ§ λ§λ€κΈ°

### 0. κΈ°λ³Έ νμ΄λΈ μμ± νμΈ

κΈ°λ³Έ νμ΄λΈμ΄ μμ±ν μνμμ κ΄λ¦¬μ κ³μ μ μμ±ν  μ μλ€.

### 1. κ΄λ¦¬μ κ³μ  λ§λ€κΈ°

```bash
$ python manage.py createsuperuser
```

- κ³μ  μμ± ν, `/admin`μΌλ‘ κ°μ κ΄λ¦¬μ νμ΄μ§μ λ‘κ·ΈμΈν  μ μλ€.

### 2. `admin.py`μ DB λ±λ‘νκΈ°

```python
rom django.contrib import admin
from .models import Article

# Register your models here.
# μ¬μ©μ μλ ₯λ§ λ³΄μ΄λλ°, μμ±μκ°, μμ μκ°λ λ³΄κ³  μΆμ΄
class ArticleAdmin(admin.ModelAdmin):   
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')
    # Article λͺ¨λΈμμ μμ±ν κ±° κ°μ Έμ΄

admin.site.register(Article, ArticleAdmin)
```

- `admin.py`λ κ΄λ¦¬μ μ¬μ΄νΈμ κ°μ²΄κ° κ΄λ¦¬μ μΈν°νμ΄μ€λ₯Ό κ°μ§κ³  μμμ μλ €μ€λ€.

  `from .models import Article`μ ν΅ν΄ Article κ°μ²΄λ₯Ό μ΄μ μΆκ°ν΄μ€λ€.

  ```python
  admin.site.register(Article)
  ```

- `list_display`λ models.pyμμ μ μν κ° νλμ κ°λ€μ admin νμ΄μ§μ μΆλ ₯νλλ‘ ν΄μ€λ€.

  νμ΄λΈ ννλ‘ λμ€κ² λλ€.

---

## λ΄κ° λλ, κ°μ₯ μ€μν μ 

1. μ μ μ°¨λ¦¬κ³  λ΄κ° λ­νλμ§ νμνλ©΄μ μ½λ μμ±νκΈ°.

   μ΄λ€ λΆλΆμ μ±μμΌ νλμ§ μκ°νκ³  μ²΄ν¬νλ©΄μ, λμΉμ§ μλλ‘ μ§μ€νμ¬ λΉ λ₯΄κ² μ±μλ£κΈ°.

   μ€κ°μ μκ°μ΄ λΉλ©΄ μμ΄λ²λ¦¬κΈ° μΌμ€λ€.

2. λ¨κ³μ μΆ©μ€νμ.

   λ¨κ³λλ‘λ§ λ°λΌν΄λ λ°μ νλ€.

3. μλ€κ°λ€ νλλΌ μ μ  μμνλ°, μ μ  μ‘κΈ°.

## νμ©νλ©΄ μ’μ ν!

- Alt + Shift + λ°©ν₯ν€: μ§μ ν μ€μ μ½λλ₯Ό μλλ‘ λ³΅μ¬ κ°λ₯

- Ctrl + Alt + ν΄λ¦­: μ»€μ μ¬λ¬ κ° μμ±νμ¬ ν λ²μ μ¬λ¬ λ² μλ ₯ κ°λ₯

- (Bootstrap μ¬μ©ν  λ,) `h1.fw-bold` μ κ°μ΄ λ¨μΆνμ¬ νκ·Έμ ν΄λμ€λ₯Ό ν λ²μ μμ±ν  μ μλ€. 

  γ΄ ν΄λμ€λ₯Ό μ ννκ² μμμΌ μ¬μ©μ΄ κ°λ₯νλ€. λͺ¨λ₯΄λ©΄ [bootstrap docs](https://getbootstrap.com/docs/5.1/getting-started/introduction/)λ₯Ό μ°Έκ³ νμ.