from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods, require_POST, require_safe
from .models import Article
from .forms import ArticleForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    # create
    if request.method == 'POST':
        form = ArticleForm(request.POST)    # 첫 번째 인자로, 입력된 데이터를 통째로 받음 -> 채워진 폼이 됨
        # 유효성 검사
        if form.is_valid(): # 메서드 is_valid() - 통과 못하면, 에러메시지 출력해줌
            article = form.save()   # 저장하면, 객체가 하나 나옴
            return redirect('articles:detail', article.pk)
    else:
    # new
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


    # create

@require_safe
def detail(request, pk):
    # article = Article.objects.get(pk=pk)      # 예외 시, 500
    article = get_object_or_404(Article, pk=pk) # 예외 시, 404
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    pass

def update(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    # update
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)  # 인자가 하나 더!
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    # edit
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)



