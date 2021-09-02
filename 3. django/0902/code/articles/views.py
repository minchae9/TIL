from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    #READ
    articles = Article.objects.all()[::-1]  # 순서 반대로 (파이썬)
    # articles = Article.objects.order_by('-id') # 순서 반대로 (ORM)
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
    # return render(request, 'articles/create.html') # create.html 페이지 나옴
    # return redirect('articles:index')   # 바로 articles/index/ 페이지로 이동
    return redirect('articles:detail', article.pk)  # detail 페이지로 redirect

def detail(request, pk):
    article = Article.objects.get(pk=pk) # url에서 pk 받아오고, 해당 pk에 해당하는 거 찾아오기
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
        return redirect('articles:detail', article.pk)  # 주소창에 치면 GET방식 -> 삭제 X

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article, # 수정할 게시글 보여주기
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 사용자가 edit에서 입력한 값으로 수정하는 것
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)  # 수정된 글의 상세 페이지로 이동