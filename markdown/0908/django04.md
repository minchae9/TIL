๐ฌ ์์ ์์๋๊ธฐ, ํด์ผํ  ์ฌํญ ๊ธฐ์ตํ๊ธฐ

# Static Files

## 1. Static Files (์ ์  ํ์ผ)

> ์ฌ์ฉ์์ ์์ฒญ์ ๋ฐ๋ผ ๋ณํ๋ ๊ฒ์ด ์๋๋ผ, ๋ฏธ๋ฆฌ ์ ์๋ ๊ฒ์ ๊ทธ๋๋ก ๋ณด์ฌ์ฃผ๋ฉด ๋๋ ํ์ผ.
>
> ***๊ฐ๋ฐ์๊ฐ ์ฐ๋ ๊ฒ***

- ### โ ๊ตฌ์ฑ

  <django ์ ์ด๋ฏธ ๋์ด์๋ ๋ถ๋ถ>

  1. settings.py์ INSTALLED_APPS์ `django.contrib.staticfiles`๊ฐ ์๋์ง ํ์ธํ๋ค.

     : django ๋ผ์ด๋ธ๋ฌ๋ฆฌ์ contrib ํจํค์ง ์ staticfiles ์ฑ

     : django์์ ์ ์  ํ์ผ์ ๊ด๋ฆฌํด์ฃผ๋ ์ฑ

  2. settings.py์์ `STATIC_URL`์ ์ ์ํ๋ค.

     ```python
     # settings.py
     STATIC_URL = '/static/'
     ```

  < ์ฐ๋ฆฌ๊ฐ ํด์ผํ  ๋ถ๋ถ>

  3. ํํ๋ฆฟ์์ `img ํ๊ทธ`๋ฅผ ์ฌ์ฉํ  ๋, `src` ์์ฑ๊ฐ์ **static ํํ๋ฆฟ ํ๊ทธ**๋ก url์ ๋ง๋ค์ด์ค๋ค.

     ```django
     {# template #}
     {% load static %}
     <img src="{% static 'articles/example.jpg' %}" alt="sample image">
     ```

     - `static ํ๊ทธ` ์์ ๊ฒฝ๋ก๋ ํด๋น ์ด๋ฏธ์ง์ url์ ์ค์ ํ  ๋, `ํธ์คํธ์ฃผ์/static/`์ ๋ท๋ถ๋ถ์ ์ด์ด์ง ๋ถ๋ถ์ด๋ค. static์ ์ฐพ์๋ณผ ๋ ๊ธฐ๋ณธ์ ์ผ๋ก 'app ๋ด static ํด๋'๋ฅผ ์ฐพ์๋ณด๋๋ฐ, ์ด๋ฆ๊ณต๊ฐ ๋ถ๋ฆฌ๋ฅผ ์ํด ํ์ ํด๋๋ก ์ฑ ์ด๋ฆ์ ํด๋๋ฅผ ํ๋ ๋ ๋ง๋ค์ด์ฃผ๋ฉด:

       `์ฑ/static/์ฑ์ด๋ฆ/example.jpg`์ ๊ฒฝ๋ก์ ์๊ฒ ๋๋ ๊ฒ์ด๋ค.

     - *load๋ฅผ ํ์๋ก ํด์ผ ํ๋ค.*

  4. ์ฑ์ `static ํด๋`์ ์ ์  ํ์ผ์ ์ ์ฅํ๋ค.

<br/>

- ### `static ํ๊ทธ` ๋ฏ์ด๋ณด๊ธฐ

  - `{% load static %}`

    : ํน์  ๋ผ์ด๋ธ๋ฌ๋ฆฌ๊ฐ ๊ฐ์ง ๋ชจ๋  filter์ tag๋ฅผ ํด๋น template์์ ์ฌ์ฉํ๊ธฐ ์ํจ

    : `extends ํ๊ทธ` ์๋์ ์์ฑํ๋ค.

    (โป์ฐธ๊ณ : extends ํ๊ทธ๋ ์ด๋ค ํ๊ทธ๋ณด๋ค ์ฐ์ ํ์ฌ ์์นํด์ผ ํ๋ค - ํํ๋ฆฟ์ ์ต์๋จ)

  - `{% static '' %}`

    - `STATIC_ROOT`์ ์ ์ฅ๋ ์ ์  ํ์ผ์ ์ฐ๊ฒฐ

      โป ์ฐธ๊ณ : STATIC_ROOT --- ๋ฐฐํฌ ์์ ์ฌ์ฉํจ. ๊ฐ๋ฐ ์์ ์ฌ์ฉ X.

      > ์๋น์ค ๋ฐฐํฌ ์์, django๊ฐ ๋ชจ๋  ์ ์  ํ์ผ์ ๋ค๋ฅธ ์น ์๋ฒ์ ์ ๊ณตํ๊ธฐ ์ํ ๊ฒฝ๋ก.
      >
      > collectstatic ๋ช๋ น์ด๋ก ํ์ฌ django์์ ์ฌ์ฉํ๋ ๋ชจ๋  ์ ์  ํ์ผ์ ์์งํ๋ค.
      >
      > ๊ฐ๋ฐ ๊ณผ์ ์์๋ settings.py์ DEBUG ๊ฐ์ด True์ด๋ฏ๋ก ์์ฉํ์ง ์์ง๋ง, ์ต์ข ๋จ๊ณ์ ์ง์  settings.py์ ์์ฑํด์ฃผ์ด ์ฌ์ฉํ๋ค.
      >
      > ```bash
      > $ python manage.py collectstatic
      > ```

      ```python
      STATIC_ROOT = BASE_DIR / 'staticfiles'
      ```

  - `STATIC_URL` (์์ฑ๋์ด ์์)

    ```python
    # settings.py
    STATIC_URL = '/static/'
    ```

    > ์ ์  ํ์ผ์ ๋ํ url์ ์์ฑํ๋ค.

    - ๊ธฐ๋ณธ์ ์ผ๋ก ์ฑ/static/ ๊ฒฝ๋ก๋ฅผ ํ์ํ๊ณ , ์ถ๊ฐ์ ์ผ๋ก `STATICFILES_DIRS`์ ์ ์๋ ์ถ๊ฐ ๊ฒฝ๋ก๋ฅผ ํ์ํ๋ค.

      - ์ถ๊ฐ ๊ฒฝ๋ก๋ `STATICFILES_DIRS`์ ๋ฆฌ์คํธ ํํ๋ก ์์ฑํ๋ค.

        ```python
        STATICFILES_DIRS = [
            BASE_DIR / 'static',
        ]
        ```

    - end slash(/)๊ฐ ํ์์ด๋ค.

  <img src="django04.assets/staticroute.PNG" alt="staticroute" style="zoom:61%;" />

## 3. Image Upload

### [1] ๊ธฐ๋ณธ ์ค์ 

> **Media File**์ด๋?
>
> ***์ฌ์ฉ์๊ฐ***  ์น์์ ์๋ก๋ํ๋ ์ ์  ํ์ผ (user-uploaded)

#### โ ๊ตฌ์ฑ

1. settings.py์ `MEDIA_ROOT`์ `MEDIA_URL`์ ์ค์ ํ๋ค. (๋ชจ๋ ์ถ๊ฐํด์ค์ผ ํจ)

   ```python
   # settings.py
   # MEDIA_ROOT: ๋ฏธ๋์ด ํ์ผ์ ๋ณด๊ดํ  ๋๋ ํ ๋ฆฌ์ ์ ๋๊ฒฝ๋ก (๋๋ ํ ๋ฆฌ๋ ์๋ก๋ ์ ์๋์์ฑ)
   MEDIA_ROOT = BASE_DIR / 'media'
   
   MEDIA_URL = '/media/'
   ```

2. models.py์์ `upload_to` ์์ฑ์ ์ ์ํ์ฌ, ํ์ผ์ ์ฌ์ฉํ  MEDIA_ROOT์ ํ์ ๊ฒฝ๋ก๋ฅผ ์ง์ ํ๋ค. (`upload_to`๋ optional)

3. url์ด ๋ง๋ค์ด์ง ์ ์๋๋ก urls.py์ ์ถ๊ฐ ๊ฒฝ๋ก๋ฅผ ์์ฑํด์ค๋ค.

   ๐ [๊ณต์๋ฌธ์์์ ์ฝ๋ ๋ค๊ณ ์ค๊ธฐ](https://docs.djangoproject.com/ko/3.2/howto/static-files/#serving-files-uploaded-by-a-user-during-development)

   ![urls](django04.assets/urls.PNG)

   ์์ ์ฝ๋๋ฅผ ์์ฑํด์ค๋ค.

   - settings.MEDIA_URL: media file public URL์ ์๋ฏธ

   - document_root: ์ค์  ํด๋น ๋ฏธ๋์ด ํ์ผ์ ์ด๋์ ์๋์ง

     ์ด๋, document_root๋ ํค์๋ ์ธ์๋ก media file์ด ์์นํ ๊ฒฝ๋ก๋ฅผ ์ ๋ฌํ๋ค.

4. ์๋ก๋ ๋ ํ์ผ์ url์ django์ url ์์ฑ์ ํตํด ์ป์ ์ ์๋ค:

   ```django
   <img src="{{ article.image.url }}" alt="{{ article.image }}"
   ```

<br/>

- #### ImageField

: ์ด๋ฏธ์ง ์๋ก๋์ ์ฌ์ฉํ๋ Model field

- **FileField**๋ฅผ ์์๋ฐ๋ ์๋ธ ํด๋ฆฌ์ค์ด๋ค - FileField์ ์์ฑ๊ณผ ๋ฉ์๋๋ฅผ ์ฌ์ฉํ  ์ ์๋ค.

  ๐ [FileField](https://docs.djangoproject.com/en/3.2/ref/models/fields/#filefield)

  ๐ [ImageField](https://docs.djangoproject.com/en/3.2/ref/models/fields/#imagefield)

- ์ ํจ์ฑ ๊ฒ์ฌ๋ฅผ ํ๋ค.

- DB์ ImageField ์ปฌ๋ผ ์์๋ *์ด๋ฏธ์ง ํ์ผ ์์ฒด๊ฐ ์๋, **๊ฒฝ๋ก**๊ฐ <u>๋ฌธ์์ด</u>๋ก ๋ค์ด๊ฐ๋ค.*

  (์ด์ : ์ฑ๋ฅ)

- ImageField๋ฅผ ์ฌ์ฉํ๋ ค๋ฉด, [Pillow ๋ผ์ด๋ธ๋ฌ๋ฆฌ](https://pillow.readthedocs.io/en/stable/installation.html)์ ์ค์น๊ฐ <u>ํ์</u>์ ์ด๋ค.

  ```bash
  $ pip install Pillow
  ```

  

<br/>

- FileField - ์ ํ์ธ์ ์ค `upload_to`

  > ์ด๋ฏธ์ง๋ฅผ ์๋ก๋ํ  ๋๋ ํ ๋ฆฌ, ๊ทธ๋ฆฌ๊ณ  ํ์ผ ์ด๋ฆ์ ์ค์ ํ  ์ ์๋ค.

  ์์ฑ๋ฐฉ์ 2๊ฐ์ง: *(`models.py`์ ์์ฑํ๋ ๊ฒ)*

  (1) ๋ฌธ์์ด๋ก ์์ฑ

  - ๊ฒฝ๋ก์ ์์์ ์ ๋ `MEDIA_ROOT/` ์ดํ์ด๋ค.
  - ํ์ด์ฌ์ `strftime()` ํ์ ์ฐธ์กฐํ๊ธฐ: [์ฌ๊ธฐ](https://docs.python.org/3/library/datetime.html#datetime.date.strftime)

  ```python
  # models.py
  class Article(models.Model):
      # MEDIA_ROOT/uploads/ ๊ฒฝ๋ก๋ก ์๋ก๋
      upload = models.FileField(upload_to='uploads/')
      # MEDIA_ROOT/uploads/์ฐ/์/์ผ ๊ฒฝ๋ก๋ก ์๋ก๋
      upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
  ```

  (2) ํจ์ ํธ์ถ

  - ์ธ์: (1) instance	 (2) filename

    - instance

      : ๋ชจ๋ธ์ ์ธ์คํด์ค. ์์ง DB์ ์ ์ฅ๋์ง ์์์ pk๊ฐ์ด ์กด์ฌํ์ง ์์ ์ ์๋ค.

    - filename

      : ๊ธฐ์กด ํ์ผ์ ์ ๊ณต๋ ํ์ผ ์ด๋ฆ

    - ๋ชจ๋ธ ํด๋์ค ์์ชฝ์ ํจ์ ํ๋๋ฅผ ๋ง๋ ๋ค:

      ```python
      # models.py
      def articles_image_path(instance, filename):
          # MEDIA_ROOT/user_<pk>/ ๊ฒฝ๋ก๋ก, <filename> ์ด๋ฆ์ผ๋ก ์๋ก๋
          return f'user_{instance.pk}/{filename}'
      
      class Article(models.Model):
          image = models.ImageField(upload_to=articles_image_path)
      ```

      ๊ฒฝ๋ก๊ฐ์ ๋ง๋ค๊ณ , ๊ทธ๊ฑธ `upload_to`์ ์์ฑ๊ฐ์ผ๋ก ๋ฃ๋๋ค.
      
      > โ **Question**: ํจ์์ ์ธ์๋ฅผ ๋ฃ์ด์ฃผ์ง ์๋๋ฐ ์ด๋ป๊ฒ ์ฌ์ฉ๋๋ ๊ฑธ๊น?
      
      > โ **Answer**: Django๊ฐ instance์ filename์ ํด๋นํ๋ ์ ์ญ๋ณ์๋ฅผ ๊ฐ์ง๊ณ  ์์ด์, `upload_to`์ ๊ฐ์ผ๋ก ํจ์๊ฐ ์ ๋ฌ๋๋ฉด, ์๋์ผ๋ก ์ฒซ ๋ฒ์งธ ์ธ์๋ก instance๋ฅผ, ๋ ๋ฒ์งธ ์ธ์๋ก filename์ ๋ฃ์ด์ ๊ฐ์ ๋ฐ๋๋ค.
      >
      > ํจ์๋ช์ด๋ ํจ์์ ์ธ์ ์ด๋ฆ๊ณผ๋ ์๊ด์ด ์๋ค.

<br/>

### [2] CREATE

#### โ ๊ตฌ์ฑ

##### 1) ImageField ์์ฑ

```python
# models.py
class Article(models.Model):
    ...
    image = models.ImageField(upload_to='images/', blank=True)
```

- `blank=True`์ ์๋ฏธ๋:

  โ DB์๋ ๋น ๋ฌธ์์ด(' ')์ด ์ ์ฅ๋๋ค.

  - ๊ธฐ์กด์ฌํ๋ ๊ฒ์๊ธ๋ค ์ค ์ด๋ฏธ์ง ํ๋๊ฐ ๋น์ด์๋ ๊ฒฝ์ฐ, ๋น ๊ฐ์ผ๋ก๋ DB์ ์ ์ฅ๋  ์ ์๊ฒ๋, ์ฆ ๋น ๊ฐ๋ ํ์ฉํ๊ฒ๋ ํ๊ฒ ๋ค๋ ๊ฒ

  - ์ด๋ฏธ์ง ํ๋์ ๋น ๊ฐ์ ํ์ฉํจ์ผ๋ก์จ ์ด๋ฏธ์ง๋ฅผ ์ ํ์ ์ผ๋ก ์๋ก๋ํ  ์ ์๋๋ก ํ๊ฒ ๋ค๋ ๊ฒ

  - ์ฆ, ์ ํจ์ฑ ๊ฒ์ฌ์์ ๋น ๊ฐ์์ ์๋ฌ๋ฅผ ์ ๊ธฐํ์ง ์๊ณ  ํ์ฉํ๊ฒ ๋ค๋ ๊ฒ!

  - **[์ฐธ๊ณ ] `null` ์์ฑ๊ณผ ๋น๊ต**

    > null์ ์๋์ ์ผ๋ก ๋น์์ ๋ํ๋ธ๋ค.

    โ ๋น ๊ฐ์ ๋ํด, ๋น ๋ฌธ์์ด์ด ์๋ NULL์ด ์ ์ฅ๋๋ค.

    - Django ์์๋ ๊ธฐ๋ณธ์ ์ผ๋ก NOT NULL ์ํ์ด๋ฉฐ, ๋น ๊ฐ์ ๋น ๋ฌธ์์ด๋ก ์ฒ๋ฆฌํ๋ค.

    - ์ฃผ์์ฌํญ:

      - ๋ฌธ์์ด ๊ธฐ๋ฐ ํ๋์๋ `null=True`๋ก ์ค์ ํ๋ ๊ฒ์ ์ง์ํด์ผ ํ๋ค.
    
        : '๋ฐ์ดํฐ ์์'์ ์๋ฏธ๊ฐ ๋ ๊ฐ์ง๋ก ์ ๋ฌ๋๋ค. ์ฆ, ์๋ฏธ๊ฐ ์ค๋ณต๋๋ค.

  โ `blank` ์์ฑ์ ์ ํจ์ฑ(validation)๊ณผ ๊ด๋ จ๋ ๊ฒ์ด๊ณ , `null` ์์ฑ์ DB ์ ์ฅ์ ๊ด๋ จ๋ ๊ฒ์ด๋ค.
  
  (null์ DB์์ ์ค๋ฅ๋ฅผ ์ผ์ผํฌ ์ ์์ผ๋ฏ๋ก ๊ฐ๊ธ์  ์ฌ์ฉํ์ง ์๋ ํธ์ด ๊ถ์ฅ๋๋ค.)

<br/>

##### 2) ํํ๋ฆฟ์ form์์ `enctype` ์์ฑ๊ฐ ์ง์ ํ๊ธฐ

```django
<form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="์์ฑ">
</form>
```

๋ชจ๋ธ์์ ์ด๋ฏธ์ง๋ฅผ ๋ฐ๊ฒ ๋๋ฉด, ModelForm์ผ๋ก ์์ฑ๋ ํผ์์๋ ์ด๋ฏธ์ง๋ฅผ ๋ฐ์ ์ ์๋ ํํ๊ฐ ๋๋ค. ์ด๋, ์ด๋ฏธ์ง๋ฅผ ๋ฐ์ ์ ์๋๋ก `enctype` ์์ฑ์ ์ถ๊ฐ๋ก ์ง์ ํด์ค์ผ ํ๋ค.

: ์์ฑ๊ฐ์ผ๋ก `multipart/form-data` ์ ์ด์ฃผ๋ฉด ๋๋ค.

: `<input type="file">`์ ์ฌ์ฉํ  ๊ฒฝ์ฐ์ ์ ์ด์ค๋ค.

โ	โบ `<input type="file">`์์ `accept` ์์ฑ

โ	๐ [MDN ๋ฌธ์](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file)

> ํ์ผ์ด ์๋ก๋ ๋  ๋ ํ์ฉํ  ํ์ผ ์ ํ์ ๋ํ๋ธ๋ค.
>
> โญ ์ค์: ํ์ผ์ ๊ฒ์ฆํ๋ ๊ฒ์ ์๋๋ค. ์ฆ, ํน์  ํ์ผ ์ ํ์ accept์ ์ง์ ํ๋ค ํ๋๋ผ๋, ๋ค๋ฅธ ํ์ผ ์ ํ์ ์ฌ๋ฆด ์ ์๋ค.
>
> โ ํ์ผ ์ ํ ํ๋ฉด์ ํน์  ํ์ผ ์ ํ๋ง ๋ฐ ์ ์๋๋ก ํํฐ๋ง ๊ธฐ๋ฅ์ ์ ๊ณตํจ์ผ๋ก์จ, ์ฌ์ฉ์ ๊ฒฝํ์ ํฅ์์ํฌ ์ ์๋ค.

<img src="django04.assets/accept.PNG" alt="accept" style="zoom:61%;" />

##### 3) views.py์ create ํจ์ ์์ ํ๊ธฐ

```python
# views.py

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        # form = ArticleForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

- ์ด๋ฏธ์ง๋ `request.POST`๊ฐ ์๋, `request.FILES`์ ๋ค์ด์๋ค. 

  ๋ฐ๋ผ์, ModelForm์ ์์๋ฐ์ ArticleForm์ ๋ ๋ฒ์งธ ์ธ์๋ก `request.FILES`๋ฅผ ์ ๋ฌํด์ฃผ์ด์ผ ํ๋ค.

  (์ด๋, data๊ฐ ์ฒซ ๋ฒ์งธ ์ธ์์ด๊ณ , files๊ฐ ๋ ๋ฒ์งธ ์ธ์์ด๊ธฐ์ ๋ ์ธ์ ๋ชจ๋ ์์น์ธ์๋ก ์์ฑํ  ์ ์๋ ๊ฒ์ด๋ค.

  ํ์ด์ฌ ๋ฌธ๋ฒ์ ๋ ์ฌ๋ฆฌ๋ฉฐ, ํค์๋ ์ธ์๊ฐ ์์น ์ธ์์ ์์ค ์ ์์์ ๊ธฐ์ตํ์.)

- ์ฐธ๊ณ 

  Q. ์ฌ์ฉ์๊ฐ ๊ฐ์ ์ด๋ฆ์ ์ด๋ฏธ์ง ํ์ผ์ ์ฌ๋ฆฌ๋ฉด ์ด๋ป๊ฒ ๋ ๊น?

  A. django์์ ์๋ก์ด ํ์ผ์ ๋ค์ชฝ์๋ ์์์ ๋์๊ฐ์ ๋ถ์ฌ์ ์๋ก ๋ค๋ฅธ ์ด๋ฆ์ผ๋ก ๋ง๋ค์ด ์ ์ฅํด์ค๋ค.

<br/>

### [3] READ

```django
<!--detail.html-->
...
<img src="{{ article.image.url }}" alt="{{ article.image }}">
```

์๋ก๋๋ ํ์ผ์ ๊ฒฝ๋ก๋ django ์์ ์ ๊ณตํ๋ `url` ์์ฑ์ ํตํด ์ป์ ์ ์๋ค.

์ด๋ฏธ์ง๋ฅผ ์กฐํํ๊ธฐ ์ํด์๋ ์๋ฒ์ ์์ฒญํด์ผ ํ๊ณ , ์๋ฒ์ ์์ฒญํ๊ธฐ ์ํ ๋ฐฉ๋ฒ์ด url ์ฃผ์์ด๋ค.

- `{{ article.image.url }}`์ url์ด๊ณ , `{{ article.image }}`๋ ๊ฒฝ๋ก๋ฅผ ๋ํ๋ด๋ ๋ฌธ์์ด๋ก, ์ด๋ฏธ์ง์ ์ด๋ฆ์ด๋ค.

<br/>

### [4] UPDATE

์ด๋ฏธ์ง๋ ์ผ๋ถ๋ง ์์ ํ๋ ๊ฒ์ด ๋ถ๊ฐ๋ฅํ๋ค. (โต ๋ฐ์ด๋๋ฆฌ ๋ฐ์ดํฐ (ํ๋์ ๋ฉ์ด๋ฆฌ)์ด๊ธฐ ๋๋ฌธ์ด๋ค.)

๋ฐ๋ผ์, ์ด๋ฏธ์ง๋ฅผ ์์ ํ๋ ๊ฒ์ ๊ธฐ์กด์ ์ด๋ฏธ์ง๋ฅผ ๋ค๋ฅธ ์ด๋ฏธ์ง๋ก ๋ฎ์ด์์ฐ๋ ๋ฐฉ๋ฒ์ ์ฌ์ฉํ๋ค.

#### โ ๊ตฌ์ฑ

1. update.html์ `enctype` ์์ฑ ์ถ๊ฐํ๊ธฐ

   ์์ ํ๋ ํ๋ฉด์์๋ ์ด๋ฏธ์ง๋ฅผ ๋ฐ์ ์ ์๊ฒ ํ๊ธฐ ์ํจ์ด๋ค.

   ```django
   <!--update.html-->
   <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
       ...
   </form>
   ```

2. views.py์ update ํจ์ ์์ ํ๊ธฐ

   ์ธ์์ `request.FILES`๋ฅผ ์ถ๊ฐํ์ฌ ์ด๋ฏธ์ง๋ ์ ๋ฌ๋ฐ์ ์ ์๋๋ก ํ๋ค.

   ```python
   # views.py
   @require_http_methods(['GET', 'POST'])
   def update(request, pk):
       article = Article.objects.get(pk=pk)
       if request.method == 'POST':
           form = ArticleForm(request.POST, request.FILES, instance=article)
           if form.is_valid():
               form.save()
               return redirect('articles:detail', article.pk)
       else:
           form = ArticleForm(instance=article)
       context = {
           'article': article,
           'form': form,
       }
       return render(request, 'articles/update.html', context)
   ```

3. detail.html์์, ์ด๋ฏธ์ง๊ฐ ์๋ ๊ฒฝ์ฐ ValueError๊ฐ ๋จ๋ฉด์ ์ค๋ฅ๊ฐ ๋๋ฏ๋ก, ์ด๋ฅผ ํด๊ฒฐ

   โ `if๋ฌธ`์ผ๋ก ์ด๋ฏธ์ง๊ฐ ์๋ ๊ฒฝ์ฐ์๋ง ์ถ๋ ฅํ๋๋ก ํ๋ค.

   ```django
   <!--detail.html-->
   {% extends 'base.html' %}
   
   {% block content %}
     {% if article.image %}
       <img src="{{ article.image.url}}" alt="{{ article.image }}">
     {% endif %}
   	...
   {% endblock content %}
   ```

   

## 4. Image Resizing

์๋ณธ ์ด๋ฏธ์ง๊ฐ ํฐ ๊ฒฝ์ฐ, ๊ทธ๋๋ก ์๋ฒ์ ์๋ก๋ํ๋ ๊ฑด ์๋ฒ์ ๋ถ๋ด์ ๊ฐ์ค์ํจ๋ค.

๋ฐ๋ผ์, ์ด๋ฏธ์ง ์ฌ์ด์ฆ๋ฅผ ์กฐ์ ํ๋ ์์์ด ํ์ํ  ์ ์๋ค.

- [๋ฐฉ๋ฒ 1] `<img>` ํ๊ทธ์์ width์ height ์์ฑ ๋ฑ์ ์ ์ํ์ฌ ์กฐ์ ํ๋ค.

- [๋ฐฉ๋ฒ 2] ์๋ก๋ ๋  ๋ ์ด๋ฏธ์ง ์์ฒด์ ์ฌ์ด์ฆ๋ฅผ ๋ฐ๊พธ๋ ๋ฐฉ๋ฒ

  โ			: <u>django-imagekit ๋ผ์ด๋ธ๋ฌ๋ฆฌ</u> ํ์ฉ โ

###  django-imagekit ์ค์น ๋ฐ ์ฌ์ฉ

๐ [django-imagekit ๊นํ ์ฝ์ด๋ณด๊ธฐ](https://github.com/matthewwithanm/django-imagekit)

- ์ค์น

  (1)

  ```bash
  $ pip install django-imagekit
  
  # requirements.txt ์๋ฐ์ดํธ
  $ pip freeze > requirements.txt
  ```

  (2) settings.py์ INSTALLED_APPS์ `'imagekit'` ์ถ๊ฐ

  

- ์ฉ๋ก (`models.py`์ ์์ฑ)

  1) ์๋ณธ๊ณผ ์ธ๋ค์ผ์ด ๊ฐ๊ฐ ์๋ ๋ฐฉ์

     - ์บ์ฌ ํ์ผ์ด ์๊ธฐ๊ณ  ์ธ๋ค์ผ ํ์ผ์ด ์ ์ฅ๋จ (CACHE/images/)

       >**์บ์(CACHE)**
       >
       >์์ ์ ์ฅ์.
       >
       >ํ์ด์ง๋ฅผ ๋์ฐ๊ธฐ ์ํด ์ด๋ฏธ์ง ๋ฑ์ ์ฌ์ฉํ๋๋ฐ, ์ฐฝ์ ๋์ธ ๋๋ง๋ค ๋งค๋ฒ ๋ธ๋ผ์ฐ์ ๊ฐ ๊ตฌ์ฑ์์๋ฅผ ์์ฒญํด์ ๊ฐ์ ธ์ค๋ฉด ์๋ชจ์ ์ด๋ฏ๋ก, ์ฉ๋์ด ํฐ ํ์ผ์ ๋ธ๋ผ์ฐ์ ์ ์บ์ ๋ฉ๋ชจ๋ฆฌ์ ์ ์ฅํด๋๊ณ , ํ์ด์ง ์์ฒญ์ด ๋ค์ด์ค๋ฉด ์ ์ฅ์์์ ๊บผ๋ด์ ์ฌ์ฉํ๋ ๋ฐฉ์์ ํ์ฉํ๋ค.

     - ์ผ๋จ ์๋ณธ์ ์ ์ฅํ๊ณ , ์กฐํํ  ๋ ์ธ๋ค์ผ์ด ๋ง๋ค์ด์ง

     ![firstway](django04.assets/firstway.PNG)

  2) ์๋ณธ ์์ด, ์ธ๋ค์ผ๋ง ์๋ ๋ฐฉ์ (๊ธฐ๋ณธ)

     ![secondway](django04.assets/secondway.PNG)

