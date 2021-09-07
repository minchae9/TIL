from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from .models import Article
from .forms import ArticleForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(data=request.POST)   # 'data=' 생략 가능
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else: 
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)

@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()   # article에 수정 완료된 데이터 한 줄이 들어감
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)    # 기존 내용 담은 종이
    context = {
        'article': article, # article.pk를 a태그에 사용하기 위함
        'form': form,
    }
    return render(request, 'articles/update.html', context)