# ๐จ Django์ ์ผํ์ฑ ๋ฉ์์ง ์ถ๋ ฅ ๊ธฐ๋ฅ ์ฌ์ฉํด๋ณด๊ธฐ 

## ๐ ์ฐธ๊ณ  ์ฌ์ดํธ:

- [๋ธ๋ก๊ทธ](https://jjinisystem.tistory.com/47)
- [๊ณต์๋ฌธ์: Django Messages Framework](https://docs.djangoproject.com/en/3.2/ref/contrib/messages/)

## ์๊ณ ๊ฐ๊ธฐ

0. 1ํ๋ง ๋ธ์ถ๋๊ณ , ์๋ก๊ณ ์นจ์ ํ๋ฉด ์ฌ๋ผ์ง๋ค.

0. Django ํ๋ก์ ํธ์ settings.py ์์ ํด๋น ๊ธฐ๋ฅ์ ์คํํ๊ธฐ ์ํ ๊ธฐ๋ณธ์  ์์๊ฐ ๊ฐ์ถ์ด์ ธ ์๋ค.

   (์์ธํ ๋ด์ฉ์ ๊ณต์๋ฌธ์ ์ฐธ๊ณ )

0. ๋ฉ์์ง์ ๊ฒฝ์ค์ ๋ฐ๋ผ level์ ์กฐ์ ํ  ์ ์๋ค. Level์ ๋ฐ๋ผ ๋ฉ์์ง๊ฐ ์ถ๋ ฅ๋๋ ์์์ด ๋ฌ๋ผ์ง๋ค.

   `tags`๋ผ๋ ์ด๋ฆ์ ์์ฑ์ผ๋ก ์ ๊ทผํ  ์ ์๋ค.

   ![image-20210909190520062](DjangoStaticFiles_mystudy.assets/image-20210909190520062.png)

## ์ฌ์ฉํ๊ธฐ

1. `settings.py`์ ๋ค์์ ์์ฑํ๋ค:

   ```python
   # settings.py
   MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
   ```

2. `views.py`์์ ํด๋น ๊ธฐ๋ฅ์ ์ ์ฉํ  ํจ์๋ฅผ ์์ ํ๋ค.

   > [๋ฐฉ๋ฒ 1] `messages.add_message(request, messages.<๋ ๋ฒจ>, '๋ฉ์์ง ๋ด์ฉ')`
   >
   > [๋ฐฉ๋ฒ 2] `messages.<๋ ๋ฒจ>(request, '๋ฉ์์ง ๋ด์ฉ')`

   

   ```python
   # views.py
   from django.contrib import messages
   
   ## ๋ฐฉ๋ฒ 1
   messages.add_message(request, messages.INFO, '๊ฒ์๊ธ์ด ์ฑ๊ณต์ ์ผ๋ก ์์ฑ๋์์ต๋๋ค.')
   ## ๋ฐฉ๋ฒ 2
   messages.info(request, '๊ฒ์๊ธ ์์ฑ ์๋ฃ!')
   ```

   - [๋ฐฉ๋ฒ 1]์ 'INFO'์ [๋ฐฉ๋ฒ 2]์ 'info' ๋ถ๋ถ์ ์ํ๋ level์ ๋ฉ์์ง ํ๊ทธ๋ก ๋ฐ๊พธ๋ฉด ๋๋ค.

   - ๋ถํธ์คํธ๋ฉ ํ๊ฒฝ์์ 'error (ERROR)'์ ์์ด ํฐ์์ด ๋์ด (โ)

   - ์์:

     ```python
     # views.py์ create ํจ์
     @require_http_methods(["GET", "POST"])
     def create(request):
         if request.method == 'POST':
             form = ArticleForm(request.POST, request.FILES) # data= ์๋ต ๊ฐ๋ฅ
             if form.is_valid():
                 form.save()
                 ## add_message
                 # messages.add_message(request, messages.INFO, '๊ฒ์๊ธ์ด ์ฑ๊ณต์ ์ผ๋ก ์์ฑ๋์์ต๋๋ค.')
                 ## shortcut
                 #messages.info(request, '๊ฒ์๊ธ ์์ฑ ์๋ฃ!')
                 return redirect('articles:index')
         else:
             form = ArticleForm()
         context = { 
             'form': form,
         }
         return render(request, 'articles/create.html', context)
     ```

## ๊ฒฐ๊ณผ๋ฌผ ์์

- ๊ธ ์์ฑ ์์ `info` ํ๊ทธ์ '๊ฒ์๊ธ ์์ฑ ์๋ฃ!' ๋ฉ์์ง ์ถ๋ ฅ

![image-20210909191811146](DjangoStaticFiles_mystudy.assets/image-20210909191811146.png)

